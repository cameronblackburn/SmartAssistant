import sys, threading
from datetime import datetime, timedelta
from PySide6 import QtWidgets, QtCore
from src.gui.view.main_window import MyMainWindow
from src.gui.controller import parser, offline_tts
from src.gui.model.model import model_instance

class Controller:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MyMainWindow()

        self.update_weather() # update the weather on start-up

        self.window.textbox.returnPressed.connect(self.input_box_logic)

        """Getting the current local device time and calculating
        how long until the next hour, setting a one-shot timer
        and then setting an hourly timer to automatically
        update the weather
        """
        now = datetime.now()
        next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
        delay_ms = int((next_hour - now).total_seconds() * 1000)

        QtCore.QTimer.singleShot(delay_ms, self.start_hourly_updates)


    def start_hourly_updates(self):
        self.update_weather()

        self.weather_timer = QtCore.QTimer()
        self.weather_timer.timeout.connect(self.update_weather)
        self.weather_timer.start(3600000) # 1-hr timer

    def input_box_logic(self):
        """Logic for input box to take user input and pass it as an
        argument to the parser, then clear the input box
        output to main out, and send to TTS
        """

        user_input = self.window.textbox.text()
        self.window.textbox.clear()
        self.window.output.append(f"You: {user_input}")

        if user_input == "weather":
            response, weather_data = parser.handle_command(user_input)
            model_instance.set_weather_data(weather_data)
            self.window.weather_widget.update_weather()
        else:
            response = parser.handle_command(user_input)
        
        self.assistant_output(response)


        if user_input.strip().lower() == "exit":
            offline_tts.shutdown()
            QtWidgets.QApplication.quit()
        
    def assistant_output(self, response):
        self.window.output.append(f"Assistant: {response}")
        offline_tts.speak(response)
        
    def update_weather(self):
        """Method for auto updating the weather without running TTS"""
        _, weather_data = parser.handle_command("weather")
        model_instance.set_weather_data(weather_data)
        self.window.weather_widget.update_weather()
    
    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
