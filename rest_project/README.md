✅ README.md Template for rest_project
# 🌦️ REST Project – Weather Forecast CLI (Week 2)
This project implements a simple command-line Python application that retrieves a weather forecast using the [National Weather Service API](https://www.weather.gov/documentation/services-web-api).

## 📋 Description

You provide latitude and longitude as command-line arguments, and the program:
1. Validates the coordinates.
2. Retrieves grid information from the National Weather Service.
3. Fetches and displays a 7-day weather forecast.

Example:
```bash
python weather.py --lat 42.3601 --lng -71.0589

📂 Project Structure
rest_project/
│
├── weather.py         # Main script
├── README.md          # This file
└── requirements.txt   # Python dependencies

📌 Example Output
Getting weather forecast for coordinates: (42.3601, -71.0589)

Weather Forecast for (42.3601, -71.0589)
Office: BOX, Grid: (69, 106)
============================================================

Today
Temperature: 72°F
Wind: 10 mph NE
Forecast: Sunny with a breeze ☀️
...

⚙️ Requirements
Python 3.7+
requests library
Install with:
pip install requests

👩‍💻 Developer Info
Author: Katie Barnes
Email: barneska@merrimack.edu
Course: CSC6304 – Week 2 REST Project
Date: July 2025

✅ How to Run
python weather.py --lat <latitude> --lng <longitude>

Example:
python weather.py --lat 42.3601 --lng -71.0589
📌 Notes
Ensure you have an internet connection to reach the api.weather.gov.
The API may throttle or rate-limit requests, so don't spam it.