import requests

api_key = "YOUR_API_KEY"

city = input("Enter a city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Current weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind speed: {data['wind']['speed']} meter/sec")
else:
    print("Error fetching weather data.")
