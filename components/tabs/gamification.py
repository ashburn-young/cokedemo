"""
Gamification Tab - Leaderboards, Achievements, and Team Competitions
AI-powered gamification with GPT-4o driven insights and recommendations
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

def generate_leaderboard_data():
    """Generate realistic sales rep leaderboard data"""
    reps = [
        {"name": "Sarah Chen", "region": "West", "level": "Senior", "photo": "👩‍💼"},
        {"name": "Mike Rodriguez", "region": "Southwest", "level": "Senior", "photo": "👨‍💼"},
        {"name": "Jennifer Smith", "region": "Northeast", "level": "Mid", "photo": "👩‍💻"},
        {"name": "David Kim", "region": "Southeast", "level": "Senior", "photo": "👨‍💻"},
        {"name": "Amanda Wilson", "region": "Midwest", "level": "Junior", "photo": "👩‍🎓"},
        {"name": "Carlos Ruiz", "region": "Southwest", "level": "Mid", "photo": "👨‍🎓"},
        {"name": "Lisa Park", "region": "West", "level": "Senior", "photo": "👩‍💼"},
        {"name": "Tom Bradley", "region": "Northeast", "level": "Mid", "photo": "👨‍💼"},
        {"name": "Maria Garcia", "region": "Southeast", "level": "Junior", "photo": "👩‍💻"},
        {"name": "James Foster", "region": "Midwest", "level": "Senior", "photo": "👨‍💻"}
    ]
    
    leaderboard_data = []
    for i, rep in enumerate(reps):
        base_performance = random.uniform(0.7, 1.4)
        level_multiplier = {"Junior": 0.8, "Mid": 1.0, "Senior": 1.2}[rep["level"]]
        
        data = {
            "Rank": i + 1,
            "Rep_Name": rep["name"],
            "Photo": rep["photo"],
            "Region": rep["region"],
            "Level": rep["level"],
            "Total_Points": int(random.randint(750, 1500) * base_performance * level_multiplier),
            "Revenue_YTD": random.randint(1200000, 3500000) * base_performance,
            "Deals_Closed": random.randint(15, 45) * base_performance,
            "New_Customers": random.randint(8, 25) * base_performance,
            "Customer_Satisfaction": random.uniform(4.1, 4.9),
            "Activity_Score": random.randint(85, 100),
            "Streak_Days": random.randint(0, 30),
            "Achievements": random.randint(3, 12),
            "Team_Contributions": random.randint(5, 20),
            "Monthly_Growth": random.uniform(-5, 25)
        }
        leaderboard_data.append(data)
    
    # Sort by total points
    leaderboard_df = pd.DataFrame(leaderboard_data).sort_values('Total_Points', ascending=False)
    leaderboard_df['Rank'] = range(1, len(leaderboard_df) + 1)
    
    return leaderboard_df

def generate_achievements():
    """Generate achievement system data"""
    achievements = [
        {
            "name": "Revenue Rockstar",
            "description": "Exceed quarterly revenue target by 20%",
            "icon": "🚀",
            "category": "Revenue",
            "points": 500,
            "rarity": "Epic",
            "unlocked_by": ["Sarah Chen", "Mike Rodriguez", "David Kim"],
            "progress_req": "120% of target",
            "ai_tip": "GPT-4o suggests focusing on high-value accounts for faster achievement"
        },
        {
            "name": "Customer Whisperer",
            "description": "Achieve 95%+ customer satisfaction for 3 months",
            "icon": "🎯",
            "category": "Satisfaction",
            "points": 300,
            "rarity": "Rare",
            "unlocked_by": ["Jennifer Smith", "Lisa Park", "Amanda Wilson"],
            "progress_req": "95% satisfaction",
            "ai_tip": "AI analysis shows follow-up timing is key to high satisfaction scores"
        },
        {
            "name": "Deal Closer",
            "description": "Close 30+ deals in a single month",
            "icon": "💪",
            "category": "Activity",
            "points": 250,
            "rarity": "Common",
            "unlocked_by": ["Mike Rodriguez", "Carlos Ruiz", "Tom Bradley", "James Foster"],
            "progress_req": "30 deals",
            "ai_tip": "Focus on smaller accounts for volume-based achievements"
        },
        {
            "name": "Innovation Champion",
            "description": "Successfully introduce Freestyle to 5 new accounts",
            "icon": "💡",
            "category": "Innovation",
            "points": 400,
            "rarity": "Epic",
            "unlocked_by": ["Sarah Chen", "David Kim"],
            "progress_req": "5 Freestyle deployments",
            "ai_tip": "GPT-4o recommends targeting entertainment venues for Freestyle adoption"
        },
        {
            "name": "Team Player",
            "description": "Assist teammates to close 10 deals",
            "icon": "🤝",
            "category": "Collaboration",
            "points": 200,
            "rarity": "Rare",
            "unlocked_by": ["Amanda Wilson", "Maria Garcia", "Lisa Park"],
            "progress_req": "10 assisted deals",
            "ai_tip": "Share competitive intelligence to boost team performance"
        },
        {
            "name": "Streak Master",
            "description": "Maintain daily activity for 30 consecutive days",
            "icon": "🔥",
            "category": "Consistency",
            "points": 350,
            "rarity": "Rare",
            "unlocked_by": ["Jennifer Smith", "Tom Bradley"],
            "progress_req": "30-day streak",
            "ai_tip": "Set daily reminders for consistent CRM updates"
        }
    ]
    
    return achievements

def generate_team_challenges():
    """Generate current team challenges"""
    challenges = [
        {
            "name": "Q4 Revenue Blitz",
            "description": "All regions compete to exceed Q4 targets by the highest percentage",
            "duration": "90 days",
            "prize": "$10,000 team bonus + extra vacation days",
            "current_leader": "West Region",
            "progress": 0.78,
            "participants": ["West", "Northeast", "Southeast", "Midwest", "Southwest"],
            "leaderboard": [
                {"team": "West", "progress": 0.78, "percentage": "125%"},
                {"team": "Northeast", "progress": 0.71, "percentage": "118%"},
                {"team": "Southeast", "progress": 0.69, "percentage": "115%"},
                {"team": "Midwest", "progress": 0.65, "percentage": "112%"},
                {"team": "Southwest", "progress": 0.63, "percentage": "110%"}
            ],
            "ai_insight": "GPT-4o predicts West Region will maintain lead with 89% confidence"
        },
        {
            "name": "Customer Satisfaction Championship",
            "description": "Achieve highest average customer satisfaction scores",
            "duration": "30 days",
            "prize": "Customer Excellence Awards + Recognition Trip",
            "current_leader": "Northeast Region",
            "progress": 0.82,
            "participants": ["All Regions"],
            "leaderboard": [
                {"team": "Northeast", "progress": 0.82, "percentage": "4.6/5.0"},
                {"team": "Southeast", "progress": 0.79, "percentage": "4.5/5.0"},
                {"team": "West", "progress": 0.76, "percentage": "4.4/5.0"},
                {"team": "Midwest", "progress": 0.74, "percentage": "4.3/5.0"},
                {"team": "Southwest", "progress": 0.71, "percentage": "4.2/5.0"}
            ],
            "ai_insight": "AI suggests Northeast's follow-up methodology is driving their success"
        },
        {
            "name": "Freestyle Innovation Challenge",
            "description": "Deploy the most Freestyle machines to new accounts",
            "duration": "60 days",
            "prize": "Innovation Awards + Technology Early Access",
            "current_leader": "West Region",
            "progress": 0.45,
            "participants": ["West", "Northeast", "Southeast"],
            "leaderboard": [
                {"team": "West", "progress": 0.45, "percentage": "23 deployments"},
                {"team": "Northeast", "progress": 0.41, "percentage": "21 deployments"},
                {"team": "Southeast", "progress": 0.37, "percentage": "19 deployments"}
            ],
            "ai_insight": "Entertainment venues show highest Freestyle adoption rates per AI analysis"
        }
    ]
    
    return challenges

def generate_ai_recommendations():
    """Generate AI-powered gamification recommendations"""
    return [
        {
            "type": "achievement",
            "title": "Personalized Achievement Suggestion",
            "content": "Based on your activity patterns, you're 87% likely to unlock 'Consistency Master' if you maintain daily CRM updates for 7 more days.",
            "action": "Set daily reminder",
            "confidence": 0.87
        },
        {
            "type": "competition",
            "title": "Optimal Challenge Participation",
            "content": "GPT-4o analysis suggests joining the 'Customer Satisfaction Championship' aligns perfectly with your strengths. 94% win probability.",
            "action": "Join challenge",
            "confidence": 0.94
        },
        {
            "type": "strategy",
            "title": "Leaderboard Advancement",
            "content": "To move up 2 positions in leaderboard, focus on new customer acquisition. AI predicts 3 new customers will boost you to #4.",
            "action": "Target 3 prospects",
            "confidence": 0.91
        },
        {
            "type": "team",
            "title": "Team Collaboration Opportunity",
            "content": "Helping Amanda Wilson with her Enterprise accounts could unlock 'Mentor' achievement and boost team score by 15%.",
            "action": "Offer assistance",
            "confidence": 0.83
        }
    ]

def render_gamification():
    """Main function to render the Gamification tab"""
    
    st.markdown("# 🏆 Sales Gamification Hub")
    st.markdown("*Leaderboards, achievements, challenges, and AI-powered competition insights*")
    
    # Generate data
    leaderboard_df = generate_leaderboard_data()
    achievements = generate_achievements()
    challenges = generate_team_challenges()
    ai_recommendations = generate_ai_recommendations()
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_points = leaderboard_df['Total_Points'].sum()
        st.metric("Total Points Earned", f"{total_points:,}", "+2,450")
    
    with col2:
        active_players = len(leaderboard_df)
        st.metric("Active Players", active_players, "+3")
    
    with col3:
        total_achievements = sum(len(ach['unlocked_by']) for ach in achievements)
        st.metric("Achievements Unlocked", total_achievements, "+12")
    
    with col4:
        active_challenges = len(challenges)
        st.metric("Active Challenges", active_challenges, "0")
    
    st.divider()
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏆 Leaderboards", 
        "🎖️ Achievements", 
        "🚀 Team Challenges", 
        "📊 Performance Analytics",
        "🤖 AI Insights"
    ])
    
    with tab1:
        st.markdown("### 🏆 Sales Rep Leaderboard")
        
        # Leaderboard display
        for i, row in leaderboard_df.head(10).iterrows():
            rank_emoji = "🥇" if row['Rank'] == 1 else "🥈" if row['Rank'] == 2 else "🥉" if row['Rank'] == 3 else f"#{row['Rank']}"
            
            with st.container():
                st.markdown(f"""
                <div style="
                    background: {'linear-gradient(135deg, #FFC72C, #FFD700)' if row['Rank'] == 1 else 'linear-gradient(135deg, #f8f9fa, #e9ecef)' if row['Rank'] == 2 else 'linear-gradient(135deg, #6c757d, #adb5bd)' if row['Rank'] == 3 else COKE_COLORS['classic_white']};
                    border: 2px solid {COKE_COLORS['primary_red'] if row['Rank'] <= 3 else '#dee2e6'};
                    border-radius: 12px;
                    padding: 20px;
                    margin: 10px 0;
                    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
                ">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                        <div style="display: flex; align-items: center;">
                            <div style="font-size: 28px; margin-right: 15px;">{rank_emoji}</div>
                            <div style="font-size: 28px; margin-right: 15px;">{row['Photo']}</div>
                            <div>
                                <h4 style="margin: 0; color: {COKE_COLORS['coke_black'] if row['Rank'] > 3 else COKE_COLORS['classic_white']}; font-weight: 600;">{row['Rep_Name']}</h4>
                                <small style="color: {COKE_COLORS['dark_gray'] if row['Rank'] > 3 else COKE_COLORS['classic_white']}; font-size: 14px;">{row['Region']} • {row['Level']} Level</small>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <h3 style="margin: 0; color: {COKE_COLORS['coke_black'] if row['Rank'] > 3 else COKE_COLORS['classic_white']}; font-weight: 700; font-size: 24px;">{row['Total_Points']:,} pts</h3>
                            <small style="color: {COKE_COLORS['dark_gray'] if row['Rank'] > 3 else COKE_COLORS['classic_white']}; font-size: 14px;">${row['Revenue_YTD']:,.0f} revenue</small>
                        </div>
                    </div>
                    <div style="margin-top: 15px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; font-size: 13px; color: {COKE_COLORS['coke_black'] if row['Rank'] > 3 else COKE_COLORS['classic_white']};">
                        <div><strong>Deals:</strong> {row['Deals_Closed']:.0f}</div>
                        <div><strong>New Customers:</strong> {row['New_Customers']:.0f}</div>
                        <div><strong>Satisfaction:</strong> {row['Customer_Satisfaction']:.1f}/5</div>
                        <div><strong>Streak:</strong> {row['Streak_Days']:.0f} days</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Performance distribution charts
        st.markdown("### 📊 Performance Distribution")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Points distribution by region
            region_points = leaderboard_df.groupby('Region')['Total_Points'].sum().reset_index()
            fig_region = px.bar(
                region_points, 
                x='Region', 
                y='Total_Points',
                title="Total Points by Region",
                color='Total_Points',
                color_continuous_scale='Reds'
            )
            fig_region.update_layout(
                height=300,
                font_color=COKE_COLORS['coke_black'],
                paper_bgcolor=COKE_COLORS['classic_white']
            )
            st.plotly_chart(fig_region, use_container_width=True)
        
        with col2:
            # Level distribution
            level_dist = leaderboard_df.groupby('Level').size().reset_index(name='Count')
            fig_level = px.pie(
                level_dist, 
                values='Count', 
                names='Level',
                title="Representation by Experience Level",
                color_discrete_map={'Senior': COKE_COLORS['primary_red'], 'Mid': COKE_COLORS['coke_gold'], 'Junior': COKE_COLORS['info_blue']}
            )
            fig_level.update_layout(
                height=300,
                font_color=COKE_COLORS['coke_black'],
                paper_bgcolor=COKE_COLORS['classic_white']
            )
            st.plotly_chart(fig_level, use_container_width=True)
    
    with tab2:
        st.markdown("### 🎖️ Achievement System")
        
        # Achievement categories
        categories = list(set(ach['category'] for ach in achievements))
        selected_category = st.selectbox("Filter by category:", ["All"] + categories)
        
        # Display achievements
        for ach in achievements:
            if selected_category == "All" or ach['category'] == selected_category:
                rarity_color = "#FFD700" if ach['rarity'] == "Epic" else "#C0C0C0" if ach['rarity'] == "Rare" else "#CD7F32"
                
                with st.expander(f"{ach['icon']} {ach['name']} ({ach['rarity']})"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"**Description:** {ach['description']}")
                        st.markdown(f"**Category:** {ach['category']}")
                        st.markdown(f"**Requirements:** {ach['progress_req']}")
                        st.markdown(f"**💡 AI Tip:** {ach['ai_tip']}")
                    
                    with col2:
                        st.metric("Points Value", f"{ach['points']} pts")
                        st.markdown(f"**Rarity:** <span style='color: {rarity_color}'>{ach['rarity']}</span>", unsafe_allow_html=True)
                        st.markdown(f"**Unlocked by {len(ach['unlocked_by'])} reps:**")
                        for rep in ach['unlocked_by']:
                            st.markdown(f"• {rep}")
        
        # Achievement progress tracking
        st.markdown("### 📈 Your Achievement Progress")
        
        # Simulate user progress
        user_progress = [
            {"achievement": "Revenue Rockstar", "progress": 0.85, "status": "In Progress"},
            {"achievement": "Customer Whisperer", "progress": 1.0, "status": "Completed"},
            {"achievement": "Deal Closer", "progress": 0.67, "status": "In Progress"},
            {"achievement": "Innovation Champion", "progress": 0.4, "status": "In Progress"},
            {"achievement": "Team Player", "progress": 1.0, "status": "Completed"},
            {"achievement": "Streak Master", "progress": 0.23, "status": "In Progress"}
        ]
        
        for prog in user_progress:
            status_color = "#28a745" if prog['status'] == "Completed" else "#007bff"
            
            st.markdown(f"""
            <div style="background: {COKE_COLORS['classic_white']}; border-left: 4px solid {status_color}; padding: 15px; margin: 10px 0; border-radius: 5px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="color: {COKE_COLORS['coke_black']};">{prog['achievement']}</strong>
                    <span style="color: {status_color}; font-weight: 600;">{prog['status']}</span>
                </div>
                <div style="margin-top: 10px;">
                    <div style="background: #e9ecef; border-radius: 10px; height: 8px;">
                        <div style="background: {status_color}; width: {prog['progress']*100}%; height: 8px; border-radius: 10px;"></div>
                    </div>
                    <small style="color: {COKE_COLORS['dark_gray']}; margin-top: 5px; display: block; font-weight: 500;">{prog['progress']*100:.0f}% Complete</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🚀 Team Challenges")
        
        for challenge in challenges:
            with st.expander(f"🏁 {challenge['name']} - {challenge['current_leader']} Leading"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Description:** {challenge['description']}")
                    st.markdown(f"**Duration:** {challenge['duration']}")
                    st.markdown(f"**Prize:** {challenge['prize']}")
                    st.markdown(f"**🤖 AI Insight:** {challenge['ai_insight']}")
                
                with col2:
                    st.metric("Overall Progress", f"{challenge['progress']*100:.0f}%")
                    st.metric("Current Leader", challenge['current_leader'])
                
                # Challenge leaderboard
                st.markdown("#### 🏆 Challenge Leaderboard")
                
                for i, team in enumerate(challenge['leaderboard']):
                    position = i + 1
                    medal = "🥇" if position == 1 else "🥈" if position == 2 else "🥉" if position == 3 else f"#{position}"
                    
                    st.markdown(f"""
                    <div style="
                        background: {'#fff3cd' if position == 1 else '#d1ecf1' if position == 2 else '#f8d7da' if position == 3 else 'white'};
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        padding: 10px;
                        margin: 5px 0;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                    ">
                        <div><strong>{medal} {team['team']} Region</strong></div>
                        <div>
                            <span style="font-size: 16px; font-weight: bold;">{team['percentage']}</span>
                            <div style="background: #e9ecef; width: 100px; height: 6px; border-radius: 3px; margin-top: 2px;">
                                <div style="background: #007bff; width: {team['progress']*100}%; height: 6px; border-radius: 3px;"></div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                if st.button(f"Join {challenge['name']}", key=f"join_{challenge['name']}"):
                    st.success(f"✅ Successfully joined {challenge['name']}!")
        
        # Create new challenge
        st.markdown("### ➕ Suggest New Challenge")
        
        with st.form("new_challenge"):
            challenge_name = st.text_input("Challenge Name")
            challenge_desc = st.text_area("Description")
            challenge_duration = st.selectbox("Duration", ["1 week", "2 weeks", "1 month", "3 months"])
            challenge_prize = st.text_input("Prize/Reward")
            
            if st.form_submit_button("Submit Challenge Idea"):
                st.success("✅ Challenge idea submitted for review!")
    
    with tab4:
        st.markdown("### 📊 Performance Analytics")
        
        # Performance trends
        st.markdown("#### 📈 Performance Trends")
        
        # Generate trend data
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        trend_data = {
            'Date': dates,
            'Total_Points': np.cumsum(np.random.normal(150, 50, 30)),
            'Daily_Revenue': np.random.normal(85000, 15000, 30),
            'Activity_Score': np.random.normal(88, 8, 30),
            'Team_Collaboration': np.random.normal(75, 12, 30)
        }
        
        trend_df = pd.DataFrame(trend_data)
        
        # Multi-metric chart
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Points Accumulation', 'Daily Revenue', 'Activity Score', 'Team Collaboration'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        fig.add_trace(
            go.Scatter(x=trend_df['Date'], y=trend_df['Total_Points'], name='Points'),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=trend_df['Date'], y=trend_df['Daily_Revenue'], name='Revenue'),
            row=1, col=2
        )
        
        fig.add_trace(
            go.Scatter(x=trend_df['Date'], y=trend_df['Activity_Score'], name='Activity'),
            row=2, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=trend_df['Date'], y=trend_df['Team_Collaboration'], name='Collaboration'),
            row=2, col=2
        )
        
        fig.update_layout(height=500, showlegend=False, title_text="30-Day Performance Dashboard")
        st.plotly_chart(fig, use_container_width=True)
        
        # Performance comparison
        st.markdown("#### 🔄 Performance Comparison")
        
        comparison_metrics = ['Total_Points', 'Revenue_YTD', 'Deals_Closed', 'Customer_Satisfaction']
        selected_metric = st.selectbox("Select metric to compare:", comparison_metrics)
        
        # Top vs average comparison
        top_performers = leaderboard_df.head(3)[selected_metric].mean()
        all_performers = leaderboard_df[selected_metric].mean()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Top 3 Average", f"{top_performers:,.1f}")
        
        with col2:
            st.metric("Overall Average", f"{all_performers:,.1f}")
        
        with col3:
            improvement = ((top_performers - all_performers) / all_performers) * 100
            st.metric("Performance Gap", f"+{improvement:.1f}%")
    
    with tab5:
        st.markdown("### 🤖 AI-Powered Gamification Insights")
        
        # AI recommendations
        st.markdown("#### 🎯 Personalized Recommendations")
        
        for rec in ai_recommendations:
            icon = "🎖️" if rec["type"] == "achievement" else "🏆" if rec["type"] == "competition" else "📈" if rec["type"] == "strategy" else "🤝"
            color = "#28a745" if rec["confidence"] > 0.9 else "#007bff" if rec["confidence"] > 0.8 else "#ffc107"
            
            with st.container():
                st.markdown(f"""
                <div style="
                    border-left: 4px solid {color};
                    background: {COKE_COLORS['classic_white']};
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h4 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{icon} {rec['title']}</h4>
                    <p style="margin: 10px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">{rec['content']}</p>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <button style="
                                background: {color}; 
                                color: white; 
                                border: none; 
                                padding: 8px 16px; 
                                border-radius: 4px; 
                                cursor: pointer;
                            ">{rec['action'].title()}</button>
                        </div>
                        <small style="color: #777;">AI Confidence: {rec['confidence']:.0%}</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # AI Performance Predictor
        st.markdown("#### 🔮 Performance Predictor")
        
        st.markdown("**What would you like to predict?**")
        
        prediction_type = st.selectbox(
            "Choose prediction type:",
            [
                "Chance to reach next rank",
                "Achievement unlock probability", 
                "Challenge win likelihood",
                "Monthly point potential"
            ]
        )
        
        if prediction_type:
            # Simulate AI prediction
            confidence = random.uniform(0.75, 0.95)
            
            predictions = {
                "Chance to reach next rank": f"87% probability to advance to rank #{leaderboard_df.iloc[4]['Rank']-1} by month end",
                "Achievement unlock probability": "94% chance to unlock 'Revenue Rockstar' with 2 more high-value deals",
                "Challenge win likelihood": "76% probability to win 'Customer Satisfaction Championship' if current trend continues",
                "Monthly point potential": f"Projected to earn {random.randint(800, 1200)} points this month based on current activity"
            }
            
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                border-radius: 10px;
                margin: 15px 0;
                text-align: center;
            ">
                <h3 style="margin: 0;">🔮 AI Prediction</h3>
                <p style="font-size: 18px; margin: 15px 0;">{predictions[prediction_type]}</p>
                <small>Confidence Level: {confidence:.0%}</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Gamification optimization
        st.markdown("#### ⚙️ Gamification Optimization")
        
        optimization_tips = [
            "📊 **Leaderboard Strategy**: Focus on consistency over bursts - steady performers rank higher long-term",
            "🎯 **Achievement Focus**: Complete 'Team Player' achievements for bonus multipliers on individual scores",
            "🏆 **Challenge Selection**: Join challenges that align with your natural strengths for higher win rates",
            "🔥 **Streak Building**: Daily activities compound - a 30-day streak provides 50% bonus on all points",
            "🤝 **Team Dynamics**: Collaborative achievements unlock exclusive team challenges with bigger rewards"
        ]
        
        for tip in optimization_tips:
            st.markdown(tip)
        
        # AI Chat Interface
        st.markdown("#### 💬 Gamification AI Assistant")
        
        if "gamification_chat_history" not in st.session_state:
            st.session_state.gamification_chat_history = []
        
        user_question = st.text_input("Ask about achievements, leaderboards, or strategy:")
        
        if user_question:
            # Simulate AI response
            ai_responses = [
                f"Based on gamification analytics, your question about {user_question} suggests focusing on team collaboration achievements...",
                f"Looking at your performance patterns for {user_question}, I recommend prioritizing consistency-based challenges...",
                f"The leaderboard data shows that {user_question} correlates strongly with revenue performance metrics...",
            ]
            
            response = random.choice(ai_responses)
            
            st.session_state.gamification_chat_history.append({
                "user": user_question,
                "ai": response,
                "timestamp": datetime.now()
            })
        
        # Display chat history
        if st.session_state.gamification_chat_history:
            st.markdown("#### 💭 Recent Conversations")
            for chat in st.session_state.gamification_chat_history[-3:]:  # Show last 3
                st.markdown(f"**You**: {chat['user']}")
                st.markdown(f"**AI**: {chat['ai']}")
                st.markdown("---")

if __name__ == "__main__":
    render_gamification()
