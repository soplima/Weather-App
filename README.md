# Weather-App
This is a simple weather app created in Python that allows the user to enter a location and displays the current weather conditions and forecast for that location. The app uses the OpenWeatherMap API to retrieve weather data.

Installation
To run the weather app, you will need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

You will also need to sign up for a free API key on the OpenWeatherMap website: https://openweathermap.org/api

Once you have Python and an API key, follow these steps to run the app:

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the requests module by running the command pip install requests (if you don't already have it installed).
4. Open the weather.py file in a text editor and replace "YOUR_API_KEY" with your actual API key.
5. Save the file and run the command python weather.py in the terminal.

Usage:
When you run the weather.py script, the app will prompt you to enter a city. Type in the name of the city you want to get weather data for and press Enter.

The app will then make a request to the OpenWeatherMap API and display the current weather conditions for the specified city. If there was an error fetching the weather data, the app will display an error message.

Note that this app only displays the current weather conditions for the specified city. To display a forecast, you will need to modify the code to use a different API endpoint and parse the response JSON accordingly.


