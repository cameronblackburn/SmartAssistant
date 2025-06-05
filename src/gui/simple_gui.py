# ------------------------------- Libraries ---------------------------
import tkinter as tk
from tkinter import ttk
import threading
from src.tts import offline_tts
from src.cli import parser

# ------------------------------- Constants ---------------------------



# ------------------------------- Methods -----------------------------

def handle_interaction(user_input, output_callback):
    reply = parser.handle_command(user_input)
    output_callback(reply)
    threading.Thread(target=offline_tts.speak, args=(reply,), daemon=True).start()
    return reply

def launch_gui():
    def write_to_gui(text):
        output_box.insert(tk.END, text + "\n")
        output_box.see(tk.END)


    def handle_submit():
        user_input = input_box.get()
        input_box.delete(0, tk.END)

        write_to_gui(f"You: {user_input}")
        if user_input == "exit":
            root.destroy()
            return
        
        handle_interaction(user_input, write_to_gui)



# -------------------------- GUI Setup -----------------------------
    root = tk.Tk()
    root.title("C.A.S.E. Smart Assistant")
    root.geometry("500x300")

    output_box = tk.Text(root, wrap="word", height=15, width=60)
    output_box.pack(pady=10)

    input_box = ttk.Entry(root, width=50)
    input_box.pack(pady=5)
    input_box.bind("<Return>", lambda e: handle_submit())

    submit_button = ttk.Button(root, text="Send", command=handle_submit)
    submit_button.pack()

    # Welcome message
    welcome = "Hello user!\nCASE is listening...\n" \
    "Please give one of the following commands: 'time', 'date'" \
    ", 'weather', 'exit'"

    write_to_gui(welcome)


    root.mainloop()

