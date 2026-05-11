import streamlit as st

# Set page config
st.set_page_config(page_title="Algorithm Storyteller", layout="wide")

# Title
st.title("Algorithm Storyteller")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    
    # Dropdown to select programming language
    selected_language = st.selectbox(
        "Select Programming Language:",
        ["C", "Java", "Python"]
    )

# Main content area
st.subheader("Paste Your Code")

# Large text area for code input
code_input = st.text_area(
    label="Enter your code here:",
    height=400,
    placeholder="Paste your code here and let the storyteller explain it..."
)

# Display selected language
if code_input:
    st.info(f"Language Selected: **{selected_language}**")
    
    # Placeholder for explanation (will be enhanced with AI)
    st.subheader("Code Explanation")
    st.write("Explanation feature will be added with AI integration...")
