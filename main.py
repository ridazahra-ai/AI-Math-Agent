import streamlit as st
from agent import chat

st.set_page_config(page_title = "AI Math Agrent", page_icon = "🧮", layout = "centered")
st.title("🧮 AI Math Agent")

print("\nType exit or quit for exiting from this...")
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = chat(user_input)

    print(f"\nAI: {response}")
