# ------------------------------- Libraries ---------------------------
import requests

# ------------------------------- Constants -----------------------------

# ------------------------------- Methods -----------------------------
def get_location():

    x = requests.get("http://ip-api.com/json")
    data = x.json()

    lat = data["lat"]
    lon = data["lon"]

    coords = [lat, lon]

    return coords
