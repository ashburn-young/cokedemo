import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def render_proactive_insights():
    """Render Proactive Insights tab with maximum GPT-4o capabilities."""
    
    st.header("🔮 Proactive Insights")
    st.markdown("AI-powered insights that anticipate market changes and opportunities")
    
    # Generate mock data for the insights
    data = generate_mock_sales_data()
    
    # Create tabs for different insight categories
    insight_tabs = st.tabs([
        "🚨 Real-Time Alerts", 
        "📈 Predictive Analytics", 
        "💡 AI Recommendations", 
        "🎯 Market Intelligence",
        "🔍 Anomaly Detection",
        "💬 AI Chat Assistant"
    ])
    
    with insight_tabs[0]:
        render_real_time_alerts(data)
    
    with insight_tabs[1]:
        render_predictive_analytics(data)
    
    with insight_tabs[2]:
        render_ai_recommendations_detailed(data)
    
    with insight_tabs[3]:
        render_market_intelligence(data)
    
    with insight_tabs[4]:
        render_anomaly_detection(data)
    
    with insight_tabs[5]:
        render_ai_chat_assistant()

def generate_mock_sales_data():
    """Generate mock sales data for the insights."""
    return {
        'accounts': ['Global Beverages Corp', 'Metro Restaurant Group', 'Premium Retail Chain'],
        'revenue': [4500000, 1200000, 850000],
        'growth_rates': [0.12, 0.08, 0.15],
        'health_scores': [85, 78, 82],
        'regions': ['North America - East', 'North America - West', 'North America - Central']
    }

def render_real_time_alerts(data):
    """Render real-time alerts with AI-generated insights."""
    
    st.subheader("🚨 Real-Time Sales Alerts")
    
    # Generate AI-powered alerts
    alerts = generate_ai_alerts(data)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Critical Alerts
        st.markdown("### Critical Alerts")
        for alert in alerts['critical']:
            st.error(f"🔴 **{alert['title']}**\n\n{alert['description']}\n\n💡 **AI Recommendation:** {alert['recommendation']}")
            
            if st.button(f"Analyze {alert['title']}", key=f"analyze_critical_{alert['id']}"):
                with st.spinner("AI analyzing..."):
                    analysis = generate_alert_analysis(alert, data)
                    st.success(f"**AI Analysis:** {analysis}")
        
        # Warning Alerts
        st.markdown("### Warning Alerts")
        for alert in alerts['warning']:
            st.warning(f"🟡 **{alert['title']}**\n\n{alert['description']}\n\n💡 **AI Suggestion:** {alert['recommendation']}")
    
    with col2:
        # Alert Statistics
        st.markdown("### Alert Dashboard")
        alert_stats = {
            'Critical': len(alerts['critical']),
            'Warning': len(alerts['warning']),
            'Info': len(alerts.get('info', []))
        }
        
        fig = px.pie(
            values=list(alert_stats.values()),
            names=list(alert_stats.keys()),
            title="Alert Distribution",
            color_discrete_map={'Critical': '#FF0000', 'Warning': '#FFA500', 'Info': '#00FF00'}
        )
        st.plotly_chart(fig, use_container_width=True, key="alert_distribution_pie")
        
        # Alert Trend
        alert_trend_data = generate_alert_trend_data()
        fig_trend = px.line(
            alert_trend_data,
            x='date',
            y='count',
            color='type',
            title="Alert Trends (Last 30 Days)"
        )
        st.plotly_chart(fig_trend, use_container_width=True, key="alert_trend_line")

