@echo off
REM Coca-Cola Sales AI Platform - Enhanced Startup Script (Windows)
REM This script launches the enhanced modular Streamlit dashboard

echo 🥤 Starting Coca-Cola Sales Executive Intelligence Platform...
echo ====================================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo ⚠️ Streamlit not found. Installing...
    pip install streamlit plotly pandas numpy
)

echo 🚀 Launching Enhanced Coca-Cola Sales AI Platform...
echo 📊 Features available:
echo    ✅ Executive Overview with KPIs
echo    ✅ Account Portfolio Management  
echo    ✅ Revenue Opportunities Pipeline
echo    ✅ AI Recommendations Engine
echo    🚧 Additional features under development
echo.
echo 🌐 Dashboard will open at: http://localhost:8510
echo ⏹️  Press Ctrl+C to stop the server
echo.

REM Launch the enhanced dashboard
streamlit run enhanced_streamlit_dashboard.py --server.port=8510

pause
