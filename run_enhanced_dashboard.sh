#!/bin/bash

# Coca-Cola Sales AI Platform - Enhanced Startup Script
# This script launches the enhanced modular Streamlit dashboard

echo "🥤 Starting Coca-Cola Sales Executive Intelligence Platform..."
echo "===================================================="

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    exit 1
fi

# Check if Streamlit is installed
if ! python -c "import streamlit" &> /dev/null; then
    echo "⚠️ Streamlit not found. Installing..."
    pip install streamlit plotly pandas numpy
fi

# Set environment variables for enhanced features
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false

echo "🚀 Launching Enhanced Coca-Cola Sales AI Platform..."
echo "📊 Features available:"
echo "   ✅ Executive Overview with KPIs"
echo "   ✅ Account Portfolio Management"
echo "   ✅ Revenue Opportunities Pipeline"
echo "   ✅ AI Recommendations Engine"
echo "   🚧 Additional features under development"
echo ""
echo "🌐 Dashboard will open at: http://localhost:8501"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

# Launch the enhanced dashboard
streamlit run enhanced_streamlit_dashboard.py --server.port=8501
