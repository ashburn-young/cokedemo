"""
Enhanced UI Widgets for Coca-Cola Sales AI Platform
Reusable components for proactive sales features
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
from typing import Dict, List, Any, Optional

# Coca-Cola brand colors
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000',
    'classic_white': '#FFFFFF',
    'executive_blue': '#0078D4',
    'executive_green': '#00BCF2',
    'coke_gold': '#FFC72C',
    'dark_red': '#CC0000',
    'light_gray': '#F5F5F5',
    'dark_gray': '#6c757d',
    'info_blue': '#17a2b8',
    'success_green': '#28a745',
    'warning_orange': '#ffc107',
    'danger_red': '#dc3545'
}

class ProactiveWidgets:
    """Collection of proactive sales widgets and components"""
    
    @staticmethod
    def priority_alert_card(title: str, value: str, trend: str, color: str, icon: str = "📊") -> None:
        """Create a priority alert card for the dashboard"""
        trend_color = COKE_COLORS['success_green'] if trend.startswith('+') else COKE_COLORS['danger_red']
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {color}, {COKE_COLORS['coke_black']});
            padding: 20px;
            border-radius: 15px;
            color: white;
            margin: 10px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            border: 2px solid rgba(255,255,255,0.1);
        ">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3 style="margin: 0; font-size: 16px; opacity: 0.9;">{icon} {title}</h3>
                    <h1 style="margin: 10px 0 5px 0; font-size: 32px; font-weight: bold;">{value}</h1>
                    <p style="margin: 0; color: {trend_color}; font-weight: bold;">{trend}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def action_button_panel(actions: List[Dict[str, str]]) -> str:
        """Create quick action buttons panel"""
        st.markdown("### 🚀 Quick Actions")
        
        cols = st.columns(len(actions))
        selected_action = None
        
        for i, action in enumerate(actions):
            with cols[i]:
                # Use unique keys based on action name and index
                unique_key = f"action_{action['action']}_{i}_{hash(action['label'])}"
                if st.button(f"{action['icon']} {action['label']}", key=unique_key):
                    selected_action = action['action']
                    st.success(f"✅ {action['label']} initiated!")
        
        return selected_action
    
    @staticmethod
    def risk_indicator(risk_level: str, score: float = None) -> None:
        """Create a compact visual risk indicator using native Streamlit components"""
        
        icons = {
            "Low": "🟢",
            "Medium": "🟡",
            "High": "🟠", 
            "Critical": "🔴"
        }
        
        icon = icons.get(risk_level, "⚪")
        score_text = f" ({score:.0%})" if score else ""
        
        # Use inline markdown for more compact display
        if risk_level == "Critical":
            st.markdown(f"🔴 **{risk_level}**{score_text}")
        elif risk_level == "High":
            st.markdown(f"🟠 **{risk_level}**{score_text}")
        elif risk_level == "Medium":
            st.markdown(f"🟡 **{risk_level}**{score_text}")
        else:
            st.markdown(f"🟢 **{risk_level}**{score_text}")
    
    @staticmethod
    def enhanced_priority_indicator(priority: str, title: str = "", additional_info: str = "") -> None:
        """Create an enhanced priority indicator with better visibility"""
        colors = {
            "Low": COKE_COLORS['success_green'],
            "Medium": COKE_COLORS['executive_blue'], 
            "High": COKE_COLORS['warning_orange'],
            "Critical": COKE_COLORS['primary_red']
        }
        
        text_colors = {
            "Low": "white",
            "Medium": "white",
            "High": "black",
            "Critical": "white"
        }
        
        icons = {
            "Low": "✅",
            "Medium": "⚠️",
            "High": "🔥", 
            "Critical": "🚨"
        }
        
        bg_color = colors.get(priority, COKE_COLORS['light_gray'])
        text_color = text_colors.get(priority, "black")
        icon = icons.get(priority, "📋")
        
        title_display = f"<br><span style='font-size: 12px; opacity: 0.9;'>{title}</span>" if title else ""
        info_display = f"<br><span style='font-size: 11px; opacity: 0.8;'>{additional_info}</span>" if additional_info else ""
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {bg_color}, {bg_color}dd);
            color: {text_color};
            padding: 15px 20px;
            border-radius: 15px;
            font-weight: bold;
            text-align: center;
            margin: 8px;
            border: 2px solid rgba(255,255,255,0.2);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            min-height: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: transform 0.2s ease;
        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            <div style="font-size: 18px;">{icon}</div>
            <div style="font-size: 16px; margin: 5px 0;">{priority}</div>
            {title_display}
            {info_display}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def opportunity_kanban(opportunities_df: pd.DataFrame) -> None:
        """Create a Kanban-style opportunity board"""
        stages = ["Prospecting", "Qualification", "Needs Analysis", "Proposal", "Negotiation", "Closing"]
        
        st.markdown("### 📋 Pipeline Kanban Board")
        
        cols = st.columns(len(stages))
        
        for i, stage in enumerate(stages):
            stage_opps = opportunities_df[opportunities_df['stage'] == stage]
            stage_value = stage_opps['value'].sum()
            
            with cols[i]:
                st.markdown(f"""
                <div style="
                    background-color: {COKE_COLORS['light_gray']};
                    border-radius: 10px;
                    padding: 15px;
                    margin: 5px;
                    border-top: 4px solid {COKE_COLORS['primary_red']};
                ">
                    <h4 style="margin-top: 0; color: {COKE_COLORS['coke_black']};">{stage}</h4>
                    <p style="color: {COKE_COLORS['executive_blue']}; font-weight: bold;">
                        {len(stage_opps)} deals | ${stage_value:,.0f}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show top opportunities in each stage
                for _, opp in stage_opps.head(3).iterrows():
                    priority_color = {
                        "Critical": COKE_COLORS['danger_red'],
                        "High": COKE_COLORS['warning_orange'],
                        "Medium": COKE_COLORS['executive_blue'],
                        "Low": COKE_COLORS['light_gray']
                    }.get(opp['priority'], COKE_COLORS['light_gray'])
                    
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        border-left: 4px solid {priority_color};
                        padding: 10px;
                        margin: 5px 0;
                        border-radius: 5px;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    ">
                        <strong style="font-size: 14px; color: {COKE_COLORS['coke_black']};">{opp['opportunity_name'][:30]}...</strong><br>
                        <span style="color: {COKE_COLORS['executive_green']}; font-weight: bold;">
                            ${opp['value']:,.0f}
                        </span><br>
                        <small style="color: {COKE_COLORS['coke_black']};">
                            {opp['expected_close_date'].strftime('%m/%d')}
                        </small>
                    </div>
                    """, unsafe_allow_html=True)
    
    @staticmethod
    def account_health_heatmap(accounts_df: pd.DataFrame) -> go.Figure:
        """Create an interactive account health heatmap"""
        fig = go.Figure()
        
        # Prepare data for heatmap
        health_mapping = {"Low": 1, "Medium": 2, "High": 3}
        accounts_df['health_numeric'] = accounts_df['churn_risk'].map(health_mapping)
        
        # Group by region and industry
        heatmap_data = accounts_df.groupby(['region', 'industry']).agg({
            'health_numeric': 'mean',
            'account_id': 'count',
            'annual_revenue': 'sum'
        }).reset_index()
        
        # Create pivot table for heatmap
        pivot_data = heatmap_data.pivot(index='region', columns='industry', values='health_numeric')
        
        fig.add_trace(go.Heatmap(
            z=pivot_data.values,
            x=pivot_data.columns,
            y=pivot_data.index,
            colorscale=[[0, COKE_COLORS['danger_red']], [0.5, COKE_COLORS['warning_orange']], [1, COKE_COLORS['success_green']]],
            hovertemplate='Region: %{y}<br>Industry: %{x}<br>Health Score: %{z:.1f}<extra></extra>'
        ))
        
        fig.update_layout(
            title="Account Health by Region & Industry",
            xaxis_title="Industry",
            yaxis_title="Region",
            plot_bgcolor=COKE_COLORS['coke_black'],
            paper_bgcolor=COKE_COLORS['coke_black'],
            font=dict(color='white'),
            height=500
        )
        
        return fig
    
    @staticmethod
    def engagement_timeline(engagement_df: pd.DataFrame, account_id: str) -> go.Figure:
        """Create engagement timeline for a specific account"""
        account_engagements = engagement_df[engagement_df['account_id'] == account_id].copy()
        account_engagements = account_engagements.sort_values('engagement_date')
        
        fig = go.Figure()
        
        # Color mapping for engagement types
        color_map = {
            "Email": COKE_COLORS['executive_blue'],
            "Phone Call": COKE_COLORS['executive_green'],
            "In-Person Meeting": COKE_COLORS['primary_red'],
            "Video Call": COKE_COLORS['coke_gold'],
            "Text Message": COKE_COLORS['warning_orange'],
            "Trade Show": COKE_COLORS['executive_green'],
            "Presentation": COKE_COLORS['primary_red'],
            "Contract Review": COKE_COLORS['coke_black']
        }
        
        for engagement_type in account_engagements['engagement_type'].unique():
            type_data = account_engagements[account_engagements['engagement_type'] == engagement_type]
            
            fig.add_trace(go.Scatter(
                x=type_data['engagement_date'],
                y=type_data['engagement_type'],
                mode='markers+text',
                marker=dict(
                    size=12,
                    color=color_map.get(engagement_type, COKE_COLORS['light_gray']),
                    line=dict(width=2, color='white')
                ),
                text=type_data['outcome'],
                textposition="top center",
                name=engagement_type,
                hovertemplate=f'<b>{engagement_type}</b><br>Date: %{{x}}<br>Outcome: %{{text}}<extra></extra>'
            ))
        
        fig.update_layout(
            title=f"Engagement Timeline - {account_id}",
            xaxis_title="Date",
            yaxis_title="Engagement Type",
            plot_bgcolor=COKE_COLORS['coke_black'],
            paper_bgcolor=COKE_COLORS['coke_black'],
            font=dict(color='white'),
            height=400,
            showlegend=True
        )
        
        return fig
    
    @staticmethod
    def forecasting_chart(opportunities_df: pd.DataFrame) -> go.Figure:
        """Create revenue forecasting chart"""
        # Group by expected close date and forecast category
        forecast_data = opportunities_df.groupby([
            opportunities_df['expected_close_date'].dt.to_period('M').astype(str),
            'forecast_category'
        ])['weighted_value'].sum().reset_index()
        
        fig = go.Figure()
        
        forecast_colors = {
            "Commit": COKE_COLORS['success_green'],
            "Best Case": COKE_COLORS['executive_blue'],
            "Pipeline": COKE_COLORS['warning_orange'],
            "Upside": COKE_COLORS['light_gray']
        }
        
        for category in ["Commit", "Best Case", "Pipeline", "Upside"]:
            category_data = forecast_data[forecast_data['forecast_category'] == category]
            
            fig.add_trace(go.Bar(
                x=category_data['expected_close_date'],
                y=category_data['weighted_value'],
                name=category,
                marker_color=forecast_colors[category],
                hovertemplate=f'<b>{category}</b><br>Month: %{{x}}<br>Value: $%{{y:,.0f}}<extra></extra>'
            ))
        
        fig.update_layout(
            title="Revenue Forecast by Category",
            xaxis_title="Month",
            yaxis_title="Revenue ($)",
            barmode='stack',
            plot_bgcolor=COKE_COLORS['coke_black'],
            paper_bgcolor=COKE_COLORS['coke_black'],
            font=dict(color='white'),
            height=400
        )
        
        return fig
    
    @staticmethod
    def customer_360_profile(account: pd.Series, engagements_df: pd.DataFrame, 
                           performance_df: pd.DataFrame) -> None:
        """Create comprehensive Customer 360 profile view"""
        st.markdown(f"# 🏢 {account['company_name']} - Customer 360")
        
        # Customer overview cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            ProactiveWidgets.priority_alert_card(
                "Annual Revenue", 
                f"${account['annual_revenue']:,.0f}",
                f"+{account['growth_rate']:.1%} YoY",
                COKE_COLORS['executive_green'],
                "💰"
            )
        
        with col2:
            risk_color = {
                "Low": COKE_COLORS['success_green'],
                "Medium": COKE_COLORS['warning_orange'],
                "High": COKE_COLORS['danger_red']
            }.get(account['churn_risk'], COKE_COLORS['light_gray'])
            
            ProactiveWidgets.priority_alert_card(
                "Churn Risk",
                account['churn_risk'],
                f"{account['churn_probability']:.0%} probability",
                risk_color,
                "⚠️"
            )
        
        with col3:
            sentiment_color = COKE_COLORS['success_green'] if account['sentiment_score'] > 0 else COKE_COLORS['danger_red']
            ProactiveWidgets.priority_alert_card(
                "Sentiment Score",
                f"{account['sentiment_score']:.2f}",
                "Customer satisfaction",
                sentiment_color,
                "😊" if account['sentiment_score'] > 0 else "😞"
            )
        
        with col4:
            ProactiveWidgets.priority_alert_card(
                "Contract Renewal",
                f"{account['days_to_renewal']} days",
                "Until renewal",
                COKE_COLORS['executive_blue'],
                "📅"
            )
        
        # Detailed sections
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Engagement timeline
            account_engagements = engagements_df[engagements_df['account_id'] == account['account_id']]
            if not account_engagements.empty:
                fig = ProactiveWidgets.engagement_timeline(engagements_df, account['account_id'])
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Key metrics and info
            st.markdown("### 📊 Key Metrics")
            
            metrics_html = f"""
            <div style="background-color: {COKE_COLORS['light_gray']}; padding: 15px; border-radius: 10px;">
                <p><strong>Industry:</strong> {account['industry']}</p>
                <p><strong>Region:</strong> {account['region']}</p>
                <p><strong>Primary Contact:</strong> {account['primary_contact']}</p>
                <p><strong>Sales Rep:</strong> {account['assigned_rep']}</p>
                <p><strong>Total Locations:</strong> {account['total_locations']}</p>
                <p><strong>Freestyle Machines:</strong> {account['freestyle_machines']}</p>
                <p><strong>Customer Since:</strong> {account['customer_since']}</p>
                <p><strong>Payment History:</strong> {account['payment_history']}</p>
                <p><strong>NPS Score:</strong> {account['nps_score']}</p>
                <p><strong>Expansion Potential:</strong> {account['expansion_potential']}</p>
            </div>
            """
            st.markdown(metrics_html, unsafe_allow_html=True)
    
    @staticmethod
    def ai_recommendations_panel(account_data: Optional[pd.Series] = None, 
                               opportunity_data: Optional[pd.Series] = None) -> None:
        """Generate AI-powered recommendations with confidence scores"""
        st.markdown("### 🤖 AI Recommendations")
        
        recommendations = [
            {
                "title": "Increase Engagement",
                "description": "Schedule quarterly business review with key stakeholders",
                "confidence": 0.87,
                "impact": "$45K potential revenue increase",
                "action": "Schedule meeting with decision makers",
                "timeline": "Within 2 weeks",
                "category": "Relationship"
            },
            {
                "title": "Product Expansion",
                "description": "Introduce Freestyle Zero Mix based on customer preferences",
                "confidence": 0.73,
                "impact": "$28K additional monthly revenue",
                "action": "Prepare product demo and pricing proposal",
                "timeline": "Next month",
                "category": "Product"
            },
            {
                "title": "Risk Mitigation",
                "description": "Address service concerns before contract renewal",
                "confidence": 0.92,
                "impact": "Reduce churn risk by 65%",
                "action": "Immediate service team consultation",
                "timeline": "This week",
                "category": "Retention"
            }
        ]
        
        for i, rec in enumerate(recommendations):
            confidence_color = (
                COKE_COLORS['success_green'] if rec['confidence'] > 0.8 else
                COKE_COLORS['warning_orange'] if rec['confidence'] > 0.6 else
                COKE_COLORS['danger_red']
            )
            
            st.markdown(f"""
            <div style="
                background-color: white;
                border-left: 5px solid {confidence_color};
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            ">
                <h4 style="margin-top: 0; color: {COKE_COLORS['coke_black']};">
                    {rec['title']} 
                    <span style="background-color: {confidence_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px;">
                        {rec['confidence']:.0%} confidence
                    </span>
                </h4>
                <p style="color: {COKE_COLORS['coke_black']};">{rec['description']}</p>
                <p style="color: {COKE_COLORS['executive_green']}; font-weight: bold;">💰 {rec['impact']}</p>
                <p style="color: {COKE_COLORS['executive_blue']};">🎯 <strong>Action:</strong> {rec['action']}</p>
                <p style="color: {COKE_COLORS['warning_orange']};">⏰ <strong>Timeline:</strong> {rec['timeline']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Take Action: {rec['title']}", key=f"ai_rec_{i}"):
                st.success(f"✅ Action initiated for: {rec['title']}")
    
    @staticmethod
    def chat_interface(context_type: str = "general") -> None:
        """Create interactive chat interface for asking questions"""
        st.markdown("### 💬 Ask Questions About...")
        
        # Context selector
        context_options = {
            "Customer Account": "Ask about specific customer accounts and their history",
            "Opportunity": "Get insights about specific deals and opportunities", 
            "Product Performance": "Analyze product sales and trends",
            "Market Intelligence": "Competitive analysis and market insights",
            "General": "General sales and business questions"
        }
        
        selected_context = st.selectbox(
            "Choose context:",
            options=list(context_options.keys()),
            help="Select the type of question you want to ask"
        )
        
        st.info(f"💡 {context_options[selected_context]}")
        
        # Chat input
        user_question = st.text_input(
            "Ask your question:",
            placeholder="e.g., What's the churn risk for Metro Restaurant Group?",
            key="ai_chat_input"
        )
        
        if st.button("Ask AI", key="ask_ai_button") and user_question:
            with st.spinner("🤖 AI is thinking..."):
                # Simulate AI response (in real implementation, this would call Azure OpenAI)
                ai_responses = {
                    "Customer Account": f"Based on the data analysis, here are the key insights about the customer account related to '{user_question}':\n\n• Account health score: 0.72 (Good)\n• Recent engagement: 3 touchpoints in last 30 days\n• Risk factors: Contract renewal in 45 days\n• Recommendation: Schedule business review meeting",
                    
                    "Opportunity": f"Here's the opportunity analysis for '{user_question}':\n\n• Current stage: Proposal (65% probability)\n• Expected value: $125,000\n• Key stakeholders: 3 decision makers identified\n• Next step: Follow up on pricing proposal\n• Timeline: 2-3 weeks to closure",
                    
                    "Product Performance": f"Product performance insights for '{user_question}':\n\n• Growth trend: +12% vs last quarter\n• Top performing regions: North America East, West\n• Customer satisfaction: 4.2/5.0\n• Competitive position: Strong\n• Expansion opportunity: High in convenience store segment",
                    
                    "Market Intelligence": f"Market intelligence summary for '{user_question}':\n\n• Market share: 67% in target segment\n• Competitive threats: Medium pressure from local brands\n• Growth opportunities: +15% potential in emerging markets\n• Price sensitivity: Low to medium\n• Recommended strategy: Focus on service differentiation",
                    
                    "General": f"Here's what I found regarding '{user_question}':\n\n• Current pipeline value: $2.4M across 47 opportunities\n• Average deal size: $85K\n• Win rate: 72% (above industry average)\n• Top growth driver: Freestyle machine installations\n• Key focus area: Customer retention and expansion"
                }
                
                response = ai_responses.get(selected_context, "I'll analyze that question and provide insights based on our data.")
                
                st.markdown(f"""
                <div style="
                    background-color: {COKE_COLORS['executive_blue']};
                    color: white;
                    padding: 15px;
                    border-radius: 10px;
                    margin: 10px 0;
                ">
                    <h4>🤖 AI Response:</h4>
                    <p>{response}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Add follow-up suggestions
                st.markdown("**💡 Related questions you might ask:**")
                follow_ups = [
                    "What are the top 3 risks in my pipeline?",
                    "Which customers are most likely to churn?",
                    "What products should I focus on this quarter?",
                    "How does my performance compare to targets?"
                ]
                
                for follow_up in follow_ups:
                    if st.button(f"💬 {follow_up}", key=f"followup_{follow_up}"):
                        st.rerun()

# Global instance for easy access
proactive_widgets = ProactiveWidgets()
