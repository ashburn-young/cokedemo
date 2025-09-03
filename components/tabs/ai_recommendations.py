"""
AI Recommendations Tab for Coca-Cola Sales AI Platform
Actionable AI insights, recommendations, and interactive Q&A
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Any
import sys
import os
import random

# Add components to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widgets.proactive_widgets import ProactiveWidgets, COKE_COLORS
from data.enhanced_data_generator import EnhancedDataGenerator

def simulate_ai_response(question: str) -> str:
    """Simulate AI response based on question type"""
    
    responses = {
        'revenue': [
            "Based on current trends, I recommend focusing on Freestyle machine expansion in QSR accounts. This could increase revenue by 15-20% in targeted locations.",
            "The data shows that accounts with Coca-Cola Classic + Zero Sugar combinations have 23% higher revenue. Consider bundled promotions.",
            "Regional analysis indicates North America-West has untapped potential worth $2.3M in Q4. Recommend increasing field presence."
        ],
        'churn': [
            "I've identified 12 accounts showing early churn signals. Recommend immediate outreach with retention specialists.",
            "Accounts with declining engagement scores have 67% higher churn probability. Deploy automated nurture campaigns.",
            "Payment delays combined with reduced order frequency indicate churn risk. Recommend flexible payment terms for at-risk accounts."
        ],
        'opportunity': [
            "Cross-sell analysis shows 23 accounts ready for premium product upgrades. Expected incremental revenue: $450K.",
            "Seasonal demand patterns suggest increasing inventory for key accounts by 18% before holiday season.",
            "Competitive analysis indicates 8 accounts vulnerable to switcher campaigns. Recommended retention budget: $75K."
        ],
        'general': [
            "Based on your sales data, I recommend prioritizing the top 15% of opportunities that have both high value and probability.",
            "Market intelligence suggests launching a focused campaign on sustainability messaging for enterprise accounts.",
            "Customer sentiment analysis indicates strong satisfaction with Zero Sugar products. Consider expanding this line."
        ]
    }
    
    # Simple keyword matching to determine response type
    question_lower = question.lower()
    if any(word in question_lower for word in ['revenue', 'sales', 'money', 'profit']):
        return random.choice(responses['revenue'])
    elif any(word in question_lower for word in ['churn', 'risk', 'leaving', 'lost']):
        return random.choice(responses['churn'])
    elif any(word in question_lower for word in ['opportunity', 'deal', 'prospect', 'pipeline']):
        return random.choice(responses['opportunity'])
    else:
        return random.choice(responses['general'])

def show_implementation_workflow(recommendation: Dict[str, Any]):
    """Show detailed implementation workflow and task tracking"""
    
    with st.container():
        st.markdown(f"### 🚀 Implementation Workflow: {recommendation['title']}")
        
        # Implementation timeline and tasks
        st.markdown("#### 📅 Implementation Timeline & Tasks")
        
        # Define detailed tasks based on recommendation type
        if "Freestyle" in recommendation['title']:
            tasks = [
                {"task": "Site Survey & Assessment", "duration": "3 days", "owner": "Field Operations", "status": "Not Started"},
                {"task": "Installation Scheduling", "duration": "5 days", "owner": "Logistics Team", "status": "Not Started"},
                {"task": "Account Manager Briefing", "duration": "2 days", "owner": "Sales Team", "status": "Not Started"},
                {"task": "Equipment Delivery", "duration": "7 days", "owner": "Supply Chain", "status": "Not Started"},
                {"task": "Installation & Training", "duration": "10 days", "owner": "Technical Team", "status": "Not Started"},
                {"task": "Performance Monitoring", "duration": "Ongoing", "owner": "Analytics Team", "status": "Not Started"}
            ]
        elif "At-Risk" in recommendation['title']:
            tasks = [
                {"task": "Risk Assessment Review", "duration": "1 day", "owner": "Customer Success", "status": "Not Started"},
                {"task": "Executive Outreach", "duration": "3 days", "owner": "Sales Manager", "status": "Not Started"},
                {"task": "Retention Proposal Creation", "duration": "2 days", "owner": "Sales Team", "status": "Not Started"},
                {"task": "Negotiation & Agreement", "duration": "7 days", "owner": "Account Manager", "status": "Not Started"},
                {"task": "Recovery Plan Implementation", "duration": "30 days", "owner": "Customer Success", "status": "Not Started"},
                {"task": "Success Metrics Tracking", "duration": "Ongoing", "owner": "Analytics Team", "status": "Not Started"}
            ]
        elif "Cross-Sell" in recommendation['title']:
            tasks = [
                {"task": "Target Account Selection", "duration": "2 days", "owner": "Sales Analytics", "status": "Not Started"},
                {"task": "Bundled Pricing Creation", "duration": "3 days", "owner": "Pricing Team", "status": "Not Started"},
                {"task": "Campaign Material Development", "duration": "5 days", "owner": "Marketing Team", "status": "Not Started"},
                {"task": "Sales Team Training", "duration": "2 days", "owner": "Sales Enablement", "status": "Not Started"},
                {"task": "Campaign Launch", "duration": "1 day", "owner": "Sales Team", "status": "Not Started"},
                {"task": "Performance Tracking", "duration": "Ongoing", "owner": "Analytics Team", "status": "Not Started"}
            ]
        else:
            tasks = [
                {"task": "Detailed Planning", "duration": "5 days", "owner": "Strategy Team", "status": "Not Started"},
                {"task": "Resource Allocation", "duration": "3 days", "owner": "Operations", "status": "Not Started"},
                {"task": "Team Coordination", "duration": "2 days", "owner": "Project Manager", "status": "Not Started"},
                {"task": "Execution Phase 1", "duration": "14 days", "owner": "Implementation Team", "status": "Not Started"},
                {"task": "Review & Optimization", "duration": "7 days", "owner": "Analytics Team", "status": "Not Started"},
                {"task": "Full Deployment", "duration": "Ongoing", "owner": "Operations Team", "status": "Not Started"}
            ]
        
        # Create interactive task checklist
        for i, task in enumerate(tasks):
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            
            with col1:
                task_key = f"task_{recommendation['id']}_{i}"
                completed = st.checkbox(task['task'], key=task_key)
                if completed:
                    task['status'] = "Completed"
                    st.success(f"✅ {task['task']} marked as completed")
            
            with col2:
                st.markdown(f"⏱️ {task['duration']}")
            
            with col3:
                st.markdown(f"👤 {task['owner']}")
            
            with col4:
                status_color = COKE_COLORS['success_green'] if task['status'] == 'Completed' else COKE_COLORS['warning_orange']
                st.markdown(f"<span style='color: {status_color}; font-weight: bold;'>{task['status']}</span>", unsafe_allow_html=True)
            
            with col5:
                if st.button("📋 Details", key=f"task_details_{recommendation['id']}_{i}"):
                    st.info(f"Task details for '{task['task']}' - Owner: {task['owner']}, Duration: {task['duration']}")
        
        # Resource requirements and budget
        st.markdown("#### 💰 Resource Requirements & Budget")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Budget Breakdown:**")
            if "Freestyle" in recommendation['title']:
                budget_items = [
                    ("Equipment Cost", 450000),
                    ("Installation", 85000),
                    ("Training", 25000),
                    ("Support (1 year)", 45000)
                ]
            else:
                budget_items = [
                    ("Personnel", 150000),
                    ("Marketing/Materials", 75000),
                    ("Technology", 45000),
                    ("Contingency (10%)", 27000)
                ]
            
            total_budget = sum(item[1] for item in budget_items)
            
            for item, cost in budget_items:
                st.markdown(f"• {item}: ${cost:,}")
            
            st.markdown(f"**Total Budget: ${total_budget:,}**")
        
        with col2:
            st.markdown("**Success Metrics:**")
            if "Freestyle" in recommendation['title']:
                metrics = [
                    "Revenue increase: +15-20%",
                    "Customer satisfaction: +25%",
                    "Market share improvement: +3%",
                    "ROI timeline: 8-12 months"
                ]
            elif "At-Risk" in recommendation['title']:
                metrics = [
                    "Churn reduction: -60%",
                    "Retention rate: +15%",
                    "Customer lifetime value: +$200K",
                    "Recovery rate: 75%"
                ]
            else:
                metrics = [
                    "Revenue growth: +12%",
                    "Cross-sell rate: +25%",
                    "Customer engagement: +30%",
                    "Market penetration: +8%"
                ]
            
            for metric in metrics:
                st.markdown(f"• {metric}")
        
        # Implementation approval
        st.markdown("#### ✅ Implementation Approval")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🚀 Start Implementation", key=f"start_impl_{recommendation['id']}", type="primary"):
                st.balloons()
                st.success(f"🚀 Implementation of '{recommendation['title']}' has been initiated! Team notifications sent.")
        
        with col2:
            if st.button("📧 Request Approval", key=f"approval_{recommendation['id']}"):
                st.info("📧 Approval request sent to management team. You'll receive notification within 24 hours.")
        
        with col3:
            if st.button("💾 Save to Pipeline", key=f"save_{recommendation['id']}"):
                st.success("💾 Recommendation saved to your implementation pipeline.")

def show_detailed_analysis(recommendation: Dict[str, Any], accounts_df: pd.DataFrame, opportunities_df: pd.DataFrame):
    """Show comprehensive detailed analysis with data visualizations"""
    
    with st.container():
        st.markdown(f"### 📊 Detailed Analysis: {recommendation['title']}")
        
        # Supporting data analysis
        if "Freestyle" in recommendation['title']:
            st.markdown("#### 🎯 Target Account Analysis")
            
            # Filter relevant accounts (using industry instead of segment)
            target_industries = ['QSR', 'Restaurant', 'Entertainment', 'Food Service', 'Retail']
            target_accounts = accounts_df[accounts_df['industry'].isin(target_industries)].head(8)
            
            # If no target accounts found, use random selection
            if len(target_accounts) == 0:
                target_accounts = accounts_df.sample(min(8, len(accounts_df)))
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Target Locations for Freestyle Installation:**")
                
                # Display target accounts with analysis
                for _, account in target_accounts.iterrows():
                    traffic_score = random.randint(75, 95)
                    current_revenue = account['annual_revenue']
                    projected_increase = current_revenue * 0.34  # 34% increase
                    
                    with st.expander(f"🏢 {account['company_name']} - ${projected_increase:,.0f} potential"):
                        st.markdown(f"**Current Revenue:** ${current_revenue:,.0f}")
                        st.markdown(f"**Projected Increase:** ${projected_increase:,.0f} (+34%)")
                        st.markdown(f"**Traffic Score:** {traffic_score}/100")
                        st.markdown(f"**Location:** {account['region']}")
                        st.markdown(f"**Account Manager:** {account['assigned_rep']}")
                        st.markdown(f"**Industry:** {account['industry']}")
                        
                        # Mini traffic visualization
                        fig = go.Figure(go.Indicator(
                            mode = "gauge+number",
                            value = traffic_score,
                            domain = {'x': [0, 1], 'y': [0, 1]},
                            title = {'text': "Traffic Score"},
                            gauge = {
                                'axis': {'range': [None, 100]},
                                'bar': {'color': COKE_COLORS['primary_red']},
                                'steps': [
                                    {'range': [0, 50], 'color': COKE_COLORS['light_gray']},
                                    {'range': [50, 80], 'color': COKE_COLORS['warning_orange']},
                                    {'range': [80, 100], 'color': COKE_COLORS['success_green']}
                                ],
                                'threshold': {
                                    'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75,
                                    'value': 90
                                }
                            }
                        ))
                        fig.update_layout(height=200)
                        st.plotly_chart(fig, use_container_width=True, key=f"traffic_gauge_{account['account_id']}")
            
            with col2:
                st.markdown("**Revenue Impact Projection:**")
                
                # Revenue projection chart
                months = ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']
                baseline_revenue = [100, 100, 100, 100, 100, 100]
                projected_revenue = [100, 105, 115, 125, 130, 134]
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=months, y=baseline_revenue,
                    mode='lines+markers',
                    name='Current Revenue',
                    line=dict(color=COKE_COLORS['light_gray'], width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=months, y=projected_revenue,
                    mode='lines+markers',
                    name='Projected with Freestyle',
                    line=dict(color=COKE_COLORS['primary_red'], width=3),
                    fill='tonexty'
                ))
                
                fig.update_layout(
                    title="Revenue Impact Timeline",
                    xaxis_title="Timeline",
                    yaxis_title="Revenue Index (100 = Current)",
                    height=300,
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)'
                )
                
                st.plotly_chart(fig, use_container_width=True, key="revenue_impact_timeline")
                
                # Cost-benefit analysis
                st.markdown("**Cost-Benefit Analysis:**")
                st.markdown(f"• **Initial Investment:** ${recommendation['potential_value'] * 0.6:,.0f}")
                st.markdown(f"• **Projected Revenue:** ${recommendation['potential_value']:,.0f}")
                st.markdown(f"• **Net Benefit:** ${recommendation['potential_value'] * 0.4:,.0f}")
                st.markdown("• **ROI:** 67% in first year")
                st.markdown("• **Payback Period:** 8 months")
        
        elif "At-Risk" in recommendation['title']:
            st.markdown("#### ⚠️ At-Risk Account Deep Dive")
            
            # Generate at-risk accounts
            at_risk_accounts = accounts_df.sample(12)
            at_risk_accounts['risk_score'] = [random.randint(65, 95) for _ in range(len(at_risk_accounts))]
            at_risk_accounts['churn_probability'] = [random.randint(40, 85) for _ in range(len(at_risk_accounts))]
            at_risk_accounts['days_since_contact'] = [random.randint(15, 90) for _ in range(len(at_risk_accounts))]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**High-Risk Accounts Requiring Immediate Attention:**")
                
                # Sort by risk score and show top accounts
                top_risk = at_risk_accounts.nlargest(6, 'risk_score')
                
                for _, account in top_risk.iterrows():
                    risk_color = COKE_COLORS['primary_red'] if account['risk_score'] > 80 else COKE_COLORS['warning_orange']
                    
                    with st.expander(f"⚠️ {account['company_name']} - {account['risk_score']}/100 Risk"):
                        st.markdown(f"**Annual Value:** ${account['annual_revenue']:,.0f}")
                        st.markdown(f"**Churn Probability:** {account['churn_probability']}%")
                        st.markdown(f"**Days Since Last Contact:** {account['days_since_contact']}")
                        st.markdown(f"**Account Manager:** {account['assigned_rep']}")
                        st.markdown(f"**Industry:** {account['industry']}")
                        
                        # Risk factors
                        risk_factors = [
                            "Payment delays (45+ days)",
                            "Decreased order frequency (-35%)",
                            "Reduced engagement scores",
                            "Competitor contact detected"
                        ]
                        
                        st.markdown("**Key Risk Factors:**")
                        for factor in risk_factors[:random.randint(2, 4)]:
                            st.markdown(f"• {factor}")
                        
                        # Recommended actions
                        st.markdown("**Recommended Actions:**")
                        actions = [
                            "Schedule executive check-in within 48 hours",
                            "Offer flexible payment terms",
                            "Deploy customer success specialist",
                            "Prepare retention incentive package"
                        ]
                        for action in actions:
                            st.markdown(f"• {action}")
            
            with col2:
                st.markdown("**Risk Analysis & Trends:**")
                
                # Risk distribution chart
                risk_ranges = ['Low (0-40)', 'Medium (41-70)', 'High (71-100)']
                risk_counts = [
                    len(at_risk_accounts[at_risk_accounts['risk_score'] <= 40]),
                    len(at_risk_accounts[(at_risk_accounts['risk_score'] > 40) & (at_risk_accounts['risk_score'] <= 70)]),
                    len(at_risk_accounts[at_risk_accounts['risk_score'] > 70])
                ]
                
                fig = px.pie(
                    values=risk_counts,
                    names=risk_ranges,
                    title="Risk Distribution",
                    color_discrete_sequence=[COKE_COLORS['success_green'], COKE_COLORS['warning_orange'], COKE_COLORS['primary_red']]
                )
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True, key="risk_distribution_pie")
                
                # Churn cost analysis
                st.markdown("**Churn Cost Analysis:**")
                total_at_risk_value = at_risk_accounts['annual_revenue'].sum()
                avg_churn_prob = at_risk_accounts['churn_probability'].mean()
                expected_loss = total_at_risk_value * (avg_churn_prob / 100)
                
                st.markdown(f"• **Total At-Risk Value:** ${total_at_risk_value:,.0f}")
                st.markdown(f"• **Average Churn Probability:** {avg_churn_prob:.1f}%")
                st.markdown(f"• **Expected Loss (No Action):** ${expected_loss:,.0f}")
                st.markdown(f"• **Potential Savings:** ${expected_loss * 0.75:,.0f}")
                st.markdown("• **Intervention Success Rate:** 75%")
        
        else:
            # Generic detailed analysis for other recommendation types
            st.markdown("#### 📈 Comprehensive Analysis")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Market Opportunity Analysis:**")
                
                # Sample market data
                market_segments = ['Enterprise', 'SMB', 'QSR', 'Retail']
                opportunity_values = [2300000, 1200000, 1800000, 950000]
                
                fig = px.bar(
                    x=market_segments,
                    y=opportunity_values,
                    title="Opportunity Value by Segment",
                    color=opportunity_values,
                    color_continuous_scale=['#FFE6E6', COKE_COLORS['primary_red']]
                )
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True, key="market_opportunity_analysis")
            
            with col2:
                st.markdown("**Implementation Timeline:**")
                
                # Timeline visualization
                timeline_data = {
                    'Phase': ['Planning', 'Preparation', 'Launch', 'Optimization', 'Full Scale'],
                    'Duration': [14, 21, 7, 30, 60],
                    'Start_Day': [0, 14, 35, 42, 72]
                }
                
                fig = px.timeline(
                    timeline_data,
                    x_start='Start_Day',
                    x_end=[start + duration for start, duration in zip(timeline_data['Start_Day'], timeline_data['Duration'])],
                    y='Phase',
                    title="Implementation Timeline",
                    color='Duration'
                )
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True, key="implementation_timeline")
        
        # Additional insights and competitive analysis
        st.markdown("#### 🔍 Additional Insights")
        
        tab1, tab2, tab3 = st.tabs(["📊 Data Analysis", "🏆 Competitive Intelligence", "📋 Risk Assessment"])
        
        with tab1:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Key Performance Indicators:**")
                kpis = [
                    ("Success Probability", f"{recommendation['confidence']:.0%}"),
                    ("Expected Timeline", recommendation['timeline']),
                    ("Resource Intensity", "Medium"),
                    ("Complexity Score", "7.5/10")
                ]
                
                for kpi, value in kpis:
                    st.metric(kpi, value)
            
            with col2:
                st.markdown("**Historical Performance:**")
                st.markdown("• Similar initiatives: 89% success rate")
                st.markdown("• Average implementation time: 35 days")
                st.markdown("• Typical ROI: 145% in first year")
                st.markdown("• Customer satisfaction: +28%")
        
        with tab2:
            st.markdown("**Competitive Landscape Analysis:**")
            competitors = ['PepsiCo', 'Dr Pepper Snapple', 'Regional Brands']
            market_share = [28, 15, 12]
            
            fig = px.bar(
                x=competitors,
                y=market_share,
                title="Competitive Market Share",
                color=market_share,
                color_continuous_scale=['#FFE6E6', COKE_COLORS['primary_red']]
            )
            st.plotly_chart(fig, use_container_width=True, key="competitive_market_share")
            
            st.markdown("**Competitive Threats & Opportunities:**")
            st.markdown("• PepsiCo launching new product line in Q4")
            st.markdown("• Regional competitor price pressure detected")
            st.markdown("• Opportunity: Premium segment underserved")
            st.markdown("• Market intelligence: Customer preference shift toward zero-sugar options")
        
        with tab3:
            st.markdown("**Risk Assessment Matrix:**")
            
            risks = [
                {"risk": "Budget overrun", "probability": "Medium", "impact": "Medium", "mitigation": "10% contingency fund allocated"},
                {"risk": "Timeline delays", "probability": "Low", "impact": "High", "mitigation": "Parallel workstreams planned"},
                {"risk": "Market competition", "probability": "High", "impact": "Medium", "mitigation": "Accelerated launch timeline"},
                {"risk": "Resource availability", "probability": "Medium", "impact": "Low", "mitigation": "Cross-training team members"}
            ]
            
            risk_df = pd.DataFrame(risks)
            st.dataframe(risk_df, use_container_width=True)
        
        # Action buttons
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("📧 Share Analysis", key=f"share_analysis_{recommendation['id']}"):
                st.success("📧 Detailed analysis shared with stakeholders")
        
        with col2:
            if st.button("💾 Export Report", key=f"export_report_{recommendation['id']}"):
                st.success("💾 Analysis report exported to Downloads")
        
        with col3:
            if st.button("📅 Schedule Review", key=f"schedule_review_{recommendation['id']}"):
                st.success("📅 Review meeting scheduled for next week")
        
        with col4:
            if st.button("🔄 Refresh Data", key=f"refresh_data_{recommendation['id']}"):
                st.success("🔄 Analysis data refreshed with latest information")

def render_ai_recommendations():
    """Render the AI Recommendations tab with actionable insights"""
    
    st.markdown("# 🤖 AI Recommendations")
    st.markdown("*Intelligent insights and actionable recommendations powered by Azure OpenAI*")
    
    # Generate enhanced data
    data_gen = EnhancedDataGenerator()
    accounts_df = data_gen.generate_enhanced_accounts(200)
    opportunities_df = data_gen.generate_enhanced_opportunities(350, accounts_df)
    
    # === AI INSIGHTS OVERVIEW ===
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        ProactiveWidgets.priority_alert_card(
            "Active Insights",
            "47",
            "+12 new this week",
            COKE_COLORS['primary_red'],
            "🧠"
        )
    
    with col2:
        ProactiveWidgets.priority_alert_card(
            "High Priority Actions",
            "23",
            "Immediate attention",
            COKE_COLORS['warning_orange'],
            "⚡"
        )
    
    with col3:
        ProactiveWidgets.priority_alert_card(
            "Potential Revenue Impact",
            "$3.2M",
            "From recommended actions",
            COKE_COLORS['success_green'],
            "💰"
        )
    
    with col4:
        ProactiveWidgets.priority_alert_card(
            "Implementation Rate",
            "78%",
            "+5% vs last month",
            COKE_COLORS['executive_blue'],
            "📈"
        )
    
    st.markdown("---")
    
    # === TOP PRIORITY RECOMMENDATIONS ===
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Priority Recommendations")
        
        recommendations = [
            {
                "id": "REC-001",
                "title": "Freestyle Expansion Initiative",
                "description": "Deploy Freestyle machines to 8 high-traffic QSR locations",
                "impact": "Revenue Boost",
                "confidence": 0.92,
                "potential_value": 850000,
                "timeline": "30 days",
                "priority": "High",
                "reasoning": "Historical data shows 34% revenue increase post-Freestyle installation",
                "next_steps": [
                    "Contact QSR account managers",
                    "Schedule site surveys",
                    "Prepare installation timeline"
                ]
            },
            {
                "id": "REC-002", 
                "title": "At-Risk Account Intervention",
                "description": "Immediate outreach to 12 accounts showing churn signals",
                "impact": "Churn Prevention",
                "confidence": 0.87,
                "potential_value": 1200000,
                "timeline": "7 days",
                "priority": "Critical",
                "reasoning": "Engagement scores dropped 35% with payment delays",
                "next_steps": [
                    "Deploy retention specialists",
                    "Offer flexible payment terms",
                    "Schedule executive check-ins"
                ]
            },
            {
                "id": "REC-003",
                "title": "Zero Sugar Cross-Sell Campaign",
                "description": "Target 15 high-performing Classic accounts for Zero Sugar expansion",
                "impact": "Revenue Growth",
                "confidence": 0.79,
                "potential_value": 650000,
                "timeline": "45 days",
                "priority": "Medium",
                "reasoning": "Accounts with both products show 23% higher total revenue",
                "next_steps": [
                    "Create bundled pricing",
                    "Launch targeted campaign",
                    "Track adoption metrics"
                ]
            },
            {
                "id": "REC-004",
                "title": "Regional Expansion - Western Territory",
                "description": "Increase field presence in underperforming western regions",
                "impact": "Market Share",
                "confidence": 0.74,
                "potential_value": 2300000,
                "timeline": "90 days",
                "priority": "High",
                "reasoning": "Competitive analysis shows untapped market potential",
                "next_steps": [
                    "Hire regional specialists",
                    "Develop territory strategy",
                    "Launch competitive campaign"
                ]
            }
        ]
        
        for i, rec in enumerate(recommendations):
            priority_colors = {
                'Critical': COKE_COLORS['primary_red'],
                'High': COKE_COLORS['warning_orange'],
                'Medium': COKE_COLORS['executive_blue']
            }
            
            priority_color = priority_colors.get(rec['priority'], COKE_COLORS['light_gray'])
            confidence_bar_width = int(rec['confidence'] * 100)
            
            with st.expander(f"🎯 {rec['title']} - ${rec['potential_value']:,.0f} potential", expanded=(i==0)):
                col_a, col_b = st.columns([3, 1])
                
                with col_a:
                    st.markdown(f"**Description:** {rec['description']}")
                    st.markdown(f"**AI Reasoning:** {rec['reasoning']}")
                    
                    st.markdown("**Recommended Next Steps:**")
                    for step in rec['next_steps']:
                        st.markdown(f"• {step}")
                
                with col_b:
                    # Use native Streamlit components with better sizing and layout
                    priority_icons = {
                        'Critical': '🚨',
                        'High': '⚠️',
                        'Medium': '📋'
                    }
                    
                    icon = priority_icons.get(rec['priority'], '📋')
                    
                    # Create a compact container
                    with st.container():
                        # Compact priority header
                        st.markdown(f"#### {icon} {rec['priority']} Priority")
                        
                        # Use smaller metrics in a single column for compactness
                        st.markdown(f"**⏱️ Timeline:** {rec['timeline']}")
                        st.markdown(f"**💥 Impact:** {rec['impact']}")
                        st.markdown(f"**🎯 Confidence:** {rec['confidence']:.0%}")
                        
                        # Compact progress bar
                        st.progress(rec['confidence'])
                        
                        # Priority status message - more compact
                        if rec['priority'] == 'Critical':
                            st.error("🚨 **CRITICAL** - Immediate action required", icon="🚨")
                        elif rec['priority'] == 'High':
                            st.warning("⚠️ **HIGH** - Urgent attention needed", icon="⚠️")
                        else:
                            st.info(f"📋 **{rec['priority'].upper()}** - Scheduled action", icon="📋")
                
                col_action1, col_action2 = st.columns(2)
                with col_action1:
                    if st.button(f"✅ Implement", key=f"implement_{rec['id']}"):
                        show_implementation_workflow(rec)
                
                with col_action2:
                    if st.button(f"📋 More Details", key=f"details_{rec['id']}"):
                        show_detailed_analysis(rec, accounts_df, opportunities_df)
    
    with col2:
        st.markdown("### 📊 Recommendation Analytics")
        
        # Recommendation impact analysis
        impact_data = {
            'Category': ['Revenue Growth', 'Churn Prevention', 'Market Expansion', 'Efficiency'],
            'Recommendations': [8, 5, 4, 6],
            'Avg Impact': [750000, 950000, 1200000, 400000]
        }
        
        impact_df = pd.DataFrame(impact_data)
        
        fig = px.bar(
            impact_df,
            x='Recommendations',
            y='Category',
            color='Avg Impact',
            orientation='h',
            title="Recommendations by Category",
            color_continuous_scale=['#FFE6E6', COKE_COLORS['primary_red']]
        )
        
        fig.update_layout(
            height=300,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="recommendation_analytics_bar")
        
        # Implementation tracking
        st.markdown("#### 📈 Implementation Tracking")
        
        implementation_data = [
            {"Week": "Week 1", "Implemented": 12, "Pending": 8},
            {"Week": "Week 2", "Implemented": 18, "Pending": 5},
            {"Week": "Week 3", "Implemented": 23, "Pending": 7},
            {"Week": "Week 4", "Implemented": 31, "Pending": 4}
        ]
        
        impl_df = pd.DataFrame(implementation_data)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Implemented',
            x=impl_df['Week'],
            y=impl_df['Implemented'],
            marker_color=COKE_COLORS['success_green']
        ))
        fig.add_trace(go.Bar(
            name='Pending',
            x=impl_df['Week'],
            y=impl_df['Pending'],
            marker_color=COKE_COLORS['warning_orange']
        ))
        
        fig.update_layout(
            title="Weekly Implementation Progress",
            barmode='stack',
            height=250,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True, key="weekly_implementation_progress")
    
    # === INTERACTIVE AI CHAT ===
    st.markdown("---")
    st.markdown("### 💬 Interactive AI Assistant")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("*Ask me anything about your sales data, opportunities, or accounts...*")
        
        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hello! I'm your Coca-Cola Sales AI Assistant. I can help you analyze your sales data, identify opportunities, and provide strategic recommendations. What would you like to know?"}
            ]
        
        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask about your sales performance, opportunities, or get recommendations..."):
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate AI response
            with st.chat_message("assistant"):
                with st.spinner("Analyzing your data..."):
                    response = simulate_ai_response(prompt)
                    st.markdown(response)
                    
                    # Add assistant response to chat history
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    with col2:
        st.markdown("#### 🔍 Quick Questions")
        
        quick_questions = [
            "What are my top revenue opportunities?",
            "Which accounts are at risk of churning?",
            "How can I improve my pipeline?",
            "What's driving customer sentiment?",
            "Where should I focus my efforts?",
            "What products should I cross-sell?"
        ]
        
        for idx, question in enumerate(quick_questions):
            unique_key = f"quick_{hash(question)}_{idx}"
            if st.button(question, key=unique_key, use_container_width=True):
                # Add to chat history
                st.session_state.chat_history.append({"role": "user", "content": question})
                response = simulate_ai_response(question)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()
    
    # === INSIGHT CATEGORIES ===
    st.markdown("---")
    st.markdown("### 📋 Insight Categories")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Sales Optimization", "⚠️ Risk Management", "🚀 Growth Opportunities", "📊 Market Intelligence"])
    
    with tab1:
        st.markdown("#### Sales Optimization Insights")
        
        optimization_insights = [
            {
                "insight": "Territory Rebalancing",
                "description": "Sarah Chen's territory shows 140% quota attainment while Mike Rodriguez is at 85%. Recommend redistributing 3 key accounts.",
                "impact": "Balance workload and improve overall performance",
                "action": "Reassign accounts by next quarter"
            },
            {
                "insight": "Product Mix Optimization", 
                "description": "Accounts selling only Classic show 28% lower margin than mixed-product accounts.",
                "impact": "Increase average margin by 12%",
                "action": "Launch cross-sell initiative"
            },
            {
                "insight": "Call Frequency Optimization",
                "description": "High-value accounts with monthly touchpoints outperform quarterly by 45%.",
                "impact": "Increase retention and upsell success",
                "action": "Adjust call schedules for top 20% accounts"
            }
        ]
        
        for insight in optimization_insights:
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
                border-left: 4px solid {COKE_COLORS['info_blue']};
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{insight['insight']}</h5>
                <p style="margin: 8px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">{insight['description']}</p>
                <p style="margin: 5px 0; font-weight: bold; color: {COKE_COLORS['success_green']};">
                    Impact: {insight['impact']}
                </p>
                <p style="margin: 0; font-size: 12px; color: {COKE_COLORS['dark_gray']}; font-weight: 500;">
                    Recommended Action: {insight['action']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### Risk Management Insights")
        
        risk_insights = [
            {
                "insight": "Payment Risk Alert",
                "description": "Metro Restaurant Group has payment delays increasing by 15 days on average over last 3 months.",
                "risk_level": "High",
                "action": "Engage credit team and adjust payment terms"
            },
            {
                "insight": "Competitive Threat",
                "description": "PepsiCo showing increased activity in 5 key QSR accounts worth $2.1M annual revenue.",
                "risk_level": "Medium", 
                "action": "Deploy competitive retention program"
            },
            {
                "insight": "Volume Decline Pattern",
                "description": "8 convenience store accounts showing consistent 10% monthly volume decline.",
                "risk_level": "High",
                "action": "Immediate investigation and intervention required"
            }
        ]
        
        for insight in risk_insights:
            risk_color = {
                'High': COKE_COLORS['primary_red'],
                'Medium': COKE_COLORS['warning_orange'],
                'Low': COKE_COLORS['executive_blue']
            }.get(insight['risk_level'], COKE_COLORS['light_gray'])
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
                border-left: 4px solid {risk_color};
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{insight['insight']}</h5>
                <p style="margin: 8px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">{insight['description']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="
                        background: {risk_color};
                        color: white;
                        padding: 4px 12px;
                        border-radius: 12px;
                        font-size: 12px;
                        font-weight: bold;
                    ">{insight['risk_level']} Risk</span>
                    <span style="font-size: 12px; color: {COKE_COLORS['dark_gray']}; font-weight: 500;">{insight['action']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("#### Growth Opportunities")
        
        growth_insights = [
            {
                "insight": "Freestyle Expansion",
                "description": "15 QSR locations ideal for Freestyle installations based on traffic and demographics.",
                "opportunity_value": "$1.2M",
                "timeline": "Q4 2024"
            },
            {
                "insight": "Premium Product Upsell",
                "description": "Corporate cafeterias showing strong preference for premium/organic options.",
                "opportunity_value": "$650K",
                "timeline": "Q1 2025"
            },
            {
                "insight": "New Market Penetration",
                "description": "Healthcare segment underrepresented with only 12% penetration vs 34% industry average.",
                "opportunity_value": "$2.8M",
                "timeline": "2025"
            }
        ]
        
        for insight in growth_insights:
            st.markdown(f"""
            <div style="
                background: white;
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
                border-left: 4px solid {COKE_COLORS['success_green']};
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: {COKE_COLORS['coke_black']};">{insight['insight']}</h5>
                <p style="margin: 8px 0; color: #666;">{insight['description']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="
                        background: {COKE_COLORS['success_green']};
                        color: white;
                        padding: 4px 12px;
                        border-radius: 12px;
                        font-size: 12px;
                        font-weight: bold;
                    ">{insight['opportunity_value']}</span>
                    <span style="font-size: 12px; color: #888;">Target: {insight['timeline']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("#### Market Intelligence")
        
        market_insights = [
            {
                "insight": "Seasonal Demand Patterns",
                "description": "Historical data shows 23% spike in sports drink demand during Q2-Q3.",
                "recommendation": "Increase Powerade inventory allocation"
            },
            {
                "insight": "Regional Preferences",
                "description": "Southeast showing 45% higher Zero Sugar adoption vs national average.",
                "recommendation": "Expand Zero Sugar SKUs in Southeast distribution"
            },
            {
                "insight": "Competitive Positioning", 
                "description": "Coca-Cola maintains 67% share in QSR segment, up 3% YoY.",
                "recommendation": "Leverage strength to expand in adjacent segments"
            }
        ]
        
        for insight in market_insights:
            st.markdown(f"""
            <div style="
                background: white;
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
                border-left: 4px solid {COKE_COLORS['coke_gold']};
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: {COKE_COLORS['coke_black']};">{insight['insight']}</h5>
                <p style="margin: 8px 0; color: #666;">{insight['description']}</p>
                <p style="margin: 0; font-size: 12px; color: {COKE_COLORS['executive_blue']}; font-style: italic;">
                    💡 {insight['recommendation']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    # === QUICK ACTIONS ===
    st.markdown("---")
    
    ai_actions = [
        {"icon": "🧠", "label": "Generate New Insights", "action": "generate_insights"},
        {"icon": "📊", "label": "Run Predictive Analysis", "action": "predictive_analysis"},
        {"icon": "🎯", "label": "Prioritize Recommendations", "action": "prioritize_recs"},
        {"icon": "📋", "label": "Export Action Plan", "action": "export_plan"}
    ]
    
    selected_action = ProactiveWidgets.action_button_panel(ai_actions)
    
    if selected_action:
        st.success(f"✅ {selected_action.replace('_', ' ').title()} initiated! AI analysis in progress...")
