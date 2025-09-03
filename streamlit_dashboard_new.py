"""
Coca-Cola Executive Sales Intelligence Platform
Enterprise-grade sales insights for business executives and sales representatives
Powered by Azure AI & Semantic Kernel
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import requests
import json
import random
from typing import Dict, List, Any
import time

# Configure Streamlit page
st.set_page_config(
    page_title="Coca-Cola Executive Sales Intelligence Platform",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Authentic Coca-Cola Color Palette - Enhanced
COKE_COLORS = {
    'primary_red': '#DC143C',
    'dark_red': '#B91C1C',
    'light_red': '#EF4444',
    'coke_black': '#1F2937',
    'coke_white': '#FFFFFF',
    'coke_gold': '#F59E0B',
    'executive_green': '#10B981',
    'executive_blue': '#3B82F6',
    'executive_amber': '#F59E0B',
    'executive_purple': '#8B5CF6',
    'warning_orange': '#F97316',
    'critical_red': '#DC2626',
    'success_green': '#059669',
    'neutral_gray': '#6B7280',
    'dark_gray': '#374151',
    'light_gray': '#F9FAFB'
}

# Expanded product catalog
COKE_PRODUCTS = [
    'Coca-Cola Classic', 'Coca-Cola Zero Sugar', 'Diet Coke', 'Sprite', 
    'Fanta Orange', 'Fanta Grape', 'Minute Maid Lemonade', 'Powerade',
    'Powerade Zero Sugar', 'smartwater', 'Dasani', 'Coca-Cola Energy',
    'Coca-Cola Freestyle', 'Simply Orange', 'Honest Tea', 'Gold Peak Tea',
    'Vitaminwater', 'Peace Tea', 'Fuze Tea', 'Minute Maid Apple Juice'
]

# Account industry types for realistic data
ACCOUNT_INDUSTRIES = [
    'Quick Service Restaurants', 'Casual Dining', 'Movie Theaters', 
    'Convenience Stores', 'Grocery Chains', 'Mass Merchandisers',
    'Vending Operations', 'Office Coffee Service', 'Educational Institutions',
    'Healthcare Systems', 'Sports & Entertainment Venues', 'Airports',
    'Gas Stations', 'Bottling Partners', 'Distributors'
]

# Geographic regions for enterprise coverage
GEOGRAPHIC_REGIONS = [
    'North America - Northeast', 'North America - Southeast', 'North America - Central',
    'North America - West Coast', 'North America - Southwest', 'North America - Northwest',
    'North America - Mountain West', 'North America - Great Lakes', 'North America - Mid-Atlantic',
    'North America - Texas', 'North America - Florida', 'North America - California'
]

# Enhanced Custom CSS with Executive Coca-Cola branding
def load_css():
    st.markdown(f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Global styling with executive Coca-Cola theme */
    .main {{
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        color: #F9FAFB;
        font-family: 'Inter', sans-serif;
    }}
    
    /* Executive header */
    .executive-header {{
        background: linear-gradient(135deg, #DC143C 0%, #B91C1C 50%, #1F2937 100%);
        padding: 2rem;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 10px 30px rgba(220, 20, 60, 0.3);
    }}
    
    .executive-title {{
        font-size: 2.5rem;
        font-weight: 800;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }}
    
    .executive-subtitle {{
        font-size: 1.2rem;
        color: #F3F4F6;
        font-weight: 400;
        margin-bottom: 0;
    }}
    
    /* KPI cards */
    .kpi-card {{
        background: linear-gradient(135deg, #374151 0%, #1F2937 100%);
        border: 1px solid #4B5563;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }}
    
    .kpi-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 35px rgba(220, 20, 60, 0.2);
        border-color: #DC143C;
    }}
    
    .kpi-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #DC143C, #F59E0B, #10B981);
    }}
    
    .kpi-value {{
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0.5rem 0;
        background: linear-gradient(45deg, #DC143C, #F59E0B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    .kpi-label {{
        font-size: 0.9rem;
        color: #9CA3AF;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    .kpi-change {{
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin-top: 0.5rem;
        display: inline-block;
    }}
    
    .kpi-change.positive {{
        background: linear-gradient(45deg, #10B981, #059669);
        color: white;
    }}
    
    .kpi-change.negative {{
        background: linear-gradient(45deg, #DC2626, #B91C1C);
        color: white;
    }}
    
    /* AI Insights cards */
    .ai-insight-card {{
        background: linear-gradient(135deg, #374151 0%, #1F2937 100%);
        border-left: 4px solid #DC143C;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    
    .ai-insight-card:hover {{
        transform: translateX(8px);
        box-shadow: 0 8px 25px rgba(220, 20, 60, 0.3);
    }}
    
    .insight-priority-critical {{
        border-left-color: #DC2626;
        background: linear-gradient(135deg, rgba(220, 38, 38, 0.1) 0%, #374151 100%);
    }}
    
    .insight-priority-high {{
        border-left-color: #DC2626;
        background: linear-gradient(135deg, rgba(220, 38, 38, 0.1) 0%, #374151 100%);
    }}
    
    .insight-priority-medium {{
        border-left-color: #F59E0B;
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, #374151 100%);
    }}
    
    .insight-priority-low {{
        border-left-color: #10B981;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, #374151 100%);
    }}
    
    .insight-title {{
        font-size: 1.1rem;
        font-weight: 700;
        color: #F9FAFB;
        margin-bottom: 0.5rem;
    }}
    
    .insight-description {{
        color: #D1D5DB;
        line-height: 1.6;
        margin-bottom: 1rem;
    }}
    
    .insight-confidence {{
        background: linear-gradient(45deg, #DC143C, #B91C1C);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }}
    
    /* Chart containers */
    .chart-container {{
        background: linear-gradient(135deg, #374151 0%, #1F2937 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        border: 1px solid #4B5563;
    }}
    
    /* Status indicators */
    .status-excellent {{
        background: linear-gradient(45deg, #10B981, #059669);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }}
    
    .status-good {{
        background: linear-gradient(45deg, #3B82F6, #1D4ED8);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }}
    
    .status-fair {{
        background: linear-gradient(45deg, #F59E0B, #D97706);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }}
    
    .status-poor {{
        background: linear-gradient(45deg, #F97316, #EA580C);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }}
    
    .status-critical {{
        background: linear-gradient(45deg, #DC2626, #B91C1C);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.7; }}
    }}
    
    /* Action buttons */
    .action-button {{
        background: linear-gradient(45deg, #DC143C, #B91C1C);
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 0.5rem 0.5rem 0.5rem 0;
        display: inline-block;
        text-decoration: none;
    }}
    
    .action-button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(220, 20, 60, 0.4);
        background: linear-gradient(45deg, #B91C1C, #991B1B);
    }}
    
    /* Custom Streamlit component overrides */
    .stMetric > label {{
        color: #9CA3AF !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
    }}
    
    .stMetric > div {{
        color: #F9FAFB !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
    }}
    
    /* Hide Streamlit default elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Enhanced alert boxes */
    .stAlert > div {{
        background: linear-gradient(135deg, rgba(220, 20, 60, 0.1), rgba(220, 20, 60, 0.05)) !important;
        border: 1px solid rgba(220, 20, 60, 0.3) !important;
        border-radius: 12px !important;
        color: #F9FAFB !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Generate comprehensive enterprise sales data
@st.cache_data
def generate_enterprise_sales_data():
    """Generate realistic enterprise-level Coca-Cola sales data"""
    np.random.seed(42)  # For consistent demo data
    
    # Generate 500+ accounts for enterprise scale
    accounts_data = []
    for i in range(523):
        account_id = f"ACC{i+1000:04d}"
        base_revenue = np.random.lognormal(15, 1.5)  # Log-normal for realistic revenue distribution
        
        # Account health based on multiple factors
        payment_timeliness = np.random.beta(8, 2)
        communication_sentiment = np.random.beta(7, 3)
        growth_trend = np.random.normal(1.05, 0.15)
        product_adoption = np.random.beta(6, 2)
        
        health_score = (payment_timeliness * 0.3 + 
                       communication_sentiment * 0.25 + 
                       min(growth_trend, 1.2) * 0.25 +
                       product_adoption * 0.2) * 100
        
        # Determine health status
        if health_score >= 85:
            health_status = "Excellent"
        elif health_score >= 75:
            health_status = "Good"
        elif health_score >= 65:
            health_status = "Fair"
        elif health_score >= 55:
            health_status = "Poor"
        else:
            health_status = "Critical"
            
        # Generate realistic account names
        company_types = ["Group", "Corp", "Inc", "LLC", "Co", "Enterprises", "Holdings", "Systems"]
        business_names = [
            "Metro", "Pacific", "Atlantic", "Central", "Global", "Premier", "Superior", 
            "Elite", "Prime", "Summit", "Crown", "Royal", "Diamond", "Platinum",
            "National", "Regional", "United", "Allied", "Consolidated", "Integrated",
            "Advanced", "Dynamic", "Strategic", "Capital", "Venture", "Pioneer"
        ]
        
        name_prefix = np.random.choice(business_names)
        name_suffix = np.random.choice(company_types)
        industry = np.random.choice(ACCOUNT_INDUSTRIES)
        region = np.random.choice(GEOGRAPHIC_REGIONS)
        
        # Industry-specific naming
        if "Restaurant" in industry:
            food_names = ["Burger", "Pizza", "Taco", "Grill", "Cafe", "Diner", "Kitchen", "Bistro"]
            account_name = f"{np.random.choice(food_names)} {np.random.choice(['Palace', 'Express', 'Corner', 'Central'])}"
        elif "Theater" in industry:
            account_name = f"{name_prefix} {np.random.choice(['Cinemas', 'Theaters', 'Entertainment'])}"
        elif "Grocery" in industry:
            account_name = f"{name_prefix} {np.random.choice(['Market', 'Grocery', 'Foods', 'Mart'])}"
        else:
            account_name = f"{name_prefix} {name_suffix}"
            
        accounts_data.append({
            'account_id': account_id,
            'account_name': account_name,
            'industry': industry,
            'region': region,
            'annual_revenue': base_revenue,
            'health_score': health_score,
            'health_status': health_status,
            'payment_timeliness': payment_timeliness * 100,
            'communication_sentiment': communication_sentiment * 100,
            'growth_trend': (growth_trend - 1) * 100,
            'product_adoption_score': product_adoption * 100,
            'contract_end_date': datetime.now() + timedelta(days=np.random.randint(30, 730)),
            'last_order_date': datetime.now() - timedelta(days=np.random.randint(1, 45)),
            'primary_products': np.random.choice(COKE_PRODUCTS, size=np.random.randint(2, 6), replace=False).tolist()
        })
    
    return pd.DataFrame(accounts_data)

@st.cache_data
def generate_opportunity_data():
    """Generate realistic sales opportunity data"""
    np.random.seed(42)
    
    opportunities_data = []
    stages = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']
    stage_probabilities = [25, 45, 65, 80, 100, 0]
    
    for i in range(247):  # Enterprise-level opportunity count
        opp_id = f"OPP{i+5000:04d}"
        stage = np.random.choice(stages)
        probability = stage_probabilities[stages.index(stage)] + np.random.randint(-10, 10)
        probability = max(0, min(100, probability))
        
        # Opportunity types based on industry trends
        opp_types = [
            "Freestyle Machine Installation", "Annual Contract Renewal", "Product Line Extension",
            "Seasonal Promotion Campaign", "Territory Expansion", "New Location Rollout",
            "Equipment Upgrade Program", "Volume Commitment Increase", "Exclusive Partnership",
            "Digital Marketing Collaboration", "Sports Sponsorship Deal", "Menu Innovation Project"
        ]
        
        opp_type = np.random.choice(opp_types)
        
        # Realistic value ranges based on opportunity type
        if "Freestyle" in opp_type:
            base_value = np.random.lognormal(14, 0.8)  # $500K - $5M
        elif "Annual Contract" in opp_type:
            base_value = np.random.lognormal(16, 1.2)  # $2M - $20M
        elif "Territory Expansion" in opp_type:
            base_value = np.random.lognormal(15.5, 1.0)  # $1M - $15M
        else:
            base_value = np.random.lognormal(13.5, 1.0)  # $200K - $3M
            
        close_date = datetime.now() + timedelta(days=np.random.randint(15, 365))
        
        opportunities_data.append({
            'opportunity_id': opp_id,
            'account_id': f"ACC{np.random.randint(1000, 1523):04d}",
            'opportunity_name': opp_type,
            'stage': stage,
            'probability': probability,
            'value': base_value,
            'expected_close_date': close_date,
            'days_to_close': (close_date - datetime.now()).days,
            'created_date': datetime.now() - timedelta(days=np.random.randint(30, 180)),
            'products_involved': np.random.choice(COKE_PRODUCTS, size=np.random.randint(1, 4), replace=False).tolist(),
            'competitor_involved': np.random.choice([True, False], p=[0.3, 0.7]),
            'decision_maker_engaged': np.random.choice([True, False], p=[0.7, 0.3]),
            'budget_confirmed': np.random.choice([True, False], p=[0.6, 0.4])
        })
    
    return pd.DataFrame(opportunities_data)

@st.cache_data
def generate_ai_insights_data():
    """Generate comprehensive AI insights for enterprise dashboard"""
    insights = [
        {
            'id': 'AI001',
            'type': 'Churn Risk',
            'priority': 'Critical',
            'confidence': 89,
            'title': 'Critical Account Alert: Metro Restaurant Group',
            'description': 'Metro Restaurant Group (127 locations) showing 87% churn probability. Key indicators: 35% decline in Coca-Cola Classic orders, 42% drop in Freestyle utilization, and 60-day payment delays.',
            'account_name': 'Metro Restaurant Group',
            'potential_impact': 3200000,
            'timeline': '72 hours',
            'recommendation': 'Immediate C-level intervention required. Schedule emergency meeting within 48 hours.',
            'next_actions': [
                'Schedule emergency CEO/CFO meeting',
                'Prepare retention package with volume incentives',
                'Analyze competitive threats in market',
                'Review payment terms and credit facilities'
            ],
            'products_affected': ['Coca-Cola Classic', 'Coca-Cola Zero Sugar', 'Freestyle Systems'],
            'created_date': datetime.now() - timedelta(hours=6)
        },
        {
            'id': 'AI002',
            'type': 'Growth Opportunity',
            'priority': 'High',
            'confidence': 82,
            'title': 'Freestyle Expansion: Pacific Cinema Chain',
            'description': 'Pacific Cinema Chain (89 locations) analysis indicates 67% revenue increase potential with Freestyle deployment. Current beverage mix optimization shows $2.8M opportunity.',
            'account_name': 'Pacific Cinema Chain',
            'potential_impact': 2800000,
            'timeline': '90 days',
            'recommendation': 'Present comprehensive Freestyle ROI analysis with pilot program proposal.',
            'next_actions': [
                'Develop customized ROI presentation',
                'Propose 10-location pilot program',
                'Arrange Freestyle demo at flagship location',
                'Negotiate volume-based pricing structure'
            ],
            'products_affected': ['Coca-Cola Freestyle', 'Coca-Cola Classic', 'Sprite'],
            'created_date': datetime.now() - timedelta(hours=18)
        },
        {
            'id': 'AI003',
            'type': 'Product Opportunity',
            'priority': 'High',
            'confidence': 78,
            'title': 'Powerade Cross-Sell: Athletic Performance Venues',
            'description': 'Sports venues analysis reveals untapped Powerade opportunity. 15 key accounts show 45% sports drink sales increase but only carry competitor products.',
            'account_name': 'Multiple Sports Venues',
            'potential_impact': 1200000,
            'timeline': '120 days',
            'recommendation': 'Launch coordinated Powerade placement initiative with promotional support.',
            'next_actions': [
                'Analyze competitor pricing and placement',
                'Develop trial program with promotional support',
                'Coordinate with athlete endorsement team',
                'Design custom POS materials'
            ],
            'products_affected': ['Powerade', 'Powerade Zero Sugar'],
            'created_date': datetime.now() - timedelta(hours=24)
        },
        {
            'id': 'AI004',
            'type': 'Competitive Threat',
            'priority': 'High',
            'confidence': 84,
            'title': 'Regional Market Share Decline: Southwest Territory',
            'description': 'Southwest region showing 18% volume decline despite market growth. Competitive analysis indicates aggressive regional competitor pricing affecting Coca-Cola Classic and Sprite share.',
            'account_name': 'Southwest Regional Portfolio',
            'potential_impact': 4100000,
            'timeline': '60 days',
            'recommendation': 'Implement defensive pricing strategy and enhanced promotional support.',
            'next_actions': [
                'Conduct comprehensive competitive pricing analysis',
                'Develop regional promotional campaign',
                'Negotiate volume incentives with distributors',
                'Launch consumer loyalty programs'
            ],
            'products_affected': ['Coca-Cola Classic', 'Sprite', 'Fanta Orange'],
            'created_date': datetime.now() - timedelta(days=2)
        },
        {
            'id': 'AI005',
            'type': 'Contract Renewal',
            'priority': 'Medium',
            'confidence': 91,
            'title': 'Strategic Renewal: National Grocery Chain',
            'description': 'National Grocery Chain contract renewal in 90 days. Historical analysis shows early engagement increases renewal probability by 23% and contract value by 12%.',
            'account_name': 'National Grocery Chain',
            'potential_impact': 1800000,
            'timeline': '30 days',
            'recommendation': 'Initiate renewal discussions with performance review showcasing growth opportunities.',
            'next_actions': [
                'Prepare 3-year performance analytics report',
                'Schedule renewal strategy meeting',
                'Develop expansion opportunity proposals',
                'Negotiate multi-year volume commitments'
            ],
            'products_affected': ['Full Product Portfolio'],
            'created_date': datetime.now() - timedelta(days=1)
        },
        {
            'id': 'AI006',
            'type': 'Sentiment Alert',
            'priority': 'Medium',
            'confidence': 74,
            'title': 'Communication Sentiment Decline: SuperMart Network',
            'description': 'SuperMart Network communications show 40% increase in negative sentiment over 30 days. Key concerns: delivery scheduling, product mix optimization, promotional support.',
            'account_name': 'SuperMart Network',
            'potential_impact': 850000,
            'timeline': '21 days',
            'recommendation': 'Conduct immediate relationship health assessment and address operational concerns.',
            'next_actions': [
                'Schedule relationship review call',
                'Audit delivery and logistics performance',
                'Review promotional effectiveness metrics',
                'Propose enhanced account management'
            ],
            'products_affected': ['Coca-Cola Classic', 'Diet Coke', 'Sprite'],
            'created_date': datetime.now() - timedelta(days=3)
        }
    ]
    
    return insights

@st.cache_data  
def generate_sales_metrics_data():
    """Generate sales performance metrics and analytics"""
    # Monthly sales data for trending
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
    monthly_revenue = [245000000, 238000000, 267000000, 284000000, 292000000, 301000000, 318000000]
    monthly_volume = [23400000, 22800000, 25600000, 27200000, 28000000, 28900000, 30500000]
    
    # Product performance data
    product_performance = [
        {'Product': 'Coca-Cola Classic', 'Revenue': 156000000, 'Volume': 18500000, 'Growth': 8.3},
        {'Product': 'Coca-Cola Zero Sugar', 'Revenue': 78000000, 'Volume': 8200000, 'Growth': 15.7},
        {'Product': 'Sprite', 'Revenue': 34000000, 'Volume': 4100000, 'Growth': 6.2},
        {'Product': 'Diet Coke', 'Revenue': 28000000, 'Volume': 3200000, 'Growth': -2.1},
        {'Product': 'Fanta Orange', 'Revenue': 22000000, 'Volume': 2500000, 'Growth': 12.4}
    ]
    
    # Regional performance data
    regional_performance = [
        {'Region': 'North America - East', 'Revenue': 95000000, 'Accounts': 145, 'Health': 88.5},
        {'Region': 'North America - Central', 'Revenue': 87000000, 'Accounts': 178, 'Health': 85.2},
        {'Region': 'North America - West', 'Revenue': 76000000, 'Accounts': 134, 'Health': 82.1},
        {'Region': 'North America - Southeast', 'Revenue': 60000000, 'Accounts': 156, 'Health': 91.3}
    ]
    
    return {
        'monthly_trends': {
            'months': months,
            'revenue': monthly_revenue,
            'volume': monthly_volume
        },
        'product_performance': product_performance,
        'regional_performance': regional_performance
    }

def create_executive_header():
    """Create the executive header section"""
    st.markdown("""
    <div class="executive-header">
        <div class="executive-title">🥤 Coca-Cola Executive Sales Intelligence Platform</div>
        <div class="executive-subtitle">Powered by Azure AI & Semantic Kernel | Real-time Enterprise Sales Analytics</div>
    </div>
    """, unsafe_allow_html=True)

def display_executive_kpis(accounts_df, opportunities_df):
    """Display executive-level KPIs"""
    # Calculate key metrics
    total_pipeline = opportunities_df['value'].sum()
    active_accounts = len(accounts_df)
    avg_health_score = accounts_df['health_score'].mean()
    at_risk_accounts = len(accounts_df[accounts_df['health_status'].isin(['Poor', 'Critical'])])
    
    # KPI columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Pipeline Value",
            value=f"${total_pipeline/1000000:.1f}M",
            delta="+8.7%"
        )
    
    with col2:
        st.metric(
            label="🏢 Active Accounts", 
            value=f"{active_accounts:,}",
            delta="+3.2%"
        )
    
    with col3:
        st.metric(
            label="📊 Avg Health Score",
            value=f"{avg_health_score:.1f}%",
            delta="+2.1%"
        )
    
    with col4:
        st.metric(
            label="⚠️ At-Risk Accounts",
            value=f"{at_risk_accounts}",
            delta="-5.1%",
            delta_color="inverse"
        )

def display_ai_insights(insights_data):
    """Display AI insights with enhanced formatting"""
    st.markdown("### 🤖 Strategic AI Insights")
    
    # Priority filter
    priority_filter = st.selectbox(
        "Filter by Priority:",
        ["All", "Critical", "High", "Medium", "Low"],
        key="insights_priority_filter"
    )
    
    filtered_insights = insights_data
    if priority_filter != "All":
        filtered_insights = [insight for insight in insights_data if insight['priority'] == priority_filter]
    
    for insight in filtered_insights[:6]:  # Show top 6 insights
        priority_class = f"insight-priority-{insight['priority'].lower()}"
        
        with st.expander(f"🎯 {insight['title']}", expanded=(insight['priority'] == 'Critical')):
            st.markdown(f"""
            <div class="ai-insight-card {priority_class}">
                <div class="insight-title">{insight['title']}</div>
                <div class="insight-description">{insight['description']}</div>
                <div style="margin: 1rem 0;">
                    <span class="insight-confidence">Confidence: {insight['confidence']}%</span>
                    <span style="margin-left: 1rem; background: linear-gradient(45deg, #3B82F6, #1D4ED8); color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;">
                        Impact: ${insight['potential_impact']:,.0f}
                    </span>
                    <span style="margin-left: 1rem; background: linear-gradient(45deg, #8B5CF6, #7C3AED); color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;">
                        Timeline: {insight['timeline']}
                    </span>
                </div>
                <div style="margin-top: 1rem;">
                    <strong>Recommendation:</strong> {insight['recommendation']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Next actions
            if insight['next_actions']:
                st.markdown("**Next Actions:**")
                for action in insight['next_actions']:
                    st.markdown(f"• {action}")
            
            # Products affected
            if insight['products_affected']:
                st.markdown(f"**Products:** {', '.join(insight['products_affected'])}")
            
            # Action button
            if st.button(f"Take Action on {insight['id']}", key=f"action_{insight['id']}"):
                st.success(f"Action initiated for {insight['title']}")

def display_opportunity_pipeline(opportunities_df):
    """Display comprehensive opportunity pipeline analysis"""
    st.markdown("### 🎯 Revenue Opportunity Pipeline")
    
    # Pipeline summary metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_opportunities = len(opportunities_df)
        st.metric("Total Opportunities", f"{total_opportunities:,}")
    
    with col2:
        total_value = opportunities_df['value'].sum()
        st.metric("Pipeline Value", f"${total_value/1000000:.1f}M")
    
    with col3:
        avg_deal_size = opportunities_df['value'].mean()
        st.metric("Avg Deal Size", f"${avg_deal_size:,.0f}")
    
    # Opportunity filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        stage_filter = st.selectbox(
            "Filter by Stage:",
            ["All"] + list(opportunities_df['stage'].unique()),
            key="opp_stage_filter"
        )
    
    with col2:
        min_value = st.slider(
            "Minimum Value ($)",
            min_value=0,
            max_value=int(opportunities_df['value'].max()),
            value=0,
            step=100000,
            format="$%d",
            key="opp_min_value"
        )
    
    with col3:
        days_filter = st.selectbox(
            "Closing Timeline:",
            ["All", "Next 30 days", "Next 60 days", "Next 90 days"],
            key="opp_days_filter"
        )
    
    # Apply filters
    filtered_opps = opportunities_df.copy()
    
    if stage_filter != "All":
        filtered_opps = filtered_opps[filtered_opps['stage'] == stage_filter]
    
    if min_value > 0:
        filtered_opps = filtered_opps[filtered_opps['value'] >= min_value]
    
    if days_filter != "All":
        days_map = {"Next 30 days": 30, "Next 60 days": 60, "Next 90 days": 90}
        max_days = days_map[days_filter]
        filtered_opps = filtered_opps[filtered_opps['days_to_close'] <= max_days]
    
    # Opportunity pipeline chart
    fig_pipeline = px.funnel(
        opportunities_df.groupby('stage')['value'].sum().reset_index(),
        x='value',
        y='stage',
        title="Sales Pipeline by Stage",
        color_discrete_sequence=[COKE_COLORS['primary_red']]
    )
    fig_pipeline.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_pipeline, use_container_width=True)
    
    # Top opportunities table
    st.markdown("#### 🏆 Top Opportunities")
    
    # Sort by value and display top opportunities
    top_opps = filtered_opps.nlargest(10, 'value')[
        ['opportunity_name', 'stage', 'value', 'probability', 'days_to_close', 'products_involved']
    ].copy()
    
    # Format for display
    top_opps['value'] = top_opps['value'].apply(lambda x: f"${x:,.0f}")
    top_opps['probability'] = top_opps['probability'].apply(lambda x: f"{x}%")
    top_opps['products_involved'] = top_opps['products_involved'].apply(lambda x: ', '.join(x[:2]) + ('...' if len(x) > 2 else ''))
    
    st.dataframe(
        top_opps,
        column_config={
            "opportunity_name": "Opportunity",
            "stage": "Stage",
            "value": "Value",
            "probability": "Probability",
            "days_to_close": "Days to Close",
            "products_involved": "Products"
        },
        use_container_width=True,
        hide_index=True
    )

