import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def render_customer_360():
    """Render Customer 360 tab with comprehensive AI-powered customer insights."""
    
    st.header("👥 Customer 360°")
    st.markdown("Complete AI-powered customer intelligence and relationship management")
    
    # Customer selection
    customer_selector = st.selectbox(
        "Select Customer for Deep Analysis:",
        options=[
            "Global Beverages Corp",
            "Metro Restaurant Group", 
            "Premium Retail Chain",
            "University Campus Network",
            "Sports Arena Consortium",
            "Healthcare System Alliance",
            "Transportation Hub Corp",
            "Entertainment District LLC"
        ],
        key="customer_360_selector"
    )
    
    # Generate customer data based on selection
    customer_data = generate_customer_profile(customer_selector)
    
    # Main customer overview
    render_customer_overview(customer_data)
    
    # Create detailed tabs
    customer_tabs = st.tabs([
        "📊 Performance Analytics",
        "🤖 AI Insights", 
        "📈 Relationship Health",
        "💰 Revenue Optimization",
        "🎯 Strategic Opportunities",
        "📞 Interaction Timeline",
        "🔮 Predictive Models"
    ])
    
    with customer_tabs[0]:
        render_performance_analytics(customer_data)
    
    with customer_tabs[1]:
        render_ai_customer_insights(customer_data)
    
    with customer_tabs[2]:
        render_relationship_health(customer_data)
    
    with customer_tabs[3]:
        render_revenue_optimization(customer_data)
    
    with customer_tabs[4]:
        render_strategic_opportunities(customer_data)
    
    with customer_tabs[5]:
        render_interaction_timeline(customer_data)
    
    with customer_tabs[6]:
        render_predictive_models(customer_data)

def generate_customer_profile(customer_name):
    """Generate comprehensive customer profile with AI insights."""
    
    base_data = {
        "Global Beverages Corp": {
            "industry": "Beverage Distribution",
            "size": "Enterprise",
            "annual_revenue": 45000000,
            "relationship_length": "8 years",
            "locations": 150,
            "employees": 2500,
            "decision_makers": ["Sarah Johnson (CEO)", "Mike Chen (COO)", "Lisa Rodriguez (CFO)"],
            "health_score": 85,
            "satisfaction_score": 92,
            "growth_potential": "High",
            "churn_risk": "Low"
        },
        "Metro Restaurant Group": {
            "industry": "Food Service",
            "size": "Mid-Market",
            "annual_revenue": 12000000,
            "relationship_length": "5 years",
            "locations": 45,
            "employees": 800,
            "decision_makers": ["David Kim (Owner)", "Jennifer Smith (Operations)", "Carlos Martinez (Purchasing)"],
            "health_score": 78,
            "satisfaction_score": 88,
            "growth_potential": "Medium",
            "churn_risk": "Low"
        }
    }
    
    # Default profile if customer not found
    default_profile = {
        "industry": "Retail",
        "size": "Mid-Market", 
        "annual_revenue": 8000000,
        "relationship_length": "3 years",
        "locations": 25,
        "employees": 400,
        "decision_makers": ["John Doe (GM)", "Jane Smith (Procurement)"],
        "health_score": 72,
        "satisfaction_score": 85,
        "growth_potential": "Medium",
        "churn_risk": "Medium"
    }
    
    profile = base_data.get(customer_name, default_profile)
    profile["name"] = customer_name
    
    # Add AI-generated metrics
    profile.update({
        "nps_score": random.randint(50, 85),
        "engagement_score": random.randint(70, 95),
        "digital_adoption": random.randint(40, 90),
        "payment_terms": random.choice(["Net 30", "Net 45", "Net 60"]),
        "credit_rating": random.choice(["AAA", "AA+", "AA", "A+"]),
        "competitive_threat": random.choice(["Low", "Medium", "High"]),
        "expansion_probability": random.randint(60, 95)
    })
    
    return profile

