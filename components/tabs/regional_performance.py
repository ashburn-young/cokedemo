"""
Regional Performance Tab - Interactive Geographic Performance Analytics
AI-powered regional analysis with maps, territory optimization, and competitive intelligence
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
from datetime import datetime, timedelta
import time

def generate_mock_regional_data():
    """Generate realistic regional performance data"""
    regions = [
        {"name": "Northeast", "states": ["NY", "MA", "CT", "NJ", "PA"], "lat": 40.7128, "lon": -74.0060},
        {"name": "Southeast", "states": ["FL", "GA", "NC", "SC", "VA"], "lat": 33.7490, "lon": -84.3880},
        {"name": "Midwest", "states": ["IL", "OH", "MI", "IN", "WI"], "lat": 41.8781, "lon": -87.6298},
        {"name": "Southwest", "states": ["TX", "AZ", "NM", "OK"], "lat": 32.7767, "lon": -96.7970},
        {"name": "West", "states": ["CA", "WA", "OR", "NV", "CO"], "lat": 34.0522, "lon": -118.2437},
        {"name": "Mountain", "states": ["UT", "ID", "MT", "WY"], "lat": 39.7392, "lon": -104.9903}
    ]
    
    # Generate regional performance metrics
    regional_data = []
    for region in regions:
        base_performance = random.uniform(0.7, 1.3)
        
        data = {
            "Region": region["name"],
            "Revenue": random.randint(15000000, 45000000) * base_performance,
            "Growth_Rate": random.uniform(-2, 15) * base_performance,
            "Market_Share": random.uniform(25, 45),
            "Customer_Count": random.randint(800, 2500),
            "Avg_Deal_Size": random.randint(8000, 25000),
            "Sales_Cycle": random.randint(30, 120),
            "Satisfaction_Score": random.uniform(3.8, 4.9),
            "Latitude": region["lat"],
            "Longitude": region["lon"],
            "Competitive_Threat": random.choice(["Low", "Medium", "High"]),
            "Territory_Efficiency": random.uniform(65, 95),
            "States": len(region["states"])
        }
        regional_data.append(data)
    
    return pd.DataFrame(regional_data)

def generate_territory_opportunities():
    """Generate territory optimization opportunities"""
    return [
        {
            "Territory": "Northeast Metro",
            "Opportunity": "Redistribute QSR accounts between NY and NJ territories",
            "Impact": "15% efficiency gain",
            "AI_Confidence": 0.87,
            "Implementation": "Q1 2024",
            "Details": "AI analysis shows 23 QSR accounts in NY territory could be better served from NJ hub, reducing travel time by 40%"
        },
        {
            "Territory": "Southeast Coastal",
            "Opportunity": "Create specialized tourism/hospitality sub-territory",
            "Impact": "22% revenue increase",
            "AI_Confidence": 0.91,
            "Implementation": "Q2 2024",
            "Details": "High-value tourism accounts in FL require specialized attention during peak seasons"
        },
        {
            "Territory": "Texas Central",
            "Opportunity": "Expand coverage to underserved rural markets",
            "Impact": "12% market expansion",
            "AI_Confidence": 0.73,
            "Implementation": "Q3 2024",
            "Details": "GPT-4o identified 45 untapped rural communities with strong demographic fit"
        },
        {
            "Territory": "California North",
            "Opportunity": "Split tech corridor accounts into dedicated territory",
            "Impact": "30% growth potential",
            "AI_Confidence": 0.94,
            "Implementation": "Q1 2024",
            "Details": "Silicon Valley accounts require specialized approach and dedicated resources"
        }
    ]

def generate_competitive_intelligence():
    """Generate competitive intelligence by region"""
    return {
        "Northeast": {
            "Primary_Competitor": "Pepsi",
            "Market_Share_Gap": "8%",
            "Recent_Activity": "Launched new energy drink campaign targeting Gen Z",
            "Threat_Level": "High",
            "Counter_Strategy": "Focus on Coca-Cola Energy and Zero Sugar positioning"
        },
        "Southeast": {
            "Primary_Competitor": "Dr Pepper",
            "Market_Share_Gap": "12%",
            "Recent_Activity": "Expanded fountain partnerships in QSR segment",
            "Threat_Level": "Medium",
            "Counter_Strategy": "Leverage Freestyle technology advantage"
        },
        "Midwest": {
            "Primary_Competitor": "Pepsi",
            "Market_Share_Gap": "6%",
            "Recent_Activity": "Price promotion in convenience channel",
            "Threat_Level": "Medium",
            "Counter_Strategy": "Emphasize brand loyalty and taste preference"
        },
        "Southwest": {
            "Primary_Competitor": "Local Brands",
            "Market_Share_Gap": "4%",
            "Recent_Activity": "Hispanic market targeting with local flavors",
            "Threat_Level": "Low",
            "Counter_Strategy": "Expand multicultural marketing initiatives"
        },
        "West": {
            "Primary_Competitor": "Premium Brands",
            "Market_Share_Gap": "15%",
            "Recent_Activity": "Health-conscious product launches",
            "Threat_Level": "High",
            "Counter_Strategy": "Promote Zero Sugar and natural ingredient lines"
        },
        "Mountain": {
            "Primary_Competitor": "Regional Players",
            "Market_Share_Gap": "3%",
            "Recent_Activity": "Outdoor recreation sponsorships",
            "Threat_Level": "Low",
            "Counter_Strategy": "Leverage outdoor lifestyle partnerships"
        }
    }

def render_ai_regional_insights():
    """Render AI-powered regional insights"""
    st.markdown("### 🤖 AI Regional Intelligence")
    
    # GPT-4o powered insights
    insights = [
        {
            "type": "opportunity",
            "title": "West Coast Expansion Opportunity",
            "content": "GPT-4o analysis indicates 34% untapped potential in premium segment. Recommend launching craft cola initiatives in Portland and Seattle markets.",
            "confidence": 0.89,
            "action": "Schedule market research for Q1 2024"
        },
        {
            "type": "threat",
            "title": "Northeast Competitive Pressure",
            "content": "Competitor activity increased 45% in NY/NJ corridor. AI predicts 8% market share risk if no action taken within 60 days.",
            "confidence": 0.92,
            "action": "Deploy premium promotion campaign immediately"
        },
        {
            "type": "optimization",
            "title": "Midwest Territory Realignment",
            "content": "Machine learning model suggests redistributing 17 accounts could improve territory efficiency by 23% and reduce costs by $2.1M annually.",
            "confidence": 0.85,
            "action": "Present realignment proposal to regional manager"
        }
    ]
    
    for insight in insights:
        icon = "🎯" if insight["type"] == "opportunity" else "⚠️" if insight["type"] == "threat" else "⚙️"
        color = "success" if insight["type"] == "opportunity" else "error" if insight["type"] == "threat" else "info"
        
        with st.container():
            st.markdown(f"""
            <div style="
                border-left: 4px solid {'#28a745' if color == 'success' else '#dc3545' if color == 'error' else '#007bff'};
                background: {'#d4edda' if color == 'success' else '#f8d7da' if color == 'error' else '#d1ecf1'};
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
            ">
                <h4 style="margin: 0; color: #333;">{icon} {insight['title']}</h4>
                <p style="margin: 10px 0; color: #666;">{insight['content']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <small style="color: #777;">AI Confidence: {insight['confidence']:.0%}</small>
                    <strong style="color: #333;">➡️ {insight['action']}</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_regional_performance():
    """Main function to render the Regional Performance tab"""
    
    st.markdown("# 🗺️ Regional Performance Analytics")
    st.markdown("*AI-powered regional insights, territory optimization, and competitive intelligence*")
    
    # Generate data
    regional_df = generate_mock_regional_data()
    territory_opps = generate_territory_opportunities()
    competitive_intel = generate_competitive_intelligence()
    
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = regional_df['Revenue'].sum()
        st.metric("Total Regional Revenue", f"${total_revenue/1000000:.1f}M", "+8.5%")
    
    with col2:
        avg_growth = regional_df['Growth_Rate'].mean()
        st.metric("Average Growth Rate", f"{avg_growth:.1f}%", "+2.3%")
    
    with col3:
        avg_market_share = regional_df['Market_Share'].mean()
        st.metric("Average Market Share", f"{avg_market_share:.1f}%", "+1.2%")
    
    with col4:
        total_customers = regional_df['Customer_Count'].sum()
        st.metric("Total Customers", f"{total_customers:,}", "+156")
    
    st.divider()
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🗺️ Interactive Map", 
        "📊 Regional Dashboard", 
        "🎯 Territory Optimization", 
        "⚔️ Competitive Intelligence",
        "🤖 AI Insights"
    ])
    
    with tab1:
        st.markdown("### 🗺️ Regional Performance Heatmap")
        
        # Create interactive map
        fig = go.Figure()
        
        # Add regional performance markers
        fig.add_trace(go.Scattermapbox(
            lat=regional_df['Latitude'],
            lon=regional_df['Longitude'],
            mode='markers',
            marker=dict(
                size=regional_df['Revenue'] / 1000000,  # Size based on revenue
                color=regional_df['Growth_Rate'],  # Color based on growth
                colorscale='RdYlGn',
                colorbar=dict(title="Growth Rate %"),
                sizemode='diameter',
                sizeref=0.1
            ),
            text=regional_df.apply(lambda x: f"""
            <b>{x['Region']}</b><br>
            Revenue: ${x['Revenue']/1000000:.1f}M<br>
            Growth: {x['Growth_Rate']:.1f}%<br>
            Market Share: {x['Market_Share']:.1f}%<br>
            Customers: {x['Customer_Count']:,}
            """, axis=1),
            hovertemplate='%{text}<extra></extra>',
            name="Regional Performance"
        ))
        
        fig.update_layout(
            mapbox=dict(
                style="open-street-map",
                center=dict(lat=39.8283, lon=-98.5795),  # Center of US
                zoom=3
            ),
            height=500,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Map insights
        st.markdown("#### 🔍 Map Insights")
        col1, col2 = st.columns(2)
        
        with col1:
            best_region = regional_df.loc[regional_df['Growth_Rate'].idxmax()]
            st.success(f"🏆 **Top Performer**: {best_region['Region']} ({best_region['Growth_Rate']:.1f}% growth)")
            
        with col2:
            challenge_region = regional_df.loc[regional_df['Growth_Rate'].idxmin()]
            st.warning(f"📈 **Growth Opportunity**: {challenge_region['Region']} ({challenge_region['Growth_Rate']:.1f}% growth)")
    
    with tab2:
        st.markdown("### 📊 Regional Performance Dashboard")
        
        # Performance comparison charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Revenue by region
            fig_revenue = px.bar(
                regional_df, 
                x='Region', 
                y='Revenue',
                title="Revenue by Region",
                color='Growth_Rate',
                color_continuous_scale='RdYlGn'
            )
            fig_revenue.update_layout(height=300)
            st.plotly_chart(fig_revenue, use_container_width=True)
            
        with col2:
            # Market share comparison
            fig_share = px.pie(
                regional_df, 
                values='Market_Share', 
                names='Region',
                title="Market Share Distribution"
            )
            fig_share.update_layout(height=300)
            st.plotly_chart(fig_share, use_container_width=True)
        
        # Regional metrics table
        st.markdown("### 📋 Regional Metrics Overview")
        
        # Format the dataframe for display
        display_df = regional_df.copy()
        display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"${x/1000000:.1f}M")
        display_df['Growth_Rate'] = display_df['Growth_Rate'].apply(lambda x: f"{x:.1f}%")
        display_df['Market_Share'] = display_df['Market_Share'].apply(lambda x: f"{x:.1f}%")
        display_df['Customer_Count'] = display_df['Customer_Count'].apply(lambda x: f"{x:,}")
        display_df['Avg_Deal_Size'] = display_df['Avg_Deal_Size'].apply(lambda x: f"${x:,}")
        display_df['Territory_Efficiency'] = display_df['Territory_Efficiency'].apply(lambda x: f"{x:.1f}%")
        
        selected_cols = ['Region', 'Revenue', 'Growth_Rate', 'Market_Share', 'Customer_Count', 'Avg_Deal_Size', 'Territory_Efficiency']
        st.dataframe(display_df[selected_cols], use_container_width=True)
    
    with tab3:
        st.markdown("### 🎯 AI-Powered Territory Optimization")
        
        st.markdown("#### 🚀 Optimization Opportunities")
        
        for opp in territory_opps:
            with st.expander(f"🎯 {opp['Territory']} - {opp['Impact']} potential"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Opportunity**: {opp['Opportunity']}")
                    st.markdown(f"**Details**: {opp['Details']}")
                    st.markdown(f"**Implementation Timeline**: {opp['Implementation']}")
                
                with col2:
                    st.metric("Expected Impact", opp['Impact'])
                    st.metric("AI Confidence", f"{opp['AI_Confidence']:.0%}")
                    
                    if st.button(f"Approve Plan", key=f"approve_{opp['Territory']}"):
                        st.success("✅ Optimization plan approved for implementation!")
        
        # Territory efficiency visualization
        st.markdown("#### 📈 Territory Efficiency Analysis")
        
        efficiency_data = {
            'Territory': ['Northeast Metro', 'Southeast Coastal', 'Midwest Central', 'Texas Central', 'California North', 'Mountain West'],
            'Current_Efficiency': [78, 85, 92, 67, 88, 74],
            'Optimized_Efficiency': [89, 94, 95, 84, 92, 87],
            'Improvement': [11, 9, 3, 17, 4, 13]
        }
        efficiency_df = pd.DataFrame(efficiency_data)
        
        fig_efficiency = go.Figure()
        
        fig_efficiency.add_trace(go.Bar(
            name='Current',
            x=efficiency_df['Territory'],
            y=efficiency_df['Current_Efficiency'],
            marker_color='lightblue'
        ))
        
        fig_efficiency.add_trace(go.Bar(
            name='Optimized',
            x=efficiency_df['Territory'],
            y=efficiency_df['Optimized_Efficiency'],
            marker_color='darkblue'
        ))
        
        fig_efficiency.update_layout(
            title="Territory Efficiency: Current vs Optimized",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_efficiency, use_container_width=True)
    
    with tab4:
        st.markdown("### ⚔️ Competitive Intelligence Dashboard")
        
        # Competitive overview
        st.markdown("#### 🔍 Regional Competitive Landscape")
        
        for region, intel in competitive_intel.items():
            threat_color = "#dc3545" if intel["Threat_Level"] == "High" else "#ffc107" if intel["Threat_Level"] == "Medium" else "#28a745"
            
            with st.container():
                st.markdown(f"""
                <div style="
                    border: 2px solid {threat_color};
                    border-radius: 10px;
                    padding: 15px;
                    margin: 10px 0;
                    background: {'#fff5f5' if intel['Threat_Level'] == 'High' else '#fffbf0' if intel['Threat_Level'] == 'Medium' else '#f0fff4'};
                ">
                    <h4 style="color: {threat_color}; margin: 0;">🏆 {region} Region</h4>
                    <div style="margin: 10px 0;">
                        <strong>Primary Competitor:</strong> {intel['Primary_Competitor']}<br>
                        <strong>Market Share Gap:</strong> {intel['Market_Share_Gap']}<br>
                        <strong>Threat Level:</strong> <span style="color: {threat_color};">{intel['Threat_Level']}</span>
                    </div>
                    <div style="margin: 10px 0;">
                        <strong>Recent Activity:</strong> {intel['Recent_Activity']}
                    </div>
                    <div style="background: #f8f9fa; padding: 10px; border-radius: 5px; margin-top: 10px;">
                        <strong>🎯 Counter Strategy:</strong> {intel['Counter_Strategy']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Competitive trends
        st.markdown("#### 📈 Competitive Activity Trends")
        
        # Generate trend data
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        competitor_activity = {
            'Date': dates,
            'Pepsi_Activity': np.random.normal(50, 15, 30),
            'Dr_Pepper_Activity': np.random.normal(30, 10, 30),
            'Local_Brands_Activity': np.random.normal(20, 8, 30)
        }
        trend_df = pd.DataFrame(competitor_activity)
        
        fig_trends = go.Figure()
        
        fig_trends.add_trace(go.Scatter(
            x=trend_df['Date'],
            y=trend_df['Pepsi_Activity'],
            mode='lines',
            name='Pepsi Activity',
            line=dict(color='blue')
        ))
        
        fig_trends.add_trace(go.Scatter(
            x=trend_df['Date'],
            y=trend_df['Dr_Pepper_Activity'],
            mode='lines',
            name='Dr Pepper Activity',
            line=dict(color='red')
        ))
        
        fig_trends.add_trace(go.Scatter(
            x=trend_df['Date'],
            y=trend_df['Local_Brands_Activity'],
            mode='lines',
            name='Local Brands Activity',
            line=dict(color='green')
        ))
        
        fig_trends.update_layout(
            title="Competitive Activity Index (Last 30 Days)",
            xaxis_title="Date",
            yaxis_title="Activity Index",
            height=400
        )
        
        st.plotly_chart(fig_trends, use_container_width=True)
    
    with tab5:
        render_ai_regional_insights()
        
        # AI-powered recommendations
        st.markdown("### 🎯 Strategic Recommendations")
        
        recommendations = [
            {
                "priority": "High",
                "region": "West Coast",
                "action": "Launch premium positioning campaign",
                "reasoning": "GPT-4o analysis shows 89% correlation between premium messaging and revenue growth in similar demographics",
                "timeline": "30 days",
                "roi": "245%"
            },
            {
                "priority": "Medium",
                "region": "Southeast",
                "action": "Expand QSR partnerships",
                "reasoning": "Machine learning model predicts 34% growth opportunity in underserved QSR segment",
                "timeline": "60 days",
                "roi": "178%"
            },
            {
                "priority": "Medium",
                "region": "Midwest",
                "action": "Implement loyalty program",
                "reasoning": "Customer behavior analysis indicates high retention potential with targeted loyalty initiatives",
                "timeline": "90 days",
                "roi": "156%"
            }
        ]
        
        for rec in recommendations:
            priority_color = "#dc3545" if rec["priority"] == "High" else "#ffc107" if rec["priority"] == "Medium" else "#28a745"
            
            with st.container():
                st.markdown(f"""
                <div style="
                    border-left: 5px solid {priority_color};
                    background: white;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <h4 style="margin: 0; color: #333;">{rec['region']}: {rec['action']}</h4>
                        <span style="background: {priority_color}; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px;">
                            {rec['priority']} Priority
                        </span>
                    </div>
                    <p style="color: #666; margin: 10px 0;">{rec['reasoning']}</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-top: 10px;">
                        <div><strong>Timeline:</strong> {rec['timeline']}</div>
                        <div><strong>Expected ROI:</strong> {rec['roi']}</div>
                        <div><strong>AI Confidence:</strong> 87%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Real-time AI chat assistant
        st.markdown("### 💬 Regional Performance AI Assistant")
        
        # Chat interface
        if "regional_chat_history" not in st.session_state:
            st.session_state.regional_chat_history = []
        
        user_question = st.text_input("Ask about regional performance, territories, or competitive landscape:")
        
        if user_question:
            # Simulate AI response
            ai_responses = [
                f"Based on our regional data analysis, I can see that {user_question} relates to territory optimization. Let me analyze the current performance metrics...",
                f"Looking at the competitive intelligence for your question about {user_question}, I recommend focusing on market share growth strategies...",
                f"The regional performance data shows interesting patterns related to {user_question}. Here's my analysis...",
            ]
            
            response = random.choice(ai_responses)
            
            st.session_state.regional_chat_history.append({
                "user": user_question,
                "ai": response,
                "timestamp": datetime.now()
            })
        
        # Display chat history
        if st.session_state.regional_chat_history:
            st.markdown("#### 💭 Recent Conversations")
            for chat in st.session_state.regional_chat_history[-3:]:  # Show last 3
                st.markdown(f"**You**: {chat['user']}")
                st.markdown(f"**AI**: {chat['ai']}")
                st.markdown("---")

if __name__ == "__main__":
    render_regional_performance()
