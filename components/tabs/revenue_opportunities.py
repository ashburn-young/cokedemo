"""
Revenue Opportunities Tab for Coca-Cola Sales AI Platform
Pipeline management, Kanban board, opportunity forecasting
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np
import random

# Coca-Cola Brand Colors
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000',
    'classic_white': '#FFFFFF',
    'executive_blue': '#0078D4',
    'coke_gold': '#FFC72C',
    'success_green': '#28a745',
    'warning_orange': '#ffc107',
    'light_gray': '#f8f9fa',
    'dark_gray': '#6c757d'
}

def generate_mock_opportunities_data():
    """Generate mock opportunities data"""
    stages = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']
    priorities = ['High', 'Medium', 'Low', 'Critical']
    
    opportunities = []
    for i in range(50):
        opportunity = {
            'id': f'OPP-{i+1:03d}',
            'name': f'Opportunity {i+1}',
            'account': f'Account {random.randint(1, 20)}',
            'stage': random.choice(stages),
            'value': random.randint(10000, 500000),
            'probability': random.randint(10, 95),
            'close_date': datetime.now() + timedelta(days=random.randint(1, 365)),
            'product': random.choice(['Coca-Cola Classic', 'Diet Coke', 'Coke Zero', 'Sprite', 'Fanta']),
            'region': random.choice(['North', 'South', 'East', 'West', 'Central']),
            'priority': random.choice(priorities),
            'ai_score': random.randint(1, 100),
            'expected_revenue': random.randint(10000, 500000) * random.uniform(0.1, 0.95)
        }
        opportunities.append(opportunity)
    
    return pd.DataFrame(opportunities)

def generate_mock_accounts_data():
    """Generate mock accounts data"""
    accounts = []
    for i in range(20):
        account = {
            'id': f'ACC-{i+1:03d}',
            'name': f'Account {i+1}',
            'type': random.choice(['Enterprise', 'SMB', 'Strategic']),
            'revenue': random.randint(100000, 2000000),
            'region': random.choice(['North', 'South', 'East', 'West', 'Central']),
            'industry': random.choice(['Retail', 'Food Service', 'Convenience', 'Grocery']),
            'health_score': random.randint(1, 100),
            'total_opportunities': random.randint(1, 10)
        }
        accounts.append(account)
    
    return pd.DataFrame(accounts)

def render_kanban_board(opportunities_df: pd.DataFrame):
    """Render interactive Kanban board for opportunity pipeline"""
    
    stages = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']
    stage_colors = {
        'Prospecting': '#E8F4FD',
        'Qualification': '#D1E7DD', 
        'Proposal': '#FFF3CD',
        'Negotiation': '#F8D7DA',
        'Closed Won': '#D4EDDA',
        'Closed Lost': '#F5C6CB'
    }
    
    cols = st.columns(len(stages))
    
    for i, stage in enumerate(stages):
        with cols[i]:
            stage_opps = opportunities_df[opportunities_df['stage'] == stage]
            stage_value = stage_opps['value'].sum()
            
            # Simple approach: colored background with white text box overlay
            st.markdown(f"""
            <div style="
                background: {stage_colors[stage]};
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 10px;
                border: 2px solid #333;
                position: relative;
            ">
                <div style="
                    background: white;
                    color: black;
                    padding: 10px;
                    border-radius: 5px;
                    text-align: center;
                    border: 1px solid #000;
                ">
                    <strong style="font-size: 16px; color: black;">{stage}</strong><br>
                    <span style="font-size: 14px; color: black; font-weight: bold;">{len(stage_opps)} opps • ${stage_value:,.0f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Show top opportunities in this stage
            for _, opp in stage_opps.head(3).iterrows():
                probability_color = COKE_COLORS['success_green'] if opp['probability'] > 0.7 else COKE_COLORS['warning_orange']
                
                st.markdown(f"""
                <div style="
                    background: white;
                    padding: 8px;
                    border-radius: 6px;
                    margin: 5px 0;
                    border-left: 3px solid {COKE_COLORS['primary_red']};
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    cursor: move;
                ">
                    <h6 style="margin: 0; font-size: 12px; color: {COKE_COLORS['coke_black']};">
                        {opp['name'][:20]}...
                    </h6>
                    <p style="margin: 2px 0; font-size: 11px; color: {COKE_COLORS['coke_black']}; font-weight: 500;">
                        <strong style="color: {COKE_COLORS['coke_black']};">${opp['value']:,.0f}</strong>
                    </p>
                    <p style="margin: 2px 0; font-size: 10px; color: {probability_color}; font-weight: 600;">
                        {opp['probability']:.0%} probability
                    </p>
                    <p style="margin: 0; font-size: 9px; color: {COKE_COLORS['dark_gray']}; font-weight: 500;">
                        {opp['close_date'].strftime('%Y-%m-%d')}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            if len(stage_opps) > 3:
                st.markdown(f"<small>+ {len(stage_opps) - 3} more deals</small>", unsafe_allow_html=True)


def render_revenue_opportunities():
    """Main function to render the Revenue Opportunities tab"""
    
    st.markdown("# 💰 Revenue Opportunities & Pipeline Management")
    st.markdown("*AI-powered opportunity scoring, pipeline forecasting, and deal acceleration*")
    
    # Generate mock data
    try:
        opportunities_df = generate_mock_opportunities_data()
        accounts_df = generate_mock_accounts_data()
    except Exception as e:
        st.error(f"Error generating data: {e}")
        return
    
    # === TOP METRICS ===
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_pipeline = opportunities_df['value'].sum()
    weighted_pipeline = (opportunities_df['value'] * opportunities_df['probability']).sum()
    avg_deal_size = opportunities_df['value'].mean()
    deals_this_quarter = len(opportunities_df[opportunities_df['close_date'] <= pd.Timestamp.now() + pd.Timedelta(days=90)])
    
    with col1:
        st.metric("💰 Total Pipeline", f"${total_pipeline:,.0f}", "12% vs last month")
    
    with col2:
        st.metric("🎯 Weighted Pipeline", f"${weighted_pipeline:,.0f}", "8% vs last month")
    
    with col3:
        st.metric("📊 Avg Deal Size", f"${avg_deal_size:,.0f}", "5% vs last month")
    
    with col4:
        st.metric("📅 Q4 Forecasted Deals", deals_this_quarter, "15% vs Q3")
    
    with col5:
        st.metric("⏱️ Avg Sales Cycle", "45 days", "-3 days vs last quarter")
    
    st.markdown("---")
    
    # === FILTERS & CONTROLS ===
    st.markdown("### 🎛️ Pipeline Filters & Controls")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        stage_filter = st.multiselect(
            "Filter by Stage",
            options=opportunities_df['stage'].unique(),
            default=opportunities_df['stage'].unique()
        )
    
    with col2:
        priority_filter = st.multiselect(
            "Filter by Priority",
            options=opportunities_df['priority'].unique(),
            default=opportunities_df['priority'].unique()
        )
    
    with col3:
        min_value = st.number_input("Min Deal Value", value=0, step=10000)
    
    with col4:
        forecast_period = st.selectbox(
            "Forecast Period",
            ["Next 30 Days", "Next Quarter", "Next 6 Months", "Next Year"],
            index=1
        )
    
    # Apply filters
    filtered_opps = opportunities_df[
        (opportunities_df['stage'].isin(stage_filter)) &
        (opportunities_df['priority'].isin(priority_filter)) &
        (opportunities_df['value'] >= min_value)
    ]
    
    st.markdown("---")
    
    # === QUICK ACTIONS ===
    st.markdown("### ⚡ Quick Actions")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🔄 Refresh Pipeline", use_container_width=True):
            st.success("✅ Pipeline data refreshed!")
    
    with col2:
        if st.button("📊 Generate Forecast", use_container_width=True):
            st.success("✅ Forecast generated!")
            
            # Calculate forecast metrics
            q1_forecast = opportunities_df[
                opportunities_df['close_date'] <= pd.Timestamp.now() + pd.Timedelta(days=90)
            ]['value'].sum() * 0.8  # Apply conversion rate
            
            q2_forecast = opportunities_df[
                (opportunities_df['close_date'] > pd.Timestamp.now() + pd.Timedelta(days=90)) &
                (opportunities_df['close_date'] <= pd.Timestamp.now() + pd.Timedelta(days=180))
            ]['value'].sum() * 0.7
            
            col_f1, col_f2, col_f3 = st.columns(3)
            with col_f1:
                st.metric("Q1 Forecast", f"${q1_forecast:,.0f}", "15% ↗️")
            with col_f2:
                st.metric("Q2 Forecast", f"${q2_forecast:,.0f}", "8% ↗️")
            with col_f3:
                st.metric("Confidence", "82%", "High")
    
    with col3:
        if st.button("🎯 Identify Hot Leads", use_container_width=True):
            st.success("✅ Hot leads identified!")
            
            # Filter for hot leads (high value, high probability, recent activity)
            hot_leads = opportunities_df[
                (opportunities_df['value'] > opportunities_df['value'].quantile(0.7)) &
                (opportunities_df['probability'] > 70) &
                (opportunities_df['ai_score'] > 75)
            ].head(5)
            
            if len(hot_leads) > 0:
                st.markdown("#### 🔥 Top Hot Leads Identified:")
                for _, lead in hot_leads.iterrows():
                    with st.container():
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(90deg, {COKE_COLORS['primary_red']}20, {COKE_COLORS['success_green']}20);
                            padding: 15px;
                            border-radius: 8px;
                            margin: 10px 0;
                            border-left: 4px solid {COKE_COLORS['primary_red']};
                        ">
                            <h5 style="margin: 0; color: {COKE_COLORS['coke_black']};">🎯 {lead['name']}</h5>
                            <p style="margin: 5px 0; color: {COKE_COLORS['coke_black']};">
                                <strong>Account:</strong> {lead['account']} | 
                                <strong>Value:</strong> ${lead['value']:,.0f} | 
                                <strong>Probability:</strong> {lead['probability']:.0%} | 
                                <strong>AI Score:</strong> {lead['ai_score']}/100
                            </p>
                            <p style="margin: 5px 0; color: {COKE_COLORS['coke_black']};">
                                <strong>Stage:</strong> {lead['stage']} | 
                                <strong>Close Date:</strong> {lead['close_date'].strftime('%Y-%m-%d')}
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("No hot leads found matching the criteria.")
    
    with col4:
        if st.button("📧 Send Follow-ups", use_container_width=True):
            st.success("✅ Follow-up emails queued!")
            
            # Find opportunities that need follow-ups (older opportunities with low probability)
            follow_up_needed = opportunities_df[
                (opportunities_df['probability'] < 50) &
                (opportunities_df['stage'].isin(['Prospecting', 'Qualification']))
            ].head(3)
            
            if len(follow_up_needed) > 0:
                st.markdown("#### 📧 Follow-ups Scheduled:")
                for _, opp in follow_up_needed.iterrows():
                    st.markdown(f"""
                    <div style="
                        background: {COKE_COLORS['warning_orange']}20;
                        padding: 10px;
                        border-radius: 5px;
                        margin: 5px 0;
                        border-left: 3px solid {COKE_COLORS['warning_orange']};
                    ">
                        📧 <strong>{opp['account']}</strong> - {opp['name']} (${opp['value']:,.0f})
                        <br><small>Probability: {opp['probability']:.0%} | Stage: {opp['stage']}</small>
                    </div>
                    """, unsafe_allow_html=True)
    
    with col5:
        if st.button("📈 Export Report", use_container_width=True):
            st.success("✅ Report exported!")
    
    st.markdown("---")
    
    # === KANBAN BOARD ===
    st.markdown("### 📋 Pipeline Kanban Board")
    render_kanban_board(filtered_opps)
    
    st.markdown("---")
    
    # === PIPELINE ANALYTICS ===
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Pipeline Velocity & Trends")
        
        # Create pipeline flow analysis
        stage_conversion = {
            'Prospecting': 0.25,
            'Qualification': 0.40,
            'Proposal': 0.60,
            'Negotiation': 0.80,
            'Closed Won': 1.0
        }
        
        stages = list(stage_conversion.keys())
        values = []
        
        for stage in stages:
            stage_opps = filtered_opps[filtered_opps['stage'] == stage]
            weighted_value = (stage_opps['value'] * stage_opps['probability']).sum()
            values.append(weighted_value)
        
        fig = go.Figure(go.Funnel(
            y=stages,
            x=values,
            textinfo="value+percent initial",
            marker=dict(
                color=[COKE_COLORS['primary_red'], COKE_COLORS['warning_orange'], 
                       COKE_COLORS['coke_gold'], COKE_COLORS['executive_blue'], 
                       COKE_COLORS['success_green']]
            )
        ))
        
        fig.update_layout(
            title="Pipeline Flow & Conversion",
            height=400,
            font=dict(size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="pipeline_funnel_chart")
    
    with col2:
        st.markdown("### 🎯 Opportunity Scoring & Prioritization")
        
        # Create opportunity scoring chart
        scoring_data = filtered_opps.copy()
        scoring_data['ai_score'] = (
            scoring_data['probability'] * 0.4 +
            (scoring_data['value'] / scoring_data['value'].max()) * 0.3 +
            np.random.random(len(scoring_data)) * 0.3
        )
        
        fig = px.scatter(
            scoring_data, 
            x='value', 
            y='probability',
            size='ai_score',
            color='stage',
            hover_data=['name', 'account'],
            title="Opportunity Value vs Probability",
            color_discrete_map={
                'Prospecting': COKE_COLORS['primary_red'],
                'Qualification': COKE_COLORS['warning_orange'],
                'Proposal': COKE_COLORS['coke_gold'],
                'Negotiation': COKE_COLORS['executive_blue'],
                'Closed Won': COKE_COLORS['success_green']
            }
        )
        
        fig.update_layout(
            height=400,
            xaxis_title="Deal Value ($)",
            yaxis_title="Probability",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="opportunity_scoring_chart")
    
    st.markdown("---")
    
    # === TOP OPPORTUNITIES ===
    st.markdown("### 🏆 Top Priority Opportunities")
    
    # Sort by AI score and show top 10
    top_opps = filtered_opps.nlargest(10, 'value')
    
    for _, opp in top_opps.iterrows():
        priority_color = {
            'Critical': COKE_COLORS['primary_red'],
            'High': COKE_COLORS['warning_orange'],
            'Medium': COKE_COLORS['executive_blue'],
            'Low': COKE_COLORS['light_gray']
        }.get(opp['priority'], COKE_COLORS['light_gray'])
        
        with st.expander(f"💰 {opp['name']} - ${opp['value']:,.0f}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**Account Details**")
                st.markdown(f"**Company:** {opp['account']}")
                st.markdown(f"**Stage:** {opp['stage']}")
                st.markdown(f"**Priority:** {opp['priority']}")
                st.markdown(f"**Probability:** {opp['probability']:.0%}")
            
            with col2:
                st.markdown("**Financial Information**")
                st.markdown(f"**Deal Value:** ${opp['value']:,.0f}")
                st.markdown(f"**Expected Close:** {opp['close_date'].strftime('%Y-%m-%d')}")
                st.markdown(f"**Deal Type:** {opp.get('deal_type', 'New Business')}")
                st.markdown(f"**Product Line:** {opp.get('product_line', 'Mixed')}")
            
            with col3:
                st.markdown("**Next Actions**")
                if opp['stage'] == 'Prospecting':
                    st.markdown("- Schedule discovery call")
                    st.markdown("- Send product information")
                elif opp['stage'] == 'Qualification':
                    st.markdown("- Conduct needs assessment")
                    st.markdown("- Identify decision makers")
                elif opp['stage'] == 'Proposal':
                    st.markdown("- Follow up on proposal")
                    st.markdown("- Address any concerns")
                elif opp['stage'] == 'Negotiation':
                    st.markdown("- Finalize terms")
                    st.markdown("- Prepare contract")
                
                # Action buttons
                button_col1, button_col2 = st.columns(2)
                with button_col1:
                    if st.button(f"📞 Call Client", key=f"call_{opp['id']}"):
                        st.success("✅ Call scheduled!")
                
                with button_col2:
                    if st.button(f"📧 Send Email", key=f"email_{opp['id']}"):
                        st.success("✅ Email sent!")
    
    st.markdown("---")
    
    # === FORECAST ANALYSIS ===
    st.markdown("### 📊 Sales Forecast & Trend Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Monthly Forecast Trend")
        
        # Generate forecast data
        months = pd.date_range(start='2024-01-01', periods=12, freq='M')
        forecast_values = [
            2500000, 2800000, 2600000, 3200000, 2900000, 3500000,
            3800000, 3600000, 4200000, 4000000, 4500000, 4800000
        ]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=months,
            y=forecast_values,
            mode='lines+markers',
            name='Forecast',
            line=dict(color=COKE_COLORS['primary_red'], width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="12-Month Revenue Forecast",
            xaxis_title="Month",
            yaxis_title="Revenue ($)",
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="forecast_trend_chart")
    
    with col2:
        st.markdown("#### 📊 Win Rate by Stage")
        
        stages = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation']
        win_rates = [0.25, 0.45, 0.65, 0.85]
        
        fig = go.Figure(data=[
            go.Bar(
                x=stages,
                y=win_rates,
                marker_color=[COKE_COLORS['primary_red'], COKE_COLORS['warning_orange'], 
                             COKE_COLORS['coke_gold'], COKE_COLORS['success_green']]
            )
        ])
        
        fig.update_layout(
            title="Win Rate by Pipeline Stage",
            xaxis_title="Stage",
            yaxis_title="Win Rate (%)",
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        fig.update_yaxes(tickformat='.0%')
        
        st.plotly_chart(fig, use_container_width=True, key="win_rate_chart")
    
    # === AI INSIGHTS ===
    st.markdown("---")
    st.markdown("### 🤖 AI-Powered Pipeline Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🎯 Deal Acceleration Opportunities")
        st.success("✅ Metro Restaurant Group: Schedule final demo to close by month-end")
        st.warning("⚠️ Golden Gate Grocers: Address pricing concerns within 48 hours")
        st.info("ℹ️ Summit Entertainment: Introduce Freestyle technology for competitive edge")
    
    with col2:
        st.markdown("#### 🚨 Risk Alerts")
        st.error("❗ Pacific Food Distributors: No activity in 14 days - risk of stalling")
        st.warning("⚠️ Central Valley Markets: Competitor mentioned in last call")
        st.warning("⚠️ West Coast Beverages: Budget approval delayed - follow up needed")
    
    with col3:
        st.markdown("#### 💡 Recommendations")
        st.success("✅ Focus on Q4 opportunities > $500K for maximum impact")
        st.info("ℹ️ Increase Freestyle positioning in QSR segment")
        st.info("ℹ️ Leverage health trends for Zero Sugar product line")


if __name__ == "__main__":
    render_revenue_opportunities()