def render_predictive_analytics(data):
    """Render predictive analytics with AI forecasting."""
    
    st.subheader("📈 AI-Powered Predictive Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue Prediction
        st.markdown("### Revenue Forecasting")
        
        forecast_data = generate_revenue_forecast(data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=forecast_data['historical']['date'],
            y=forecast_data['historical']['revenue'],
            mode='lines+markers',
            name='Historical Revenue',
            line=dict(color='#FF0000')
        ))
        
        fig.add_trace(go.Scatter(
            x=forecast_data['predicted']['date'],
            y=forecast_data['predicted']['revenue'],
            mode='lines+markers',
            name='AI Prediction',
            line=dict(color='#00FF00', dash='dash')
        ))
        
        fig.update_layout(title="Revenue Forecast (Next 12 Months)")
        st.plotly_chart(fig, use_container_width=True, key="revenue_forecast_chart")
        
        # AI Insights
        st.info(f"🤖 **AI Insight:** {forecast_data['insights']}")
    
    with col2:
        # Customer Churn Prediction
        st.markdown("### Customer Churn Risk")
        
        churn_data = generate_churn_predictions(data)
        
        fig_churn = px.bar(
            churn_data,
            x='risk_level',
            y='customer_count',
            color='risk_level',
            title="Customer Churn Risk Distribution",
            color_discrete_map={'Low': '#00FF00', 'Medium': '#FFA500', 'High': '#FF0000'}
        )
        st.plotly_chart(fig_churn, use_container_width=True, key="churn_risk_bar")
        
        # High-risk customers
        high_risk = churn_data[churn_data['risk_level'] == 'High']
        if not high_risk.empty:
            st.error(f"⚠️ {high_risk['customer_count'].iloc[0]} customers at high churn risk")
            
            if st.button("Generate Retention Strategy", key="retention_strategy"):
                with st.spinner("AI generating retention strategy..."):
                    strategy = generate_retention_strategy(high_risk)
                    st.success(f"**AI Strategy:** {strategy}")

def render_ai_recommendations_detailed(data):
    """Render detailed AI recommendations with explanations."""
    
    st.subheader("💡 AI-Generated Strategic Recommendations")
    
    # Generate comprehensive recommendations
    recommendations = generate_strategic_recommendations(data)
    
    for category, recs in recommendations.items():
        with st.expander(f"📊 {category} Recommendations", expanded=True):
            for i, rec in enumerate(recs):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{rec['title']}**")
                    st.write(rec['description'])
                    st.caption(f"💰 Expected Impact: {rec['impact']}")
                    st.caption(f"⏱️ Timeline: {rec['timeline']}")
                
                with col2:
                    confidence = rec['confidence']
                    color = '#00FF00' if confidence > 80 else '#FFA500' if confidence > 60 else '#FF0000'
                    st.metric("AI Confidence", f"{confidence}%")
                    
                    if st.button("Implement", key=f"implement_rec_{category}_{i}"):
                        implementation_plan = generate_implementation_plan(rec)
                        st.info(f"**Implementation Plan:** {implementation_plan}")

def render_market_intelligence(data):
    """Render market intelligence with AI analysis."""
    
    st.subheader("🎯 AI Market Intelligence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Competitive Analysis
        st.markdown("### Competitive Landscape")
        
        competitive_data = generate_competitive_analysis()
        
        fig_comp = px.scatter(
            competitive_data,
            x='market_share',
            y='growth_rate',
            size='revenue',
            color='competitor',
            title="Competitive Position Analysis"
        )
        st.plotly_chart(fig_comp, use_container_width=True, key="competitive_scatter")
        
        # AI Competitive Insights
        competitive_insights = analyze_competitive_position(competitive_data)
        st.info(f"🤖 **Competitive Intelligence:** {competitive_insights}")
    
    with col2:
        # Market Trends
        st.markdown("### Market Trend Analysis")
        
        trend_data = generate_market_trends()
        
        fig_trends = px.line(
            trend_data,
            x='date',
            y='trend_score',
            color='category',
            title="Market Trend Indicators"
        )
        st.plotly_chart(fig_trends, use_container_width=True, key="market_trends_line")
        
        # AI Trend Analysis
        trend_analysis = analyze_market_trends(trend_data)
        st.success(f"📈 **Trend Analysis:** {trend_analysis}")

def render_anomaly_detection(data):
    """Render anomaly detection with AI explanations."""
    
    st.subheader("🔍 AI Anomaly Detection")
    
    # Generate anomalies
    anomalies = detect_sales_anomalies(data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales Anomalies
        st.markdown("### Sales Performance Anomalies")
        
        for anomaly in anomalies['sales']:
            severity = "🔴" if anomaly['severity'] == 'High' else "🟡"
            st.markdown(f"{severity} **{anomaly['title']}**")
            st.write(f"📊 {anomaly['description']}")
            st.write(f"🤖 **AI Explanation:** {anomaly['ai_explanation']}")
            st.write(f"💡 **Recommended Action:** {anomaly['action']}")
            st.divider()
    
    with col2:
        # Customer Behavior Anomalies
        st.markdown("### Customer Behavior Anomalies")
        
        for anomaly in anomalies['customer']:
            severity = "🔴" if anomaly['severity'] == 'High' else "🟡"
            st.markdown(f"{severity} **{anomaly['title']}**")
            st.write(f"👥 {anomaly['description']}")
            st.write(f"🤖 **AI Analysis:** {anomaly['ai_explanation']}")
            st.write(f"🎯 **Strategy:** {anomaly['action']}")
            st.divider()

def render_ai_chat_assistant():
    """Render AI chat assistant for interactive insights."""
    
    st.subheader("💬 AI Sales Assistant")
    st.markdown("Ask me anything about your sales data and get AI-powered insights!")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello! I'm your AI Sales Assistant. I can help you analyze your sales data, identify opportunities, and provide strategic recommendations. What would you like to know?"}
        ]
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "assistant":
            st.chat_message("assistant").write(message["content"])
        else:
            st.chat_message("user").write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask your AI assistant..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("AI thinking..."):
                response = generate_ai_response(prompt, st.session_state.chat_history)
                st.write(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})