def render_customer_overview(customer_data):
    """Render customer overview section."""
    
    st.markdown("---")
    
    # Key metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        health_color = "🟢" if customer_data["health_score"] > 80 else "🟡" if customer_data["health_score"] > 60 else "🔴"
        st.metric("Health Score", f"{customer_data['health_score']}/100", f"{health_color}")
    
    with col2:
        st.metric("Annual Revenue", f"${customer_data['annual_revenue']:,.0f}", "+12%")
    
    with col3:
        st.metric("Satisfaction", f"{customer_data['satisfaction_score']}%", "+5%")
    
    with col4:
        st.metric("Locations", customer_data['locations'], "+3")
    
    with col5:
        st.metric("Relationship", customer_data['relationship_length'], "Strong")
    
    # Customer summary
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Customer Profile")
        st.markdown(f"**Industry:** {customer_data['industry']}")
        st.markdown(f"**Size:** {customer_data['size']}")
        st.markdown(f"**Employees:** {customer_data['employees']:,}")
        st.markdown(f"**Growth Potential:** {customer_data['growth_potential']}")
        st.markdown(f"**Churn Risk:** {customer_data['churn_risk']}")
        
        # Decision makers
        st.markdown("**Key Decision Makers:**")
        for dm in customer_data['decision_makers']:
            st.markdown(f"• {dm}")
    
    with col2:
        # AI-generated customer insights
        st.markdown("### 🤖 AI Quick Insights")
        
        insights = generate_quick_insights(customer_data)
        for insight in insights:
            st.info(insight)
        
        # Action buttons
        if st.button("🎯 Generate Action Plan", key="generate_action_plan"):
            action_plan = generate_customer_action_plan(customer_data)
            st.success(f"**Action Plan Generated:**\n\n{action_plan}")

