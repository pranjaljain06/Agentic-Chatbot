import streamlit as st

from src.LanggraphAgenticAI.ui.streamlit.loadui import LoadStreamlitUI
from src.LanggraphAgenticAI.LLMS.groqllm import GroqLLM
from src.LanggraphAgenticAI.graph.graph_builder import GraphBuilder
from src.LanggraphAgenticAI.ui.streamlit.display_results import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the langgraph Agentic AI applications with Streamlit UI.
    This function initializes UI, handles user input,configures LLM Model
    sets up the graph based on selected use case, displays output while
    implementing exception  handling for robustness. 
    """


    #Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI")
        return 

    user_message = st.chat_input("Enter your message...")

    if user_message: 
        try:
            #Configure LLMs
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM Model could not be initialized")
                return 

            #Initializes and set up the graph based on use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected")
                return

            #Graph Builder
            graph_builder = GraphBuilder(model) 

            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed: {e}")
                return 

        except Exception as e:
            st.error(f"Error: Graph set up failed: {e}")
            return 