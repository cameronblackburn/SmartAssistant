# ------------------------------- Libraries ---------------------------
import datetime
from tts import offline_tts

# ------------------------------- Constants ---------------------------
CASE_REPLY_STANDARD = "CASE Says: The current "

# ------------------------------- Methods -----------------------------

def handle_command(user_input):
    """This method implements a simple symbolic AI for CASE
    parsing user input and giving an appropriate response
    """
    if user_input == "time":
        time = datetime.datetime.now().strftime('%H:%M:%S')
        reply = f"{CASE_REPLY_STANDARD}time is {time}"
        print(reply)
        offline_tts.speak(reply)
        return
    elif user_input == "date":
        today = datetime.date.today()
        reply = f"{CASE_REPLY_STANDARD}date is {today}"
        print(reply)
        offline_tts.speak(reply)
        return
    elif user_input == "exit":
        reply = "CASE Says: Goodbye User!"
        print(reply)
        offline_tts.speak(reply)
        return
    else:
        print("CASE Says: I don't understand...")
        return