def render_performance_analytics(customer_data):
    """Render performance analytics section."""
    
    st.subheader("📊 Performance Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue trend
        st.markdown("### Revenue Trend")
        
        revenue_data = generate_revenue_trend_data(customer_data)
        
        fig = px.line(
            revenue_data,
            x='month',
            y='revenue',
            title="Monthly Revenue Trend",
            markers=True
        )
        fig.update_traces(line_color='#FF0000')
        st.plotly_chart(fig, use_container_width=True, key="customer_revenue_trend")
        
        # Product mix analysis
        st.markdown("### Product Mix Analysis")
        
        product_data = generate_product_mix_data()
        
        fig_product = px.pie(
            product_data,
            values='revenue',
            names='product',
            title="Revenue by Product Category"
        )
        st.plotly_chart(fig_product, use_container_width=True, key="customer_product_mix")
    
    with col2:
        # Performance metrics
        st.markdown("### Key Performance Metrics")
        
        metrics_data = {
            'Metric': ['Order Frequency', 'Average Order Value', 'Payment Timeliness', 'Product Adoption', 'Support Tickets'],
            'Current': [85, 92, 98, 76, 12],
            'Target': [90, 95, 100, 85, 8],
            'Trend': ['↑', '↑', '→', '↑', '↓']
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        
        for _, row in metrics_df.iterrows():
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_a:
                st.markdown(f"**{row['Metric']}**")
            with col_b:
                st.markdown(f"{row['Current']}% / {row['Target']}%")
            with col_c:
                st.markdown(f"{row['Trend']}")
        
        # Geographic performance
        st.markdown("### Geographic Performance")
        
        geo_data = generate_geographic_data(customer_data)
        
        fig_geo = px.bar(
            geo_data,
            x='region',
            y='performance',
            title="Performance by Region",
            color='performance',
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig_geo, use_container_width=True, key="customer_geo_performance")

def render_ai_customer_insights(customer_data):
    """Render AI-powered customer insights."""
    
    st.subheader("🤖 AI-Powered Customer Intelligence")
    
    # Generate comprehensive AI insights
    if st.button("🧠 Generate Deep AI Analysis", key="deep_ai_analysis"):
        with st.spinner("AI analyzing customer data across multiple dimensions..."):
            insights = generate_deep_ai_insights(customer_data)
            
            for category, insight_list in insights.items():
                with st.expander(f"🎯 {category}", expanded=True):
                    for insight in insight_list:
                        st.markdown(f"**{insight['title']}**")
                        st.write(insight['description'])
                        st.caption(f"Confidence: {insight['confidence']}% | Impact: {insight['impact']}")
                        st.divider()
    
    # Sentiment analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Communication Sentiment Analysis")
        
        sentiment_data = generate_sentiment_analysis(customer_data)
        
        fig_sentiment = px.line(
            sentiment_data,
            x='date',
            y='sentiment_score',
            color='channel',
            title="Sentiment Trend by Communication Channel"
        )
        st.plotly_chart(fig_sentiment, use_container_width=True, key="customer_sentiment")
        
        # Sentiment insights
        avg_sentiment = sentiment_data['sentiment_score'].mean()
        if avg_sentiment > 0.7:
            st.success(f"🟢 Positive sentiment trend (Score: {avg_sentiment:.2f})")
        elif avg_sentiment > 0.5:
            st.warning(f"🟡 Neutral sentiment (Score: {avg_sentiment:.2f})")
        else:
            st.error(f"🔴 Negative sentiment detected (Score: {avg_sentiment:.2f})")
    
    with col2:
        st.markdown("### Behavioral Patterns")
        
        behavior_data = analyze_customer_behavior(customer_data)
        
        for pattern in behavior_data:
            st.markdown(f"**{pattern['pattern']}**")
            st.write(pattern['description'])
            st.caption(f"Frequency: {pattern['frequency']} | Confidence: {pattern['confidence']}%")

def render_relationship_health(customer_data):
    """Render relationship health analysis."""
    
    st.subheader("📈 Relationship Health Dashboard")
    
    # Health score breakdown
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Health score gauge
        health_score = customer_data['health_score']
        
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=health_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Overall Health Score"},
            delta={'reference': 80},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        st.plotly_chart(fig_gauge, use_container_width=True, key="health_gauge")
    
    with col2:
        # Health factors breakdown
        st.markdown("### Health Score Factors")
        
        health_factors = {
            'Communication Frequency': 92,
            'Payment Timeliness': 98,
            'Product Adoption': 76,
            'Support Satisfaction': 88,
            'Engagement Level': 85,
            'Growth Trajectory': 89
        }
        
        factors_df = pd.DataFrame(list(health_factors.items()), columns=['Factor', 'Score'])
        
        fig_factors = px.bar(
            factors_df,
            x='Score',
            y='Factor',
            orientation='h',
            title="Health Score Components",
            color='Score',
            color_continuous_scale='RdYlGn'
        )
        fig_factors.update_layout(height=400)
        st.plotly_chart(fig_factors, use_container_width=True, key="health_factors")
    
    # Relationship milestones
    st.markdown("### Relationship Milestones & Timeline")
    
    milestones = generate_relationship_milestones(customer_data)
    
    for milestone in milestones:
        col_date, col_event, col_impact = st.columns([1, 2, 1])
        
        with col_date:
            st.markdown(f"**{milestone['date']}**")
        
        with col_event:
            st.markdown(f"{milestone['event']}")
        
        with col_impact:
            impact_color = "🟢" if milestone['impact'] == 'Positive' else "🔴" if milestone['impact'] == 'Negative' else "🟡"
            st.markdown(f"{impact_color} {milestone['impact']}")

def render_revenue_optimization(customer_data):
    """Render revenue optimization opportunities."""
    
    st.subheader("💰 Revenue Optimization Opportunities")
    
    # Current vs potential revenue
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Revenue Potential Analysis")
        
        current_revenue = customer_data['annual_revenue']
        potential_revenue = current_revenue * 1.35  # 35% growth potential
        
        revenue_comparison = {
            'Category': ['Current Revenue', 'Potential Revenue'],
            'Amount': [current_revenue, potential_revenue],
            'Type': ['Current', 'Potential']
        }
        
        revenue_df = pd.DataFrame(revenue_comparison)
        
        fig_revenue = px.bar(
            revenue_df,
            x='Category',
            y='Amount',
            color='Type',
            title="Revenue Potential Analysis",
            color_discrete_map={'Current': '#FF0000', 'Potential': '#00FF00'}
        )
        st.plotly_chart(fig_revenue, use_container_width=True, key="revenue_potential")
        
        st.success(f"💡 **Optimization Opportunity:** ${(potential_revenue - current_revenue):,.0f} additional revenue potential")
    
    with col2:
        st.markdown("### Optimization Strategies")
        
        optimization_strategies = generate_optimization_strategies(customer_data)
        
        for i, strategy in enumerate(optimization_strategies):
            with st.container():
                st.markdown(f"**{strategy['title']}**")
                st.write(strategy['description'])
                st.caption(f"💰 Revenue Impact: {strategy['revenue_impact']}")
                st.caption(f"⏱️ Timeline: {strategy['timeline']}")
                st.caption(f"🎯 Probability: {strategy['success_probability']}%")
                
                if st.button(f"Implement Strategy", key=f"implement_strategy_{i}"):
                    implementation = generate_implementation_details(strategy)
                    st.info(f"**Implementation Plan:** {implementation}")
                
                st.divider()

def render_strategic_opportunities(customer_data):
    """Render strategic opportunities analysis."""
    
    st.subheader("🎯 Strategic Growth Opportunities")
    
    opportunities = generate_strategic_opportunities_list(customer_data)
    
    # Opportunity matrix
    opportunity_data = []
    for opp in opportunities:
        opportunity_data.append({
            'Opportunity': opp['name'],
            'Impact': opp['impact_score'],
            'Effort': opp['effort_score'],
            'Revenue': opp['revenue_potential']
        })
    
    opp_df = pd.DataFrame(opportunity_data)
    
    fig_matrix = px.scatter(
        opp_df,
        x='Effort',
        y='Impact',
        size='Revenue',
        hover_name='Opportunity',
        title="Opportunity Impact vs Effort Matrix",
        labels={'Effort': 'Implementation Effort', 'Impact': 'Business Impact'}
    )
    
    # Add quadrant lines
    fig_matrix.add_hline(y=5, line_dash="dash", line_color="gray")
    fig_matrix.add_vline(x=5, line_dash="dash", line_color="gray")
    
    st.plotly_chart(fig_matrix, use_container_width=True, key="opportunity_matrix")
    
    # Detailed opportunity analysis
    selected_opportunity = st.selectbox(
        "Select Opportunity for Detailed Analysis:",
        options=[opp['name'] for opp in opportunities],
        key="opportunity_selector"
    )
    
    if selected_opportunity:
        selected_opp = next(opp for opp in opportunities if opp['name'] == selected_opportunity)
        render_opportunity_details(selected_opp)

def render_interaction_timeline(customer_data):
    """Render customer interaction timeline."""
    
    st.subheader("📞 Customer Interaction Timeline")
    
    # Generate interaction data
    interactions = generate_interaction_data(customer_data)
    
    # Filter controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        interaction_type = st.selectbox(
            "Filter by Type:",
            ["All", "Email", "Phone", "Meeting", "Support", "Contract"],
            key="interaction_type_filter"
        )
    
    with col2:
        date_range = st.selectbox(
            "Time Period:",
            ["Last 30 Days", "Last 90 Days", "Last Year", "All Time"],
            key="interaction_date_filter"
        )
    
    with col3:
        if st.button("📊 Analyze Patterns", key="analyze_interaction_patterns"):
            patterns = analyze_interaction_patterns(interactions)
            st.info(f"**AI Pattern Analysis:** {patterns}")
    
    # Timeline visualization
    filtered_interactions = filter_interactions(interactions, interaction_type, date_range)
    
    fig_timeline = go.Figure()
    
    for interaction in filtered_interactions:
        fig_timeline.add_trace(go.Scatter(
            x=[interaction['date']],
            y=[interaction['type']],
            mode='markers',
            marker=dict(
                size=15,
                color=get_interaction_color(interaction['type']),
                symbol='circle'
            ),
            text=interaction['summary'],
            hovertemplate=f"<b>{interaction['type']}</b><br>" +
                         f"Date: {interaction['date']}<br>" +
                         f"Summary: {interaction['summary']}<br>" +
                         f"Outcome: {interaction['outcome']}<extra></extra>",
            showlegend=False
        ))
    
    fig_timeline.update_layout(
        title="Customer Interaction Timeline",
        xaxis_title="Date",
        yaxis_title="Interaction Type",
        height=500
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True, key="interaction_timeline")
    
    # Recent interactions table
    st.markdown("### Recent Interactions")
    
    recent_interactions = filtered_interactions[:5]
    for interaction in recent_interactions:
        with st.expander(f"{interaction['type']} - {interaction['date']}", expanded=False):
            st.markdown(f"**Summary:** {interaction['summary']}")
            st.markdown(f"**Participants:** {interaction['participants']}")
            st.markdown(f"**Outcome:** {interaction['outcome']}")
            st.markdown(f"**Next Steps:** {interaction['next_steps']}")

def render_predictive_models(customer_data):
    """Render predictive models and forecasts."""
    
    st.subheader("🔮 Predictive Customer Models")
    
    # Model selection
    model_type = st.selectbox(
        "Select Predictive Model:",
        [
            "Churn Risk Prediction",
            "Revenue Forecast",
            "Upsell Probability",
            "Payment Risk Assessment",
            "Expansion Timing",
            "Product Adoption Forecast"
        ],
        key="predictive_model_selector"
    )
    
    if st.button("🤖 Generate Prediction", key="generate_prediction"):
        with st.spinner("AI models processing customer data..."):
            prediction_result = generate_prediction(model_type, customer_data)
            display_prediction_result(model_type, prediction_result)

# Helper functions for Customer 360

def generate_quick_insights(customer_data):
    """Generate quick AI insights about the customer."""
    
    insights = []
    
    if customer_data['health_score'] > 85:
        insights.append("🟢 Strong relationship health - consider expansion opportunities")
    elif customer_data['health_score'] < 60:
        insights.append("🔴 Relationship at risk - immediate attention needed")
    
    if customer_data['growth_potential'] == 'High':
        insights.append("📈 High growth potential identified - prioritize strategic initiatives")
    
    if customer_data['digital_adoption'] < 50:
        insights.append("💻 Low digital adoption - opportunity for digital transformation")
    
    insights.append(f"🎯 Expansion probability: {customer_data['expansion_probability']}% based on behavioral patterns")
    
    return insights

def generate_customer_action_plan(customer_data):
    """Generate AI-powered action plan for the customer."""
    
    health_score = customer_data['health_score']
    growth_potential = customer_data['growth_potential']
    
    if health_score > 85 and growth_potential == 'High':
        return """
        **Strategic Growth Plan:**
        1. Schedule executive business review within 30 days
        2. Present expansion opportunities (estimated $2.3M potential)
        3. Introduce premium product portfolio
        4. Explore strategic partnership opportunities
        5. Implement quarterly innovation sessions
        """
    elif health_score < 60:
        return """
        **Relationship Recovery Plan:**
        1. Immediate executive outreach within 48 hours
        2. Conduct comprehensive satisfaction survey
        3. Develop service recovery plan
        4. Assign dedicated account management
        5. Monthly progress reviews
        """
    else:
        return """
        **Relationship Strengthening Plan:**
        1. Increase engagement touchpoints
        2. Provide value-added services
        3. Explore upsell opportunities
        4. Strengthen key stakeholder relationships
        5. Implement customer success program
        """

def generate_revenue_trend_data(customer_data):
    """Generate revenue trend data for the customer."""
    
    months = pd.date_range(start=datetime.now() - timedelta(days=365), end=datetime.now(), freq='M')
    base_revenue = customer_data['annual_revenue'] / 12
    
    revenue_data = []
    for i, month in enumerate(months):
        # Add some seasonality and growth trend
        seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * i / 12)
        growth_factor = 1 + (i * 0.01)  # 1% monthly growth
        variance = random.uniform(0.9, 1.1)
        
        revenue = base_revenue * seasonal_factor * growth_factor * variance
        
        revenue_data.append({
            'month': month,
            'revenue': revenue
        })
    
    return pd.DataFrame(revenue_data)

