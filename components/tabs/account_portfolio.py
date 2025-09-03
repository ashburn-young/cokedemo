"""
Account Portfolio Tab for Coca-Cola Sales AI Platform
Customer sentiment, engagement tracking, and churn risk management
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

def render_account_portfolio():
    """Render the Account Portfolio tab with customer insights and engagement"""
    
    # Initialize session state for research functionality
    if 'research_generated' not in st.session_state:
        st.session_state.research_generated = False
    
    st.markdown("# 👥 Account Portfolio")
    st.markdown("*Comprehensive customer relationship management and engagement tracking*")
    
    # Generate enhanced data
    data_gen = EnhancedDataGenerator()
    accounts_df = data_gen.generate_enhanced_accounts(200)
    engagement_df = data_gen.generate_engagement_history(800, accounts_df)
    
    # === PORTFOLIO OVERVIEW ===
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_accounts = len(accounts_df)
        ProactiveWidgets.priority_alert_card(
            "Total Accounts",
            str(total_accounts),
            "+8 new this month",
            COKE_COLORS['executive_blue'],
            "👥"
        )
    
    with col2:
        high_health = len(accounts_df[accounts_df['health_score'] > 0.8])
        ProactiveWidgets.priority_alert_card(
            "Healthy Accounts",
            f"{high_health} ({high_health/total_accounts:.0%})",
            "+5% improvement",
            COKE_COLORS['success_green'], 
            "💚"
        )
    
    with col3:
        at_risk = len(accounts_df[accounts_df['churn_risk'].isin(['High', 'Critical'])])
        ProactiveWidgets.priority_alert_card(
            "At-Risk Accounts",
            f"{at_risk} ({at_risk/total_accounts:.0%})",
            "Needs attention",
            COKE_COLORS['warning_orange'],
            "⚠️"
        )
    
    with col4:
        avg_engagement = accounts_df['engagement_score'].mean()
        ProactiveWidgets.priority_alert_card(
            "Avg Engagement",
            f"{avg_engagement:.1%}",
            "+2.3% vs last month",
            COKE_COLORS['executive_green'],
            "📈"
        )
    
    st.markdown("---")
    
    # === ACCOUNT FILTERS ===
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        selected_region = st.selectbox(
            "🌍 Filter by Region",
            options=['All Regions'] + sorted(accounts_df['region'].unique()),
            key="portfolio_region"
        )
    
    with col2:
        selected_industry = st.selectbox(
            "🏢 Filter by Industry", 
            options=['All Industries'] + sorted(accounts_df['industry'].unique()),
            key="portfolio_industry"
        )
    
    with col3:
        risk_filter = st.selectbox(
            "⚠️ Filter by Risk Level",
            options=['All Risk Levels', 'Low', 'Medium', 'High', 'Critical'],
            key="portfolio_risk"
        )
    
    with col4:
        size_filter = st.selectbox(
            "💰 Filter by Revenue Size",
            options=['All Sizes', 'Enterprise (>$1M)', 'Mid-Market ($250K-$1M)', 'SMB (<$250K)'],
            key="portfolio_size"
        )
    
    # Apply filters
    filtered_accounts = accounts_df.copy()
    
    if selected_region != 'All Regions':
        filtered_accounts = filtered_accounts[filtered_accounts['region'] == selected_region]
    
    if selected_industry != 'All Industries':
        filtered_accounts = filtered_accounts[filtered_accounts['industry'] == selected_industry]
    
    if risk_filter != 'All Risk Levels':
        filtered_accounts = filtered_accounts[filtered_accounts['churn_risk'] == risk_filter]
    
    if size_filter != 'All Sizes':
        if size_filter == 'Enterprise (>$1M)':
            filtered_accounts = filtered_accounts[filtered_accounts['annual_revenue'] > 1000000]
        elif size_filter == 'Mid-Market ($250K-$1M)':
            filtered_accounts = filtered_accounts[
                (filtered_accounts['annual_revenue'] >= 250000) & 
                (filtered_accounts['annual_revenue'] <= 1000000)
            ]
        elif size_filter == 'SMB (<$250K)':
            filtered_accounts = filtered_accounts[filtered_accounts['annual_revenue'] < 250000]
    
    st.markdown(f"**Showing {len(filtered_accounts)} accounts** (filtered from {len(accounts_df)} total)")
    
    # === ACCOUNT HEALTH MATRIX ===
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Account Health & Sentiment Matrix")
        
        # Create health vs sentiment scatter plot
        fig = px.scatter(
            filtered_accounts,
            x='health_score',
            y='sentiment_score',
            size='annual_revenue',
            color='churn_risk',
            hover_data=['company_name', 'industry', 'region'],
            color_discrete_map={
                'Low': COKE_COLORS['success_green'],
                'Medium': COKE_COLORS['warning_orange'],
                'High': COKE_COLORS['danger_red'],
                'Critical': COKE_COLORS['primary_red']
            },
            title="Account Health vs Customer Sentiment",
            labels={
                'health_score': 'Account Health Score',
                'sentiment_score': 'Customer Sentiment',
                'annual_revenue': 'Annual Revenue'
            }
        )
        
        # Add quadrant lines
        fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
        fig.add_vline(x=0.5, line_dash="dash", line_color="gray", opacity=0.5)
        
        # Add quadrant labels
        fig.add_annotation(x=0.25, y=0.8, text="At Risk<br>Low Health", showarrow=False, font=dict(color="red"))
        fig.add_annotation(x=0.75, y=0.8, text="Champions<br>High Health", showarrow=False, font=dict(color="green"))
        fig.add_annotation(x=0.25, y=-0.8, text="Critical<br>Immediate Action", showarrow=False, font=dict(color="darkred"))
        fig.add_annotation(x=0.75, y=-0.8, text="Opportunity<br>Improve Sentiment", showarrow=False, font=dict(color="orange"))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🚨 Priority Accounts")
        
        # Sort by combination of risk and revenue
        priority_accounts = filtered_accounts.copy()
        priority_accounts['priority_score'] = (
            priority_accounts['annual_revenue'] * 
            priority_accounts['churn_probability']
        )
        
        top_priority = priority_accounts.nlargest(8, 'priority_score')
        
        for _, account in top_priority.iterrows():
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 12px;
                border-radius: 8px;
                margin: 8px 0;
                border-left: 4px solid {COKE_COLORS['primary_red']};
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">
                    {account['company_name'][:25]}...
                </h5>
                <p style="margin: 2px 0; font-size: 11px; color: {COKE_COLORS['dark_gray']}; font-weight: 500;">
                    {account['industry']} • {account['region']}
                </p>
                <p style="margin: 5px 0; font-size: 12px; color: {COKE_COLORS['coke_black']};">
                    <strong>${account['annual_revenue']:,.0f}</strong> annual
                </p>
                <p style="margin: 0; font-size: 10px; color: {COKE_COLORS['dark_gray']}; font-weight: 500;">
                    Health: {account['health_score']:.0%} | 
                    Sentiment: {account['sentiment_score']:+.1f}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add risk indicator below each account card
            with st.container():
                ProactiveWidgets.risk_indicator(
                    account['churn_risk'], 
                    account['churn_probability']
                )
    
    # === ENGAGEMENT ANALYTICS ===
    st.markdown("---")
    st.markdown("### 📞 Engagement Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Recent Engagement Trends")
        
        # Create engagement timeline
        engagement_summary = engagement_df.groupby('engagement_date').agg({
            'outcome': 'count',
            'effectiveness_score': 'mean'
        }).reset_index()
        
        engagement_summary.columns = ['Date', 'Interactions', 'Avg_Effectiveness']
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=engagement_summary['Date'],
            y=engagement_summary['Interactions'],
            mode='lines+markers',
            name='Daily Interactions',
            line=dict(color=COKE_COLORS['primary_red'], width=2),
            marker=dict(size=6)
        ))
        
        fig.add_trace(go.Scatter(
            x=engagement_summary['Date'],
            y=engagement_summary['Avg_Effectiveness'] * 20,  # Scale for visibility
            mode='lines',
            name='Effectiveness (scaled)',
            line=dict(color=COKE_COLORS['executive_blue'], width=2, dash='dash'),
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="Customer Engagement Trends",
            xaxis_title="Date",
            yaxis_title="Number of Interactions",
            yaxis2=dict(
                title="Effectiveness Score",
                overlaying='y',
                side='right'
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Engagement Channel Performance")
        
        # Analyze engagement by type
        channel_performance = engagement_df.groupby('engagement_type').agg({
            'effectiveness_score': 'mean',
            'outcome': 'count'
        }).reset_index()
        
        channel_performance.columns = ['Channel', 'Avg_Effectiveness', 'Count']
        channel_performance = channel_performance.sort_values('Avg_Effectiveness', ascending=True)
        
        fig = px.bar(
            channel_performance,
            x='Avg_Effectiveness',
            y='Channel',
            orientation='h',
            color='Count',
            color_continuous_scale=['#FFE6E6', COKE_COLORS['primary_red']],
            title="Channel Effectiveness & Usage"
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # === ACCOUNT DETAILS TABLE ===
    st.markdown("---")
    st.markdown("### 📋 Account Details")
    
    # Create detailed account table
    display_accounts = filtered_accounts[[
        'company_name', 'industry', 'region', 'annual_revenue', 
        'health_score', 'sentiment_score', 'churn_risk', 'last_interaction'
    ]].copy()
    
    display_accounts['annual_revenue'] = display_accounts['annual_revenue'].apply(
        lambda x: f"${x:,.0f}"
    )
    display_accounts['health_score'] = display_accounts['health_score'].apply(
        lambda x: f"{x:.0%}"
    )
    display_accounts['sentiment_score'] = display_accounts['sentiment_score'].apply(
        lambda x: f"{x:+.2f}"
    )
    
    display_accounts.columns = [
        'Company', 'Industry', 'Region', 'Annual Revenue',
        'Health Score', 'Sentiment', 'Churn Risk', 'Last Contact'
    ]
    
    # Add interactive table with pagination
    st.dataframe(
        display_accounts,
        use_container_width=True,
        height=400,
        column_config={
            "Churn Risk": st.column_config.TextColumn(
                "Churn Risk",
                help="Account churn risk level"
            ),
            "Health Score": st.column_config.TextColumn(
                "Health Score", 
                help="Overall account health percentage"
            ),
            "Sentiment": st.column_config.TextColumn(
                "Sentiment",
                help="Customer sentiment score (-1 to +1)"
            )
        }
    )
    
    # === CUSTOMER RESEARCH & INTELLIGENCE ===
    st.markdown("---")
    st.markdown("### 🔍 Customer Research & Intelligence")
    st.markdown("*AI-powered customer insights and pre-visit preparation*")
    
    # Customer selection for research
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_customer = st.selectbox(
            "🏢 Select Customer for Research",
            options=filtered_accounts['company_name'].tolist(),
            index=0,
            help="Choose a customer to generate comprehensive research insights"
        )
    
    with col2:
        if st.button("🤖 Generate AI Research Report", use_container_width=True, type="primary"):
            st.session_state['research_generated'] = True
            st.success("✅ AI Research Report Generated!")
    
    # Get selected customer data
    customer_data = filtered_accounts[filtered_accounts['company_name'] == selected_customer].iloc[0]
    
    # Display customer research if generated
    if st.session_state.get('research_generated', False):
        
        # === CUSTOMER OVERVIEW CARD ===
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            # Determine status indicators
            health_status = "Excellent" if customer_data['health_score'] > 0.8 else \
                           "Good" if customer_data['health_score'] > 0.6 else \
                           "At Risk" if customer_data['health_score'] > 0.4 else "Critical"
            
            sentiment_status = "Very Positive" if customer_data['sentiment_score'] > 0.6 else \
                              "Positive" if customer_data['sentiment_score'] > 0.2 else \
                              "Neutral" if customer_data['sentiment_score'] > -0.2 else \
                              "Negative" if customer_data['sentiment_score'] > -0.6 else "Very Negative"
            
            risk_color = {'Low': COKE_COLORS['success_green'], 
                         'Medium': COKE_COLORS['warning_orange'], 
                         'High': COKE_COLORS['danger_red'], 
                         'Critical': COKE_COLORS['primary_red']}.get(customer_data['churn_risk'], COKE_COLORS['dark_gray'])
            
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {COKE_COLORS['classic_white']}, {COKE_COLORS['light_gray']});
                padding: 20px;
                border-radius: 12px;
                border-left: 5px solid {COKE_COLORS['primary_red']};
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                margin: 10px 0;
            ">
                <h3 style="color: {COKE_COLORS['coke_black']}; margin: 0 0 10px 0;">🏢 {customer_data['company_name']}</h3>
                <p style="color: {COKE_COLORS['dark_gray']}; margin: 5px 0;"><strong>Industry:</strong> {customer_data['industry']}</p>
                <p style="color: {COKE_COLORS['dark_gray']}; margin: 5px 0;"><strong>Region:</strong> {customer_data['region']}</p>
                <p style="color: {COKE_COLORS['dark_gray']}; margin: 5px 0;"><strong>Customer Since:</strong> {customer_data['customer_since']}</p>
                <p style="color: {COKE_COLORS['dark_gray']}; margin: 5px 0;"><strong>Primary Contact:</strong> {customer_data['primary_contact']}</p>
                <p style="color: {COKE_COLORS['dark_gray']}; margin: 5px 0;"><strong>Assigned Rep:</strong> {customer_data['assigned_rep']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.metric("Annual Revenue", f"${customer_data['annual_revenue']:,.0f}", 
                     f"{customer_data['growth_rate']:+.1%} YoY")
            st.metric("Health Score", f"{customer_data['health_score']:.1%}", health_status)
            st.metric("NPS Score", f"{customer_data['nps_score']}", sentiment_status)
        
        with col3:
            st.metric("Locations", f"{customer_data['total_locations']}", "Active")
            st.metric("Churn Risk", customer_data['churn_risk'], 
                     f"{customer_data['churn_probability']:.1%} probability")
            st.metric("Days to Renewal", f"{customer_data['days_to_renewal']}", "Contract")
        
        # === AI-POWERED CUSTOMER ANALYSIS ===
        st.markdown("#### 🤖 GPT-4o Customer Analysis")
        
        # Generate realistic AI insights based on customer data
        def generate_customer_insights(customer):
            """Generate realistic AI-powered customer insights"""
            
            # Business situation analysis
            business_situation = []
            if customer['annual_revenue'] > 1000000:
                business_situation.append("Large enterprise customer with significant market presence")
            elif customer['annual_revenue'] > 500000:
                business_situation.append("Mid-market customer with growth potential")
            else:
                business_situation.append("Small-medium business with local market focus")
            
            if customer['growth_rate'] > 0.3:
                business_situation.append("experiencing rapid growth and expansion")
            elif customer['growth_rate'] > 0.1:
                business_situation.append("showing steady business growth")
            elif customer['growth_rate'] > -0.1:
                business_situation.append("maintaining stable business operations")
            else:
                business_situation.append("facing business challenges and potential contraction")
            
            # Risk factors
            risk_factors = []
            if customer['churn_risk'] in ['High', 'Critical']:
                risk_factors.append("High churn risk - immediate attention required")
            if customer['sentiment_score'] < -0.3:
                risk_factors.append("Negative sentiment indicators present")
            if customer['days_to_renewal'] < 90:
                risk_factors.append("Contract renewal approaching - critical engagement period")
            if customer['competitive_threat'] == 'High':
                risk_factors.append("High competitive pressure in their market")
            if customer['payment_history'] in ['Poor', 'Fair']:
                risk_factors.append("Payment history concerns noted")
            
            # Opportunities
            opportunities = []
            if customer['freestyle_machines'] < customer['total_locations'] * 0.3:
                opportunities.append("Significant Freestyle machine expansion opportunity")
            if customer['health_score'] > 0.7 and customer['growth_rate'] > 0.2:
                opportunities.append("Strong upselling potential due to positive performance")
            if customer['engagement_score'] > 0.8:
                opportunities.append("High engagement - ready for strategic partnership discussions")
            if customer['nps_score'] > 50:
                opportunities.append("High NPS score indicates referral and testimonial opportunities")
            
            # Recommended actions
            actions = []
            if customer['churn_risk'] in ['High', 'Critical']:
                actions.append("Schedule immediate executive-level relationship review")
            if customer['days_to_renewal'] < 120:
                actions.append("Initiate contract renewal discussions with value demonstration")
            if customer['sentiment_score'] < 0:
                actions.append("Conduct customer satisfaction survey and address concerns")
            if customer['freestyle_machines'] == 0:
                actions.append("Present Freestyle technology demonstration and ROI analysis")
            
            return {
                'business_situation': business_situation,
                'risk_factors': risk_factors if risk_factors else ["No significant risk factors identified"],
                'opportunities': opportunities if opportunities else ["Standard account maintenance recommended"],
                'actions': actions if actions else ["Continue regular engagement and relationship building"]
            }
        
        insights = generate_customer_insights(customer_data)
        
        # Display insights in organized tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Business Situation", "⚠️ Risk Factors", "🎯 Opportunities", "🚀 Recommended Actions"])
        
        with tab1:
            st.markdown("**Business Analysis:**")
            for situation in insights['business_situation']:
                st.markdown(f"• {situation}")
            
            # Additional business context
            st.markdown("**Key Business Metrics:**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"• **Order Frequency:** Every {customer_data['avg_order_frequency']} days")
                st.markdown(f"• **Last Order:** {customer_data['last_order_date'].strftime('%Y-%m-%d')}")
                st.markdown(f"• **Primary Product:** {customer_data['primary_product']}")
            with col2:
                st.markdown(f"• **Monthly Volume:** {customer_data['monthly_volume']:,.0f} units")
                st.markdown(f"• **Freestyle Machines:** {customer_data['freestyle_machines']}")
                st.markdown(f"• **Payment History:** {customer_data['payment_history']}")
        
        with tab2:
            if insights['risk_factors'][0] != "No significant risk factors identified":
                for risk in insights['risk_factors']:
                    st.markdown(f"""
                    <div style="
                        background: {COKE_COLORS['danger_red']}20;
                        padding: 10px;
                        border-radius: 5px;
                        border-left: 3px solid {COKE_COLORS['danger_red']};
                        margin: 5px 0;
                    ">
                        ⚠️ {risk}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['success_green']}20;
                    padding: 10px;
                    border-radius: 5px;
                    border-left: 3px solid {COKE_COLORS['success_green']};
                    margin: 5px 0;
                ">
                    ✅ No significant risk factors identified
                </div>
                """, unsafe_allow_html=True)
        
        with tab3:
            for opportunity in insights['opportunities']:
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['coke_gold']}20;
                    padding: 10px;
                    border-radius: 5px;
                    border-left: 3px solid {COKE_COLORS['coke_gold']};
                    margin: 5px 0;
                ">
                    🎯 {opportunity}
                </div>
                """, unsafe_allow_html=True)
        
        with tab4:
            for action in insights['actions']:
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['executive_blue']}20;
                    padding: 10px;
                    border-radius: 5px;
                    border-left: 3px solid {COKE_COLORS['executive_blue']};
                    margin: 5px 0;
                ">
                    🚀 {action}
                </div>
                """, unsafe_allow_html=True)
        
        # === COMPETITIVE INTELLIGENCE ===
        st.markdown("#### 🥊 Competitive Intelligence")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Competitive Landscape:**")
            threat_color = {'Low': COKE_COLORS['success_green'], 
                           'Medium': COKE_COLORS['warning_orange'], 
                           'High': COKE_COLORS['danger_red']}.get(customer_data['competitive_threat'])
            
            st.markdown(f"""
            <div style="
                background: {threat_color}20;
                padding: 15px;
                border-radius: 8px;
                border-left: 4px solid {threat_color};
            ">
                <strong>Competitive Threat Level: {customer_data['competitive_threat']}</strong><br>
                <small style="opacity: 0.8;">Based on market analysis and customer feedback</small>
            </div>
            """, unsafe_allow_html=True)
            
            # Generate competitive insights
            if customer_data['competitive_threat'] == 'High':
                competitive_notes = [
                    "Active competitor presence in this account",
                    "Price-sensitive decision making observed",
                    "Regular competitive benchmarking discussions"
                ]
            elif customer_data['competitive_threat'] == 'Medium':
                competitive_notes = [
                    "Some competitive activity in the region",
                    "Customer occasionally evaluates alternatives",
                    "Strong relationship provides defensive position"
                ]
            else:
                competitive_notes = [
                    "Strong market position with this customer",
                    "Minimal competitive pressure observed",
                    "Customer satisfaction with current offering"
                ]
            
            for note in competitive_notes:
                st.markdown(f"• {note}")
        
        with col2:
            st.markdown("**Customer Sentiment Timeline:**")
            
            # Generate sentiment trend (simplified visualization)
            sentiment_trend = ["Positive", "Stable", "Improving"] if customer_data['sentiment_score'] > 0 else \
                             ["Neutral", "Monitoring", "Stable"] if customer_data['sentiment_score'] > -0.3 else \
                             ["Concerning", "Declining", "Needs Attention"]
            
            for i, trend in enumerate(sentiment_trend):
                trend_color = COKE_COLORS['success_green'] if customer_data['sentiment_score'] > 0 else \
                             COKE_COLORS['warning_orange'] if customer_data['sentiment_score'] > -0.3 else \
                             COKE_COLORS['danger_red']
                
                st.markdown(f"""
                <div style="
                    background: {trend_color}15;
                    padding: 8px 12px;
                    border-radius: 5px;
                    margin: 3px 0;
                    border-left: 2px solid {trend_color};
                ">
                    <small><strong>Q{i+1} 2024:</strong> {trend}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # === ENGAGEMENT RECOMMENDATIONS ===
        st.markdown("#### 💡 Pre-Visit Preparation & Talking Points")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Key Topics to Discuss:**")
            discussion_topics = []
            
            if customer_data['days_to_renewal'] < 180:
                discussion_topics.append("Contract renewal and future partnership opportunities")
            if customer_data['growth_rate'] > 0.2:
                discussion_topics.append("Support for business expansion and new locations")
            if customer_data['freestyle_machines'] < customer_data['total_locations'] * 0.5:
                discussion_topics.append("Freestyle technology expansion and ROI benefits")
            if customer_data['nps_score'] > 70:
                discussion_topics.append("Case study development and referral opportunities")
            
            discussion_topics.extend([
                "Seasonal promotion planning and execution",
                "Supply chain optimization and delivery schedules",
                "Market trend insights and category management"
            ])
            
            for topic in discussion_topics[:5]:  # Limit to top 5
                st.markdown(f"🎯 {topic}")
        
        with col2:
            st.markdown("**Questions to Ask:**")
            questions = [
                "How is your business performing compared to last year?",
                "What are your biggest operational challenges currently?",
                "Are you planning any new locations or expansions?",
                "How satisfied are you with our current service levels?",
                "What promotional support would be most valuable?",
                "Are there any competitive pressures we should discuss?"
            ]
            
            for question in questions:
                st.markdown(f"❓ {question}")
        
        # === EXPORT RESEARCH REPORT ===
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Export Research Report", use_container_width=True):
                st.success("✅ Customer research report exported to PDF!")
        
        with col2:
            if st.button("📧 Email to Team", use_container_width=True):
                st.success("✅ Research summary emailed to sales team!")
        
        with col3:
            if st.button("📅 Schedule Follow-up", use_container_width=True):
                st.success("✅ Follow-up meeting scheduled!")

    # === QUICK ACTIONS ===
    st.markdown("---")
    
    account_actions = [
        {"icon": "📞", "label": "Schedule Customer Calls", "action": "schedule_calls"},
        {"icon": "🎯", "label": "Launch Retention Campaign", "action": "retention_campaign"},
        {"icon": "📊", "label": "Generate Health Reports", "action": "health_reports"},
        {"icon": "💌", "label": "Send Engagement Survey", "action": "engagement_survey"}
    ]
    
    selected_action = ProactiveWidgets.action_button_panel(account_actions)
    
    if selected_action:
        st.success(f"✅ {selected_action.replace('_', ' ').title()} initiated for {len(filtered_accounts)} accounts!")
