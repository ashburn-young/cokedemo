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

# Import widgets and data
import sys
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from widgets.proactive_widgets import ProactiveWidgets, COKE_COLORS

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
            
            st.markdown(f"""
            <div style="
                background: {stage_colors[stage]};
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 10px;
                border: 1px solid #ddd;
            ">
                <h4 style="margin: 0; text-align: center; color: #000000 !important; font-weight: bold;">
                    {stage}
                </h4>
                <p style="margin: 5px 0; text-align: center; font-weight: bold; color: #000000 !important; font-size: 14px;">
                    {len(stage_opps)} opps • ${stage_value:,.0f}
                </p>
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
                        {opp['opportunity_name'][:20]}...
                    </h6>
                    <p style="margin: 2px 0; font-size: 11px; color: #666;">
                        <strong style="color: #000000;">${opp['value']:,.0f}</strong>
                    </p>
                    <p style="margin: 2px 0; font-size: 10px; color: {probability_color};">
                        {opp['probability']:.0%} probability
                    </p>
                    <p style="margin: 0; font-size: 9px; color: #888;">
                        {opp['expected_close_date']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            if len(stage_opps) > 3:
                st.markdown(f"<small>+ {len(stage_opps) - 3} more deals</small>", unsafe_allow_html=True)


def render_revenue_opportunities():
    """Main function to render the Revenue Opportunities tab"""
    
    st.markdown("# 💰 Revenue Opportunities & Pipeline Management")
    st.markdown("*AI-powered opportunity scoring, pipeline forecasting, and deal acceleration*")
    
    # Import and prepare data
    try:
        from data.enhanced_data_generator import enhanced_data_generator
        data = enhanced_data_generator()
        opportunities_df = data['opportunities']
        accounts_df = data['accounts']
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return
    
    # === TOP METRICS ===
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_pipeline = opportunities_df['value'].sum()
    weighted_pipeline = (opportunities_df['value'] * opportunities_df['probability']).sum()
    avg_deal_size = opportunities_df['value'].mean()
    deals_this_quarter = len(opportunities_df[opportunities_df['expected_close_date'] <= pd.Timestamp.now() + pd.Timedelta(days=90)])
    
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
    
    with col3:
        if st.button("🎯 Identify Hot Leads", use_container_width=True):
            st.success("✅ Hot leads identified!")
    
    with col4:
        if st.button("📧 Send Follow-ups", use_container_width=True):
            st.success("✅ Follow-up emails queued!")
    
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
            hover_data=['opportunity_name', 'company_name'],
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
        
        with st.expander(f"💰 {opp['opportunity_name']} - ${opp['value']:,.0f}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**Account Details**")
                st.markdown(f"**Company:** {opp['company_name']}")
                st.markdown(f"**Stage:** {opp['stage']}")
                st.markdown(f"**Priority:** {opp['priority']}")
                st.markdown(f"**Probability:** {opp['probability']:.0%}")
            
            with col2:
                st.markdown("**Financial Information**")
                st.markdown(f"**Deal Value:** ${opp['value']:,.0f}")
                st.markdown(f"**Expected Close:** {opp['expected_close_date']}")
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
                    if st.button(f"📞 Call Client", key=f"call_{opp['opportunity_id']}"):
                        st.success("✅ Call scheduled!")
                
                with button_col2:
                    if st.button(f"📧 Send Email", key=f"email_{opp['opportunity_id']}"):
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
        
        fig.update_yaxis(tickformat='.0%')
        
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