def generate_product_mix_data():
    """Generate product mix data for the customer."""
    
    products = ['Coca-Cola Classic', 'Coca-Cola Zero', 'Diet Coke', 'Sprite', 'Fanta', 'Water Products']
    revenues = [40, 25, 15, 10, 7, 3]  # Percentage distribution
    
    return pd.DataFrame({
        'product': products,
        'revenue': revenues
    })

def generate_geographic_data(customer_data):
    """Generate geographic performance data."""
    
    regions = ['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West']
    performance = [random.randint(70, 95) for _ in regions]
    
    return pd.DataFrame({
        'region': regions,
        'performance': performance
    })

def generate_deep_ai_insights(customer_data):
    """Generate comprehensive AI insights across multiple categories."""
    
    insights = {
        "Behavioral Analysis": [
            {
                'title': 'Ordering Pattern Optimization',
                'description': 'AI detected suboptimal ordering frequency resulting in 15% higher logistics costs. Recommend shifting to bi-weekly delivery schedule.',
                'confidence': 87,
                'impact': 'High'
            },
            {
                'title': 'Product Preference Evolution',
                'description': 'Machine learning models show 34% increase in preference for health-conscious products over past 6 months.',
                'confidence': 92,
                'impact': 'Medium'
            }
        ],
        "Financial Intelligence": [
            {
                'title': 'Payment Behavior Analysis',
                'description': 'Consistent early payment pattern (avg 3 days before due) indicates strong cash flow and credit worthiness.',
                'confidence': 96,
                'impact': 'Low'
            },
            {
                'title': 'Budget Cycle Prediction',
                'description': 'Historical analysis suggests Q4 budget availability increases by 28% annually - optimal timing for major proposals.',
                'confidence': 84,
                'impact': 'High'
            }
        ],
        "Relationship Dynamics": [
            {
                'title': 'Stakeholder Influence Mapping',
                'description': 'CEO influence on purchasing decisions increased 45% following recent organizational changes.',
                'confidence': 78,
                'impact': 'High'
            },
            {
                'title': 'Communication Preference Analysis',
                'description': 'Response rates 67% higher for morning communications vs afternoon, particularly for technical content.',
                'confidence': 89,
                'impact': 'Medium'
            }
        ]
    }
    
    return insights

