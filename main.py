import streamlit as st
from datetime import date

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Luminous Tech CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #05070a;
        color: #e0e0e0;
    }
    
    /* THE ORIEN PROJECT - High Luminosity */
    .main-title {
        color: #ffffff !important;
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 0px;
        text-shadow: 0px 0px 20px rgba(0, 212, 255, 1), 0px 0px 10px rgba(0, 212, 255, 0.8);
    }
    
    /* Subtitles and Section Headers - Subtle Glow */
    .sub-title, h3, .stSubheader p {
        color: #00d4ff !important;
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.6) !important;
    }

    /* Checkbox Labels and General Text - Subtle Glow */
    .stCheckbox label, p, span, .stMarkdown {
        color: #e0e0e0;
        text-shadow: 0px 0px 5px rgba(0, 212, 255, 0.4);
    }

    /* Input Box Styling */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0c1017 !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        padding: 15px !important;
        border-radius: 4px !important;
        box-shadow: 0px 0px 10px rgba(0, 212, 255, 0.1);
    }

    input, textarea {
        color: #00d4ff !important;
        background-color: #000000 !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        text-shadow: 0px 0px 5px rgba(0, 212, 255, 0.5) !important;
    }

    /* Button Glow */
    .stButton button {
        background-color: transparent !important;
        color: #00d4ff !important;
        border: 1px solid #00d4ff !important;
        text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.8) !important;
        box-shadow: 0px 0px 10px rgba(0, 212, 255, 0.2) !important;
    }

    /* Progress Bar Glow */
    .stProgress > div > div > div > div {
        background-color: #00d4ff;
        box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Branding
st.markdown('<p class="main-title">THE ORIEN PROJECT</
