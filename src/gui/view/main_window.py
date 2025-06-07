# ------------------------------- Libraries ---------------------------
import sys
from PySide6 import QtCore, QtWidgets, QtGui

# ------------------------------- Constants ---------------------------

# ------------------------------- Methods -----------------------------

# ----------------------------- GUI Setup -----------------------------

class MyMainWindow(QtWidgets.QWidget):
    """Main window"""
    def __init__(self):
        super().__init__()

        self.smartAssOut = QtWidgets.QTextEdit() # Output for Smart Assistant Text
        self.smartAssOut.setReadOnly(True)
        self.smartAssOut.append("Testing")

        self.textbox = self.create_textbox() # Textbox for user input

        self.layout = QtWidgets.QVBoxLayout(self) # Layout manager
        self.layout.addWidget(self.smartAssOut)
        self.layout.addWidget(self.textbox)

    def create_textbox(self):

        textbox = QtWidgets.QLineEdit()
        textbox.setPlaceholderText("Type your command here...")
        #---> Set action for textbox 
        return textbox


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyMainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())