import datetime, math
from src.utils import weather

REPLY_INVALID = "I don't understand..."


def handle_command(user_input):
    """This method implements a simple symbolic AI for CASE
    parsing user input and giving an appropriate response
    """
    if not user_input or not user_input.strip():
        reply = REPLY_INVALID
        return reply
    

    user_input = user_input.lower()
    if user_input == "time":
        time = datetime.datetime.now().strftime('%H:%M')
        reply = f"The time is {time}"
        return reply
    elif user_input == "date":
        today = datetime.date.today()
        reply = today.strftime(f"The date is %B {ordinal(today.day)}, %Y")
        return reply
    elif user_input == "weather":
        reply = weather.get_weather()
        return reply
    elif user_input == "exit":
        reply = "Goodbye User!"
        return reply
    else:
        reply = REPLY_INVALID
        return reply

def ordinal(n):
    """Return oridnal date helper function"""
    return "%d%s" % (n, "tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

