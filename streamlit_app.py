# filename: debate_app.py
import streamlit as st
import debatemanager
import ststreamer
from contextlib import redirect_stdout

# Function to create and load the debate team
def create_debate_team(api_key):
    dm = debatemanager.debate(api_key)
    dm.load_team()
    return dm
    
# Function to capture the console output
def capture_console_output(func, *args, **kwargs):
    f = ststreamer.ObservableStringIO()

    with redirect_stdout(f):

        func(*args, **kwargs)
    output = f.getvalue()
    return output

# Initialize session state
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = None
if 'dm' not in st.session_state:
    st.session_state['dm'] = None

# App title
st.title("AI Debate Team - Bot v Bot")

# Sidebar for API key input
if st.session_state['api_key'] is None:
    with st.sidebar:
        api_key = st.text_input("Enter your ChatGPT API key (Tier 1 or higher account):", type="password")
        if api_key:
            st.session_state['api_key'] = api_key

# If API key is provided, create and load the debate team
if st.session_state['api_key'] and st.session_state['dm'] is None:
    with st.spinner("Creating debate team..."):
        st.session_state['dm'] = create_debate_team(st.session_state['api_key'])

# Once the debate team is created, ask for a debate proposition
if st.session_state['dm']:
    proposition = st.text_input("Enter a debate proposition:")
    if proposition:
        full_proposition = f"Debate the proposition that {proposition}"
        with st.spinner(f"Debating the proposition: {proposition}. Please be patient."):
            # Redirect console output and perform the debate
            output = capture_console_output(st.session_state['dm'].do_debate, full_proposition)
