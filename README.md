# 🌱 SmartFarm AI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi"/>
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit"/>
  <img src="https://img.shields.io/badge/Google-Gemini%20AI-4285F4?logo=google"/>
  <img src="https://img.shields.io/badge/Swagger-API%20Docs-85EA2D?logo=swagger"/>
  <img src="https://img.shields.io/badge/Dotenv-Environment-yellow"/>
</p>

**SmartFarm AI** is a global, AI-powered agriculture assistant that analyzes **crop diseases** and **seed quality** from images using **Gemini multimodal AI**.

It is designed to help farmers, researchers, and agri-tech innovators make faster and smarter decisions—anywhere in the world.

---

## 🚀 Features

### 🌿 Crop Disease Detection
- Upload a crop leaf image
- Identify crop type and possible disease
- Confidence score (0–1)
- Clear disease description
- Recommended pesticide/treatment
- Farmer-friendly guidance

### 🌾 Seed Quality Analysis
- Upload seed images
- Detect seed quality (High / Medium / Low)
- Visual observations (damage, color, defects)
- Sowing recommendations
- Confidence-based assessment

### 🎨 Modern UI
- Built with Streamlit
- Light & Dark theme support
- Clean, professional SmartFarm branding
- Image preview 

---

## 🧠 Gemini AI Integration

SmartFarm AI uses **Gemini 3 Vision (`gemini-3-flash-preview`)** as its core intelligence.

Gemini is used to:
- Analyze images (crop leaves & seeds)
- Reason about diseases and quality
- Generate structured JSON responses
- Produce farmer-friendly advice text

⚠️ No heuristic or rule-based logic is used — all insights come directly from Gemini.

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- Google Gemini 3 API
- Pillow (Image Processing)

### Frontend
- Streamlit
- Custom CSS
- Light / Dark Mode
- REST API Integration

---

## 📁 Project Structure

```text
smartfarm-ai/
│
├── backend/
│   ├── main.py
│   ├── app/
│       ├── api/
│       │   ├── routes.py
│       │   └── schemas.py
│       ├── services/
│       │   ├── gemini_client.py
│       │   ├── image_processing.py 
│    
│   
│
├── frontend/
│   └── streamlit_app.py   # Streamlit UI
|   └── assets
│
└── README.md
```
---
---

## 🔐 Security Notes

- .env is ignored via .gitignore
- API keys are never exposed

---

## 📌 Future Enhancements
- Mobile App (Flutter)
- Multi-language farmer support
- Offline disease detection
- Crop advisory dashboard

---

## 📜 License
This project is for educational, research, and demonstration purposes | MIT License

---

**✨ Developed by the IGOGs Team** | Building intelligent tools for sustainable agriculture
