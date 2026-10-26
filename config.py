
import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from tavily import TavilyClient

load_dotenv()

def get_tavily_client():
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        st.error("TAVILY_API_KEY is missing from .env")
        st.stop()

    return TavilyClient(api_key=api_key)


def get_ai_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)
