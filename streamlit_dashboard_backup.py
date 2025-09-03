"""
Coca-Cola Sales AI Agent Framework
Executive Sales Intelligence Platform - Powered by Azure AI & Semantic Kernel
Enterprise-grade sales insights for business executives and sales representatives
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
    
    /* Sidebar styling */
    .css-1d391kg {{
        background: linear-gradient(180deg, #DC143C 0%, #B91C1C 100%);
    }}
    
    .css-1d391kg .css-17eq0hr {{
        color: white;
    }}
    
    /* Header styling */
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
    
    /* Executive KPI cards */
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
    
    .action-button-secondary {{
        background: linear-gradient(45deg, #374151, #1F2937);
        color: white;
        border: 1px solid #4B5563;
        padding: 0.6rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 0.5rem 0.5rem 0.5rem 0;
    }}
    
    .action-button-secondary:hover {{
        background: linear-gradient(45deg, #4B5563, #374151);
        border-color: #DC143C;
    }}
    
    /* Opportunity cards */
    .opportunity-card {{
        background: linear-gradient(135deg, #374151 0%, #1F2937 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #4B5563;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    
    .opportunity-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(220, 20, 60, 0.2);
        border-color: #DC143C;
    }}
    
    /* Account health indicators */
    .account-health-excellent {{
        background: linear-gradient(45deg, #10B981, #059669);
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }}
    
    .account-health-good {{
        background: linear-gradient(45deg, #3B82F6, #1D4ED8);
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
    }}
    
    .account-health-fair {{
        background: linear-gradient(45deg, #F59E0B, #D97706);
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
        box-shadow: 0 0 10px rgba(245, 158, 11, 0.5);
    }}
    
    .account-health-poor {{
        background: linear-gradient(45deg, #F97316, #EA580C);
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
        box-shadow: 0 0 10px rgba(249, 115, 22, 0.5);
    }}
    
    .account-health-critical {{
        background: linear-gradient(45deg, #DC2626, #B91C1C);
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
        box-shadow: 0 0 10px rgba(220, 38, 38, 0.5);
        animation: pulse 1.5s infinite;
    }}
    
    /* Navigation tabs */
    .nav-tab {{
        background: transparent;
        color: #9CA3AF;
        border: none;
        padding: 1rem 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.3s ease;
        border-bottom: 3px solid transparent;
    }}
    
    .nav-tab.active {{
        color: #DC143C;
        border-bottom-color: #DC143C;
        background: linear-gradient(135deg, rgba(220, 20, 60, 0.1), transparent);
    }}
    
    .nav-tab:hover {{
        color: #DC143C;
        background: linear-gradient(135deg, rgba(220, 20, 60, 0.05), transparent);
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
    
    .stSuccess > div {{
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.05)) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
    }}
    
    .stWarning > div {{
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05)) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
    }}
    
    .stError > div {{
        background: linear-gradient(135deg, rgba(220, 38, 38, 0.1), rgba(220, 38, 38, 0.05)) !important;
        border: 1px solid rgba(220, 38, 38, 0.3) !important;
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
        box-shadow: 0 8px 32px rgba(220, 20, 60, 0.3);
    }}
    
    .coke-title {{
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    
    .coke-subtitle {{
        font-size: 1.2rem;
        text-align: center;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-weight: 300;
    }}
    
    /* Metric cards with Coca-Cola styling */
    .metric-card {{
        background: linear-gradient(145deg, #2a2a2a 0%, #1f1f1f 100%);
        border: 1px solid rgba(220, 20, 60, 0.3);
        border-left: 4px solid {COKE_COLORS['coke_red']};
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        color: white;
    }}
    
    .metric-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(220, 20, 60, 0.25);
    }}
    
    .metric-value {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {COKE_COLORS['coke_red']};
        margin: 0;
    }}
    
    .metric-label {{
        font-size: 1rem;
        color: #d1d5db;
        margin: 0;
        font-weight: 500;
    }}
    
    .metric-change {{
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }}
    
    .change-positive {{
        color: {COKE_COLORS['executive_green']};
    }}
    
    .change-negative {{
        color: {COKE_COLORS['coke_red']};
    }}
    
    /* AI Insights styling */
    .ai-insight {{
        background: linear-gradient(145deg, #2a2a2a 0%, #1f1f1f 100%);
        border: 1px solid #374151;
        border-top: 4px solid {COKE_COLORS['executive_blue']};
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        color: white;
    }}
    
    .insight-title {{
        font-size: 1.2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }}
    
    .insight-confidence {{
        background: {COKE_COLORS['executive_green']};
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
    }}
    
    .insight-impact {{
        background: linear-gradient(90deg, {COKE_COLORS['coke_gold']} 0%, #f59e0b 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-left: 0.5rem;
    }}
    
    /* Product badges */
    .product-classic {{ 
        background: linear-gradient(135deg, {COKE_COLORS['coke_red']} 0%, {COKE_COLORS['dark_scarlet']} 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem;
        display: inline-block;
    }}
    
    .product-zero {{ 
        background: linear-gradient(135deg, {COKE_COLORS['coke_black']} 0%, {COKE_COLORS['chocolate_kisses']} 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem;
        display: inline-block;
    }}
    
    .product-sprite {{ 
        background: linear-gradient(135deg, #00B04F 0%, #32CD32 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem;
        display: inline-block;
    }}
    
    .product-freestyle {{ 
        background: linear-gradient(135deg, {COKE_COLORS['coke_red']} 0%, {COKE_COLORS['executive_blue']} 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem;
        display: inline-block;
    }}
    
    .product-powerade {{ 
        background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem;
        display: inline-block;
    }}
    
    /* Sidebar styling */
    .css-1d391kg {{
        background: linear-gradient(180deg, {COKE_COLORS['coke_red']} 0%, {COKE_COLORS['dark_scarlet']} 100%);
    }}
    
    .css-1d391kg .css-1d391kg {{
        color: white;
    }}
    
    /* Button styling */
    .stButton > button {{
        background: linear-gradient(135deg, {COKE_COLORS['coke_red']} 0%, {COKE_COLORS['dark_scarlet']} 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(220, 20, 60, 0.3);
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(220, 20, 60, 0.4);
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Dark theme overrides for Streamlit components */
    .stMetric {{
        background: linear-gradient(145deg, #2a2a2a 0%, #1f1f1f 100%);
        border: 1px solid rgba(220, 20, 60, 0.3);
        border-left: 4px solid {COKE_COLORS['coke_red']};
        border-radius: 12px;
        padding: 1rem;
        color: white;
    }}
    
    .stMetric > div {{
        color: white;
    }}
    
    .stMetric label {{
        color: #d1d5db !important;
    }}
    
    .stAlert {{
        background: rgba(45, 45, 45, 0.95) !important;
        border: 1px solid rgba(220, 20, 60, 0.3) !important;
        color: white !important;
    }}
    
    .stExpanderHeader {{
        background: linear-gradient(145deg, #2a2a2a 0%, #1f1f1f 100%) !important;
        color: white !important;
        border: 1px solid rgba(220, 20, 60, 0.3) !important;
    }}
    
    .stExpanderContent {{
        background: rgba(45, 45, 45, 0.95) !important;
        border: 1px solid rgba(220, 20, 60, 0.2) !important;
        color: white !important;
    }}
    </style>
    """, unsafe_allow_html=True)

