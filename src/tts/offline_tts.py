# ------------------------------- Libraries ---------------------------
import pyttsx3
import platform


# ------------------------------- Pre-Checks -----------------------------    

if platform.system() == "Windows":
    engine = pyttsx3.init(driverName="sapi5")
else:
    engine = pyttsx3.init()  # fallback to default on other OS


# ------------------------------- Methods -----------------------------    

def speak(text: str):
    """Speak the given text using pyttsx3."""
    if not text or not text.strip():
        raise ValueError("Cannot speak empty 'text'.")
    engine.say(text)
    engine.runAndWait()