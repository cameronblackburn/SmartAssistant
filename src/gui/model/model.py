
class AssistantModel:
    def __init__(self):
        self.weather_data = {}

    def set_weather_data(self, data: dict):
        self.weather_data = data
    
    def get_weather_data(self) -> dict:
        return self.weather_data

model_instance = AssistantModel()