def create_header():
    """Create the sales intelligence platform header"""
    st.markdown(f"""
    <div class="coke-header">
        <h1 class="coke-title">🎯 Coca-Cola Sales AI Agent Framework</h1>
        <p class="coke-subtitle">Sales Intelligence Platform | Powered by Azure AI & Semantic Kernel</p>
    </div>
    """, unsafe_allow_html=True)

def get_sales_intelligence_data():
    """Fetch sales intelligence data from backend API or use realistic mock data"""
    try:
        # Try to fetch from backend
        response = requests.get("http://localhost:8000/api/dashboard/summary", timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    
    # Mock data focused on sales intelligence metrics
    return {
        "accounts_at_risk": 8,
        "high_opportunity_accounts": 15,
        "declining_engagement": 12,
        "total_active_accounts": 127,
        "this_month_revenue": 4200000,
        "projected_churn_risk": 2800000,
        "ai_recommendations": 23,
        "freestyle_expansion_ready": 31,
        "avg_account_health": 78.5,
        "sentiment_declining": 18
    }

def create_sales_intelligence_metrics():
    """Create sales intelligence KPIs focused on actionable insights"""
    data = get_sales_intelligence_data()
    
    st.markdown("### 🎯 Sales Intelligence Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Accounts at Risk", 
            value=data['accounts_at_risk'],
            delta="Requires Immediate Action",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            label="High Opportunity", 
            value=data['high_opportunity_accounts'],
            delta="Ready for Expansion",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Revenue at Risk", 
            value=f"${data['projected_churn_risk']/1000000:.1f}M",
            delta="Churn Protection Needed",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="AI Recommendations", 
            value=data['ai_recommendations'],
            delta="Action Items Available",
            delta_color="normal"
        )

def create_sales_performance_chart():
    """Create sales performance visualization with Coca-Cola colors"""
    # Generate sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    coca_cola_classic = [2.1, 2.3, 2.5, 2.4, 2.7, 2.9]
    coca_cola_zero = [1.2, 1.4, 1.6, 1.8, 1.9, 2.1]
    sprite = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    freestyle = [0.5, 0.7, 0.9, 1.2, 1.5, 1.8]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months, y=coca_cola_classic,
        mode='lines+markers',
        name='Coca-Cola Classic',
        line=dict(color=COKE_COLORS['coke_red'], width=4),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=coca_cola_zero,
        mode='lines+markers',
        name='Coca-Cola Zero Sugar',
        line=dict(color=COKE_COLORS['coke_black'], width=4),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=sprite,
        mode='lines+markers',
        name='Sprite',
        line=dict(color='#00B04F', width=4),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=freestyle,
        mode='lines+markers',
        name='Freestyle Systems',
        line=dict(color=COKE_COLORS['executive_blue'], width=4),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title={
            'text': 'Product Performance Trends ($ Millions)',
            'x': 0.5,
            'font': {'size': 20, 'color': 'white'}
        },
        xaxis_title='Month',
        yaxis_title='Revenue ($ Millions)',
        plot_bgcolor='rgba(45, 45, 45, 0.95)',
        paper_bgcolor='rgba(45, 45, 45, 0.95)',
        font=dict(family="Roboto, sans-serif", color="white"),
        xaxis=dict(color="white"),
        yaxis=dict(color="white"),
        height=400
    )
    
    return fig

