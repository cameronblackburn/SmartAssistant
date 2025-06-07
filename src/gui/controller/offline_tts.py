import pyttsx3, platform, threading, queue, time


class TTSEngine:
    def __init__(self):
        if platform.system() == "Windows":
            self.engine = pyttsx3.init(driverName="sapi5")
        else:
            self.engine = pyttsx3.init() # fallback to default on other OS
        
        self.engine.setProperty('rate', 150)  # standard speaking rate


        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._run, daemon=True)
        self._running = threading.Event()
        self._running.set()
        self.thread.start()

    def _run(self):
        while self._running.is_set():
            try:
                text = self.queue.get(timeout=0.5) # wait for new text or timeout to check running flag
                if text is None:
                    break
                self.engine.say(text)
                self.engine.runAndWait()
                self.queue.task_done()
            except queue.Empty:
                continue
        

    def speak(self, text: str):
        """Speak the given text using pyttsx3."""
        if not text or not text.strip():
            return
        self.queue.put(text)

    def stop(self):
        self._running.clear()
        self.queue.put(None)
        self.thread.join()
        self.engine.stop()


_tts_engine = TTSEngine()

def speak(text: str):
    _tts_engine.speak(text)

def shutdown():
    _tts_engine.stop()