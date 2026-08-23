import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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

st.sidebar.subheader("Permissions")

can_check_order = st.sidebar.checkbox(
    "Check order status",
    value=False
)

can_create_ticket = st.sidebar.checkbox(
    "Create support ticket",
    value=True
)

can_issue_refund = st.sidebar.checkbox(
    "Issue refund",
    value=False
)

can_escalate = st.sidebar.checkbox(
    "Escalate to human",
    value=True
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

st.divider()

st.subheader("Test Your Agent")

customer_message = st.text_area(
    "Customer Message",
    placeholder="e.g. My package is 5 days late and I am very frustrated."
)

if st.button("Generate Response"):

    instructions = f"""
You are an AI customer support agent.

AGENT STYLE:
Tone: {tone}
Empathy: {empathy}
Verbosity: {verbosity}
Persona: {persona}
Language: {language}

CUSTOM INSTRUCTIONS:
{custom_instructions}

PERMISSIONS:
Check order status: {can_check_order}
Create support ticket: {can_create_ticket}
Issue refund: {can_issue_refund}
Escalate to human: {can_escalate}

IMPORTANT RULES:
- Follow the configured style and custom instructions.
- Only claim you can perform an action if the corresponding permission is True.
- If a permission is False, clearly state that you cannot perform that action.
- Never pretend that you checked an order, issued a refund, created a ticket, or escalated a case when you have not actually done so.
- Do not promise future actions that you cannot perform.
- Do not invent a reason for why a permission is disabled.
- If asked why you cannot perform a disabled action, simply explain that you are not currently authorized to perform that action.
- Do not claim that an external system, database, API, or integration is unavailable unless that information has explicitly been provided.
- Permission to perform an action does not mean the action has actually been performed.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=instructions,
        input=customer_message
    )

    st.subheader("Agent Response")
    st.write(response.output_text)



if customer_message:
    st.write("**Customer said:**")
    st.write(customer_message)
