import streamlit as st
import os

from src.LanggraphAgenticAI.ui.uiconfigfile import Config
from langchain_core.messages import HumanMessage

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title_options(), layout="wide")
        st.header(self.config.get_page_title_options())

        with st.sidebar:
            # get options from config
            st.subheader("Agent Configuration")
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM Selection
            self.user_controls["selected_llm"]= st.selectbox("Select LLM", options=llm_options)

            if self.user_controls["selected_llm"]=="GROQ":
                #model_Selection
                model_options = self.config.get_groq_model_options()
                
                self.user_controls["selected_groq_models"]=st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                #Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter valid Groq API Key to proceed. Don't have? refer : https://console.groq.com/keys")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select usecases", usecase_options)

        return self.user_controls