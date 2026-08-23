import streamlit as st

st.set_page_config(
    page_title="Agent Studio",
    page_icon="🤖<3",
    layout="wide"
)

st.title("🤖 Agent Studio")
st.write("Configure and test your AI customer-support agent.")

st.sidebar.header("Agent Configuration")

tone = st.sidebar.selectbox(
    "Tone",
    ["Professional", "Friendly", "Casual"]
)

st.write("### Current Configuration")
st.write("Tone:", tone)
