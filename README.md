# Langchain Chatbot with Streamlit

## Summary
This is a comprehensive guide to set up and run a chatbot application built on Langchain and Streamlit. The chatbot leverages GPT-3.5 and DuckDuckGo's search capabilities to provide intelligent responses.

---

## Table of Contents
1. [Installation](#installation)
2. [Running the Application](#running-the-application)
3. [Features](#features)

---

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps
1. **Clone the Repository**  
   ```
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory**  
   ```
   cd langchain-ddg-openai
   ```

3. **Install Required Packages**  
   ```
   pip install -r requirements.txt
   ```

   This will install all the necessary packages listed in `requirements.txt`, such as Streamlit, langchain, and more.

3. **Rename .env.example file to .env file*

4. *Setup your API in .env file*

---

## Running the Application

To run the application, execute the following command:
```
streamlit run app.py
```
This will launch the Streamlit app, and you can interact with it through your web browser.

---

## Features

### Chat Interface
A simple chat interface for user interaction, which also maintains a chat history.

### GPT-3.5 Integration
Utilizes OpenAI's GPT-3.5 model for generating responses based on the user's queries.

### DuckDuckGo Search
Incorporates DuckDuckGo Search Run for conducting research or gathering information based on user queries.

### Streamlit Callbacks
The application uses Streamlit's callback features to update the UI in real-time.

### Environment Variables
The application makes use of `.env` files for securely storing API keys.

### Decorators
Utilizes Python decorators to enable features like chat history.
