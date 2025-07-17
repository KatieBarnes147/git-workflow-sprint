#!/usr/bin/env python3
import argparse
import requests
import json
import sys
from typing import Dict, Optional

class WeatherForecast:
    def __init__(self, latitude: float, longitude: float):
        self.lat = latitude
        self.lng = longitude
        self.office = None
        self.grid_x = None
        self.grid_y = None
        self.headers = {
            'User-Agent': '(Python Weather App, barneska@merrimack.edu)'
        }

    def get_grid_info(self) -> bool:
        try:
            url = f"https://api.weather.gov/points/{self.lat},{self.lng}"
            response = requests.get(url, headers=self.headers)

            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            if response.status_code != 200:
                print("Error: Failed to retrieve grid info.")
                return False

            data = response.json()
            self.office = data['properties']['cwa']
            self.grid_x = data['properties']['gridX']
            self.grid_y = data['properties']['gridY']

            print(f"Office: {self.office}, Grid: ({self.grid_x}, {self.grid_y})")
            return True
        except Exception as e:
            print(f"Error retrieving grid info: {e}")
            return False

    def get_weather_forecast(self) -> Dict:
        try:
            if not all([self.office, self.grid_x, self.grid_y]):
                print("Grid information is incomplete.")
                return {}

            url = f"https://api.weather.gov/gridpoints/{self.office}/{self.grid_x},{self.grid_y}/forecast"
            response = requests.get(url, headers=self.headers)

            print(f"Forecast Status Code: {response.status_code}")
            if response.status_code != 200:
                print("Error: Failed to retrieve forecast.")
                return {}

            data = response.json()
            print(f"Found {len(data.get('properties', {}).get('periods', []))} forecast periods.")
            return data
        except Exception as e:
            print(f"Error retrieving weather forecast: {e}")
            return {}

    def display_forecast(self, forecast_data: Dict) -> None:
        if not forecast_data:
            print("No forecast data available.")
            return

        periods = forecast_data.get('properties', {}).get('periods', [])

        if not periods:
            print("No forecast periods found.")
            return

        print(f"\nWeather Forecast for ({self.lat}, {self.lng})")
        print(f"Office: {self.office}, Grid: ({self.grid_x}, {self.grid_y})")
        print("=" * 60)

        for i, period in enumerate(periods[:7]):
            print(f"\n{period.get('name', 'Unknown')}")
            print(f"Temperature: {period.get('temperature', 'N/A')}\u00b0{period.get('temperatureUnit', 'F')}")
            print(f"Wind: {period.get('windSpeed', 'N/A')} {period.get('windDirection', 'N/A')}")
            print(f"Forecast: {period.get('shortForecast', 'N/A')}")

    def run(self) -> bool:
        print(f"Getting weather forecast for coordinates: ({self.lat}, {self.lng})")

        if not self.get_grid_info():
            print("Failed to get grid information.")
            return False

        forecast_data = self.get_weather_forecast()
        if not forecast_data:
            print("Failed to get weather forecast.")
            return False

        self.display_forecast(forecast_data)
        return True

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Get weather forecast for a specific location using latitude and longitude coordinates.'
    )
    parser.add_argument('--lat', type=float, required=True, help='Latitude (e.g., 42.3601 for Boston)')
    parser.add_argument('--lng', type=float, required=True, help='Longitude (e.g., -71.0589 for Boston)')
    return parser.parse_args()

def validate_coordinates(lat: float, lng: float) -> bool:
    if not (-90 <= lat <= 90):
        print("Error: Latitude must be between -90 and 90.")
        return False
    if not (-180 <= lng <= 180):
        print("Error: Longitude must be between -180 and 180.")
        return False
    return True

def main():
    args = parse_arguments()
    if not validate_coordinates(args.lat, args.lng):
        print("Error: Invalid coordinates provided.")
        sys.exit(1)

    weather = WeatherForecast(args.lat, args.lng)
    success = weather.run()

    if success:
        print("\nForecast completed successfully!")
        sys.exit(0)
    else:
        print("\nForecast failed. Please check your coordinates and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
