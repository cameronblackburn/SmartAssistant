# ------------------------------- Libraries ---------------------------
import datetime
from src.utils import weather

# ------------------------------- Constants ---------------------------
CASE_REPLY_INVALID = "I don't understand..."

# ------------------------------- Methods -----------------------------

def handle_command(user_input):
    """This method implements a simple symbolic AI for CASE
    parsing user input and giving an appropriate response
    """
    if not user_input or not user_input.strip():
        reply = CASE_REPLY_INVALID
        return reply
    

    user_input = user_input.lower()
    if user_input == "time":
        time = datetime.datetime.now().strftime('%H:%M')
        reply = f"The time is {time}"
        return reply
    elif user_input == "date":
        today = datetime.date.today()
        reply = f"The date is {today}"
        return reply
    elif user_input == "weather":
        reply = weather.get_weather()
        return reply
    elif user_input == "exit":
        reply = "Goodbye User!"
        return reply
    else:
        reply = CASE_REPLY_INVALID
        return reply