def create_account_health_map():
    """Create interactive account health map focused on sales intelligence"""
    # Realistic Coca-Cola account data focused on sales concerns
    accounts_data = {
        'Account': [
            'Atlanta Coca-Cola Bottling', 'QuickStop Chain (Northeast)', 'MovieMax Entertainment',
            'Chicago Food Service Group', 'Miami Beach Resort Hotels', 'Dallas MegaMart Centers',
            'Phoenix QSR Partners', 'Seattle Coffee Hub Network', 'Denver Vending Solutions'
        ],
        'Account_Type': [
            'Bottler', 'Retail Chain', 'Entertainment',
            'Food Service', 'Hospitality', 'Retail Chain',
            'QSR Partner', 'Coffee/Convenience', 'Vending/Office'
        ],
        'Latitude': [33.7490, 40.7128, 34.0522, 41.8781, 25.7617, 32.7767, 33.4484, 47.6062, 39.7392],
        'Longitude': [-84.3880, -74.0060, -118.2437, -87.6298, -80.1918, -96.7970, -112.0740, -122.3321, -104.9903],
        'Health_Score': [32, 92, 88, 75, 94, 68, 91, 45, 85],
        'Monthly_Revenue': [675000, 145000, 280000, 190000, 125000, 310000, 95000, 85000, 135000],
        'Churn_Risk': [87, 15, 22, 35, 12, 55, 16, 78, 28],
        'Engagement_Trend': ['Declining', 'Stable', 'Growing', 'Stable', 'Growing', 'Declining', 'Growing', 'Declining', 'Stable'],
        'Primary_Products': [
            'Classic, Zero, Freestyle', 'Classic, Zero, Diet', 'Classic, Zero, Sprite, Powerade',
            'Classic, Zero, Diet, Minute Maid', 'Classic, Sprite, smartwater', 'Classic, Zero, Sprite',
            'Classic, Zero, Powerade', 'Classic, Zero', 'Classic, Diet, Sprite'
        ],
        'Last_Order_Days': [45, 7, 12, 18, 5, 28, 8, 62, 14],
        'Sales_Rep': [
            'Marcus Johnson', 'Jennifer Liu', 'Carlos Rodriguez',
            'Sarah Williams', 'David Kim', 'Lisa Martinez',
            'Robert Chen', 'Amanda Brown', 'Michael Davis'
        ]
    }
    
    df = pd.DataFrame(accounts_data)
    
    # Create risk-based color mapping for sales focus
    df['Color'] = df['Churn_Risk'].apply(lambda x: 
        COKE_COLORS['dark_scarlet'] if x >= 70 else
        COKE_COLORS['coke_red'] if x >= 50 else
        COKE_COLORS['executive_amber'] if x >= 30 else
        COKE_COLORS['executive_green']
    )
    
    # Create size mapping based on revenue
    df['Size'] = (df['Monthly_Revenue'] / 10000).clip(lower=8, upper=40)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scattergeo(
        lon=df['Longitude'],
        lat=df['Latitude'],
        text=df.apply(lambda row: f"""
        <b>{row['Account']}</b><br>
        <b>Type:</b> {row['Account_Type']}<br>
        <b>Sales Rep:</b> {row['Sales_Rep']}<br>
        <b>Health Score:</b> {row['Health_Score']}%<br>
        <b>Monthly Revenue:</b> ${row['Monthly_Revenue']:,}<br>
        <b>Churn Risk:</b> {row['Churn_Risk']}%<br>
        <b>Engagement:</b> {row['Engagement_Trend']}<br>
        <b>Last Order:</b> {row['Last_Order_Days']} days ago<br>
        <b>Products:</b> {row['Primary_Products']}
        """, axis=1),
        mode='markers',
        marker=dict(
            size=df['Size'],
            color=df['Churn_Risk'],
            colorscale=[
                [0, COKE_COLORS['executive_green']],
                [0.3, COKE_COLORS['executive_amber']],
                [0.5, COKE_COLORS['coke_red']],
                [1, COKE_COLORS['dark_scarlet']]
            ],
            cmin=0,
            cmax=100,
            colorbar=dict(
                title="Churn Risk %",
                titleside="right",
                tickmode="linear",
                tick0=0,
                dtick=25
            ),
            line=dict(width=2, color='white'),
            sizemode='diameter',
            sizeref=1
        ),
        hovertemplate='%{text}<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Account Health & Churn Risk Intelligence',
            'x': 0.5,
            'font': {'size': 20, 'color': 'white'}
        },
        geo=dict(
            scope='usa',
            projection_type='albers usa',
            showland=True,
            landcolor='rgb(60, 60, 60)',
            coastlinecolor='rgb(120, 120, 120)',
            bgcolor='rgba(45, 45, 45, 0.95)'
        ),
        height=500,
        font=dict(family="Roboto, sans-serif", color="white"),
        paper_bgcolor='rgba(45, 45, 45, 0.95)',
        plot_bgcolor='rgba(45, 45, 45, 0.95)'
    )
    
    return fig

