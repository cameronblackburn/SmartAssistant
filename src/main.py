from src.gui.controller import controller  # Only import what you're actually using
import sys

if __name__ == "__main__":
    app = controller.Controller()
    app.run()
