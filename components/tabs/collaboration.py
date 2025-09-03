"""
Collaboration Tab - Team Communication, Shared Workflows, and Collective Intelligence
AI-powered collaboration with GPT-4o driven team insights and workflow optimization
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

# Coca-Cola Brand Colors
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000', 
    'classic_white': '#FFFFFF',
    'coke_gold': '#FFC72C',
    'success_green': '#28a745',
    'warning_orange': '#ffc107',
    'info_blue': '#17a2b8',
    'light_gray': '#f8f9fa',
    'dark_gray': '#6c757d'
}

def generate_team_data():
    """Generate realistic team collaboration data"""
    teams = [
        {"name": "West Coast Eagles", "region": "West", "members": 8, "lead": "Sarah Chen"},
        {"name": "Northeast Titans", "region": "Northeast", "members": 6, "lead": "Jennifer Smith"},
        {"name": "Southeast Storms", "region": "Southeast", "members": 7, "lead": "David Kim"},
        {"name": "Midwest Mavericks", "region": "Midwest", "members": 5, "lead": "James Foster"},
        {"name": "Southwest Spartans", "region": "Southwest", "members": 6, "lead": "Mike Rodriguez"}
    ]
    
    team_data = []
    for team in teams:
        base_performance = random.uniform(0.8, 1.3)
        
        data = {
            "Team_Name": team["name"],
            "Region": team["region"],
            "Team_Lead": team["lead"],
            "Members": team["members"],
            "Collaboration_Score": random.randint(75, 95),
            "Shared_Deals": random.randint(15, 35),
            "Knowledge_Shares": random.randint(45, 85),
            "Cross_Training": random.randint(8, 20),
            "Team_Revenue": random.randint(8000000, 15000000) * base_performance,
            "Communication_Frequency": random.randint(25, 45),  # Messages per week
            "Project_Completion": random.uniform(0.85, 0.98),
            "Innovation_Ideas": random.randint(12, 28),
            "Mentorship_Hours": random.randint(20, 40)
        }
        team_data.append(data)
    
    return pd.DataFrame(team_data)

def generate_shared_accounts():
    """Generate shared account management data"""
    accounts = [
        {
            "account_name": "McDonald's Corporation",
            "shared_by": ["Sarah Chen", "Mike Rodriguez", "David Kim"],
            "total_value": 15600000,
            "collaboration_type": "Strategic Partnership",
            "status": "Active",
            "last_interaction": "2 hours ago",
            "shared_opportunities": 8,
            "joint_calls": 12,
            "document_shares": 45
        },
        {
            "account_name": "Walmart Inc.",
            "shared_by": ["Jennifer Smith", "Lisa Johnson"],
            "total_value": 22400000,
            "collaboration_type": "Cross-Regional Support",
            "status": "Negotiating",
            "last_interaction": "1 day ago",
            "shared_opportunities": 5,
            "joint_calls": 8,
            "document_shares": 32
        },
        {
            "account_name": "Subway Restaurants",
            "shared_by": ["Carlos Ruiz", "Amanda Wilson", "Tom Bradley"],
            "total_value": 8900000,
            "collaboration_type": "Team Selling",
            "status": "At Risk",
            "last_interaction": "3 days ago",
            "shared_opportunities": 3,
            "joint_calls": 6,
            "document_shares": 18
        },
        {
            "account_name": "AMC Theaters",
            "shared_by": ["James Foster", "Maria Garcia"],
            "total_value": 5200000,
            "collaboration_type": "Joint Account Management",
            "status": "Active",
            "last_interaction": "5 hours ago",
            "shared_opportunities": 4,
            "joint_calls": 10,
            "document_shares": 28
        }
    ]
    
    return accounts

def generate_knowledge_base():
    """Generate knowledge sharing and documentation data"""
    knowledge_items = [
        {
            "title": "Freestyle Machine Sales Playbook",
            "author": "Sarah Chen",
            "category": "Sales Process",
            "description": "Complete guide to positioning and selling Freestyle machines to QSR accounts",
            "views": 347,
            "likes": 42,
            "downloads": 89,
            "last_updated": "2 weeks ago",
            "tags": ["Freestyle", "QSR", "Equipment", "Sales"]
        },
        {
            "title": "Competitive Response Framework - Pepsi",
            "author": "Mike Rodriguez",
            "category": "Competitive Intelligence",
            "description": "Battle cards and response strategies for competitive situations with PepsiCo",
            "views": 298,
            "likes": 38,
            "downloads": 67,
            "last_updated": "1 week ago",
            "tags": ["Competitive", "Pepsi", "Battle Cards", "Strategy"]
        },
        {
            "title": "C-Store Category Management Best Practices",
            "author": "David Kim",
            "category": "Channel Strategy",
            "description": "Proven approaches for optimizing beverage category performance in convenience stores",
            "views": 412,
            "likes": 55,
            "downloads": 103,
            "last_updated": "3 days ago",
            "tags": ["C-Store", "Category", "Merchandising", "Performance"]
        },
        {
            "title": "Digital Marketing Co-op Guidelines",
            "author": "Jennifer Smith",
            "category": "Marketing",
            "description": "Framework for collaborative digital marketing campaigns with key accounts",
            "views": 234,
            "likes": 31,
            "downloads": 56,
            "last_updated": "1 week ago",
            "tags": ["Digital", "Marketing", "Co-op", "Accounts"]
        },
        {
            "title": "New Product Launch Collaboration Toolkit",
            "author": "Lisa Johnson",
            "category": "Product Launch",
            "description": "Templates and processes for coordinating new product launches across teams",
            "views": 189,
            "likes": 28,
            "downloads": 45,
            "last_updated": "4 days ago",
            "tags": ["Launch", "Coordination", "Process", "Templates"]
        }
    ]
    
    return knowledge_items

def generate_team_projects():
    """Generate collaborative project data"""
    projects = [
        {
            "project_name": "Q4 Holiday Campaign Coordination",
            "team_members": ["Sarah Chen", "Mike Rodriguez", "Jennifer Smith", "David Kim"],
            "status": "In Progress",
            "progress": 0.73,
            "start_date": "2024-09-15",
            "target_completion": "2024-11-30",
            "budget": 450000,
            "expected_revenue": 2800000,
            "milestones": [
                {"milestone": "Campaign Strategy Development", "status": "Complete", "owner": "Jennifer Smith"},
                {"milestone": "Account Activation Plans", "status": "In Progress", "owner": "Sarah Chen"},
                {"milestone": "Creative Asset Development", "status": "In Progress", "owner": "Mike Rodriguez"},
                {"milestone": "Performance Tracking Setup", "status": "Pending", "owner": "David Kim"}
            ]
        },
        {
            "project_name": "Regional Freestyle Expansion Initiative",
            "team_members": ["Carlos Ruiz", "Amanda Wilson", "Tom Bradley", "James Foster"],
            "status": "Planning",
            "progress": 0.28,
            "start_date": "2024-10-01",
            "target_completion": "2025-03-31",
            "budget": 750000,
            "expected_revenue": 5200000,
            "milestones": [
                {"milestone": "Market Analysis Completion", "status": "Complete", "owner": "Carlos Ruiz"},
                {"milestone": "Site Selection Criteria", "status": "In Progress", "owner": "Amanda Wilson"},
                {"milestone": "Equipment Procurement", "status": "Pending", "owner": "Tom Bradley"},
                {"milestone": "Installation Coordination", "status": "Pending", "owner": "James Foster"}
            ]
        },
        {
            "project_name": "Digital Transformation Pilot",
            "team_members": ["Lisa Johnson", "Maria Garcia", "Tom Bradley"],
            "status": "Complete",
            "progress": 1.0,
            "start_date": "2024-06-01",
            "target_completion": "2024-09-30",
            "budget": 320000,
            "expected_revenue": 1850000,
            "milestones": [
                {"milestone": "Technology Selection", "status": "Complete", "owner": "Lisa Johnson"},
                {"milestone": "Pilot Implementation", "status": "Complete", "owner": "Maria Garcia"},
                {"milestone": "Results Analysis", "status": "Complete", "owner": "Tom Bradley"},
                {"milestone": "Rollout Recommendations", "status": "Complete", "owner": "Lisa Johnson"}
            ]
        }
    ]
    
    return projects

def render_collaboration():
    """Render the Collaboration tab with team insights and workflow optimization"""
    
    st.markdown("# 🤝 Collaboration & Team Intelligence")
    st.markdown("*AI-powered team collaboration, shared workflows, and collective intelligence optimization*")
    
    # Generate data
    team_df = generate_team_data()
    shared_accounts = generate_shared_accounts()
    knowledge_base = generate_knowledge_base()
    team_projects = generate_team_projects()
    
    # Create tabs for different collaboration aspects
    tab1, tab2, tab3, tab4 = st.tabs([
        "👥 Team Performance", 
        "🤝 Shared Accounts", 
        "📚 Knowledge Base",
        "🎯 Joint Projects"
    ])
    
    with tab1:
        st.markdown("### 👥 Team Collaboration Metrics")
        
        # Team performance overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            avg_collab_score = team_df['Collaboration_Score'].mean()
            st.metric("Team Collaboration Score", f"{avg_collab_score:.1f}/100", "+5.2 vs last month")
        
        with col2:
            total_shared_deals = team_df['Shared_Deals'].sum()
            st.metric("Shared Deals", total_shared_deals, "+18 vs last month")
        
        with col3:
            total_knowledge_shares = team_df['Knowledge_Shares'].sum()
            st.metric("Knowledge Shares", total_knowledge_shares, "+34 vs last month")
        
        with col4:
            avg_team_revenue = team_df['Team_Revenue'].mean()
            st.metric("Avg Team Revenue", f"${avg_team_revenue/1e6:.1f}M", "+12.3% vs LY")
        
        st.markdown("---")
        
        # Team collaboration visualization
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 📊 Team Collaboration vs Performance")
            
            fig_scatter = px.scatter(
                team_df,
                x="Collaboration_Score",
                y="Team_Revenue",
                size="Members",
                color="Region",
                hover_name="Team_Name",
                title="Team Revenue vs Collaboration Score",
                color_discrete_map={
                    'West': COKE_COLORS['primary_red'],
                    'Northeast': COKE_COLORS['info_blue'],
                    'Southeast': COKE_COLORS['success_green'],
                    'Midwest': COKE_COLORS['warning_orange'],
                    'Southwest': COKE_COLORS['coke_gold']
                }
            )
            
            fig_scatter.update_layout(height=400, font_color=COKE_COLORS['coke_black'])
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            st.markdown("#### 🏆 Top Collaborating Teams")
            
            top_teams = team_df.nlargest(5, 'Collaboration_Score')
            
            for _, team in top_teams.iterrows():
                collab_color = COKE_COLORS['success_green'] if team['Collaboration_Score'] > 90 else COKE_COLORS['warning_orange']
                
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 12px;
                    border-radius: 8px;
                    margin: 8px 0;
                    border-left: 4px solid {collab_color};
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{team['Team_Name']}</h5>
                    <p style="margin: 5px 0; color: {COKE_COLORS['dark_gray']}; font-size: 14px;">Lead: {team['Team_Lead']}</p>
                    <p style="margin: 0; color: {collab_color}; font-weight: 600;">Score: {team['Collaboration_Score']}/100</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Team activity feed
        st.markdown("#### 📱 Recent Team Activity")
        
        activities = [
            {"icon": "🤝", "message": "Sarah Chen shared account insights with Mike Rodriguez", "time": "2 hours ago"},
            {"icon": "📞", "message": "Northeast team completed joint call with Walmart", "time": "4 hours ago"},
            {"icon": "📄", "message": "David Kim updated Freestyle sales playbook", "time": "6 hours ago"},
            {"icon": "🎯", "message": "Southwest team achieved 95% collaboration score", "time": "8 hours ago"},
            {"icon": "💡", "message": "Maria Garcia submitted process improvement idea", "time": "1 day ago"},
            {"icon": "🏆", "message": "West Coast Eagles completed Q4 planning session", "time": "1 day ago"}
        ]
        
        for activity in activities:
            time_str = activity["time"]
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                border-left: 4px solid {COKE_COLORS['info_blue']};
                padding: 12px;
                margin: 8px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: {COKE_COLORS['coke_black']}; font-weight: 500;">{activity['icon']} {activity['message']}</span>
                    <small style="color: {COKE_COLORS['dark_gray']}; font-weight: 500;">{time_str}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Collaboration impact analysis
        st.markdown("#### 📈 Collaboration Impact Analysis")
        
        impact_data = {
            'Metric': ['Win Rate', 'Deal Size', 'Customer Satisfaction', 'Time to Close'],
            'Solo Work': [0.65, 45000, 4.2, 120],
            'Team Collaboration': [0.82, 67000, 4.7, 89]
        }
        
        impact_df = pd.DataFrame(impact_data)
        
        # Create comparison chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Solo Work',
            x=impact_df['Metric'][:3],  # Exclude time to close for better scaling
            y=[0.65, 45, 4.2],
            marker_color=COKE_COLORS['light_gray']
        ))
        
        fig.add_trace(go.Bar(
            name='Team Collaboration',
            x=impact_df['Metric'][:3],
            y=[0.82, 67, 4.7],
            marker_color=COKE_COLORS['primary_red']
        ))
        
        fig.update_layout(
            title="Collaboration vs Solo Performance",
            barmode='group',
            height=300,
            font_color=COKE_COLORS['coke_black']
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### 🤝 Shared Account Management")
        
        # Shared accounts overview
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 💼 Active Shared Accounts")
            
            for account in shared_accounts:
                status_color = COKE_COLORS['success_green'] if account['status'] == "Active" else COKE_COLORS['primary_red'] if account['status'] == "At Risk" else COKE_COLORS['warning_orange'] if account['status'] == "Negotiating" else COKE_COLORS['info_blue']
                
                with st.expander(f"🏢 {account['account_name']} - ${account['total_value']:,.0f}"):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        st.markdown(f"**Collaboration Type:** {account['collaboration_type']}")
                        st.markdown(f"**Status:** <span style='color: {status_color}'>{account['status']}</span>", unsafe_allow_html=True)
                        st.markdown(f"**Shared By:** {', '.join(account['shared_by'])}")
                        st.markdown(f"**Last Interaction:** {account['last_interaction']}")
                    
                    with col_b:
                        st.markdown(f"**Shared Opportunities:** {account['shared_opportunities']}")
                        st.markdown(f"**Joint Calls:** {account['joint_calls']}")
                        st.markdown(f"**Document Shares:** {account['document_shares']}")
                        st.markdown(f"**Total Value:** ${account['total_value']:,.0f}")
        
        with col2:
            st.markdown("#### 📊 Collaboration Metrics")
            
            # Calculate sharing statistics
            total_value = sum(acc['total_value'] for acc in shared_accounts)
            total_opportunities = sum(acc['shared_opportunities'] for acc in shared_accounts)
            total_calls = sum(acc['joint_calls'] for acc in shared_accounts)
            total_documents = sum(acc['document_shares'] for acc in shared_accounts)
            
            st.metric("Total Shared Value", f"${total_value/1e6:.1f}M", "+15.2% vs LY")
            st.metric("Shared Opportunities", total_opportunities, "+8 this month")
            st.metric("Joint Customer Calls", total_calls, "+12 this month")
            st.metric("Document Shares", total_documents, "+23 this month")
    
    with tab3:
        st.markdown("### 📚 Knowledge Base & Best Practices")
        
        # Knowledge sharing metrics
        col1, col2, col3, col4 = st.columns(4)
        
        total_views = sum(item['views'] for item in knowledge_base)
        total_likes = sum(item['likes'] for item in knowledge_base)
        total_downloads = sum(item['downloads'] for item in knowledge_base)
        
        with col1:
            st.metric("Total Views", f"{total_views:,}", "+142 this week")
        
        with col2:
            st.metric("Total Likes", total_likes, "+18 this week")
        
        with col3:
            st.metric("Downloads", total_downloads, "+34 this week")
        
        with col4:
            st.metric("Active Contributors", "8", "+2 this month")
        
        st.markdown("---")
        
        # Knowledge base items
        st.markdown("#### 📖 Top Knowledge Base Items")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            for item in knowledge_base:
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 15px;
                    border-radius: 10px;
                    margin: 10px 0;
                    border: 1px solid {COKE_COLORS['light_gray']};
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div style="flex: 1;">
                            <h4 style="margin: 0 0 5px 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">📄 {item['title']}</h4>
                            <p style="margin: 5px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">{item['description']}</p>
                            <div style="margin-top: 10px;">
                                <small style="color: {COKE_COLORS['dark_gray']}; font-weight: 500;">
                                    By {item['author']} • {item['category']} • Updated {item['last_updated']}
                                </small>
                            </div>
                        </div>
                        <div style="margin-left: 20px; text-align: center; min-width: 80px;">
                            <div style="color: {COKE_COLORS['info_blue']}; font-weight: 600;">👁️ {item['views']}</div>
                            <div style="color: {COKE_COLORS['success_green']}; font-weight: 600;">❤️ {item['likes']}</div>
                            <div style="color: {COKE_COLORS['warning_orange']}; font-weight: 600;">📥 {item['downloads']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🏷️ Popular Tags")
            
            all_tags = []
            for item in knowledge_base:
                all_tags.extend(item['tags'])
            
            tag_counts = {}
            for tag in all_tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            
            for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True):
                st.markdown(f"""
                <span style="
                    background: {COKE_COLORS['primary_red']};
                    color: white;
                    padding: 4px 8px;
                    border-radius: 12px;
                    font-size: 12px;
                    margin: 2px;
                    display: inline-block;
                ">{tag} ({count})</span>
                """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 🎯 Collaborative Projects")
        
        # Project overview metrics
        active_projects = [p for p in team_projects if p['status'] in ['In Progress', 'Planning']]
        completed_projects = [p for p in team_projects if p['status'] == 'Complete']
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Active Projects", len(active_projects), f"+{len(active_projects)-1} vs last quarter")
        
        with col2:
            st.metric("Completed Projects", len(completed_projects), "This quarter")
        
        with col3:
            total_budget = sum(p['budget'] for p in team_projects)
            st.metric("Total Budget", f"${total_budget/1e6:.1f}M", "Allocated")
        
        with col4:
            total_expected = sum(p['expected_revenue'] for p in team_projects)
            st.metric("Expected Revenue", f"${total_expected/1e6:.1f}M", "Pipeline")
        
        st.markdown("---")
        
        # Project details
        for project in team_projects:
            status_color = COKE_COLORS['success_green'] if project['status'] == "Complete" else COKE_COLORS['info_blue'] if project['status'] == "In Progress" else COKE_COLORS['warning_orange']
            
            with st.expander(f"🎯 {project['project_name']} - {project['status']}"):
                col_a, col_b = st.columns([2, 1])
                
                with col_a:
                    st.markdown(f"**Team Members:** {', '.join(project['team_members'])}")
                    st.markdown(f"**Timeline:** {project['start_date']} → {project['target_completion']}")
                    st.markdown(f"**Budget:** ${project['budget']:,.0f}")
                    st.markdown(f"**Expected Revenue:** ${project['expected_revenue']:,.0f}")
                    
                    # Progress bar
                    st.markdown(f"""
                    <div style="
                        background: {COKE_COLORS['classic_white']};
                        padding: 10px;
                        border-radius: 8px;
                        margin: 10px 0;
                        border: 1px solid {COKE_COLORS['light_gray']};
                    ">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <strong style="color: {COKE_COLORS['coke_black']};">Progress</strong>
                            <span style="color: {status_color}; font-weight: 600;">{project['progress']*100:.0f}%</span>
                        </div>
                        <div style="background: #e9ecef; border-radius: 10px; height: 10px;">
                            <div style="background: {status_color}; width: {project['progress']*100}%; height: 10px; border-radius: 10px;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_b:
                    st.markdown("**Project Milestones**")
                    
                    for milestone in project['milestones']:
                        milestone_color = COKE_COLORS['success_green'] if milestone['status'] == "Complete" else COKE_COLORS['info_blue'] if milestone['status'] == "In Progress" else COKE_COLORS['dark_gray']
                        
                        st.markdown(f"""
                        <div style="
                            background: {COKE_COLORS['classic_white']};
                            border-left: 4px solid {milestone_color};
                            padding: 8px;
                            margin: 5px 0;
                            border-radius: 5px;
                            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                        ">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <strong style="color: {COKE_COLORS['coke_black']}; font-size: 12px;">{milestone['milestone']}</strong>
                            </div>
                            <div style="margin-top: 5px;">
                                <span style="color: {milestone_color}; font-weight: bold; font-size: 11px;">{milestone['status']}</span>
                                <span style="color: {COKE_COLORS['dark_gray']}; margin-left: 10px; font-size: 11px;">({milestone['owner']})</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        # AI-powered collaboration recommendations
        st.markdown("---")
        st.markdown("#### 🤖 AI-Powered Collaboration Recommendations")
        
        collab_recommendations = [
            {
                "title": "Cross-Training Opportunity",
                "content": "Jennifer Smith's digital marketing expertise could benefit the Southwest team's upcoming campaign",
                "confidence": 0.92,
                "action": "Schedule knowledge transfer session"
            },
            {
                "title": "Account Sharing Suggestion",
                "content": "Sarah Chen and Mike Rodriguez show synergy potential for enterprise QSR accounts",
                "confidence": 0.87,
                "action": "Pilot joint account management"
            },
            {
                "title": "Resource Optimization",
                "content": "Northeast team's Freestyle expertise could accelerate West Coast expansion",
                "confidence": 0.89,
                "action": "Deploy specialist support"
            },
            {
                "title": "Best Practice Scaling",
                "content": "David Kim's category management approach should be shared across all C-store teams",
                "confidence": 0.94,
                "action": "Create training module"
            }
        ]
        
        for rec in collab_recommendations:
            color = COKE_COLORS['success_green'] if rec["confidence"] > 0.9 else COKE_COLORS['info_blue'] if rec["confidence"] > 0.8 else COKE_COLORS['warning_orange']
            
            st.markdown(f"""
            <div style="
                border-left: 4px solid {color};
                background: {COKE_COLORS['classic_white']};
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div style="flex: 1;">
                        <h4 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">🤝 {rec['title']}</h4>
                        <p style="margin: 10px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">{rec['content']}</p>
                        <small style="color: {COKE_COLORS['dark_gray']}; font-weight: 500;">Recommended Action: {rec['action']}</small>
                    </div>
                    <div style="margin-left: 15px;">
                        <span style="
                            background: {color}; 
                            color: white; 
                            padding: 4px 8px; 
                            border-radius: 12px; 
                            font-size: 11px; 
                            font-weight: bold;
                        ">{rec['confidence']:.0%} Confidence</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render():
    """Main render function for the collaboration tab"""
    render_collaboration()
