from src.gui.controller import offline_tts, controller
from PySide6.QtWidgets import QApplication
from src.gui.view.main_window import MyMainWindow
import sys

def run_app():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = controller.Controller()
    app.run()
