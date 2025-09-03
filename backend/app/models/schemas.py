"""
Database models for Coca-Cola Sales AI Agent Framework.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime, date
from enum import Enum
from pydantic import BaseModel, Field, validator
import uuid


class AccountType(str, Enum):
    """Account types in the Coca-Cola ecosystem."""
    BOTTLER = "bottler"
    RETAILER = "retailer"
    DISTRIBUTOR = "distributor"
    QSR = "qsr"  # Quick Service Restaurant
    CINEMA = "cinema"
    STADIUM = "stadium"
    THEME_PARK = "theme_park"
    GROCERY = "grocery"
    CONVENIENCE = "convenience"


class ProductLine(str, Enum):
    """Real Coca-Cola product lines from coca-cola.com."""
    # Core Coca-Cola Products
    CLASSIC = "coca_cola_classic"
    ZERO_SUGAR = "coca_cola_zero_sugar"
    DIET_COKE = "diet_coke"
    CHERRY_COKE = "cherry_coke"
    VANILLA_COKE = "vanilla_coke"
    
    # Sprite Products
    SPRITE = "sprite"
    SPRITE_ZERO = "sprite_zero"
    
    # Fanta Products
    FANTA_ORANGE = "fanta_orange"
    FANTA_GRAPE = "fanta_grape"
    FANTA_STRAWBERRY = "fanta_strawberry"
    
    # Minute Maid Products
    MINUTE_MAID_LEMONADE = "minute_maid_lemonade"
    MINUTE_MAID_FRUIT_PUNCH = "minute_maid_fruit_punch"
    MINUTE_MAID_APPLE_JUICE = "minute_maid_apple_juice"
    
    # Sports & Energy
    POWERADE = "powerade"
    POWERADE_ZERO = "powerade_zero"
    
    # Premium Waters
    SMARTWATER = "smartwater"
    SMARTWATER_ALKALINE = "smartwater_alkaline"
    DASANI = "dasani"
    
    # Technology
    FREESTYLE = "coca_cola_freestyle"
    
    # Juice & Coffee
    SIMPLY_ORANGE = "simply_orange"
    COSTA_COFFEE = "costa_coffee"


class OpportunityStage(str, Enum):
    """Sales opportunity stages."""
    PROSPECTING = "prospecting"
    QUALIFICATION = "qualification"
    PROPOSAL = "proposal"
    NEGOTIATION = "negotiation"
    CLOSED_WON = "closed_won"
    CLOSED_LOST = "closed_lost"


class SentimentScore(str, Enum):
    """Communication sentiment scores."""
    VERY_POSITIVE = "very_positive"
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"
    VERY_NEGATIVE = "very_negative"


class Account(BaseModel):
    """Account model representing Coca-Cola business partners."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    account_type: AccountType
    region: str
    country: str
    annual_revenue: float
    employee_count: int
    primary_contact_id: Optional[str] = None
    created_date: datetime
    last_activity_date: datetime
    health_score: float = Field(ge=0.0, le=100.0)
    churn_risk_score: float = Field(ge=0.0, le=100.0)
    lifetime_value: float
    current_products: List[ProductLine]
    
    # Freestyle machine data (if applicable)
    freestyle_machines_count: Optional[int] = None
    avg_daily_pours: Optional[float] = None
    machine_uptime_percentage: Optional[float] = None
    
    # Financial data
    credit_rating: str
    payment_terms: str
    discount_tier: str
    
    # Geographic data
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class Contact(BaseModel):
    """Contact model for account stakeholders."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str
    first_name: str
    last_name: str
    title: str
    email: str
    phone: str
    department: str
    decision_maker: bool = False
    influence_level: int = Field(ge=1, le=10)
    last_contact_date: Optional[datetime] = None
    preferred_communication: str = "email"


class Opportunity(BaseModel):
    """Sales opportunity model."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str
    name: str
    description: str
    stage: OpportunityStage
    probability: float = Field(ge=0.0, le=100.0)
    amount: float
    expected_close_date: date
    created_date: datetime
    last_modified_date: datetime
    owner_id: str
    product_lines: List[ProductLine]
    
    # AI-generated fields
    next_best_action: Optional[str] = None
    risk_factors: List[str] = []
    success_factors: List[str] = []


class Communication(BaseModel):
    """Communication tracking model."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str
    contact_id: Optional[str] = None
    opportunity_id: Optional[str] = None
    communication_type: str  # email, call, meeting, visit
    subject: str
    content: str
    date: datetime
    direction: str  # inbound, outbound
    sentiment_score: SentimentScore
    sentiment_confidence: float = Field(ge=0.0, le=1.0)
    key_topics: List[str] = []
    action_items: List[str] = []


class FreestyleMachineData(BaseModel):
    """Freestyle machine telemetry data."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str
    machine_id: str
    location_name: str
    timestamp: datetime
    
    # Usage metrics
    total_pours: int
    unique_customers: int
    avg_pour_size: float
    popular_flavors: List[str]
    
    # Performance metrics
    uptime_percentage: float = Field(ge=0.0, le=100.0)
    error_count: int
    maintenance_alerts: List[str] = []
    
    # Business metrics
    revenue: float
    cost_per_pour: float
    profit_margin: float


class SalesMetrics(BaseModel):
    """Aggregated sales metrics."""
    account_id: str
    period_start: date
    period_end: date
    
    # Volume metrics
    total_volume: float
    volume_change_percent: float
    volume_trend: str  # increasing, decreasing, stable
    
    # Revenue metrics
    total_revenue: float
    revenue_change_percent: float
    avg_order_value: float
    
    # Product mix
    product_mix: Dict[ProductLine, float]
    
    # Performance metrics
    on_time_delivery_rate: float
    quality_score: float
    customer_satisfaction: float


class AIInsight(BaseModel):
    """AI-generated insights and recommendations."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: Optional[str] = None
    opportunity_id: Optional[str] = None
    insight_type: str  # churn_risk, upsell_opportunity, retention_strategy
    title: str
    description: str
    confidence_score: float = Field(ge=0.0, le=1.0)
    priority: str  # high, medium, low
    recommended_actions: List[str]
    supporting_data: Dict[str, Any]
    created_date: datetime
    expires_date: Optional[datetime] = None
    acted_upon: bool = False


class ChurnPrediction(BaseModel):
    """Churn prediction model results."""
    account_id: str
    prediction_date: datetime
    churn_probability: float = Field(ge=0.0, le=1.0)
    risk_level: str  # low, medium, high, critical
    key_risk_factors: List[str]
    recommended_interventions: List[str]
    model_confidence: float = Field(ge=0.0, le=1.0)
    feature_importance: Dict[str, float]


class HeatmapData(BaseModel):
    """Data structure for dashboard heatmaps."""
    region: str
    account_count: int
    total_revenue: float
    avg_health_score: float
    churn_risk_accounts: int
    growth_opportunity_score: float
    coordinates: Dict[str, float]  # lat, lng
    
    
class DashboardSummary(BaseModel):
    """Executive dashboard summary."""
    total_accounts: int
    total_revenue: float
    revenue_growth_percent: float
    high_risk_accounts: int
    opportunities_closing_this_month: int
    avg_deal_size: float
    win_rate: float
    top_performing_regions: List[str]
    at_risk_revenue: float
    
    # Time series data
    revenue_trend: List[Dict[str, Any]]
    health_score_trend: List[Dict[str, Any]]
    churn_risk_trend: List[Dict[str, Any]]
