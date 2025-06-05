# ------------------------------- Libraries ---------------------------
from src.tts import offline_tts
from src.gui.simple_gui import launch_gui
# ------------------------------- Constants ---------------------------

# ------------------------------- Methods -----------------------------

# ------------------------------- Main Declaration --------------------
def main():

    welcome_message = "Hello user!\nCASE is listening..."
    print(welcome_message)
    offline_tts.speak(welcome_message)

        
if __name__ == "__main__":
    launch_gui()
