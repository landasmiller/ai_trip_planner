
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool





class GraphBuilder():

    def __init__ (self, model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        self.tools = []
        # Initialize the tools and collect the tools within the list
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()

        self.tools.extend([* self.weather_tools.weather_tool_list,
                           * self.place_search_tools.place_search_tool_list,
                           * self.calculator_tools.calculator_tool_list,
                           * self.currency_converter_tools.currency_converter_tool_list])

        self.llm_with_tools = self.llm.bind_tools(self.tools)  # We bind the tools to the LLM
        self.graph = None

        
        self.system_prompt = SYSTEM_PROMPT

def agent_function(self, state: MessagesState):
    """ Main agent function"""
    user_question = state["messages"]
    input_question = [self.system_prompt] + user_question
    response = self.llm_with_tools.invoke(input_question)
    return {"messages": [response]}

# the agent function makes a decision 

def build_graph(self):
    graph_builder =StateGraph(MessagesState)  # we create a graph builder agent that calls the tools node #
    graph_builder.add_node(START, "agent")
    graph_builder.add_node("agent", self.agent_function)
    graph_builder.add_node("tools", ToolNode(tools=self.tools))
    graph_builder.add_node_conditional_edges("agent", tools_condition)
    graph_builder.add_edge("tools", "agent")
    graph_builder.add_edge("agent", END)
    self.graph = graph_builder.compile()
    return self.graph 

# inside the graph we have the agent that passes the cursor. the agent works in the loop until it hits the END node.
# agentinc function works as a brain. The input is being passed to the agentic function. Based on the input, the agentic function decides which tool to call.
#  




def __call__(self):
    return self.build_graph()

