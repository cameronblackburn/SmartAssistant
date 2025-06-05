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
    engine.say(text)
    engine.runAndWait()