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

# Add components to path
current_dir = os.path.dirname(__file__)
components_dir = os.path.join(current_dir, 'components')
sys.path.append(components_dir)

# Import tab modules
TABS_AVAILABLE = {}

try:
    from components.tabs.executive_overview import render_executive_overview
    TABS_AVAILABLE['executive_overview'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import executive_overview: {e}")
    TABS_AVAILABLE['executive_overview'] = False

try:
    from components.tabs.account_portfolio import render_account_portfolio
    TABS_AVAILABLE['account_portfolio'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import account_portfolio: {e}")
    TABS_AVAILABLE['account_portfolio'] = False

try:
    from components.tabs.revenue_opportunities import render_revenue_opportunities
    TABS_AVAILABLE['revenue_opportunities'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import revenue_opportunities: {e}")
    TABS_AVAILABLE['revenue_opportunities'] = False

try:
    from components.tabs.ai_recommendations import render_ai_recommendations
    TABS_AVAILABLE['ai_recommendations'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import ai_recommendations: {e}")
    TABS_AVAILABLE['ai_recommendations'] = False

try:
    from components.tabs.proactive_playbook import render_proactive_playbook
    TABS_AVAILABLE['proactive_playbook'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import proactive_playbook: {e}")
    TABS_AVAILABLE['proactive_playbook'] = False

try:
    from components.tabs.proactive_insights import render_proactive_insights
    TABS_AVAILABLE['proactive_insights'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import proactive_insights: {e}")
    TABS_AVAILABLE['proactive_insights'] = False

try:
    from components.tabs.customer_360 import render_customer_360
    TABS_AVAILABLE['customer_360'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import customer_360: {e}")
    TABS_AVAILABLE['customer_360'] = False

try:
    from components.tabs.regional_performance import render_regional_performance
    TABS_AVAILABLE['regional_performance'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import regional_performance: {e}")
    TABS_AVAILABLE['regional_performance'] = False

try:
    from components.tabs.gamification import render_gamification
    TABS_AVAILABLE['gamification'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import gamification: {e}")
    TABS_AVAILABLE['gamification'] = False

try:
    from components.tabs.collaboration import render_collaboration
    TABS_AVAILABLE['collaboration'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import collaboration: {e}")
    TABS_AVAILABLE['collaboration'] = False

try:
    from components.tabs.data_insights import render_data_insights
    TABS_AVAILABLE['data_insights'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import data_insights: {e}")
    TABS_AVAILABLE['data_insights'] = False

try:
    from components.tabs.architecture import render_architecture
    TABS_AVAILABLE['architecture'] = True
except ImportError as e:
    st.error(f"⚠️ Could not import architecture: {e}")
    TABS_AVAILABLE['architecture'] = False

# Coca-Cola Brand Styling
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000',
    'classic_white': '#FFFFFF',
    'executive_blue': '#0078D4',
    'coke_gold': '#FFC72C',
    'success_green': '#28a745',
    'warning_orange': '#ffc107',
    'light_gray': '#f8f9fa',
    'dark_gray': '#6c757d'
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
        
        # Initialize session state
        if 'selected_tab' not in st.session_state:
            st.session_state.selected_tab = "📈 Executive Overview"
        if 'tab_section' not in st.session_state:
            st.session_state.tab_section = "core"
        
        # Section toggle buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎯 Core Features", 
                        use_container_width=True, 
                        type="primary" if st.session_state.tab_section == "core" else "secondary",
                        help="Essential business functions"):
                st.session_state.tab_section = "core"
                if st.session_state.selected_tab not in tab_options[:4]:
                    st.session_state.selected_tab = "📈 Executive Overview"
                st.rerun()
        
        with col2:
            if st.button("🚀 Advanced AI", 
                        use_container_width=True, 
                        type="primary" if st.session_state.tab_section == "advanced" else "secondary",
                        help="AI-powered features"):
                st.session_state.tab_section = "advanced"
                if st.session_state.selected_tab not in tab_options[4:]:
                    st.session_state.selected_tab = "📋 Proactive Playbook"
                st.rerun()
        
        st.markdown("---")
        
        # Render appropriate navigation based on current section
        if st.session_state.tab_section == "core":
            st.markdown("**🎯 Core Business Features**")
            core_options = tab_options[:4]
            
            # Find current index for core features
            current_index = 0
            if st.session_state.selected_tab in core_options:
                current_index = core_options.index(st.session_state.selected_tab)
            
            selected_core = st.radio(
                "Select feature:",
                options=core_options,
                index=current_index,
                key="core_tab_radio",
                help="Essential features for daily sales operations"
            )
            
            # Update selected tab when core feature is chosen
            if selected_core != st.session_state.selected_tab:
                st.session_state.selected_tab = selected_core
                st.rerun()
        
        else:  # advanced section
            st.markdown("**🚀 Advanced AI Features**")
            advanced_options = tab_options[4:]
            
            # Find current index for advanced features
            current_index = 0
            if st.session_state.selected_tab in advanced_options:
                current_index = advanced_options.index(st.session_state.selected_tab)
            
            selected_advanced = st.radio(
                "Select AI feature:",
                options=advanced_options,
                index=current_index,
                key="advanced_tab_radio",
                help="AI-powered insights and automation"
            )
            
            # Update selected tab when advanced feature is chosen
            if selected_advanced != st.session_state.selected_tab:
                st.session_state.selected_tab = selected_advanced
                st.rerun()
        
        st.divider()
        
        # Current Section Indicator
        current_section = "Core Features" if st.session_state.tab_section == "core" else "Advanced AI Features"
        section_color = COKE_COLORS['primary_red'] if st.session_state.tab_section == "core" else COKE_COLORS['coke_gold']
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(90deg, {section_color}20, {section_color}10);
            padding: 8px 12px;
            border-radius: 6px;
            border-left: 3px solid {section_color};
            margin: 8px 0;
            text-align: center;
        ">
            <small><strong>📍 Current Section:</strong> {current_section}</small><br>
            <small style="opacity: 0.8;"><strong>Active:</strong> {st.session_state.selected_tab}</small>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Section Switch
        st.markdown("**⚡ Quick Switch**")
        switch_col1, switch_col2 = st.columns(2)
        
        with switch_col1:
            if st.button("📈 Dashboard", use_container_width=True, help="Go to Executive Overview"):
                st.session_state.tab_section = "core"
                st.session_state.selected_tab = "📈 Executive Overview"
                st.rerun()
        
        with switch_col2:
            if st.button("🤖 AI Hub", use_container_width=True, help="Go to AI Recommendations"):
                st.session_state.tab_section = "core"
                st.session_state.selected_tab = "🤖 AI Recommendations"
                st.rerun()
        
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
        
        # Smart navigation buttons based on current location
        if st.session_state.tab_section == "core":
            if st.button("🎯 Go to Opportunities", use_container_width=True, key="go_to_opps_btn"):
                st.session_state.selected_tab = "💰 Revenue Opportunities"
                st.rerun()
                
            if st.button("🚀 Try Advanced AI", use_container_width=True, key="try_advanced_btn"):
                st.session_state.tab_section = "advanced"
                st.session_state.selected_tab = "📋 Proactive Playbook"
                st.rerun()
        else:
            if st.button("🏠 Back to Core", use_container_width=True, key="back_to_core_btn"):
                st.session_state.tab_section = "core"
                st.session_state.selected_tab = "📈 Executive Overview"
                st.rerun()
                
            if st.button("🤖 Ask AI Assistant", use_container_width=True, key="ask_ai_btn"):
                st.session_state.selected_tab = "🤖 AI Recommendations"
                st.session_state.tab_section = "core"
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
        
        # Navigation Help
        with st.expander("ℹ️ Navigation Help"):
            st.markdown("""
            **🧭 How to Navigate:**
            
            **Section Switching:**
            - **🎯 Core Features** - Essential business functions (radio buttons)
            - **🚀 Advanced AI** - AI-powered features (radio buttons)
            - Toggle between sections using the buttons at the top
            
            **Quick Navigation:**
            - **📈 Dashboard** - Jump to Executive Overview
            - **🤖 AI Hub** - Jump to AI Recommendations
            - **🏠 Back to Core** - Return from advanced features
            - **🚀 Try Advanced AI** - Explore new AI features
            
            **Current Status:**
            - View your current section and active tab in the status box
            - Smart action buttons change based on your location
            
            **🎯 Core Features (Always Available):**
            - 📈 Executive Overview - KPIs and strategic insights
            - 📊 Account Portfolio - Customer relationship management
            - 💰 Revenue Opportunities - Sales pipeline and deals
            - 🤖 AI Recommendations - AI-powered sales insights
            
            **🚀 Advanced AI Features (New):**
            - 📋 Proactive Playbook - AI-generated action plans
            - 💡 Proactive Insights - Real-time alerts and predictions
            - 🎯 Customer 360 - Complete customer intelligence
            - 🗺️ Regional Performance - Geographic analytics
            - 🏆 Gamification - Performance tracking and rewards
            - 🤝 Collaboration - Team communication and workflows
            - 📊 Data Insights - Advanced analytics and BI
            - 🏗️ Architecture - System diagrams and documentation
            
            **💡 Tips:**
            - Use Quick Switch buttons for instant navigation
            - The current section indicator shows where you are
            - Action buttons adapt to your current location
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
    
    # Initialize session state safely
    if 'selected_tab' not in st.session_state:
        st.session_state.selected_tab = "📈 Executive Overview"
    if 'tab_section' not in st.session_state:
        st.session_state.tab_section = "core"
    if 'last_update' not in st.session_state:
        st.session_state.last_update = "Just now"
    
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
    
    # Current view indicator with enhanced styling
    current_section = "Core Features" if st.session_state.get('tab_section', 'core') == "core" else "Advanced AI Features"
    section_emoji = "🎯" if st.session_state.get('tab_section', 'core') == "core" else "🚀"
    section_color = COKE_COLORS['primary_red'] if st.session_state.get('tab_section', 'core') == "core" else COKE_COLORS['coke_gold']
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(90deg, {section_color}15, {section_color}05);
        padding: 12px 20px;
        border-radius: 10px;
        border-left: 5px solid {section_color};
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    ">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <strong style="color: {COKE_COLORS['coke_black']}; font-size: 16px;">
                    {section_emoji} {current_section}
                </strong>
                <div style="color: {COKE_COLORS['dark_gray']}; font-size: 14px; margin-top: 2px;">
                    📍 Active: {selected_tab}
                </div>
            </div>
            <div style="text-align: right;">
                <div style="
                    background: {section_color};
                    color: white;
                    padding: 4px 8px;
                    border-radius: 12px;
                    font-size: 11px;
                    font-weight: bold;
                ">
                    {current_section.split()[0]}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Render selected tab content
    if selected_tab == "📈 Executive Overview":
        if TABS_AVAILABLE.get('executive_overview', False):
            render_executive_overview()
        else:
            st.error("⚠️ Executive Overview module not available")
            
    elif selected_tab == "📊 Account Portfolio":
        if TABS_AVAILABLE.get('account_portfolio', False):
            render_account_portfolio()
        else:
            st.error("⚠️ Account Portfolio module not available")
            
    elif selected_tab == "💰 Revenue Opportunities":
        if TABS_AVAILABLE.get('revenue_opportunities', False):
            render_revenue_opportunities()
        else:
            st.error("⚠️ Revenue Opportunities module not available")
            
    elif selected_tab == "🤖 AI Recommendations":
        if TABS_AVAILABLE.get('ai_recommendations', False):
            render_ai_recommendations()
        else:
            st.error("⚠️ AI Recommendations module not available")
            
    elif selected_tab == "📋 Proactive Playbook":
        if TABS_AVAILABLE.get('proactive_playbook', False):
            render_proactive_playbook()
        else:
            st.error("⚠️ Proactive Playbook module not available")
            
    elif selected_tab == "💡 Proactive Insights":
        if TABS_AVAILABLE.get('proactive_insights', False):
            render_proactive_insights()
        else:
            st.error("⚠️ Proactive Insights module not available")
    
    elif selected_tab == "🎯 Customer 360":
        if TABS_AVAILABLE.get('customer_360', False):
            render_customer_360()
        else:
            st.error("⚠️ Customer 360 module not available")
    
    elif selected_tab == "🗺️ Regional Performance":
        if TABS_AVAILABLE.get('regional_performance', False):
            render_regional_performance()
        else:
            st.error("⚠️ Regional Performance module not available")
    
    elif selected_tab == "🏆 Gamification":
        if TABS_AVAILABLE.get('gamification', False):
            render_gamification()
        else:
            st.error("⚠️ Gamification module not available")
    
    elif selected_tab == "🤝 Collaboration":
        if TABS_AVAILABLE.get('collaboration', False):
            render_collaboration()
        else:
            st.error("⚠️ Collaboration module not available")
    
    elif selected_tab == "📊 Data Insights":
        if TABS_AVAILABLE.get('data_insights', False):
            render_data_insights()
        else:
            st.error("⚠️ Data Insights module not available")
    
    elif selected_tab == "🏗️ Architecture":
        if TABS_AVAILABLE.get('architecture', False):
            render_architecture()
        else:
            st.error("⚠️ Architecture module not available")

if __name__ == "__main__":
    main()
