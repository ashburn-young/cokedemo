"""
Executive Overview Tab for Coca-Cola Sales AI Platform
High-level KPIs, top opportunities, and executive insights
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Any
import sys
import os

# Add components to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widgets.proactive_widgets import ProactiveWidgets, COKE_COLORS
from data.enhanced_data_generator import EnhancedDataGenerator

def render_executive_overview():
    """Render the Executive Overview tab with KPIs and top opportunities"""
    
    st.markdown("# 🎯 Executive Overview")
    st.markdown("*Strategic insights and key performance indicators for Coca-Cola sales leadership*")
    
    # Generate enhanced data
    data_gen = EnhancedDataGenerator()
    accounts_df = data_gen.generate_enhanced_accounts(150)
    opportunities_df = data_gen.generate_enhanced_opportunities(300, accounts_df) 
    engagement_df = data_gen.generate_engagement_history(500, accounts_df)
    
    # === TOP METRICS ROW ===
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = accounts_df['annual_revenue'].sum()
        ProactiveWidgets.priority_alert_card(
            "Annual Revenue",
            f"${total_revenue/1e6:.1f}M",
            "+12.5% vs LY",
            COKE_COLORS['primary_red'],
            "💰"
        )
    
    with col2:
        total_opportunities = len(opportunities_df)
        pipeline_value = opportunities_df['value'].sum()
        ProactiveWidgets.priority_alert_card(
            "Pipeline Value", 
            f"${pipeline_value/1e6:.1f}M",
            f"{total_opportunities} opportunities",
            COKE_COLORS['executive_blue'],
            "🎯"
        )
    
    with col3:
        avg_health = accounts_df['health_score'].mean()
        ProactiveWidgets.priority_alert_card(
            "Account Health",
            f"{avg_health:.1%}",
            "+3.2% vs last month",
            COKE_COLORS['success_green'],
            "💚"
        )
    
    with col4:
        high_risk_accounts = len(accounts_df[accounts_df['churn_risk'] == 'High'])
        ProactiveWidgets.priority_alert_card(
            "At-Risk Accounts", 
            str(high_risk_accounts),
            "Immediate attention needed",
            COKE_COLORS['warning_orange'],
            "⚠️"
        )
    
    st.markdown("---")
    
    # === STRATEGIC INSIGHTS ===
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📈 Revenue Performance by Region")
        
        # Calculate regional performance
        regional_revenue = accounts_df.groupby('region').agg({
            'annual_revenue': 'sum',
            'health_score': 'mean',
            'churn_risk': lambda x: (x == 'High').sum()
        }).round(2)
        
        regional_revenue['revenue_millions'] = regional_revenue['annual_revenue'] / 1e6
        
        fig = px.bar(
            regional_revenue.reset_index(),
            x='region',
            y='revenue_millions',
            color='health_score',
            color_continuous_scale=['#FF6B6B', '#4ECDC4', '#45B7D1'],
            title="Regional Revenue Performance ($M)",
            labels={'revenue_millions': 'Revenue ($M)', 'region': 'Region'}
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#2c3e50'),
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🚨 Priority Actions")
        
        # High-priority opportunities
        high_value_opps = opportunities_df.nlargest(5, 'value')
        
        for _, opp in high_value_opps.iterrows():
            probability_color = COKE_COLORS['success_green'] if opp['probability'] > 0.7 else COKE_COLORS['warning_orange']
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 15px;
                border-radius: 10px;
                margin: 10px 0;
                border-left: 4px solid {COKE_COLORS['primary_red']};
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            ">
                <h4 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{opp['opportunity_name']}</h4>
                <p style="margin: 5px 0; color: {COKE_COLORS['coke_black']}; font-weight: 500;"><strong>${opp['value']:,.0f}</strong> • 
                <span style="color: {probability_color};">{opp['probability']:.0%} probability</span></p>
                <p style="margin: 0; font-size: 12px; color: {COKE_COLORS['dark_gray']};">Expected close: {opp['expected_close_date']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # === MARKET INSIGHTS ===
    st.markdown("---")
    st.markdown("### 🎯 Market Intelligence & Competitive Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📊 Product Performance")
        
        # Simulate product performance data
        product_data = {
            'Product': ['Coca-Cola Classic', 'Coke Zero', 'Diet Coke', 'Sprite', 'Fanta'],
            'Market Share': [0.42, 0.18, 0.15, 0.12, 0.08],
            'Growth': [0.03, 0.15, -0.02, 0.08, 0.05]
        }
        product_df = pd.DataFrame(product_data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=product_df['Market Share'],
            y=product_df['Growth'],
            mode='markers+text',
            text=product_df['Product'],
            textposition='top center',
            marker=dict(
                size=20,
                color=COKE_COLORS['primary_red'],
                line=dict(width=2, color='white')
            )
        ))
        
        fig.update_layout(
            title="Product Portfolio Matrix",
            xaxis_title="Market Share",
            yaxis_title="Growth Rate",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 🏆 Top Performing Sales Reps")
        
        # Generate rep performance data
        rep_performance = pd.DataFrame({
            'Rep': ['Sarah Chen', 'Mike Rodriguez', 'Jennifer Smith', 'David Kim', 'Lisa Johnson'],
            'Revenue': [850000, 720000, 680000, 650000, 620000],
            'Quota Attainment': [1.15, 1.08, 1.02, 0.98, 0.95]
        })
        
        for _, rep in rep_performance.iterrows():
            quota_color = COKE_COLORS['success_green'] if rep['Quota Attainment'] >= 1.0 else COKE_COLORS['warning_orange']
            
            st.markdown(f"""
            <div style="
                background: linear-gradient(90deg, {COKE_COLORS['light_gray']}, white);
                padding: 10px;
                border-radius: 8px;
                margin: 5px 0;
                border-left: 3px solid {quota_color};
            ">
                <strong style="color: {COKE_COLORS['coke_black']}; font-size: 16px;">{rep['Rep']}</strong><br>
                <span style="color: {COKE_COLORS['coke_black']};">${rep['Revenue']:,.0f}</span> • 
                <span style="color: {quota_color};">{rep['Quota Attainment']:.0%} quota</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("#### 🎲 AI-Powered Recommendations")
        
        recommendations = [
            {
                "title": "Focus on Freestyle Expansion",
                "impact": "High",
                "description": "3 key accounts ready for Freestyle machine upgrades",
                "action": "Schedule demos this week"
            },
            {
                "title": "Churn Prevention Campaign", 
                "impact": "Critical",
                "description": "5 high-value accounts showing decline signals",
                "action": "Deploy retention specialists"
            },
            {
                "title": "Cross-Sell Opportunity",
                "impact": "Medium", 
                "description": "Premium accounts underutilizing product portfolio",
                "action": "Launch targeted campaign"
            }
        ]
        
        for rec in recommendations:
            impact_color = {
                'Critical': COKE_COLORS['primary_red'],
                'High': COKE_COLORS['warning_orange'],
                'Medium': COKE_COLORS['executive_blue']
            }.get(rec['impact'], COKE_COLORS['light_gray'])
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 12px;
                border-radius: 8px;
                margin: 8px 0;
                border: 1px solid {impact_color};
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{rec['title']}</h5>
                <p style="margin: 5px 0; font-size: 12px; color: {COKE_COLORS['coke_black']};">{rec['description']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="
                        background: {impact_color};
                        color: white;
                        padding: 2px 8px;
                        border-radius: 12px;
                        font-size: 10px;
                        font-weight: bold;
                    ">{rec['impact']}</span>
                    <span style="font-size: 11px; color: {COKE_COLORS['dark_gray']}; font-weight: 500;">{rec['action']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # === QUICK ACTIONS ===
    st.markdown("---")
    
    quick_actions = [
        {"icon": "📊", "label": "Generate Weekly Report", "action": "generate_report"},
        {"icon": "🎯", "label": "Review Top Opportunities", "action": "review_opportunities"},
        {"icon": "⚠️", "label": "Address At-Risk Accounts", "action": "address_risks"},
        {"icon": "📞", "label": "Schedule Executive Briefing", "action": "schedule_briefing"}
    ]
    
    selected_action = ProactiveWidgets.action_button_panel(quick_actions)
    
    if selected_action:
        st.info(f"✅ Action '{selected_action}' has been initiated. You will receive updates shortly.")
