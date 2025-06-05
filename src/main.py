# ------------------------------- Libraries ---------------------------
from src.cli import parser
from src.tts import offline_tts
#from tts import offline_tts
# ------------------------------- Constants ---------------------------

# ------------------------------- Methods -----------------------------

def handle_interaction(user_input):
    reply = parser.handle_command(user_input)
    print(reply)
    offline_tts.speak(reply)
    return reply

# ------------------------------- Main Declaration --------------------
def main():

    welcome_message = "Hello user!\nCASE is listening..."
    print(welcome_message)
    offline_tts.speak(welcome_message)

    while True:
        print("Please give one of the following commands: 'time', 'date', " \
        "'exit'")
        user_input = input("You: ")
        reply = handle_interaction(user_input)
            
        if user_input == "exit":
            break

        
if __name__ == "__main__":
    main()
