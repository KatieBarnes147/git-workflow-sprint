#!/usr/bin/env python3
"""
Weather Forecast CLI Application - Student Assignment
====================================================

This script provides a shell for a weather forecast application using the National Weather Service API.
Students must implement two key methods to make the application functional.

Usage:
    python weather_forecast.py --lat 40.7128 --lng -74.0060

Requirements:
- Implement get_grid_info() method to get office and grid coordinates
- Implement get_weather_forecast() method to get forecast data
- Use the National Weather Service API (https://api.weather.gov)

API Documentation: https://www.weather.gov/documentation/services-web-api
Base URL: https://api.weather.gov

Total Points: 25 points
"""

import argparse
import requests
import json
import sys
from typing import Dict, Optional


class WeatherForecast:
    """
    A simple class to fetch and display weather forecasts using the National Weather Service API.
    """
    
    def __init__(self, latitude: float, longitude: float):
        """Initialize the WeatherForecast object with coordinates."""
        self.lat = latitude
        self.lng = longitude
        self.base_url = ""
        
        # These will be set by get_grid_info()
        self.office = None
        self.grid_x = None
        self.grid_y = None
        
        # Required headers for NWS API
        self.headers = {
            'User-Agent': '(Python Weather App, student@example.com)'
        }
    
    def get_grid_info(self) -> bool:
        """
        Get the NWS office and grid coordinates from latitude/longitude.
        
        Returns:
            bool: True if successful, False if failed
            
        TODO: Implement this method
        Steps:
        1. Create URL: f"{self.base_url}/points/{self.lat},{self.lng}"
        2. Make GET request with self.headers
        3. Parse JSON response
        4. Set self.office = response['properties']['cwa']
        5. Set self.grid_x = response['properties']['gridX'] 
        6. Set self.grid_y = response['properties']['gridY']
        7. Print: f"Office: {self.office}, Grid: ({self.grid_x}, {self.grid_y})"
        8. Return True if successful, False if error
        
        Hint: Use try/except for error handling
        """
        # YOUR CODE HERE
        pass
    
    def get_weather_forecast(self) -> Dict:
        """
        Get weather forecast data using office and grid coordinates.
        
        Returns:
            Dict: Forecast data if successful, empty dict if failed
            
        TODO: Implement this method
        Steps:
        1. Check if self.office, self.grid_x, self.grid_y are set
        2. Create URL: f"{self.base_url}/gridpoints/{self.office}/{self.grid_x},{self.grid_y}/forecast"
        3. Make GET request with self.headers
        4. Parse JSON response
        5. Return response (the full JSON response)
        6. Print number of forecast periods found
        7. Return empty dict {} if error
        
        Hint: Use try/except for error handling
        """
        # YOUR CODE HERE
        pass
    
    def display_forecast(self, forecast_data: Dict) -> None:
        """Display the weather forecast in a simple format."""
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
        
        # Show first 5 periods
        for i, period in enumerate(periods[:5]):
            print(f"\n{period.get('name', 'Unknown')}")
            print(f"Temperature: {period.get('temperature', 'N/A')}°{period.get('temperatureUnit', 'F')}")
            print(f"Wind: {period.get('windSpeed', 'N/A')} {period.get('windDirection', 'N/A')}")
            print(f"Forecast: {period.get('shortForecast', 'N/A')}")
    
    def run(self) -> bool:
        """
        Run the complete forecast process.
        
        Returns:
            bool: True if successful, False if failed
        """
        print(f"Getting weather forecast for coordinates: ({self.lat}, {self.lng})")
        
        # Step 1: Get grid info
        if not self.get_grid_info():
            print("Failed to get grid information.")
            return False
        
        # Step 2: Get weather forecast
        forecast_data = self.get_weather_forecast()
        if not forecast_data:
            print("Failed to get weather forecast.")
            return False
        
        # Step 3: Display results
        self.display_forecast(forecast_data)
        return True


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Get weather forecast for a specific location using latitude and longitude coordinates.'
    )
    
    parser.add_argument(
        '--lat', 
        type=float, 
        required=True, 
        help='Latitude coordinate (e.g., 40.7128 for New York City)'
    )
    
    parser.add_argument(
        '--lng', 
        type=float, 
        required=True, 
        help='Longitude coordinate (e.g., -74.0060 for New York City)'
    )
    
    return parser.parse_args()


def validate_coordinates(lat: float, lng: float) -> bool:
    """
    Validate latitude and longitude coordinates.
    
    TODO: Implement this function
    - Check if lat is between -90 and 90
    - Check if lng is between -180 and 180
    - Print error message if invalid
    - Return True if valid, False if invalid
    """
    # YOUR CODE HERE
    pass


def main():
    """Main function to run the weather forecast application."""
    # Parse command line arguments
    args = parse_arguments()
    
    # Validate coordinates
    if not validate_coordinates(args.lat, args.lng):
        print("Error: Invalid coordinates provided.")
        sys.exit(1)
    
    # Create WeatherForecast instance with lat/lng from command line
    weather = WeatherForecast(args.lat, args.lng)
    
    # Run the forecast process
    success = weather.run()
    
    # Exit with appropriate code
    if success:
        print("\nForecast completed successfully!")
        sys.exit(0)
    else:
        print("\nForecast failed. Please check your coordinates and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()


# ============================================================================
# TESTING EXAMPLES
# ============================================================================
"""
Test your implementation with these example coordinates:

1. New York City:
   python weather_forecast.py --lat 40.7128 --lng -74.0060

2. Miami:
   python weather_forecast.py --lat 25.7617 --lng -80.1918

3. Chicago:
   python weather_forecast.py --lat 41.8781 --lng -87.6298

Expected Output:
===============
Getting weather forecast for coordinates: (40.7128, -74.0060)
Office: OKX, Grid: (33, 37)
Found 14 forecast periods

Weather Forecast for (40.7128, -74.0060)
Office: OKX, Grid: (33, 37)
============================================================

Tonight
Temperature: 45°F
Wind: 10 mph NW
Forecast: Partly Cloudy

Tomorrow
Temperature: 52°F
Wind: 8 mph W
Forecast: Sunny
...
"""

# ============================================================================
# GRADING RUBRIC
# ============================================================================
"""
Grading Rubric (50 points total):

1. validate_coordinates() function (10 points)
   - Correctly validates latitude range (-90 to 90)
   - Correctly validates longitude range (-180 to 180)
   - Returns appropriate boolean values

2. get_grid_info() method (20 points)
   - Constructs correct API URL with lat/lng
   - Makes HTTP request with proper headers
   - Extracts office, grid_x, grid_y from response
   - Sets class properties correctly
   - Handles errors appropriately

3. get_weather_forecast() method (20 points)
   - Constructs correct forecast API URL
   - Makes HTTP request with proper headers
   - Returns complete JSON response
   - Handles errors appropriately
   - Checks that grid info is available first

Bonus Points (up to 5 points):
- Excellent error handling with specific error messages
- Additional validation or features
- Clean, readable code with good practices
"""