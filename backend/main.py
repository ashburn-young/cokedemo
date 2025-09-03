"""
Coca-Cola Sales AI Agent Framework - Main Application Entry Point

This module sets up the FastAPI application with Semantic Kernel integration
for AI-powered sales insights and recommendations.
"""

import os
import asyncio
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from dotenv import load_dotenv
import logging

from app.core.config import get_settings
from app.core.database import init_db
from app.core.semantic_kernel_service import SemanticKernelService
from app.api.routes import sales_router, agents_router, dashboard_router, set_data_service, set_semantic_kernel_service
from app.services.data_generator import DataGeneratorService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Global variables for services
semantic_kernel_service: SemanticKernelService = None
data_generator_service: DataGeneratorService = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown events."""
    global semantic_kernel_service, data_generator_service
    
    logger.info("Starting Coca-Cola Sales AI Agent Framework...")
    
    try:
        # Initialize database
        await init_db()
        logger.info("Database initialized successfully")
        
        # Initialize Semantic Kernel service
        settings = get_settings()
        semantic_kernel_service = SemanticKernelService(
            azure_openai_api_key=settings.azure_openai_api_key,
            azure_openai_endpoint=settings.azure_openai_endpoint,
            deployment_name=settings.azure_openai_deployment_name,
            api_version=settings.azure_openai_api_version
        )
        await semantic_kernel_service.initialize()
        logger.info("Semantic Kernel service initialized successfully")
        
        # Initialize data generator
        data_generator_service = DataGeneratorService()
        await data_generator_service.generate_sample_data()
        logger.info("Sample data generated successfully")
        
        # Set global services for dependency injection
        set_data_service(data_generator_service)
        set_semantic_kernel_service(semantic_kernel_service)
        
        logger.info("Coca-Cola Sales AI Agent Framework started successfully!")
        
        yield
        
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        raise
    finally:
        logger.info("Shutting down Coca-Cola Sales AI Agent Framework...")
        if semantic_kernel_service:
            await semantic_kernel_service.cleanup()
        logger.info("Application shutdown complete")

# Create FastAPI application
app = FastAPI(
    title="Coca-Cola Sales AI Agent Framework",
    description="AI-powered sales insights and recommendations for Coca-Cola",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Include routers
app.include_router(sales_router, prefix="/api/v1/sales", tags=["Sales"])
app.include_router(agents_router, prefix="/api/v1/agents", tags=["AI Agents"])
app.include_router(dashboard_router, prefix="/api/v1/dashboard", tags=["Dashboard"])

@app.get("/")
async def root():
    """Root endpoint with basic application information."""
    return {
        "message": "Coca-Cola Sales AI Agent Framework",
        "version": "1.0.0",
        "status": "running",
        "documentation": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        # Check if semantic kernel service is available
        if semantic_kernel_service and await semantic_kernel_service.health_check():
            return {"status": "healthy", "services": {"semantic_kernel": "up", "database": "up"}}
        else:
            return {"status": "degraded", "services": {"semantic_kernel": "down", "database": "up"}}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Service unavailable")

if __name__ == "__main__":
    import uvicorn
    
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
        log_level="info"
    )
