import sys, threading
from PySide6 import QtWidgets
from gui.view.main_window import MyMainWindow
from gui.controller import parser, offline_tts

class Controller:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MyMainWindow()

        self.window.textbox.returnPressed.connect(self.input_box_logic)


    def input_box_logic(self):
        """Logic for input box to take user input and pass it as an
        argument to the parser, then clear the input box
        output to main out, and send to TTS
        """

        user_input = self.window.textbox.text()
        self.window.textbox.clear()
        self.window.output.append(f"You: {user_input}")
        response = parser.handle_command(user_input)
        self.assistant_output(response)


        if user_input.strip().lower() == "exit":
            offline_tts.shutdown()
            QtWidgets.QApplication.quit()
        
    def assistant_output(self, response):
        self.window.output.append(f"Assistant: {response}")
        offline_tts.speak(response)



    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
