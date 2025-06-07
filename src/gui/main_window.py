# ------------------------------- Libraries ---------------------------
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

# ------------------------------- Constants ---------------------------

# ------------------------------- Methods -----------------------------

# ----------------------------- GUI Setup -----------------------------

class MyWidget(QtWidgets.QWidget):
    """Main window"""
    def __init__(self):
        super().__init__()

        self.smartAssOut = QtWidgets.QTextEdit() # Output for Smart Assistant Text
        self.smartAssOut.setReadOnly(True)
        self.smartAssOut.append("Testing")

        self.textbox = QtWidgets.QLineEdit(self) # Textbox for user input

        self.layout = QtWidgets.QVBoxLayout(self) # Layout manager
        self.layout.addWidget(self.smartAssOut)
        self.layout.addWidget(self.textbox)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())