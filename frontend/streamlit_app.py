# Streamlit frontend for SmartFarm AI

"""
This Streamlit app serves as the user interface for the SmartFarm AI system.
Farmers can upload images of crops or seeds, select analysis type, and receive AI-powered insights and recommendations in their local language, along with audio advice. 

## Backend workflow:
    Streamlit UI
    ↓
    POST /analyze
    ↓
    routes.py
    ↓
    image_processing.py
    ↓
    gemini_client.py  (Gemini Vision → JSON)
    ↓
    voice_service.py  (gTTS → mp3)
    ↓
    Response:
    {
    crop_name
    disease_name
    confidence
    description
    recommended_pesticide
    message
    audio_file
    }
"""
import streamlit as st
import requests
import os

# ---------------- CONFIG ----------------
BACKEND_URL = "captivating-expression-production-5fe7.up.railway.app"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



st.set_page_config(
    page_title="SmartFarm AI 👨‍🌾",
    page_icon="🌱", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# st.title("🌱 SmartFarm AI Assistant")

# ---------------- THEME ----------------
if "dark" not in st.session_state:
    st.session_state.dark = False

def toggle_theme():
    st.session_state.dark = not st.session_state.dark

st.sidebar.button("🌗 Toggle Theme", on_click=toggle_theme)

if st.session_state.dark:
    st.markdown("""
        <style>
            body { background-color: #0e1117; color: white; }
            .card { background:#161b22; padding:10px; border-radius:10px; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .card { background:#f6f8fa; padding:10px; border-radius:10px; }
        </style>
    """, unsafe_allow_html=True)

# ---------------- HEADER ----------------
c1, c2 = st.columns([1, 6])
with c1:
    st.markdown("<h1 style='text-align:center;'>🌱</h1>", unsafe_allow_html=True)
with c2:
    st.markdown("""
        <h2>SmartFarm AI 👨‍🌾</h2>
        <p> AI-powered pocket assistant for smart agriculture decisions</p>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- MAIN ----------------
left, right = st.columns(2)

# -------- LEFT --------
with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📤 Upload Image")

    mode = st.radio(
        "Select Analysis Type",
        ["🌿 Crop Disease Analysis", "🌾 Seed Quality Analysis"]
    )

    country = st.text_input(
        "Country (for recommendations)",
        value="Global"
    )

    image = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    seed_type = None
    if "Seed" in mode:
        seed_type = st.text_input("Seed Type", "Unknown")

    analyze = st.button("🔍 Analyze")
    st.markdown("</div>", unsafe_allow_html=True)

# -------- RIGHT --------
with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Result")

    if analyze:
        if not image:
            st.warning("Please upload an image")
        else:
            with st.spinner("Analyzing..."):
                if "Crop" in mode:
                    res = requests.post(
                        f"{BACKEND_URL}/api/analyze-disease",
                        files={"image": image},
                        params={"country": country, "lang": "ur"}
                    )
                else:
                    res = requests.post(
                        f"{BACKEND_URL}/api/analyze-seed",
                        files={"image": image},
                        # data={"seed_type": seed_type},
                        params={"seed_type": seed_type, "lang": "ur"}
                    )

            if res.status_code != 200:
                st.error("Backend error")
            else:
                data = res.json()
                st.image(image, width="content")

                if "Crop" in mode:
                    st.markdown(f"**🌱 Crop:** {data['crop_name']}")
                    st.markdown(f"**🦠 Disease:** {data['disease_name']}")
                    st.markdown(f"**📊 Confidence:** {data['confidence']}")
                    st.markdown(f"**🧪 Pesticide:** {data['recommended_pesticide']}")
                    st.markdown(f"**🗣 Urdu Advice:** {data['message']}")
                    st.audio(f"{BACKEND_URL}/{data['audio_url']}")
                else:
                    st.markdown(f"**🌾 Seed Type:** {data['seed_type']}")
                    st.markdown(f"**⭐ Quality:** {data['quality']}")
                    st.markdown(f"**📊 Confidence:** {data['confidence']}")
                    st.markdown(f"**🔍 Observations:** {data['observations']}")
                    st.markdown(f"**🌱 Sowing Advice:** {data['sowing_recommendation']}")
                    st.markdown(f"**🗣 Message:** {data['message']}")
                    

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.divider()
f1, f2 = st.columns([6, 1])
with f1:
    st.markdown("<p style='opacity:0.6;'>SmartFarm AI © 2026 • For Farmers 🌍</p>", unsafe_allow_html=True)
with f2:
    st.markdown("<h1 style='text-align:center;'>🌱</h1>", unsafe_allow_html=True)
    st.caption("Developed by Team Kashmala")