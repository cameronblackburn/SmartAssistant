import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyMainWindow(QtWidgets.QWidget):
    """Main window"""
    def __init__(self):
        super().__init__()

        self.output = QtWidgets.QTextEdit() # Output for Smart Assistant Text
        self.output.setReadOnly(True)
        self.output.append("Welcome user!\nCommand list:\n'time'\n'date'\n'weather'\n'exit'")

        self.textbox = self.create_textbox() # Textbox for user input
        

        self.layout = QtWidgets.QVBoxLayout(self) # Layout manager
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.textbox)

    def create_textbox(self):

        textbox = QtWidgets.QLineEdit()
        textbox.setPlaceholderText("Type your command here...")
        return textbox


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyMainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())