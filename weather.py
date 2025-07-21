import os
import httpx

from dotenv import load_dotenv

load_dotenv()


def get_weather_data(lat, lon, units="metric"):
    appid = os.getenv("OPEN_WEATHER_MAP_APPID")
    print(f"appid: {appid}")

    api = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "appid": appid,
        "lat": lat,
        "lon": lon,
        "units": units
    }

    # Current weather data
    response = httpx.get(api, params=params)
    data = response.json()
    # print(json.dumps(data, indent=4))

    print(f"Datetime: {data["dt"]}")
    print(f"Temp: {data["main"]["temp"]}")
    print(f"Coord: {data["coord"]}")


if __name__ == "__main__":
    get_weather_data("37.498229", "127.032748")
