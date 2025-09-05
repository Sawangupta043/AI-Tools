import streamlit as st
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = "AIzaSyClsxpM-1g2eCVWECPZGrpXFuz79-6v5fA"
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    convert_system_message_to_human=True
    )

@tool
def refine_idea(input: str) -> str:
    """Refines a vague startup idea into a clear problem and solution statement."""
    prompt = f"Refine this vague idea into a clear problem-solution statement:\n\nIdea: {input}"
    return llm.invoke(prompt).content.strip()

@tool
def market_research(input: str) -> str:
    """Performs basic market research for a startup idea."""
    prompt = f"Do basic market research for the following startup idea:\n\n{input}\n\nInclude market size, trends, and capital requirements."
    return llm.invoke(prompt).content.strip()

@tool
def business_model_canvas(input: str) -> str:
    """Generates a Business Model Canvas for a startup idea."""
    prompt = f"Generate a Business Model Canvas for this startup:\n\n{input}"
    return llm.invoke(prompt).content.strip()

@tool
def pitch_deck_outline(input: str) -> str:
    """Generates a pitch deck outline for the startup idea."""
    prompt = f"Create a startup pitch deck outline for the following idea:\n\n{input}"
    return llm.invoke(prompt).content.strip()

@tool
def elevator_pitch(input: str) -> str:
    """Creates a short and compelling elevator pitch for the startup."""
    prompt = f"Write a concise, compelling 30-second elevator pitch for this startup:\n\n{input}"
    return llm.invoke(prompt).content.strip()

st.set_page_config(page_title="Startup Builder", layout="wide")
st.title("🚀 All-in-One Startup Builder")

idea = st.text_area("Enter your startup idea or a problem you'd like to solve:",height=150,placeholder="e.g., I want to start a business of xyz.")

run_button = st.button("Generate Full Startup Analysis")

if run_button and idea:
    with st.spinner("Generating... Please wait"):
        refined = refine_idea.invoke(idea)
        research = market_research.invoke(idea)
        canvas = business_model_canvas.invoke(idea)
        deck = pitch_deck_outline.invoke(idea)
        pitch = elevator_pitch.invoke(idea)

    st.success("✅ Thanks for waiting")

    st.markdown("### 🧠 Refined Startup Idea")
    st.markdown(refined)

    st.markdown("### 📊 Market Research")
    st.markdown(research)

    st.markdown("### 🧩 Business Model Canvas")
    st.markdown(canvas)

    st.markdown("### 🎯 Pitch Deck Outline")
    st.markdown(deck)

    st.markdown("### 🗣️ Elevator Pitch")
    st.markdown(pitch)