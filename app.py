import streamlit as st

st.set_page_config(
    page_title="Agent Studio",
    page_icon="🤖<3",
    layout="wide"
)

st.title("🤖 Agent Studio")
st.write("Configure your AI customer-support agent.")

# ---- Agent Configuration ----

st.sidebar.header("Agent Configuration")

tone = st.sidebar.selectbox(
    "Tone",
    ["Professional", "Friendly", "Casual"]
)

empathy = st.sidebar.selectbox(
    "Empathy",
    ["Low", "Medium", "High"]
)

verbosity = st.sidebar.selectbox(
    "Verbosity",
    ["Concise", "Balanced", "Detailed"]
)

persona = st.sidebar.selectbox(
    "Persona",
    ["Customer Support", "Technical Support", "Sales"]
)

language = st.sidebar.selectbox(
    "Language",
    ["English", "German"]
)

custom_instructions = st.sidebar.text_area(
    "Custom Instructions",
    placeholder="e.g. Always acknowledge customer frustration."
)

# ---- Show selected configuration ----

st.subheader("Current Agent Configuration")

st.write("**Tone:**", tone)
st.write("**Empathy:**", empathy)
st.write("**Verbosity:**", verbosity)
st.write("**Persona:**", persona)
st.write("**Language:**", language)

if custom_instructions:
    st.write("**Custom Instructions:**", custom_instructions)