def display_account_portfolio(accounts_df):
    """Display comprehensive account portfolio analysis"""
    st.markdown("### 🏢 Account Portfolio Health")
    
    # Account health summary
    health_summary = accounts_df['health_status'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Health distribution pie chart
        fig_health = px.pie(
            values=health_summary.values,
            names=health_summary.index,
            title="Account Health Distribution",
            color_discrete_map={
                'Excellent': COKE_COLORS['success_green'],
                'Good': COKE_COLORS['executive_blue'],
                'Fair': COKE_COLORS['executive_amber'],
                'Poor': COKE_COLORS['warning_orange'],
                'Critical': COKE_COLORS['critical_red']
            }
        )
        fig_health.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_health, use_container_width=True)
    
    with col2:
        # Revenue by region
        region_revenue = accounts_df.groupby('region')['annual_revenue'].sum().sort_values(ascending=False)
        
        fig_region = px.bar(
            x=region_revenue.values / 1000000,
            y=region_revenue.index,
            orientation='h',
            title="Revenue by Region ($M)",
            color_discrete_sequence=[COKE_COLORS['primary_red']]
        )
        fig_region.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_region, use_container_width=True)
    
    # Account search and filtering
    st.markdown("#### 🔍 Account Search & Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("Search Accounts:", placeholder="Enter account name...")
    
    with col2:
        industry_filter = st.selectbox(
            "Filter by Industry:",
            ["All"] + sorted(accounts_df['industry'].unique()),
            key="account_industry_filter"
        )
    
    with col3:
        health_filter = st.selectbox(
            "Filter by Health:",
            ["All"] + sorted(accounts_df['health_status'].unique()),
            key="account_health_filter"
        )
    
    # Apply filters
    filtered_accounts = accounts_df.copy()
    
    if search_term:
        filtered_accounts = filtered_accounts[
            filtered_accounts['account_name'].str.contains(search_term, case=False, na=False)
        ]
    
    if industry_filter != "All":
        filtered_accounts = filtered_accounts[filtered_accounts['industry'] == industry_filter]
    
    if health_filter != "All":
        filtered_accounts = filtered_accounts[filtered_accounts['health_status'] == health_filter]
    
    # Display filtered accounts
    display_accounts = filtered_accounts.nlargest(20, 'annual_revenue')[
        ['account_name', 'industry', 'region', 'health_status', 'annual_revenue', 'health_score']
    ].copy()
    
    # Format for display
    display_accounts['annual_revenue'] = display_accounts['annual_revenue'].apply(lambda x: f"${x:,.0f}")
    display_accounts['health_score'] = display_accounts['health_score'].apply(lambda x: f"{x:.1f}%")
    
    st.dataframe(
        display_accounts,
        column_config={
            "account_name": "Account Name",
            "industry": "Industry",
            "region": "Region", 
            "health_status": "Health Status",
            "annual_revenue": "Annual Revenue",
            "health_score": "Health Score"
        },
        use_container_width=True,
        hide_index=True
    )

def display_sales_analytics():
    """Display comprehensive sales analytics"""
    st.markdown("### 📊 Sales Performance Analytics")
    
    # Get sales metrics data
    metrics_data = generate_sales_metrics_data()
    
    # Monthly trend analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue trend
        fig_revenue = go.Figure()
        fig_revenue.add_trace(go.Scatter(
            x=metrics_data['monthly_trends']['months'],
            y=[x/1000000 for x in metrics_data['monthly_trends']['revenue']],
            mode='lines+markers',
            name='Revenue ($M)',
            line=dict(color=COKE_COLORS['primary_red'], width=3),
            marker=dict(size=8)
        ))
        fig_revenue.update_layout(
            title="Monthly Revenue Trend",
            xaxis_title="Month",
            yaxis_title="Revenue ($M)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        # Volume trend
        fig_volume = go.Figure()
        fig_volume.add_trace(go.Scatter(
            x=metrics_data['monthly_trends']['months'],
            y=[x/1000000 for x in metrics_data['monthly_trends']['volume']],
            mode='lines+markers',
            name='Volume (M units)',
            line=dict(color=COKE_COLORS['executive_blue'], width=3),
            marker=dict(size=8)
        ))
        fig_volume.update_layout(
            title="Monthly Volume Trend",
            xaxis_title="Month",
            yaxis_title="Volume (M units)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_volume, use_container_width=True)
    
    # Product performance analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Product revenue chart
        product_df = pd.DataFrame(metrics_data['product_performance'])
        
        fig_products = px.bar(
            product_df,
            x='Product',
            y='Revenue',
            title="Product Revenue Performance",
            color='Growth',
            color_continuous_scale=['red', 'yellow', 'green']
        )
        fig_products.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_products, use_container_width=True)
    
    with col2:
        # Regional performance
        regional_df = pd.DataFrame(metrics_data['regional_performance'])
        
        fig_regional = px.scatter(
            regional_df,
            x='Accounts',
            y='Revenue',
            size='Health',
            color='Health',
            hover_name='Region',
            title="Regional Performance Overview",
            color_continuous_scale='RdYlGn'
        )
        fig_regional.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_regional, use_container_width=True)

def main():
    """Main application function"""
    # Load CSS
    load_css()
    
    # Create executive header
    create_executive_header()
    
    # Generate enterprise data
    with st.spinner("Loading enterprise sales data..."):
        accounts_df = generate_enterprise_sales_data()
        opportunities_df = generate_opportunity_data()
        insights_data = generate_ai_insights_data()
    
    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Executive Overview",
        "💰 Revenue Opportunities", 
        "🏢 Account Portfolio",
        "📊 Sales Analytics",
        "🤖 AI Strategic Insights"
    ])
    
    with tab1:
        st.markdown("## Executive Dashboard Overview")
        
        # Display KPIs
        display_executive_kpis(accounts_df, opportunities_df)
        
        st.markdown("---")
        
        # Priority alerts
        st.markdown("### ⚠️ Priority Alerts")
        critical_insights = [insight for insight in insights_data if insight['priority'] == 'Critical']
        
        if critical_insights:
            for insight in critical_insights:
                st.error(f"🚨 **{insight['title']}** - {insight['description'][:100]}...")
        else:
            st.success("✅ No critical alerts at this time")
        
        st.markdown("---")
        
        # Quick insights preview
        st.markdown("### 📈 Quick Performance Insights")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            high_value_opps = len(opportunities_df[opportunities_df['value'] > 1000000])
            st.metric("High-Value Opportunities", f"{high_value_opps}", "+12%")
        
        with col2:
            closing_soon = len(opportunities_df[opportunities_df['days_to_close'] <= 30])
            st.metric("Closing This Month", f"{closing_soon}", "+5%")
        
        with col3:
            excellent_accounts = len(accounts_df[accounts_df['health_status'] == 'Excellent'])
            st.metric("Excellent Health Accounts", f"{excellent_accounts}", "+3%")
    
    with tab2:
        display_opportunity_pipeline(opportunities_df)
    
    with tab3:
        display_account_portfolio(accounts_df)
    
    with tab4:
        display_sales_analytics()
    
    with tab5:
        display_ai_insights(insights_data)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #6B7280;">
        <p>🥤 Coca-Cola Executive Sales Intelligence Platform</p>
        <p>Powered by Azure AI & Semantic Kernel | Enterprise Sales Analytics</p>
        <p>Last Updated: {}</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
