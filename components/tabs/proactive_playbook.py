import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import random
from typing import Dict, List, Any

class ProactivePlaybook:
    def __init__(self, data_generator, ai_service=None):
        self.data_generator = data_generator
        self.ai_service = ai_service
        
    def render(self):
        st.header("🎯 Proactive Playbook")
        st.subheader("AI-Powered Sales Strategies & Action Plans")
        
        # Top metrics and AI insights
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Active Playbooks", "12", "↑ 3")
        with col2:
            st.metric("Completion Rate", "87%", "↑ 5%")
        with col3:
            st.metric("Avg Revenue Impact", "$2.4M", "↑ 12%")
        with col4:
            st.metric("Success Rate", "94%", "↑ 8%")
        
        # AI-Generated Playbook Recommendations
        st.markdown("### 🤖 AI-Generated Playbook Recommendations")
        
        # GPT-4o powered playbook generation
        if st.button("🧠 Generate New Playbook with GPT-4o", key="generate_playbook"):
            with st.spinner("GPT-4o is analyzing market conditions and generating strategic playbooks..."):
                playbook = self._generate_ai_playbook()
                st.session_state.generated_playbook = playbook
        
        if hasattr(st.session_state, 'generated_playbook'):
            self._display_generated_playbook(st.session_state.generated_playbook)
        
        # Active Playbooks Management
        st.markdown("### 📋 Active Playbooks")
        
        # Create sample active playbooks
        active_playbooks = self._create_sample_playbooks()
        
        # Playbook selection and details
        selected_playbook = st.selectbox(
            "Select Playbook to Review:",
            options=list(active_playbooks.keys()),
            key="playbook_selector"
        )
        
        if selected_playbook:
            self._display_playbook_details(active_playbooks[selected_playbook])
        
        # Performance Analytics
        st.markdown("### 📊 Playbook Performance Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Playbook success rate chart
            success_data = pd.DataFrame({
                'Playbook': ['Territory Expansion', 'Upsell Focus', 'Retention Drive', 'New Product Launch', 'Competitive Defense'],
                'Success_Rate': [94, 87, 91, 76, 89],
                'Revenue_Impact': [2.4, 1.8, 2.1, 3.2, 1.5]
            })
            
            fig = px.scatter(success_data, x='Success_Rate', y='Revenue_Impact', 
                           size='Revenue_Impact', color='Playbook',
                           title="Playbook Performance Matrix",
                           labels={'Success_Rate': 'Success Rate (%)', 'Revenue_Impact': 'Revenue Impact ($M)'})
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True, key="playbook_performance")
        
        with col2:
            # Execution timeline
            timeline_data = self._create_timeline_data()
            fig = go.Figure()
            
            for playbook in timeline_data:
                fig.add_trace(go.Scatter(
                    x=playbook['dates'],
                    y=[playbook['name']] * len(playbook['dates']),
                    mode='markers+lines',
                    name=playbook['name'],
                    line=dict(width=8),
                    marker=dict(size=10)
                ))
            
            fig.update_layout(
                title="Playbook Execution Timeline",
                xaxis_title="Date",
                yaxis_title="Playbooks",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True, key="playbook_timeline")
        
        # AI-Powered Action Items
        st.markdown("### ⚡ AI-Powered Action Items")
        
        if st.button("🎯 Generate Personalized Actions with GPT-4o", key="generate_actions"):
            with st.spinner("GPT-4o is analyzing your performance and generating personalized action items..."):
                actions = self._generate_ai_actions()
                st.session_state.ai_actions = actions
        
        if hasattr(st.session_state, 'ai_actions'):
            self._display_ai_actions(st.session_state.ai_actions)
        
        # Playbook Templates Library
        st.markdown("### 📚 Playbook Templates Library")
        
        templates = self._create_playbook_templates()
        
        col1, col2, col3 = st.columns(3)
        
        for i, template in enumerate(templates):
            with [col1, col2, col3][i % 3]:
                with st.container():
                    st.markdown(f"**{template['name']}**")
                    st.markdown(f"*{template['description']}*")
                    st.markdown(f"Success Rate: **{template['success_rate']}%**")
                    st.markdown(f"Avg Impact: **${template['avg_impact']}M**")
                    
                    if st.button(f"Use Template", key=f"template_{i}"):
                        st.success(f"Template '{template['name']}' added to your active playbooks!")
                    
                    if st.button(f"AI Customize", key=f"customize_{i}"):
                        with st.spinner("GPT-4o is customizing this template for your territory..."):
                            customized = self._customize_template_with_ai(template)
                            st.session_state[f'customized_{i}'] = customized
                    
                    if hasattr(st.session_state, f'customized_{i}'):
                        st.markdown("**AI Customization:**")
                        st.markdown(st.session_state[f'customized_{i}'])
    
    def _generate_ai_playbook(self) -> Dict[str, Any]:
        """Generate a new playbook using GPT-4o"""
        # Simulate GPT-4o response
        playbooks = [
            {
                "name": "Q2 Market Penetration Accelerator",
                "objective": "Increase market share in underperforming territories by 15%",
                "strategy": "Focus on high-potential accounts with tailored value propositions and competitive positioning",
                "tactics": [
                    "Conduct deep-dive account analysis using AI insights",
                    "Deploy personalized product demonstrations",
                    "Leverage customer success stories from similar accounts",
                    "Implement competitive battle cards for key objections"
                ],
                "success_metrics": ["15% market share increase", "25% revenue growth", "90% customer satisfaction"],
                "timeline": "90 days",
                "ai_insights": "GPT-4o analysis indicates high success probability (89%) based on similar historical campaigns and current market conditions.",
                "risk_factors": ["Competitive response", "Economic downturn", "Resource allocation"],
                "mitigation_strategies": ["Rapid response team", "Flexible pricing", "Cross-functional support"]
            },
            {
                "name": "Customer Lifetime Value Optimizer",
                "objective": "Increase average customer lifetime value by 30% through strategic upselling",
                "strategy": "AI-driven identification of upsell opportunities with personalized engagement sequences",
                "tactics": [
                    "Deploy predictive analytics for opportunity scoring",
                    "Create personalized value propositions for each account",
                    "Implement multi-touch engagement campaigns",
                    "Leverage social proof and case studies"
                ],
                "success_metrics": ["30% CLV increase", "40% upsell rate", "95% retention"],
                "timeline": "120 days",
                "ai_insights": "Machine learning models predict 87% success rate with focus on top 20% of accounts showing expansion indicators.",
                "risk_factors": ["Customer budget constraints", "Competitive alternatives", "Implementation challenges"],
                "mitigation_strategies": ["Flexible payment terms", "ROI demonstrations", "Implementation support"]
            }
        ]
        
        # Return a random playbook (simulating AI generation)
        import random
        return random.choice(playbooks)
    
    def _display_generated_playbook(self, playbook: Dict[str, Any]):
        """Display the AI-generated playbook"""
        st.success("🎯 New Playbook Generated Successfully!")
        
        with st.expander(f"📋 {playbook['name']}", expanded=True):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Objective:** {playbook['objective']}")
                st.markdown(f"**Strategy:** {playbook['strategy']}")
                
                st.markdown("**Key Tactics:**")
                for tactic in playbook['tactics']:
                    st.markdown(f"• {tactic}")
                
                st.markdown("**Success Metrics:**")
                for metric in playbook['success_metrics']:
                    st.markdown(f"✓ {metric}")
            
            with col2:
                st.metric("Timeline", playbook['timeline'])
                st.markdown("**Risk Factors:**")
                for risk in playbook['risk_factors']:
                    st.markdown(f"⚠️ {risk}")
            
            st.info(f"🤖 **AI Insights:** {playbook['ai_insights']}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("✅ Activate Playbook", key="activate_playbook"):
                    st.success("Playbook activated and added to your dashboard!")
            with col2:
                if st.button("✏️ Customize with AI", key="customize_playbook"):
                    st.info("GPT-4o will customize this playbook based on your specific territory and goals.")
            with col3:
                if st.button("📤 Share with Team", key="share_playbook"):
                    st.success("Playbook shared with your sales team!")
    
    def _create_sample_playbooks(self) -> Dict[str, Dict]:
        """Create sample active playbooks"""
        return {
            "Territory Expansion Q2": {
                "status": "Active",
                "progress": 65,
                "owner": "Sarah Johnson",
                "start_date": "2024-04-01",
                "end_date": "2024-06-30",
                "objective": "Expand territory coverage by 25%",
                "current_metrics": {
                    "Accounts Contacted": 45,
                    "Meetings Scheduled": 28,
                    "Proposals Sent": 12,
                    "Deals Closed": 7
                },
                "ai_recommendations": [
                    "Focus on healthcare sector - 73% higher conversion rate predicted",
                    "Schedule follow-ups with 8 warm prospects within 48 hours",
                    "Leverage Johnson & Johnson case study for pharmaceutical outreach"
                ]
            },
            "Upsell Campaign - Premium Products": {
                "status": "Active",
                "progress": 82,
                "owner": "Mike Chen",
                "start_date": "2024-03-15",
                "end_date": "2024-05-31",
                "objective": "Increase premium product adoption by 40%",
                "current_metrics": {
                    "Target Accounts": 32,
                    "Presentations Given": 26,
                    "Trials Started": 18,
                    "Conversions": 14
                },
                "ai_recommendations": [
                    "High probability conversion: Acme Corp (87% confidence)",
                    "Schedule executive meeting with GlobalTech next week",
                    "Customize demo for TechStart focusing on cost savings"
                ]
            },
            "Customer Retention Drive": {
                "status": "Planning",
                "progress": 23,
                "owner": "Lisa Rodriguez",
                "start_date": "2024-05-01",
                "end_date": "2024-07-31",
                "objective": "Reduce churn rate to below 5%",
                "current_metrics": {
                    "At-Risk Accounts": 15,
                    "Health Checks": 8,
                    "Success Plans": 5,
                    "Renewals Secured": 12
                },
                "ai_recommendations": [
                    "Immediate attention needed: DataFlow Inc showing 89% churn risk",
                    "Schedule quarterly business review with top 5 accounts",
                    "Deploy customer success specialist to InnovateCorp"
                ]
            }
        }
    
    def _display_playbook_details(self, playbook: Dict):
        """Display detailed playbook information"""
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"**Objective:** {playbook['objective']}")
            st.markdown(f"**Owner:** {playbook['owner']}")
            st.markdown(f"**Timeline:** {playbook['start_date']} to {playbook['end_date']}")
        
        with col2:
            # Status badge
            status_color = {"Active": "🟢", "Planning": "🟡", "Completed": "🔵"}
            st.markdown(f"**Status:** {status_color.get(playbook['status'], '⚪')} {playbook['status']}")
        
        with col3:
            # Progress bar
            st.metric("Progress", f"{playbook['progress']}%")
            st.progress(playbook['progress'] / 100)
        
        # Current Metrics
        st.markdown("**📊 Current Metrics:**")
        metric_cols = st.columns(len(playbook['current_metrics']))
        for i, (metric, value) in enumerate(playbook['current_metrics'].items()):
            with metric_cols[i]:
                st.metric(metric, value)
        
        # AI Recommendations
        st.markdown("**🤖 AI Recommendations:**")
        for rec in playbook['ai_recommendations']:
            st.markdown(f"• {rec}")
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("📊 Detailed Analytics", key=f"analytics_{playbook['owner']}"):
                st.info("Loading detailed analytics dashboard...")
        with col2:
            if st.button("🤖 AI Optimization", key=f"optimize_{playbook['owner']}"):
                st.success("GPT-4o is analyzing and optimizing this playbook...")
        with col3:
            if st.button("📅 Update Timeline", key=f"timeline_{playbook['owner']}"):
                st.info("Timeline update interface opened.")
        with col4:
            if st.button("👥 Team Sync", key=f"sync_{playbook['owner']}"):
                st.success("Team synchronization initiated!")
    
    def _create_timeline_data(self):
        """Create timeline data for playbook execution"""
        base_date = datetime.now() - timedelta(days=90)
        return [
            {
                'name': 'Territory Expansion',
                'dates': [base_date + timedelta(days=i*10) for i in range(9)]
            },
            {
                'name': 'Upsell Campaign', 
                'dates': [base_date + timedelta(days=i*12) for i in range(8)]
            },
            {
                'name': 'Retention Drive',
                'dates': [base_date + timedelta(days=i*15) for i in range(6)]
            }
        ]
    
    def _generate_ai_actions(self) -> List[Dict[str, Any]]:
        """Generate AI-powered action items"""
        return [
            {
                "priority": "High",
                "action": "Schedule urgent call with DataFlow Inc",
                "reason": "AI detected 89% churn risk based on engagement patterns and support tickets",
                "timeline": "Within 24 hours",
                "expected_impact": "Prevent $2.3M revenue loss",
                "ai_confidence": "94%"
            },
            {
                "priority": "High", 
                "action": "Send custom ROI proposal to Acme Corp",
                "reason": "Behavioral analysis shows 87% conversion probability with ROI-focused messaging",
                "timeline": "By end of week",
                "expected_impact": "$1.8M new revenue opportunity",
                "ai_confidence": "87%"
            },
            {
                "priority": "Medium",
                "action": "Follow up with 8 warm prospects from last week",
                "reason": "Optimal follow-up timing based on response pattern analysis",
                "timeline": "Next 48 hours",
                "expected_impact": "3-4 new meetings expected",
                "ai_confidence": "76%"
            },
            {
                "priority": "Medium",
                "action": "Prepare competitive battlecard for TechStart meeting",
                "reason": "Competitor analysis shows they're evaluating alternatives",
                "timeline": "Before Thursday meeting",
                "expected_impact": "Improve win probability by 23%",
                "ai_confidence": "81%"
            },
            {
                "priority": "Low",
                "action": "Update customer success plans for Q2 renewals",
                "reason": "Proactive renewal strategy based on usage analytics",
                "timeline": "End of month",
                "expected_impact": "5% improvement in retention rate",
                "ai_confidence": "69%"
            }
        ]
    
    def _display_ai_actions(self, actions: List[Dict[str, Any]]):
        """Display AI-generated action items"""
        st.success("🎯 Personalized Action Items Generated!")
        
        # Priority filter
        priority_filter = st.selectbox(
            "Filter by Priority:",
            ["All", "High", "Medium", "Low"],
            key="action_priority_filter"
        )
        
        filtered_actions = actions if priority_filter == "All" else [a for a in actions if a['priority'] == priority_filter]
        
        for i, action in enumerate(filtered_actions):
            priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            
            with st.expander(f"{priority_color[action['priority']]} {action['action']}", expanded=action['priority'] == 'High'):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Reason:** {action['reason']}")
                    st.markdown(f"**Expected Impact:** {action['expected_impact']}")
                    st.markdown(f"**Timeline:** {action['timeline']}")
                
                with col2:
                    st.metric("AI Confidence", action['ai_confidence'])
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button("✅ Complete", key=f"complete_action_{i}"):
                            st.success("Action marked as complete!")
                    with col_b:
                        if st.button("📅 Schedule", key=f"schedule_action_{i}"):
                            st.info("Added to your calendar!")
    
    def _create_playbook_templates(self) -> List[Dict[str, Any]]:
        """Create playbook templates library"""
        return [
            {
                "name": "New Territory Launch",
                "description": "Comprehensive strategy for entering new geographic markets",
                "success_rate": 89,
                "avg_impact": 3.2,
                "duration": "120 days",
                "tactics": ["Market research", "Competitive analysis", "Partnership development"]
            },
            {
                "name": "Product Upsell Campaign",
                "description": "Systematic approach to increasing product adoption and revenue per account",
                "success_rate": 76,
                "avg_impact": 1.8,
                "duration": "90 days",
                "tactics": ["Account analysis", "Value demonstration", "Pilot programs"]
            },
            {
                "name": "Customer Retention Program", 
                "description": "Proactive strategy to reduce churn and increase customer lifetime value",
                "success_rate": 94,
                "avg_impact": 2.1,
                "duration": "180 days",
                "tactics": ["Health scoring", "Success planning", "Executive engagement"]
            },
            {
                "name": "Competitive Displacement",
                "description": "Strategic approach to winning accounts from key competitors",
                "success_rate": 67,
                "avg_impact": 4.1,
                "duration": "150 days",
                "tactics": ["Competitive intelligence", "Differentiation", "Proof of value"]
            },
            {
                "name": "Digital Transformation Sales",
                "description": "Specialized playbook for selling digital transformation solutions",
                "success_rate": 82,
                "avg_impact": 5.3,
                "duration": "200 days",
                "tactics": ["Digital assessment", "Transformation roadmap", "Change management"]
            },
            {
                "name": "Enterprise Account Growth",
                "description": "Strategic expansion within large enterprise accounts",
                "success_rate": 85,
                "avg_impact": 6.7,
                "duration": "240 days",
                "tactics": ["Stakeholder mapping", "Multi-thread strategy", "Executive sponsorship"]
            }
        ]
    
    def _customize_template_with_ai(self, template: Dict[str, Any]) -> str:
        """Customize template using AI"""
        customizations = [
            f"Based on your territory analysis, I recommend focusing on the {template['tactics'][0]} phase first, with emphasis on technology sector accounts which show 34% higher conversion rates in your region.",
            f"Your historical performance suggests extending the timeline to {int(template['duration'].split()[0]) + 30} days for optimal results, with weekly check-ins to track progress against the {template['avg_impact']}M average impact target.",
            f"Consider leveraging your strong relationship with local industry associations to accelerate the {template['tactics'][1]} component, which could improve your success rate beyond the {template['success_rate']}% baseline."
        ]
        
        import random
        return random.choice(customizations)

def render_proactive_playbook():
    """Main function to render the Proactive Playbook tab."""
    
    # Generate mock data
    mock_data = {
        'accounts': ['Global Beverages Corp', 'Metro Restaurant Group', 'Premium Retail Chain'],
        'revenue': [4500000, 1200000, 850000],
        'growth_rates': [0.12, 0.08, 0.15],
        'health_scores': [85, 78, 82]
    }
    
    # Create and render playbook
    playbook = ProactivePlaybook(data_generator=mock_data)
    playbook.render()
