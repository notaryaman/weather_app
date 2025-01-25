# weather_app

This project is a simple weather application that fetches and displays the current weather for a specified location using the OpenWeatherMap API. The app is containerized using Docker for easy deployment.

## Features
- Fetch current weather data using the OpenWeatherMap API. 
- Displays key weather details like temperature, description, humidity, and wind speed.
- Dockerized for quick and reliable setup.

## Prequisites 
- Install Docker on your system.
- Obtain an API key from https://openweathermap.org/

## Setup and Usage
1. Clone the repository
```
git clone https://github.com/your-repo/weather-app.git
cd weather-app
```
2. Configure Environment Variables: create a .env file in the project directory with the following format:
```
API_KEY=your_openweathermap_api_key
LOCATION=your_city_name
```
Replace your_openweathermap_api_key with your actual API key and your_city_name with the desired location.

3. Build a docker image: run this to build the docker image
```
docker build -t weather-app .
```
4. Run the Docker Container
```
docker run --env-file .env weather-app
```

## Example Output
```
Weather in Isla Vista:
Temperature: 22°C
Description: clear sky
Humidity: 60%
Wind Speed: 3.5 m/s
```
