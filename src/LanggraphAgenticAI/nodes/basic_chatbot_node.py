from src.LanggraphAgenticAI.state.state import State
from langchain_core.messages import BaseMessage

class BasicChatbotNode:
    """
    Basic chatbot logic implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the structure of state used in graph
        """
        response: BaseMessage = self.llm.invoke(state["messages"])
        return {"messages": [response]}   # wrap in list for add_messages
