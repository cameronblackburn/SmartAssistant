import sys
from PySide6 import QtCore, QtWidgets, QtGui
from src.gui.view.components.date_and_time import MyDateTimeWindow


class MyMainWindow(QtWidgets.QWidget):
    """Main window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Assistant")


        self.output = QtWidgets.QTextEdit() # Output for Smart Assistant Text
        self.output.setReadOnly(True)
        self.output.append("Welcome user!\nCommand list:\n'time'\n'date'\n'weather'\n'exit'")
        

        self.textbox = self.create_textbox() # Textbox for user input
        
        self.date_time_widget = MyDateTimeWindow() # Date and Time
        

        self.layout = QtWidgets.QVBoxLayout(self) # Layout manager
        
        top_bar = QtWidgets.QVBoxLayout()
        top_bar.addStretch()
        top_bar.addWidget(self.date_time_widget)
        
        self.layout.addLayout(top_bar)
        
        
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