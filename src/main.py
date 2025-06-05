# ------------------------------- Libraries ---------------------------
from cli import parser
from tts import offline_tts
#from tts import offline_tts
# ------------------------------- Constants ---------------------------

# ------------------------------- Methods -----------------------------    

# ------------------------------- Main Declaration --------------------
def main():

    welcome_message = "Hello user!\nCASE is listening..."
    print(welcome_message)
    offline_tts.speak(welcome_message)

    while True:
        print("Please give one of the following commands: 'time', 'date', " \
        "'exit'")
        user_input = input("You: ").lower()
        
        parser.handle_command(user_input)
            
        if user_input == "exit":
            break

        
main()