def create_sales_ai_insights():
    """Create AI insights section focused on actionable sales recommendations"""
    st.markdown("### 🤖 AI Sales Intelligence & Recommendations")
    
    # Critical actions needed
    critical_insights = [
        {
            'title': '🚨 URGENT: Atlanta Coca-Cola Bottling Churn Risk',
            'confidence': 87,
            'impact': '$675K/month',
            'urgency': 'CRITICAL',
            'description': 'AI detected 87% churn probability. Email sentiment analysis shows frustration with "rising costs" and "exploring alternatives". Last order 45 days ago (usual: 14 days).',
            'products': ['Coca-Cola Classic', 'Coca-Cola Zero Sugar', 'Freestyle Systems'],
            'timeline': '24-48 hours',
            'action_items': [
                'Schedule immediate executive call with Marcus Johnson',
                'Prepare volume-based loyalty incentive proposal',
                'Analyze competitor activity in Atlanta region',
                'Review last 6 months communication sentiment'
            ],
            'sales_rep': 'Marcus Johnson',
            'priority': 'CRITICAL'
        },
        {
            'title': '🎯 HIGH OPPORTUNITY: MovieMax Entertainment Freestyle Expansion',
            'confidence': 82,
            'impact': '$420K expansion',
            'urgency': 'HIGH',
            'description': 'AI analysis shows optimal conditions for Coca-Cola Freestyle rollout across 142 theater locations. Current beverage sales up 23%, high customer satisfaction scores.',
            'products': ['Coca-Cola Freestyle', 'Coca-Cola Classic', 'Sprite', 'Powerade'],
            'timeline': '90 days',
            'action_items': [
                'Prepare Freestyle ROI presentation for MovieMax',
                'Schedule site visit to flagship location',
                'Coordinate with Freestyle technical team',
                'Develop phased rollout proposal'
            ],
            'sales_rep': 'Carlos Rodriguez',
            'priority': 'HIGH'
        },
        {
            'title': '⚠️ ENGAGEMENT DECLINE: Seattle Coffee Hub Network',
            'confidence': 78,
            'impact': '$85K/month at risk',
            'urgency': 'MEDIUM',
            'description': 'Communication sentiment dropped 35% over last quarter. No promotional participation. Competitor activity detected through field reports.',
            'products': ['Coca-Cola Classic', 'Coca-Cola Zero Sugar'],
            'timeline': '30 days',
            'action_items': [
                'Schedule relationship rebuild meeting',
                'Propose localized "Share a Coke" campaign',
                'Analyze competitive pricing in Seattle market',
                'Consider exclusive coffee shop partnership'
            ],
            'sales_rep': 'Amanda Brown',
            'priority': 'MEDIUM'
        }
    ]
    
    for i, insight in enumerate(critical_insights):
        with st.expander(f"{insight['title']}", expanded=(i == 0)):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("AI Confidence", f"{insight['confidence']}%")
            with col2:
                st.metric("Revenue Impact", insight['impact'])
            with col3:
                st.metric("Timeline", insight['timeline'])
            
            st.markdown(f"**Description:** {insight['description']}")
            
            st.markdown("**🎯 Recommended Actions:**")
            for action in insight['action_items']:
                st.markdown(f"• {action}")
            
            st.markdown(f"**🥤 Products:** {', '.join(insight['products'])}")
            st.markdown(f"**👤 Sales Rep:** {insight['sales_rep']}")
            
            # Action buttons
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button(f"📞 Contact {insight['sales_rep']}", key=f"contact_{i}"):
                    st.success(f"✅ Message sent to {insight['sales_rep']}")
            with col_b:
                if st.button("📋 Create Action Plan", key=f"plan_{i}"):
                    st.success("✅ Action plan created and assigned")

