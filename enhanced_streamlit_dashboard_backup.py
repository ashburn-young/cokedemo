"""
Enhanced Coca-Cola Sales AI Platform - Main Dashboard
Modular, proactive sales and pipeline management platform
"""
import streamlit as st
import sys
import os

# Configure Streamlit page
st.set_page_config(
    page_title="Coca-Cola Sales Executive Intelligence Platform",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add componen    elif selected_tab == "🎯 Customer 360":
        if TABS_AVAILABLE:
            render_customer_360()
        else:
            st.error("⚠️ Customer 360 module not available")current_dir = os.path.dirname(__file__)
components_dir = os.path.join(current_dir, 'components')
sys.path.append(components_dir)

# Import tab modules
try:
    from components.tabs.executive_overview import render_executive_overview
    from components.tabs.account_portfolio import render_account_portfolio
    from components.tabs.revenue_opportunities import render_revenue_opportunities
    from components.tabs.ai_recommendations import render_ai_recommendations
    from components.tabs.proactive_playbook import render_proactive_playbook
    from components.tabs.proactive_insights import render_proactive_insights
    from components.tabs.customer_360 import render_customer_360
    from components.tabs.regional_performance import render_regional_performance
    from components.tabs.gamification import render_gamification
    from components.tabs.collaboration import render_collaboration
    from components.tabs.data_insights import render_data_insights
    from components.tabs.architecture import render_architecture
    TABS_AVAILABLE = True
except ImportError as e:
    st.error(f"⚠️ Could not import tab modules: {e}")
    TABS_AVAILABLE = False

# Coca-Cola Brand Styling
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000',
    'classic_white': '#FFFFFF',
    'executive_blue': '#0078D4',
    'coke_gold': '#FFC72C',
    'success_green': '#28a745',
    'warning_orange': '#ffc107'
}

# Apply custom CSS
st.markdown(f"""
<style>
    .main-header {{
        background: linear-gradient(135deg, {COKE_COLORS['primary_red']}, {COKE_COLORS['coke_black']});
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    
    .sidebar .sidebar-content {{
        background-color: #f8f9fa;
    }}
    
    .stTab > div > div > div > button {{
        background-color: white;
        color: {COKE_COLORS['coke_black']};
        border: 2px solid {COKE_COLORS['primary_red']};
        border-radius: 20px;
        padding: 10px 20px;
        margin: 5px;
        font-weight: bold;
        transition: all 0.3s ease;
    }}
    
    .stTab > div > div > div > button[aria-selected="true"] {{
        background-color: {COKE_COLORS['primary_red']};
        color: white;
        border-color: {COKE_COLORS['primary_red']};
        box-shadow: 0 4px 15px rgba(255,0,0,0.3);
    }}
    
    .metric-card {{
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 5px solid {COKE_COLORS['primary_red']};
        margin: 10px 0;
    }}
    
    /* Compact text sizing for better readability */
    .stMetric {{ 
        font-size: 14px !important; 
    }}
    
    .stMetric > div {{ 
        font-size: 14px !important; 
    }}
    
    .stMetric label {{ 
        font-size: 12px !important; 
    }}
    
    .stProgress > div > div > div > div {{ 
        height: 8px !important;
    }}
    
    /* Compact alert boxes */
    .stAlert {{ 
        padding: 8px 12px !important;
        font-size: 14px !important;
    }}
    
    /* Compact markdown */
    .stMarkdown h4 {{
        font-size: 16px !important;
        margin: 8px 0 !important;
    }}
    
    /* Better spacing for containers */
    .block-container {{
        padding-top: 2rem !important;
    }}
    
    .css-1d391kg {{
        background-color: #f8f9fa;
    }}
</style>
""", unsafe_allow_html=True)

