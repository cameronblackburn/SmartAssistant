import sys
from PySide6 import QtCore, QtWidgets, QtGui
from src.gui.model.model import model_instance

class MyWeatherWindow(QtWidgets.QWidget):    
    """Weather widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.curr_temperature = QtWidgets.QLabel()
        font = self.curr_temperature.font()
        font.setPointSize(10)
        self.curr_temperature.setFont(font)
        self.curr_temperature.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.min_max_temperature = QtWidgets.QLabel()
        font = self.min_max_temperature.font()
        font.setPointSize(10)
        self.min_max_temperature.setFont(font)
        self.min_max_temperature.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.curr_temperature)
        layout.addWidget(self.min_max_temperature)
        self.setLayout(layout)

        self.update_weather()
                
    def update_weather(self):
            data = model_instance.get_weather_data()
            if data:
                self.curr_temperature.setText(f"Now: {data['temperature_now']}°C")
                self.min_max_temperature.setText(
                    f"High: {data['temperature_max']}°C  Low: {data['temperature_min']}°C")
            
            else:
                self.curr_temperature.setText("Weather not available")
                self.min_max_temperature.setText("")


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    weather = MyWeatherWindow()
    weather.show()
    sys.exit(app.exec())