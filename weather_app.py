# Simple Weather App
# Oasis Infobyte Internship Project

import requests


API_KEY = "14c068f157258be0520660a574ad94fd"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    """Fetch and display weather details for a city."""
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # to get temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()
    except requests.exceptions.RequestException:
        print("\nError: Could not connect to the weather service. Please check your internet.")
        return

    # API sends a code like 200 (success), 404 (city not found), etc.
    code = str(data.get("cod", ""))

    if code != "200":
        # show error message from API (like "city not found")
        message = data.get("message", "Unknown error occurred")
        print("\nError from weather service:", message)
        return

    # extract main weather details
    main_data = data.get("main", {})
    weather_list = data.get("weather", [])

    temp = main_data.get("temp", "N/A")
    feels_like = main_data.get("feels_like", "N/A")
    humidity = main_data.get("humidity", "N/A")

    if weather_list:
        description = weather_list[0].get("description", "N/A")
    else:
        description = "N/A"

    # print the result
    print(f"\nWeather in {city_name.title()}:")
    print(f"Temperature : {temp} °C")
    print(f"Feels Like  : {feels_like} °C")
    print(f"Humidity    : {humidity} %")
    print(f"Condition   : {description}")


def main():
    print("--------- SIMPLE WEATHER APP ---------\n")

    if API_KEY == "YOUR_API_KEY_HERE":
        print("Please set your OpenWeatherMap API key in the API_KEY variable first.")
        return

    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty.")
        return

    get_weather(city)

    print("\nThank you for using the weather app :)")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
