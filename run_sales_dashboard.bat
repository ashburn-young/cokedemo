@echo off
REM Coca-Cola Sales AI Agent Framework - Quick Start for Windows

echo 🎯 Setting up Coca-Cola Sales AI Agent Framework...

REM Install Python packages
echo 📦 Installing required packages...
python -m pip install streamlit plotly pandas numpy requests

echo 🚀 Starting Coca-Cola Sales Intelligence Platform...
python -m streamlit run streamlit_dashboard.py

echo ✅ Dashboard available at: http://localhost:8501
