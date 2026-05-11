import streamlit as st
from explain_function import explain_code

# Set page config
st.set_page_config(page_title="Algorithm Storyteller", layout="wide")

# Custom CSS for dark theme and neon blue button
custom_css = """
<style>
    /* Dark theme background */
    body {
        background-color: #0a0e27;
        color: #e0e0e0;
    }
    
    .stApp {
        background-color: #0a0e27;
        color: #e0e0e0;
    }
    
    /* Main content area styling */
    .main {
        background-color: #0a0e27;
    }
    
    /* Sidebar dark theme */
    [data-testid="stSidebar"] {
        background-color: #1a1f3a;
        color: #e0e0e0;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #00d9ff;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background-color: #1a1f3a;
        color: #e0e0e0;
        border: 1px solid #00d9ff;
    }
    
    /* Neon blue button styling */
    .stButton > button {
        background-color: transparent;
        color: #ffffff;
        border: 2px solid #00d9ff;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 0 0 10px rgba(0, 217, 255, 0.5);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #00d9ff;
        color: #0a0e27;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.8);
    }
    
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* Info, warning boxes */
    .stInfo {
        background-color: #1a1f3a;
        border-left: 4px solid #00d9ff;
    }
    
    .stWarning {
        background-color: #2a1a1a;
        border-left: 4px solid #ff6b6b;
    }
    
    /* Select box styling */
    .stSelectbox > div > div {
        background-color: #1a1f3a;
        color: #e0e0e0;
        border: 1px solid #00d9ff;
    }
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

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

# Create "Tell the Story" button with neon styling
if st.button("Tell the Story", key="explain_button"):
    if code_input.strip():
        # Call the explain_code function
        explanation = explain_code(code_input, selected_language)
        
        # Display the explanation
        st.subheader("📖 Code Explanation")
        st.write(explanation)
    else:
        st.warning("Please paste some code first!")