def main():
    """Main application function"""
    # Load custom CSS
    load_css()
    
    # Create header
    create_header()
    
    # Sidebar navigation
    st.sidebar.markdown("## 🎯 Sales Intelligence Navigation")
    page = st.sidebar.selectbox(
        "Select View",
        ["🏠 Sales Dashboard", "🗺️ Account Health Map", "🤖 AI Recommendations", "📊 Performance Analytics"]
    )
    
    # Add refresh button
    if st.sidebar.button("🔄 Refresh Intelligence"):
        st.rerun()
    
    # Sales team quick access
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👥 Quick Access")
    if st.sidebar.button("📞 Schedule Account Call"):
        st.sidebar.success("✅ Call scheduled via CRM")
    if st.sidebar.button("📧 Alert Sales Manager"):
        st.sidebar.success("✅ Alert sent to manager")
    if st.sidebar.button("📋 Export Account Report"):
        st.sidebar.success("✅ Report generated")
    
    # Main content based on selection
    if page == "🏠 Sales Dashboard":
        st.markdown("## 🎯 Sales Intelligence Dashboard")
        create_sales_intelligence_metrics()
        
        col1, col2 = st.columns([3, 2])
        with col1:
            st.plotly_chart(create_sales_performance_chart(), use_container_width=True)
        with col2:
            st.markdown("### 🔔 Priority Alerts")
            
            # Critical Alert using Streamlit components
            with st.container():
                st.error("🚨 **CRITICAL: Atlanta Bottling**")
                st.markdown("87% churn risk detected - Immediate executive intervention required")
                if st.button("📞 Take Action Now", key="critical_action"):
                    st.success("✅ Executive call scheduled with Atlanta Bottling")
            
            st.markdown("---")
            
            # High Opportunity Alert
            with st.container():
                st.warning("🎯 **OPPORTUNITY: MovieMax Entertainment**")
                st.markdown("$420K Freestyle expansion opportunity ready for execution")
                if st.button("🚀 Pursue Opportunity", key="opportunity_action"):
                    st.success("✅ Freestyle proposal initiated for MovieMax")
    
    elif page == "🗺️ Account Health Map":
        st.markdown("## 🗺️ Account Health & Risk Intelligence")
        st.plotly_chart(create_account_health_map(), use_container_width=True)
        
        # Account summary metrics
        st.markdown("### 📈 Regional Intelligence Summary")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Critical Risk Accounts</p>
                <h2 class="metric-value">3</h2>
                <p class="metric-change change-negative">Immediate Action</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Expansion Ready</p>
                <h2 class="metric-value">15</h2>
                <p class="metric-change change-positive">High Opportunity</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Revenue at Risk</p>
                <h2 class="metric-value">$2.8M</h2>
                <p class="metric-change change-negative">Needs Protection</p>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Avg Health Score</p>
                <h2 class="metric-value">78.5%</h2>
                <p class="metric-change change-positive">Stable</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif page == "🤖 AI Recommendations":
        st.markdown("## 🤖 AI-Powered Sales Recommendations")
        create_sales_ai_insights()
        
        # Action tracking section
        st.markdown("---")
        st.markdown("### 📋 Action Item Tracking")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📞 Schedule Critical Call"):
                st.success("✅ Executive call scheduled with Atlanta Bottling for tomorrow 10 AM")
        with col2:
            if st.button("� Generate Freestyle Proposal"):
                st.success("✅ Freestyle ROI proposal generated for MovieMax Entertainment")
        with col3:
            if st.button("🎯 Create Action Plan"):
                st.success("✅ 30-day action plan created for Seattle Coffee Hub retention")
    
    elif page == "📊 Performance Analytics":
        st.markdown("## 📊 Sales Performance Analytics")
        
        # Product performance metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Coca-Cola Classic</p>
                <h2 class="metric-value">$2.9M</h2>
                <p class="metric-change change-positive">↗ +12% Growth</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Zero Sugar</p>
                <h2 class="metric-value">$2.1M</h2>
                <p class="metric-change change-positive">↗ +18% Growth</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Freestyle Systems</p>
                <h2 class="metric-value">$1.8M</h2>
                <p class="metric-change change-positive">↗ +25% Growth</p>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Total Portfolio</p>
                <h2 class="metric-value">$7.2M</h2>
                <p class="metric-change change-positive">↗ +15% Growth</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.plotly_chart(create_sales_performance_chart(), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: {COKE_COLORS['coke_red']}; font-weight: 600; padding: 1rem;">
        🎯 Coca-Cola Sales AI Agent Framework | Empowering Sales Teams with Intelligent Insights
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
