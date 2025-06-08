import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyDateTimeWindow(QtWidgets.QWidget):
    """Clock and Date widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Setting the clock
        self.clock_display = QtWidgets.QLCDNumber()
        self.clock_display.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.clock_display.setDigitCount(8)
        
        # Date
        self.date_label = QtWidgets.QLabel()
        font = self.date_label.font()
        font.setPointSize(10)
        self.date_label.setFont(font)
        self.date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.clock_display)
        layout.addWidget(self.date_label)
        self.setLayout(layout)
        
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        
        self.update_datetime()
        
        self.clock_display.setFixedHeight(60)
        self.clock_display.minimumWidth()
    

        
    @QtCore.Slot()
    def update_datetime(self):
        time = QtCore.QTime.currentTime()
        date = QtCore.QDate.currentDate()
        
        
        text = time.toString("hh:mm:ss")
        
        if(time.second() % 2) == 0:
            text = text.replace(":", " ")
        
        self.clock_display.display(text)
        self.date_label.setText(date.toString("dddd, MMMM d yyyy"))
        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    clock = MyDateTimeWindow()
    clock.show()
    sys.exit(app.exec())