# Use Python 3.11 slim image for smaller footprint
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8520
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements_streamlit.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install additional packages needed for the enhanced dashboard
RUN pip install --no-cache-dir \
    pandas>=2.1.0 \
    plotly>=5.17.0 \
    numpy>=1.24.0 \
    openai>=1.0.0 \
    altair \
    pydeck \
    pillow \
    seaborn>=0.12.0 \
    matplotlib>=3.7.0 \
    scikit-learn>=1.3.0

# Copy application code
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8520

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8520/_stcore/health || exit 1

# Run Streamlit app
CMD ["streamlit", "run", "enhanced_streamlit_dashboard.py", "--server.port=8520", "--server.address=0.0.0.0", "--server.headless=true", "--server.fileWatcherType=none"]