def generate_sentiment_analysis(customer_data):
    """Generate sentiment analysis data over time."""
    
    dates = pd.date_range(start=datetime.now() - timedelta(days=180), end=datetime.now(), freq='W')
    channels = ['Email', 'Phone', 'Meetings', 'Support']
    
    data = []
    for date in dates:
        for channel in channels:
            sentiment = random.uniform(0.4, 0.9)  # Generally positive sentiment
            data.append({
                'date': date,
                'channel': channel,
                'sentiment_score': sentiment
            })
    
    return pd.DataFrame(data)

def analyze_customer_behavior(customer_data):
    """Analyze customer behavioral patterns."""
    
    behaviors = [
        {
            'pattern': 'Seasonal Ordering Increase',
            'description': 'Orders increase by 35% during summer months, primarily driven by outdoor event catering',
            'frequency': 'Annual',
            'confidence': 94
        },
        {
            'pattern': 'Premium Product Adoption',
            'description': 'Gradual shift toward premium SKUs with 12% increase in high-margin product mix',
            'frequency': 'Ongoing',
            'confidence': 87
        },
        {
            'pattern': 'Digital Engagement Growth',
            'description': 'Online ordering platform usage increased 45% year-over-year',
            'frequency': 'Monthly',
            'confidence': 92
        }
    ]
    
    return behaviors

