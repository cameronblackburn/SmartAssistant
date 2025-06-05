# ------------------------------- Libraries ---------------------------
import datetime

# ------------------------------- Constants ---------------------------
CASE_REPLY_STANDARD = "CASE Says: The current "

# ------------------------------- Methods -----------------------------

def handle_command(user_input):
    """This method implements a simple symbolic AI for CASE
    parsing user input and giving an appropriate response
    """

    user_input = user_input.lower()
    if user_input == "time":
        time = datetime.datetime.now().strftime('%H:%M:%S')
        reply = f"{CASE_REPLY_STANDARD}time is {time}"
        return reply
    elif user_input == "date":
        today = datetime.date.today()
        reply = f"{CASE_REPLY_STANDARD}date is {today}"
        return reply
    elif user_input == "exit":
        reply = "CASE Says: Goodbye User!"
        return reply
    else:
        reply = "CASE Says: I don't understand..."
        return reply