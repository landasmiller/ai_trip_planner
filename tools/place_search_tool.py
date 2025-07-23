import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv 



class PlaceSearchTool:
    def __init___(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()



    def _setup_tools(self) -> List:
        """Setu[ all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search for attractions in a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannont find the details due to a {e}.  \nFollowing are the attractions of {place} as suggested by Tavily: {tavily_result}"


        @tool
        def search_restaurants(place: str) -> str:
            """Search for restaurants in a certain place"""
            try:
                restaurants_result = self.google_places_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"Following are the restaurants of {place} as suggested by google: {restaurants_result}"

            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannont find the details due to a {e}. \nFollowing are the restaurants of {place} as suggested by Tavily: {tavily_result}"

        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            try:
                activities_result = self.google_places_search.google_search_activities(place)
                if activities_result:
                    return f"Following are the activities of {place} as suggested by google: {activities_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activities(place)
                return f"Google cannont find the details due to a {e}. \nFollowing are the activities of {place} as suggested by Tavily: {tavily_result}"
            
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the transportation options of {place} as suggested by google: {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannont find the details due to a {e}. \nFollowing are the transportation options of {place} as suggested by Tavily: {tavily_result}"
            
            return [search_attractions, search_restaurants, search_activities, search_transportation]







