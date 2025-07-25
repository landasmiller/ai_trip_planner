import streamlit as st
import datetime 
import requests 
import sys 

BASE_URL = "http://localhost:8000" 


st.set_page_config(
    page_title = " 🌍 Travel Planner Agentic Application",
    page_icon = "✈️",
    layout = "centered",
    initial_sidebar_state = "expanded"
)

st.title("Agentic AI Trip Planner Application")

#  Initailize chat histort 
if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("How can I help you in planning a trip? Let me know where do you want to visit.")

with st. form(key ="query form", clear_on_submit=True):
    user_input= st.text_input("User Input", placeholder ="e.g. Plan a trip to Philippines for 12 days")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try: 
        # Show user message 
        # Show thinking spinner while backend works its magic
        with st.spinner("Agent is thinking for you....."):
            payload = {"query": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)
            # The requests and responses come from the main.py file where we have the FastAPI app running.
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer found.")
            markdown_content = f"""# 🌍 AI Travel Plans for now





            {answer}


            "This travel plan was generated by AI. Please verify all information, especially prices, logistics, and availability.answer
            """
            st.markdown(markdown_content)
        else: 
            st.error(" Agent failed to respond: " + response.text)
    except Exception as e:
        raise RuntimeError(f"The response failed due to {e}") from e
    