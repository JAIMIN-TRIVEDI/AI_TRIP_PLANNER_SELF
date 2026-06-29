from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

# from tools.weather_info_tool import WeatherInfoTool
# from tools.place_search_tool import PlaceSearchTool
# from tools.expense_calculator_tool import ExpenseCalculatorTool
# from tools.currency_conversion_tool import CurrencyConversionTool



class Graph:
    def __init__(self):
        pass
    
    def agent_function(self):
        pass

    def build_graph(self):
        pass

    def __call__(self): 
        pass

    # __call__ method is used to make an instance of a class callable. It allows the instance to be called as if it were a function. When you call an instance of a class, Python will automatically invoke the __call__ method of that instance. In other words, it allows you to use the instance as a function, passing arguments to it and receiving a return value. This can be useful for creating objects that behave like functions or for implementing certain design patterns.