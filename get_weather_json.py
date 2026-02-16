import requests

def get_coordinates(city_name):
    """
    Use Open-Meteo's free geocoding API to convert a city name
    into latitude and longitude.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        raise ValueError(f"City '{city_name}' not found.")

    result = data["results"][0]
    return result["latitude"], result["longitude"]


def get_weather_json(lat, lon):
    """
    Fetch 7-day weather forecast JSON from Open-Meteo.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    return response.json()


def get_weather_by_city(city_name):
    """
    High-level function:
    1. Convert city name → coordinates
    2. Fetch 7-day weather JSON
    """
    lat, lon = get_coordinates(city_name)
    print(f"Coordinates for {city_name}: lat={lat}, lon={lon}")

    weather_json = get_weather_json(lat, lon)
    return weather_json


if __name__ == "__main__":
    city = input("Enter a city name: ")
    weather = get_weather_by_city(city)

    print("\n=== 7-Day Weather JSON ===")
    print(weather)
