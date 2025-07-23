import os 
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper


class GooglePlaceSearchTool: # Class has multiple methods to search for places using GooglePlaces API.

    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
# The google places api is given with the API Wrapper. We will be able to pull all the below functions using the Google API
    
    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"top attractive places in and around {place}")
    
    def google_seearch_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"What are the top 10 restaurants in and around {place}")
    
    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"Activities to do around {place}")
    
    def google_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"What are the different modes of transportation availabe in {place}")
    
class TavilyPlaceSearchTool: # Class has multiple methods to search for places using Tavily API.
    def __init__(self):
        pass 


    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using the Tavily API
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top most fun places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result 
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top erestaurants and eateries in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"Activities to do around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
                                
    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportation availabe in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
# The Tavily API is used to search for places. It has multiple functions to search for places.
# The class has methods to search for attractions, restaurants, activities, and transportation in a specified place.
# The results are returned in dictionary format.