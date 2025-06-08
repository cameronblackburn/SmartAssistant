import platform
import threading
import queue
import time
import numpy as np
import sounddevice as sd
from TTS.api import TTS

class TTSEngine:
    def __init__(self):
        # Load a pre-trained English model; you can change the model if needed
        self.tts = TTS(model_name="tts_models/en/ljspeech/fast_speech", progress_bar=False)

        # Use queue and thread for async playback
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._run, daemon=True)
        self._running = threading.Event()
        self._running.set()
        self.thread.start()

    def _run(self):
        while self._running.is_set():
            try:
                text = self.queue.get(timeout=0.5)
                if text is None:
                    break

                # Generate audio
                wav = self.tts.tts(text)
                
                # Play audio
                sd.play(wav, samplerate=self.tts.synthesizer.output_sample_rate)
                sd.wait()

                self.queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"TTS playback error: {e}")

    def speak(self, text: str):
        """Speak the given text using Coqui TTS."""
        if not text or not text.strip():
            return
        self.queue.put(text)

    def stop(self):
        self._running.clear()
        self.queue.put(None)
        self.thread.join()
        sd.stop()  # stop playback in case it's running

# Global engine instance
_tts_engine = TTSEngine()

def speak(text: str):
    _tts_engine.speak(text)

def shutdown():
    _tts_engine.stop()
