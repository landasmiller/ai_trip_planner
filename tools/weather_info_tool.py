import os 
from utils.weather_info import WeatherForecastTool
from typing import Any, Dict, Optional , List
from dotenv import load_dotenv 
# from utils.weather_info import WeatherInfo
from langchain.tools import tool
# we can create a tool within langchain 
# Tool Decorator from langchain 
# Structured Tool has more control and validation. Can pass the function and give the validation for the input and output.

class WeatherInfoTool: 

    def __init___(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHER_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key) # will capture real time data from the utils
        self.weather_tool_list = self._setup_tools()


    def _setup_tools(self) -> List: 
        """Setup all tools for the weather forecast tool"""
        @tool 
        def get_current_weather(city: str) -> str:
            """Get current weather for a city"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data: 
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"Current weather in {city}: {temp}°C, {desc}."
            return f"Could not retrieve weather data for {city}."



        @tool 
        def get_weather_forecast(city: str) -> str:
            """Get weather forecast for a city"""
            forecast_data = self.weather_service.get_weather_forecast(city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])): 
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp}°C, {desc}.")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"Could not retrieve weather forecast for {city}."
       
        return [get_current_weather, get_weather_forecast]

        