def generate_relationship_milestones(customer_data):
    """Generate relationship milestone data."""
    
    milestones = [
        {
            'date': '2024-01-15',
            'event': 'Contract Renewal - 3 Year Extension',
            'impact': 'Positive'
        },
        {
            'date': '2023-11-08',
            'event': 'Expanded to 15 New Locations',
            'impact': 'Positive'
        },
        {
            'date': '2023-09-22',
            'event': 'Premium Product Line Adoption',
            'impact': 'Positive'
        },
        {
            'date': '2023-07-10',
            'event': 'Service Issue Resolution - 48hr Response',
            'impact': 'Positive'
        },
        {
            'date': '2023-05-03',
            'event': 'Competitive Evaluation Period',
            'impact': 'Neutral'
        }
    ]
    
    return milestones

def generate_optimization_strategies(customer_data):
    """Generate revenue optimization strategies."""
    
    strategies = [
        {
            'title': 'Premium Product Upselling',
            'description': 'Target 25% of current Classic volume for Zero Sugar conversion based on health trend analysis',
            'revenue_impact': '+$450K annually',
            'timeline': '6 months',
            'success_probability': 78
        },
        {
            'title': 'Delivery Optimization',
            'description': 'Consolidate deliveries from 3x/week to 2x/week with larger order sizes',
            'revenue_impact': '+$125K cost savings',
            'timeline': '3 months',
            'success_probability': 92
        },
        {
            'title': 'Digital Platform Enhancement',
            'description': 'Implement automated reordering system based on consumption analytics',
            'revenue_impact': '+$200K efficiency gains',
            'timeline': '4 months',
            'success_probability': 85
        }
    ]
    
    return strategies

