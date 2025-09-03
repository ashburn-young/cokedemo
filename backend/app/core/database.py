"""
Database configuration and initialization for Coca-Cola Sales AI Agent Framework.
"""

import asyncio
import logging
from typing import Optional
import sqlite3
from pathlib import Path

logger = logging.getLogger(__name__)

# In-memory data store for this demo
# In production, this would be replaced with a proper database like PostgreSQL
DATABASE_PATH = "coke_sales.db"

class DatabaseService:
    """Simple database service for storing and retrieving data."""
    
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
    
    async def initialize(self):
        """Initialize the database with required tables."""
        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
            self.connection.row_factory = sqlite3.Row
            
            await self._create_tables()
            logger.info("Database initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize database: {str(e)}")
            raise
    
    async def _create_tables(self):
        """Create database tables."""
        cursor = self.connection.cursor()
        
        # Accounts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                account_type TEXT NOT NULL,
                region TEXT,
                country TEXT,
                annual_revenue REAL,
                employee_count INTEGER,
                health_score REAL,
                churn_risk_score REAL,
                lifetime_value REAL,
                created_date TEXT,
                last_activity_date TEXT,
                data_json TEXT
            )
        """)
        
        # Opportunities table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS opportunities (
                id TEXT PRIMARY KEY,
                account_id TEXT,
                name TEXT NOT NULL,
                stage TEXT,
                probability REAL,
                amount REAL,
                expected_close_date TEXT,
                created_date TEXT,
                data_json TEXT,
                FOREIGN KEY (account_id) REFERENCES accounts (id)
            )
        """)
        
        # Communications table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS communications (
                id TEXT PRIMARY KEY,
                account_id TEXT,
                communication_type TEXT,
                subject TEXT,
                content TEXT,
                date TEXT,
                sentiment_score TEXT,
                sentiment_confidence REAL,
                data_json TEXT,
                FOREIGN KEY (account_id) REFERENCES accounts (id)
            )
        """)
        
        # AI Insights table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_insights (
                id TEXT PRIMARY KEY,
                account_id TEXT,
                insight_type TEXT,
                title TEXT,
                description TEXT,
                confidence_score REAL,
                priority TEXT,
                created_date TEXT,
                data_json TEXT,
                FOREIGN KEY (account_id) REFERENCES accounts (id)
            )
        """)
        
        self.connection.commit()
    
    async def close(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()

# Global database instance
db_service: Optional[DatabaseService] = None

async def init_db():
    """Initialize the database service."""
    global db_service
    db_service = DatabaseService()
    await db_service.initialize()

def get_db():
    """Get the database service instance."""
    return db_service