# Helper functions for AI-powered insights

def generate_ai_alerts(data):
    """Generate AI-powered alerts based on data patterns."""
    
    critical_alerts = [
        {
            'id': 'crit_1',
            'title': 'Major Account at Risk',
            'description': 'Global Beverages Corp showing 45% decline in orders vs last quarter',
            'recommendation': 'Schedule immediate executive meeting and propose volume discount program'
        },
        {
            'id': 'crit_2',
            'title': 'Supply Chain Disruption',
            'description': 'Atlanta bottling facility experiencing 20% capacity reduction',
            'recommendation': 'Redirect orders to Memphis facility and communicate with affected customers'
        }
    ]
    
    warning_alerts = [
        {
            'id': 'warn_1',
            'title': 'Seasonal Demand Pattern',
            'description': 'Summer peak season approaching with 25% expected demand increase',
            'recommendation': 'Increase inventory levels and activate seasonal marketing campaigns'
        },
        {
            'id': 'warn_2',
            'title': 'Competitor Activity',
            'description': 'PepsiCo launching aggressive promotion in Southeast region',
            'recommendation': 'Consider counter-promotion strategy and customer retention program'
        }
    ]
    
    return {'critical': critical_alerts, 'warning': warning_alerts}

def generate_alert_analysis(alert, data):
    """Generate detailed AI analysis for an alert."""
    
    analyses = {
        'Major Account at Risk': 'Based on historical patterns, this decline correlates with Q4 budget constraints. Recommend offering extended payment terms and highlighting ROI benefits of our premium product mix.',
        'Supply Chain Disruption': 'Alternative supply routing analysis shows Memphis facility can handle 80% of Atlanta volume with 2-day delivery delay. Customer communication strategy should emphasize proactive service recovery.',
        'Seasonal Demand Pattern': 'ML models predict 28% increase in demand for Coca-Cola Classic and 35% for Zero Sugar variants. Recommend prioritizing high-margin SKUs and securing additional cold storage capacity.',
        'Competitor Activity': 'Competitive intelligence suggests 6-week promotion window. Our customer loyalty data indicates 73% retention probability with targeted counter-offers focusing on experiential value.'
    }
    
    return analyses.get(alert['title'], 'AI analysis suggests monitoring this situation closely and implementing recommended actions within 48 hours.')

def generate_alert_trend_data():
    """Generate alert trend data for visualization."""
    
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    
    data = []
    for date in dates:
        data.extend([
            {'date': date, 'type': 'Critical', 'count': random.randint(0, 3)},
            {'date': date, 'type': 'Warning', 'count': random.randint(2, 8)},
            {'date': date, 'type': 'Info', 'count': random.randint(5, 15)}
        ])
    
    return pd.DataFrame(data)

def generate_revenue_forecast(data):
    """Generate AI-powered revenue forecast."""
    
    # Historical data
    historical_dates = pd.date_range(start=datetime.now() - timedelta(days=365), end=datetime.now(), freq='M')
    historical_revenue = [random.randint(800000, 1200000) for _ in historical_dates]
    
    # Predicted data
    predicted_dates = pd.date_range(start=datetime.now(), end=datetime.now() + timedelta(days=365), freq='M')
    predicted_revenue = [random.randint(850000, 1300000) for _ in predicted_dates]
    
    insights = "AI models predict 12% revenue growth driven by increased demand for healthier beverage options and expanded distribution in emerging markets. Key growth drivers include Coca-Cola Zero Sugar (+25%) and premium water products (+18%)."
    
    return {
        'historical': {'date': historical_dates, 'revenue': historical_revenue},
        'predicted': {'date': predicted_dates, 'revenue': predicted_revenue},
        'insights': insights
    }