def generate_implementation_details(strategy):
    """Generate implementation details for a strategy."""
    
    details = {
        'Premium Product Upselling': 'Phase 1: Pilot program with 5 locations (Month 1-2), Phase 2: Taste testing and feedback (Month 3), Phase 3: Full rollout with marketing support (Month 4-6)',
        'Delivery Optimization': 'Week 1-2: Current route analysis, Week 3-4: New schedule design, Week 5-8: Pilot implementation, Week 9-12: Full deployment',
        'Digital Platform Enhancement': 'Month 1: Requirements gathering, Month 2: Platform development, Month 3: Testing and training, Month 4: Go-live support'
    }
    
    return details.get(strategy['title'], 'Custom implementation plan will be developed based on specific requirements and timeline.')

def generate_strategic_opportunities_list(customer_data):
    """Generate list of strategic opportunities."""
    
    opportunities = [
        {
            'name': 'Market Expansion',
            'impact_score': 8,
            'effort_score': 6,
            'revenue_potential': 2500000,
            'description': 'Expand to 20 new geographic markets within customer territory'
        },
        {
            'name': 'Product Innovation Partnership',
            'impact_score': 9,
            'effort_score': 7,
            'revenue_potential': 1800000,
            'description': 'Co-develop custom flavor profiles for customer demographic'
        },
        {
            'name': 'Digital Transformation',
            'impact_score': 7,
            'effort_score': 4,
            'revenue_potential': 800000,
            'description': 'Implement IoT-enabled smart dispensing systems'
        },
        {
            'name': 'Sustainability Initiative',
            'impact_score': 6,
            'effort_score': 5,
            'revenue_potential': 1200000,
            'description': 'Joint sustainability program with carbon-neutral delivery'
        },
        {
            'name': 'Category Management',
            'impact_score': 8,
            'effort_score': 3,
            'revenue_potential': 950000,
            'description': 'Comprehensive beverage category optimization'
        }
    ]
    
    return opportunities

def render_opportunity_details(opportunity):
    """Render detailed analysis for selected opportunity."""
    
    st.markdown(f"### 🎯 {opportunity['name']} - Detailed Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Revenue Potential", f"${opportunity['revenue_potential']:,.0f}")
    
    with col2:
        st.metric("Impact Score", f"{opportunity['impact_score']}/10")
    
    with col3:
        st.metric("Effort Score", f"{opportunity['effort_score']}/10")
    
    st.markdown(f"**Description:** {opportunity['description']}")
    
    # AI-generated opportunity analysis
    if st.button("🤖 Generate AI Analysis", key=f"analyze_{opportunity['name']}"):
        analysis = generate_opportunity_analysis(opportunity)
        st.success(f"**AI Analysis:** {analysis}")

def generate_opportunity_analysis(opportunity):
    """Generate AI analysis for an opportunity."""
    
    analyses = {
        'Market Expansion': 'Predictive models show 73% success probability based on demographic alignment and competitive landscape. Key success factors: timing with seasonal demand, local partnership strategy, and phased rollout approach.',
        'Product Innovation Partnership': 'Consumer sentiment analysis indicates strong demand for personalized products. Recommend focus on health-conscious formulations with 25% higher margin potential. Co-innovation timeline: 8-12 months.',
        'Digital Transformation': 'IoT implementation shows 85% ROI within 18 months through operational efficiency and data-driven insights. Customer digital maturity score of 78% indicates high adoption probability.',
        'Sustainability Initiative': 'ESG trends and customer values alignment score of 92% suggests strong stakeholder buy-in. Carbon footprint reduction of 30% achievable with 15% cost premium acceptable to customer.',
        'Category Management': 'Cross-category analysis reveals 23% margin improvement opportunity through portfolio optimization. Customer purchasing patterns support expanded beverage category presence.'
    }
    
    return analyses.get(opportunity['name'], 'AI analysis indicates positive opportunity with recommended deep-dive feasibility study.')

