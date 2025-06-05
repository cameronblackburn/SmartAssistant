# ------------------------------- Libraries ---------------------------
import requests
from src.utils import location

# ------------------------------- Constants ---------------------------

WEATHER_CODES = {  # For parsing data returned from open-meteo
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Freezing drizzle",
    57: "Freezing dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Thunderstorm with heavy hail"
}

# ------------------------------- Variables ---------------------------



# ------------------------------- Methods -----------------------------

def get_weather():
    """ Takes user location data and sends requests to open-meteo.
    The data is concatenated and stored in a dict "summary" which
    is returned.
    """

    coords = location.get_location()
    lat = coords[0]
    lon = coords[1]


    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current_weather=true"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max"
        f"&timezone=auto"
    )
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code\
                         {response.status_code}")
    
    data = response.json()

    current = data["current_weather"]
    daily = data["daily"]

    weathercode = current["weathercode"]
    condition =  WEATHER_CODES.get(weathercode, "Unkown")

    summary = {
        "temperature_now": current["temperature"],
        "condition": condition,
        "temperature_max": daily["temperature_2m_max"][0],
        "temperature_min": daily["temperature_2m_min"][0],
        "precipitation_probability": daily["precipitation_probability_max"][0]
    }

    temp_curr = summary['temperature_now']
    temp_min = summary['temperature_min']
    temp_max = summary['temperature_max']
    precipitation_probability = summary['precipitation_probability']

    response = (f"It is currently {temp_curr} degrees celcius"
                f" with a high of {temp_max} and low of {temp_min}.")

    return response

