"""
Simple Coca-Cola Sales Dashboard - Working Version
"""
import streamlit as st
import datetime
import random

# Configure Streamlit page
st.set_page_config(
    page_title="Coca-Cola Sales Dashboard",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🥤 Coca-Cola Sales AI Platform")
    st.markdown("### Sales Executive Intelligence Dashboard")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")
    
    # Core Features
    st.sidebar.subheader("🎯 Core Business Features")
    
    feature_options = [
        "Executive Overview",
        "Account Portfolio", 
        "Revenue Opportunities",
        "AI Recommendations",
        "Regional Performance",
        "Customer 360",
        "Sales Analytics"
    ]
    
    selected_feature = st.sidebar.selectbox("Select feature:", feature_options)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        
        if selected_feature == "Executive Overview":
            render_executive_overview()
        elif selected_feature == "Account Portfolio":
            render_account_portfolio()
        elif selected_feature == "Revenue Opportunities":
            render_revenue_opportunities()
        elif selected_feature == "AI Recommendations":
            render_ai_recommendations()
        elif selected_feature == "Regional Performance":
            render_regional_performance()
        elif selected_feature == "Customer 360":
            render_customer_360()
        elif selected_feature == "Sales Analytics":
            render_sales_analytics()

def render_executive_overview():
    st.subheader("📊 Executive Overview")
    
    # KPI metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Revenue", "$2.4M", "12.5%")
    
    with col2:
        st.metric("Active Accounts", "156", "8")
    
    with col3:
        st.metric("Pipeline Value", "$890K", "15.2%")
    
    with col4:
        st.metric("Win Rate", "68%", "4.3%")
    
    st.markdown("---")
    
    # Sample chart data
    import random
    chart_data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Revenue': [random.randint(300000, 500000) for _ in range(6)]
    }
    
    st.subheader("📈 Revenue Trend")
    st.bar_chart(chart_data)
    
    st.markdown("### 🎯 Key Insights")
    st.success("✅ Q2 performance exceeded targets by 12.5%")
    st.info("ℹ️ New customer acquisition up 25% this quarter")
    st.warning("⚠️ Monitor competitive pressure in Northeast region")

def render_account_portfolio():
    st.subheader("🏢 Account Portfolio")
    
    st.markdown("### Top Performing Accounts")
    
    accounts_data = [
        {"Account": "Walmart", "Revenue": "$450K", "Growth": "15%", "Status": "🟢 Active"},
        {"Account": "Target", "Revenue": "$320K", "Growth": "8%", "Status": "🟢 Active"},
        {"Account": "Kroger", "Revenue": "$280K", "Growth": "22%", "Status": "🟢 Active"},
        {"Account": "Costco", "Revenue": "$195K", "Growth": "-3%", "Status": "🟡 At Risk"},
        {"Account": "Amazon Fresh", "Revenue": "$165K", "Growth": "45%", "Status": "🟢 Active"}
    ]
    
    for account in accounts_data:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f"**{account['Account']}**")
        with col2:
            st.write(account['Revenue'])
        with col3:
            st.write(account['Growth'])
        with col4:
            st.write(account['Status'])

def render_revenue_opportunities():
    st.subheader("💰 Revenue Opportunities")
    
    st.markdown("### Pipeline Analysis")
    
    opportunities = [
        {"Opportunity": "Walmart Q4 Expansion", "Value": "$120K", "Probability": "85%", "Close Date": "Dec 2025"},
        {"Opportunity": "Target New Store Rollout", "Value": "$95K", "Probability": "70%", "Close Date": "Jan 2026"},
        {"Opportunity": "Kroger Premium Product Line", "Value": "$75K", "Probability": "60%", "Close Date": "Feb 2026"},
        {"Opportunity": "Costco Holiday Campaign", "Value": "$180K", "Probability": "90%", "Close Date": "Nov 2025"}
    ]
    
    for opp in opportunities:
        with st.expander(f"{opp['Opportunity']} - {opp['Value']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Probability:** {opp['Probability']}")
            with col2:
                st.write(f"**Expected Close:** {opp['Close Date']}")

def render_ai_recommendations():
    st.subheader("🤖 AI Recommendations")
    
    st.markdown("### Proactive Sales Insights")
    
    recommendations = [
        {
            "title": "Cross-sell Opportunity at Walmart",
            "description": "Data shows 23% increase in Diet Coke sales. Recommend positioning Coke Zero as complementary offering.",
            "priority": "🔴 High",
            "action": "Schedule meeting with Walmart buyer team"
        },
        {
            "title": "Seasonal Campaign for Target",
            "description": "Historical data indicates 40% sales uplift during holiday seasons. Propose limited edition packaging.",
            "priority": "🟡 Medium", 
            "action": "Prepare campaign proposal"
        },
        {
            "title": "Inventory Optimization at Kroger",
            "description": "Predictive analytics suggest stock-out risk for Classic Coke in 2 weeks.",
            "priority": "🔴 High",
            "action": "Increase delivery frequency"
        }
    ]
    
    for rec in recommendations:
        with st.container():
            st.markdown(f"**{rec['title']}** {rec['priority']}")
            st.write(rec['description'])
            st.info(f"💡 **Recommended Action:** {rec['action']}")
            st.markdown("---")

def render_regional_performance():
    st.subheader("🗺️ Regional Performance")
    
    regions = [
        {"Region": "Northeast", "Revenue": "$650K", "Growth": "12%", "Accounts": 45},
        {"Region": "Southeast", "Revenue": "$580K", "Growth": "18%", "Accounts": 38},
        {"Region": "Midwest", "Revenue": "$420K", "Growth": "8%", "Accounts": 32},
        {"Region": "West", "Revenue": "$750K", "Growth": "22%", "Accounts": 41}
    ]
    
    for region in regions:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Region", region['Region'])
        with col2:
            st.metric("Revenue", region['Revenue'])
        with col3:
            st.metric("Growth", region['Growth'])
        with col4:
            st.metric("Accounts", region['Accounts'])

def render_customer_360():
    st.subheader("👥 Customer 360 View")
    
    st.markdown("### Customer Profile: Walmart")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Account Details**")
        st.write("• **Industry:** Retail")
        st.write("• **Size:** Enterprise")
        st.write("• **Relationship:** 8 years")
        st.write("• **Primary Contact:** Sarah Johnson")
        st.write("• **Account Manager:** Mike Rodriguez")
    
    with col2:
        st.markdown("**Performance Metrics**")
        st.write("• **YTD Revenue:** $450,000")
        st.write("• **Growth Rate:** 15%")
        st.write("• **Order Frequency:** Bi-weekly")
        st.write("• **Payment Terms:** Net 30")
        st.write("• **Credit Rating:** A+")

def render_sales_analytics():
    st.subheader("📊 Sales Analytics")
    
    st.markdown("### Performance Dashboard")
    
    # Simple analytics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Product Performance**")
        products = ['Coca-Cola Classic', 'Diet Coke', 'Coke Zero', 'Sprite', 'Fanta']
        performance = [45, 25, 15, 10, 5]
        
        product_data = dict(zip(products, performance))
        st.bar_chart(product_data)
    
    with col2:
        st.markdown("**Sales by Channel**")
        channels = ['Retail', 'Food Service', 'Vending', 'Online']
        channel_performance = [60, 25, 10, 5]
        
        channel_data = dict(zip(channels, channel_performance))
        st.bar_chart(channel_data)

if __name__ == "__main__":
    main()