def generate_interaction_data(customer_data):
    """Generate customer interaction data."""
    
    interactions = []
    interaction_types = ['Email', 'Phone', 'Meeting', 'Support', 'Contract']
    
    for i in range(20):
        date = datetime.now() - timedelta(days=random.randint(1, 365))
        interaction_type = random.choice(interaction_types)
        
        interactions.append({
            'date': date.strftime('%Y-%m-%d'),
            'type': interaction_type,
            'summary': f"{interaction_type} regarding {'contract renewal' if random.random() > 0.7 else 'business review' if random.random() > 0.5 else 'product discussion'}",
            'participants': random.choice(['Sarah Johnson', 'Mike Chen', 'Lisa Rodriguez', 'David Kim']),
            'outcome': random.choice(['Positive', 'Neutral', 'Action Required']),
            'next_steps': random.choice(['Follow-up scheduled', 'Proposal pending', 'Information requested', 'Decision pending'])
        })
    
    return sorted(interactions, key=lambda x: x['date'], reverse=True)

def filter_interactions(interactions, interaction_type, date_range):
    """Filter interactions based on type and date range."""
    
    filtered = interactions
    
    if interaction_type != "All":
        filtered = [i for i in filtered if i['type'] == interaction_type]
    
    # For simplicity, return all interactions (in a real app, would filter by date)
    return filtered

def get_interaction_color(interaction_type):
    """Get color for interaction type."""
    
    colors = {
        'Email': '#1f77b4',
        'Phone': '#ff7f0e', 
        'Meeting': '#2ca02c',
        'Support': '#d62728',
        'Contract': '#9467bd'
    }
    
    return colors.get(interaction_type, '#black')

def analyze_interaction_patterns(interactions):
    """Analyze interaction patterns using AI."""
    
    patterns = [
        "Communication frequency increased 40% in last quarter, indicating growing engagement",
        "Email response rate of 87% suggests strong relationship health and communication effectiveness",
        "Meeting-to-contract ratio of 3:1 indicates efficient sales cycle management",
        "Support interaction decrease of 25% shows improved product satisfaction"
    ]
    
    return random.choice(patterns)

def generate_prediction(model_type, customer_data):
    """Generate prediction based on model type."""
    
    predictions = {
        'Churn Risk Prediction': {
            'result': 15,
            'unit': '% probability',
            'timeframe': 'next 12 months',
            'confidence': 89,
            'factors': ['Payment consistency', 'Engagement level', 'Competitive activity']
        },
        'Revenue Forecast': {
            'result': 52000000,
            'unit': 'dollars',
            'timeframe': 'next 12 months', 
            'confidence': 84,
            'factors': ['Historical growth', 'Market expansion', 'Product adoption']
        },
        'Upsell Probability': {
            'result': 73,
            'unit': '% probability',
            'timeframe': 'next 6 months',
            'confidence': 78,
            'factors': ['Product usage patterns', 'Budget availability', 'Decision maker engagement']
        }
    }
    
    return predictions.get(model_type, {
        'result': 75,
        'unit': '% probability',
        'timeframe': 'next 6 months',
        'confidence': 80,
        'factors': ['Multiple data points analyzed']
    })

def display_prediction_result(model_type, result):
    """Display prediction results."""
    
    st.success(f"🎯 **{model_type} Results:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Prediction", f"{result['result']} {result['unit']}")
    
    with col2:
        st.metric("Confidence", f"{result['confidence']}%")
    
    with col3:
        st.metric("Timeframe", result['timeframe'])
    
    st.markdown("**Key Contributing Factors:**")
    for factor in result['factors']:
        st.markdown(f"• {factor}")
    
    # AI recommendations based on prediction
    if 'Churn' in model_type and result['result'] > 20:
        st.warning("⚠️ **AI Recommendation:** Implement immediate retention strategy")
    elif 'Revenue' in model_type:
        st.info(f"💡 **AI Insight:** Revenue growth trajectory exceeds industry average by 23%")
    elif 'Upsell' in model_type and result['result'] > 70:
        st.success("✅ **AI Recommendation:** High probability - proceed with premium product presentation")