def render_sidebar():
    """Render enhanced sidebar with navigation and filters"""
    
    with st.sidebar:
        # Coca-Cola Branding
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {COKE_COLORS['primary_red']}, {COKE_COLORS['coke_black']});
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        ">
            <h1 style="color: white; margin: 0; font-size: 24px;">🥤 Coca-Cola</h1>
            <p style="color: white; margin: 5px 0; opacity: 0.9;">Sales AI Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Menu
        st.markdown("### 🧭 Navigation")
        
        # Tab selection in sidebar with better styling
        tab_options = [
            "📈 Executive Overview",
            "📊 Account Portfolio", 
            "💰 Revenue Opportunities",
            "🤖 AI Recommendations",
            "📋 Proactive Playbook",
            "💡 Proactive Insights",
            "🎯 Customer 360",
            "🗺️ Regional Performance",
            "🏆 Gamification",
            "🤝 Collaboration",
            "📊 Data Insights",
            "🏗️ Architecture"
        ]
        
        # Create a more organized navigation
        st.markdown("**Core Features** (Available Now)")
        core_options = tab_options[:4]
        
        if 'selected_tab' not in st.session_state:
            st.session_state.selected_tab = core_options[0]
            
        # Core features selector
        core_selected = st.radio(
            "Choose your view:",
            options=core_options,
            index=core_options.index(st.session_state.selected_tab) if st.session_state.selected_tab in core_options else 0,
            key="core_tab_selector"
        )
        
        st.markdown("**Advanced Features** (AI-Powered)")
        advanced_options = tab_options[4:]
        
        # Advanced features selector
        advanced_selected = st.selectbox(
            "Choose advanced feature:",
            options=["Select a feature..."] + advanced_options,
            key="advanced_tab_selector"
        )
        
        # Set the selected tab based on user choice
        if advanced_selected != "Select a feature...":
            st.session_state.selected_tab = advanced_selected
        else:
            st.session_state.selected_tab = core_selected
        
        st.divider()
        
        # Quick Action Buttons
        st.markdown("### ⚡ Quick Actions")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Refresh Data", use_container_width=True, key="refresh_data_btn"):
                st.session_state['last_update'] = "Just now"
                st.success("✅ Data refreshed!")
                st.rerun()
                
        with col2:
            if st.button("📊 Export Report", use_container_width=True, key="export_report_btn"):
                st.success("✅ Report export initiated!")
        
        if st.button("🎯 Go to Opportunities", use_container_width=True, key="go_to_opps_btn"):
            st.session_state.selected_tab = "💰 Revenue Opportunities"
            st.rerun()
            
        if st.button("🤖 Ask AI Assistant", use_container_width=True, key="ask_ai_btn"):
            st.session_state.selected_tab = "🤖 AI Recommendations"
            st.rerun()
        
        st.divider()
        
        # Quick Stats
        st.markdown("### 📊 Quick Stats")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Active Accounts", "287", "+12")
            st.metric("Pipeline Value", "$15.2M", "+8.5%")
        
        with col2:
            st.metric("Win Rate", "73%", "+2.1%")
            st.metric("Avg Deal Size", "$52K", "+5.3%")
        
        st.markdown("---")
        
        # Global Filters
        st.markdown("### 🎛️ Global Filters")
        
        time_filter = st.selectbox(
            "📅 Time Period",
            ["This Month", "This Quarter", "This Year", "Last 30 Days", "Last 90 Days"],
            index=1
        )
        
        region_filter = st.multiselect(
            "🌍 Regions",
            ["North America - East", "North America - West", "North America - Central", 
             "Canada - Ontario", "Mexico - North"],
            default=["North America - East", "North America - West"]
        )
        
        rep_filter = st.multiselect(
            "👤 Sales Reps",
            ["All Reps", "Sarah Chen", "Mike Rodriguez", "Jennifer Smith", "David Kim"],
            default=["All Reps"]
        )
        
        st.markdown("---")
        
        # Quick Actions
        st.markdown("### ⚡ Quick Actions")
        
        if st.button("📊 Generate Executive Report", use_container_width=True):
            st.success("✅ Report generation initiated!")
        
        if st.button("🎯 Update Pipeline", use_container_width=True):
            st.success("✅ Pipeline refresh started!")
        
        if st.button("📞 Schedule Team Sync", use_container_width=True):
            st.success("✅ Team sync scheduled!")
        
        st.markdown("---")
        
        # Navigation Help
        with st.expander("ℹ️ Navigation Help"):
            st.markdown("""
            **How to Navigate:**
            - **Core Features**: Use radio buttons for main views
            - **Advanced Features**: Use dropdown for upcoming features
            - **Quick Actions**: Fast access to common tasks
            - **Current View**: Shows your active section at the top
            
            **Available Now:**
            - 📈 Executive Overview - KPIs and insights
            - 📊 Account Portfolio - Customer management
            - 💰 Revenue Opportunities - Sales pipeline
            - 🤖 AI Recommendations - AI-powered insights
            
            **Coming Soon:**
            - All other features are under development
            """)
        
        # System Status
        st.markdown("### 🔧 System Status")
        
        st.markdown("""
        <div style="background: #d4edda; padding: 10px; border-radius: 5px; margin: 5px 0;">
            <small>🟢 <strong>AI Engine:</strong> Online</small>
        </div>
        <div style="background: #d4edda; padding: 10px; border-radius: 5px; margin: 5px 0;">
            <small>🟢 <strong>Data Sync:</strong> Current</small>
        </div>
        <div style="background: #fff3cd; padding: 10px; border-radius: 5px; margin: 5px 0;">
            <small>🟡 <strong>CRM Integration:</strong> Partial</small>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application entry point"""
    
    # Render sidebar
    render_sidebar()
    
    # Main header
    st.markdown(f"""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 36px;">🥤 Coca-Cola Sales Executive Intelligence Platform</h1>
        <p style="margin: 10px 0; font-size: 18px; opacity: 0.9;">
            Proactive Sales Management • AI-Powered Insights • Pipeline Optimization
        </p>
        <p style="margin: 0; font-size: 14px; opacity: 0.8;">
            Powered by Azure OpenAI & Semantic Kernel | Last Updated: {st.session_state.get('last_update', 'Just now')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Content rendering based on sidebar selection
    selected_tab = st.session_state.get('selected_tab', '📈 Executive Overview')
    
    # Current view indicator
    st.markdown(f"""
    <div style="
        background: linear-gradient(90deg, {COKE_COLORS['primary_red']}20, {COKE_COLORS['coke_black']}10);
        padding: 8px 16px;
        border-radius: 8px;
        border-left: 4px solid {COKE_COLORS['primary_red']};
        margin: 10px 0;
    ">
        <strong>📍 Current View:</strong> {selected_tab}
    </div>
    """, unsafe_allow_html=True)
    
    # Render selected tab content
    if selected_tab == "📈 Executive Overview":
        if TABS_AVAILABLE:
            render_executive_overview()
        else:
            st.error("⚠️ Executive Overview module not available")
            
    elif selected_tab == "📊 Account Portfolio":
        if TABS_AVAILABLE:
            render_account_portfolio()
        else:
            st.error("⚠️ Account Portfolio module not available")
            
    elif selected_tab == "💰 Revenue Opportunities":
        if TABS_AVAILABLE:
            render_revenue_opportunities()
        else:
            st.error("⚠️ Revenue Opportunities module not available")
            
    elif selected_tab == "🤖 AI Recommendations":
        if TABS_AVAILABLE:
            render_ai_recommendations()
        else:
            st.error("⚠️ AI Recommendations module not available")
            
    elif selected_tab == "📋 Proactive Playbook":
        if TABS_AVAILABLE:
            render_proactive_playbook()
        else:
            st.error("⚠️ Proactive Playbook module not available")
    
    elif selected_tab == "💡 Proactive Insights":
        if TABS_AVAILABLE:
            render_proactive_insights()
        else:
            st.error("⚠️ Proactive Insights module not available")
    
    elif selected_tab == "🎯 Customer 360":
        st.markdown("# 🎯 Customer 360")
        st.markdown("*Complete customer profiles with engagement history and AI insights*")
        st.info("� This advanced feature is under development. Coming soon!")
        
        st.markdown("### 🎯 Planned Capabilities")
        st.markdown("""
        - Complete customer timeline and interaction history
        - Predictive customer health scoring
        - Personalized engagement recommendations
        - Product usage analytics and optimization
        """)
    
    elif selected_tab == "🗺️ Regional Performance":
        st.markdown("# 🗺️ Regional Performance")
        st.markdown("*Interactive maps, regional trends, and territory optimization*")
        st.info("🚧 This advanced feature is under development. Coming soon!")
        
        st.markdown("### 🎯 Planned Capabilities")
        st.markdown("""
        - Interactive geographic performance heatmaps
        - Territory optimization recommendations
        - Regional trend analysis and forecasting
        - Competitive landscape mapping
        """)
    
    elif selected_tab == "🏆 Gamification":
        st.markdown("# 🏆 Gamification")
        st.markdown("*Leaderboards, achievements, sales challenges, and team competitions*")
        st.info("🚧 This advanced feature is under development. Coming soon!")
        
        st.markdown("### 🎯 Planned Capabilities")
        st.markdown("""
        - Sales rep leaderboards and rankings
        - Achievement badges and milestone tracking
        - Team challenges and competitions
        - Performance rewards and recognition
        """)
    
    elif selected_tab == "🤝 Collaboration":
        st.markdown("# 🤝 Collaboration")
        st.markdown("*Shared notes, task assignments, team dashboards, and communication*")
        st.info("🚧 This advanced feature is under development. Coming soon!")
        
        st.markdown("### 🎯 Planned Capabilities")
        st.markdown("""
        - Shared account notes and updates
        - Task assignment and tracking
        - Team communication and messaging
        - Collaborative pipeline management
        """)
    
    elif selected_tab == "📊 Data Insights":
        st.markdown("# 📊 Data Insights")
        st.markdown("*Product trends, customer segmentation, and competitive analysis*")
        st.info("🚧 This advanced feature is under development. Coming soon!")
        
        st.markdown("### 🎯 Planned Capabilities")
        st.markdown("""
        - Advanced product performance analytics
        - Customer segmentation and targeting
        - Competitive intelligence and benchmarking
        - Market trend analysis and predictions
        """)
    
    elif selected_tab == "🏗️ Architecture":
        st.markdown("# 🏗️ Architecture")
        st.markdown("*System architecture diagrams and technical documentation*")
        st.info("🏗️ Architecture diagrams available in the original dashboard. This will be enhanced soon!")

if __name__ == "__main__":
    main()
