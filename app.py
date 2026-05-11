import streamlit as st
from explain_function import explain_code

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

# Create "Tell the Story" button
if st.button("Tell the Story", key="explain_button"):
    if code_input.strip():
        # Call the explain_code function
        explanation = explain_code(code_input, selected_language)
        
        # Display the explanation
        st.subheader("📖 Code Explanation")
        st.write(explanation)
    else:
        st.warning("Please paste some code first!")
