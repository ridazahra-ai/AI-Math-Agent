import streamlit as st
from agent import chat

st.set_page_config(page_title = "AI Math Agrent", page_icon = "🧮", layout = "centered")
st.title("🧮 AI Math Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

user_input = st.chat_input("Ask me any math question...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    try:
        with st.spinner("Thinking..."):
            response = chat(user_input)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.chat_message("assistant").write(response)

    except Exception as e:
        st.error(f"Error: {e}")
        