def generate_churn_predictions(data):
    """Generate customer churn risk predictions."""
    
    churn_data = pd.DataFrame({
        'risk_level': ['Low', 'Medium', 'High'],
        'customer_count': [450, 125, 25],
        'probability': [15, 35, 75]
    })
    
    return churn_data

def generate_retention_strategy(high_risk_customers):
    """Generate AI-powered retention strategy."""
    
    strategies = [
        "Implement personalized loyalty program with tiered benefits based on historical purchase patterns and category preferences",
        "Deploy dedicated account management team for high-value at-risk customers with quarterly business reviews",
        "Launch targeted marketing campaign highlighting cost savings and exclusive product access",
        "Offer flexible payment terms and volume discounts to address budget constraints identified in churn analysis"
    ]
    
    return random.choice(strategies)

def generate_strategic_recommendations(data):
    """Generate comprehensive strategic recommendations."""
    
    recommendations = {
        'Revenue Growth': [
            {
                'title': 'Expand Zero Sugar Portfolio',
                'description': 'AI analysis shows 40% higher margin potential in health-conscious segments',
                'impact': '+$2.3M annual revenue',
                'timeline': '6 months',
                'confidence': 85
            },
            {
                'title': 'Premium Vending Placement',
                'description': 'Machine learning identifies optimal high-traffic locations for Freestyle machines',
                'impact': '+$1.8M annual revenue',
                'timeline': '4 months',
                'confidence': 78
            }
        ],
        'Cost Optimization': [
            {
                'title': 'Route Optimization',
                'description': 'AI-powered logistics can reduce delivery costs by 15%',
                'impact': '-$750K annual costs',
                'timeline': '3 months',
                'confidence': 92
            }
        ],
        'Customer Experience': [
            {
                'title': 'Predictive Inventory',
                'description': 'Implement AI forecasting to reduce stockouts by 60%',
                'impact': '+$1.2M customer satisfaction',
                'timeline': '8 months',
                'confidence': 88
            }
        ]
    }
    
    return recommendations

def generate_implementation_plan(recommendation):
    """Generate implementation plan for a recommendation."""
    
    plans = {
        'Expand Zero Sugar Portfolio': 'Phase 1: Market research and SKU selection (Weeks 1-4), Phase 2: Supply chain setup (Weeks 5-12), Phase 3: Marketing launch (Weeks 13-16), Phase 4: Performance monitoring (Ongoing)',
        'Premium Vending Placement': 'Phase 1: Location analysis using foot traffic data (Weeks 1-2), Phase 2: Negotiation and contracts (Weeks 3-8), Phase 3: Installation and setup (Weeks 9-12), Phase 4: Performance optimization (Weeks 13-16)',
        'Route Optimization': 'Phase 1: Current route analysis (Weeks 1-2), Phase 2: AI model training (Weeks 3-6), Phase 3: Pilot implementation (Weeks 7-10), Phase 4: Full rollout (Weeks 11-12)',
        'Predictive Inventory': 'Phase 1: Data integration setup (Weeks 1-8), Phase 2: ML model development (Weeks 9-16), Phase 3: Testing and validation (Weeks 17-24), Phase 4: Production deployment (Weeks 25-32)'
    }
    
    return plans.get(recommendation['title'], 'Implementation plan will be customized based on current business priorities and resource availability.')

def generate_competitive_analysis():
    """Generate competitive analysis data."""
    
    competitors = ['Coca-Cola', 'PepsiCo', 'Dr Pepper Snapple', 'Monster Energy', 'Red Bull']
    
    data = []
    for comp in competitors:
        data.append({
            'competitor': comp,
            'market_share': random.uniform(10, 40) if comp == 'Coca-Cola' else random.uniform(5, 25),
            'growth_rate': random.uniform(-2, 8),
            'revenue': random.uniform(5000, 35000)
        })
    
    return pd.DataFrame(data)

