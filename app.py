import os
import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler
from langchain.agents import AgentType, initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.callbacks import StreamlitCallbackHandler
from dotenv import load_dotenv


# Configure the Streamlit page
st.set_page_config(
    page_title="Langchain DuckDuckGo Researcher",
    page_icon='💬',
    layout='wide'
)
st.header("Chatbot Implementations with Langchain & DuckDuckGo")


# Load environment variables
load_dotenv()

# Retrieve API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Decorator to enable chat history
def enable_chat_history(func):
    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

# Method to display message on the UI
def display_msg(msg, author):
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)


# StreamHandler class
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.container.markdown(self.text)

# ChatbotTools class
class ChatbotTools:
    def __init__(self):
        self.openai_model = "gpt-3.5-turbo-0613"

    def setup_agent(self):
        ddg_search = DuckDuckGoSearchRun()
        tools = [
            Tool(
                name="DuckDuckGoSearch",
                func=ddg_search.run,
                description="Useful for when you need to research about something, Get detailed information about the research topic. Use targeted keywords for search.",
            )
        ]
        llm = ChatOpenAI(model_name=self.openai_model, streaming=True)
        
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,
            verbose=True,
            max_iterations=100,
            max_execution_time=None
        )
        return agent

    @enable_chat_history
    def main(self):
        # Initialize st.session_state.messages if it's not already initialized
        if 'messages' not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "What is it you want to search for?"}]

        # Display existing messages
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        agent = self.setup_agent()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.write(response)


# Run the application
if __name__ == "__main__":
    chatbot = ChatbotTools()
    chatbot.main()