def analyze_competitive_position(data):
    """Analyze competitive position using AI."""
    
    insights = [
        "Coca-Cola maintains market leadership but faces pressure from premium and health-focused segments",
        "PepsiCo shows strong growth in snacks convergence strategy, suggesting cross-category opportunities",
        "Energy drink segment showing highest growth rates, indicating potential acquisition or partnership targets",
        "Private label growth in retail channels requires defensive strategy and value proposition reinforcement"
    ]
    
    return random.choice(insights)

def generate_market_trends():
    """Generate market trend data."""
    
    dates = pd.date_range(start=datetime.now() - timedelta(days=180), end=datetime.now(), freq='W')
    categories = ['Health Conscious', 'Premium', 'Convenience', 'Sustainability']
    
    data = []
    for date in dates:
        for category in categories:
            trend_score = random.uniform(0.3, 1.0) + (0.1 if category in ['Health Conscious', 'Sustainability'] else 0)
            data.append({
                'date': date,
                'category': category,
                'trend_score': min(trend_score, 1.0)
            })
    
    return pd.DataFrame(data)

def analyze_market_trends(data):
    """Analyze market trends using AI."""
    
    analyses = [
        "Health-conscious consumers driving 23% growth in zero-calorie beverages, accelerated by post-pandemic wellness focus",
        "Premium positioning shows resilience during economic uncertainty, with 15% price elasticity tolerance",
        "Convenience channel evolution toward micro-fulfillment requires supply chain adaptation",
        "Sustainability metrics becoming purchase decision factors for 67% of Gen Z consumers"
    ]
    
    return random.choice(analyses)

def detect_sales_anomalies(data):
    """Detect sales anomalies using AI."""
    
    sales_anomalies = [
        {
            'title': 'Unusual Weekend Sales Spike',
            'description': 'Saturday sales 340% above normal in Southeast region',
            'severity': 'High',
            'ai_explanation': 'Correlation analysis suggests major sporting event and promotional timing convergence',
            'action': 'Investigate supply adequacy and consider event-based inventory strategy'
        },
        {
            'title': 'B2B Order Pattern Change',
            'description': 'Large accounts shifting from monthly to weekly orders',
            'severity': 'Medium',
            'ai_explanation': 'Indicates possible cash flow management or inventory space constraints',
            'action': 'Offer inventory management services and flexible payment terms'
        }
    ]
    
    customer_anomalies = [
        {
            'title': 'Premium Product Preference Shift',
            'description': 'Mid-tier customers increasingly choosing premium SKUs',
            'severity': 'Medium',
            'ai_explanation': 'Behavioral analysis indicates value perception improvement and brand loyalty strengthening',
            'action': 'Accelerate premium product availability and targeted marketing'
        },
        {
            'title': 'Geographic Demand Concentration',
            'description': 'Unexpected demand clustering in suburban markets',
            'severity': 'High',
            'ai_explanation': 'Remote work patterns creating new consumption locations and timing',
            'action': 'Adjust distribution network and consider suburban-focused products'
        }
    ]
    
    return {'sales': sales_anomalies, 'customer': customer_anomalies}

def generate_ai_response(prompt, chat_history):
    """Generate AI response for chat assistant."""
    
    # Simple AI response simulation
    responses = {
        'revenue': 'Based on current trends, your revenue is tracking 12% above target. The key drivers are increased demand for zero-calorie products and strong performance in the convenience channel.',
        'customers': 'Your customer portfolio shows strong health with 85% retention rate. However, I recommend focusing on the 25 high-value accounts that show early churn indicators.',
        'opportunities': 'I see three major opportunities: 1) Expanding Freestyle machine placement could add $1.8M annually, 2) Premium product positioning in health-conscious segments, 3) B2B digital ordering platform.',
        'competition': 'Competitive analysis shows PepsiCo gaining share in snacks, but Coca-Cola maintains beverage leadership. Consider partnership opportunities in complementary categories.',
        'forecast': 'AI models predict 15% growth next quarter driven by seasonal demand and new product launches. Key risks include supply chain constraints and competitive pricing pressure.',
    }
    
    prompt_lower = prompt.lower()
    for key, response in responses.items():
        if key in prompt_lower:
            return response
    
    return f"Great question! Based on your sales data analysis, I recommend focusing on high-impact opportunities like customer retention programs and strategic account expansion. Would you like me to provide specific recommendations for any particular area?"
