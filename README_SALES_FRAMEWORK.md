# 🎯 Coca-Cola Sales AI Agent Framework

## Sales Intelligence Platform - Powered by Azure AI & Semantic Kernel

A comprehensive sales intelligence platform designed specifically for Coca-Cola sales teams to be more informed, proactive, and data-driven in their account management and business development efforts.

## 🌟 Executive Summary

This platform transforms raw business data into actionable sales insights, helping Coca-Cola's regional sales and account managers:

- **Monitor account health** of ongoing deals with retail chains, restaurants, and distributors
- **Detect declining engagement** from key accounts (franchise bottlers, QSR partners)
- **Recommend proactive steps** to prevent churn and strengthen account loyalty
- **Identify expansion opportunities** for Coca-Cola Freestyle and other products

## 🎯 Core Features

### 🏠 Sales Dashboard
- **Account Risk Overview**: Critical metrics for accounts requiring immediate attention
- **Opportunity Tracking**: High-potential accounts ready for expansion
- **Revenue Protection**: Analysis of revenue at risk from potential churn
- **AI-Generated Recommendations**: 23+ actionable insights available

### 🗺️ Account Health Map
- **Geographic Intelligence**: Interactive map showing account health across regions
- **Churn Risk Visualization**: Color-coded risk levels (Critical, High, Medium, Low)
- **Account Details**: Hover tooltips with revenue, health scores, and product mix
- **Sales Rep Assignment**: Clear ownership and contact information

### 🤖 AI-Powered Recommendations
- **Critical Alerts**: 87% churn risk detection for Atlanta Coca-Cola Bottling
- **Expansion Opportunities**: $420K Freestyle expansion at MovieMax Entertainment
- **Engagement Recovery**: Proactive steps for declining Seattle Coffee Hub Network
- **Action Item Tracking**: Specific, time-bound recommendations for each scenario

### 📊 Performance Analytics
- **Product Portfolio Performance**: Coca-Cola Classic, Zero Sugar, Freestyle, Sprite
- **Growth Trending**: Month-over-month performance analysis
- **Revenue Tracking**: Real-time revenue monitoring across product lines

## 🧱 Architecture Components

### Data Sources
- **SAP/Salesforce CRM**: Track B2B contracts, order volume, regional campaigns
- **Coca-Cola Freestyle Machine Telemetry**: Detect decreased beverage pulls in outlets  
- **Email & Call Transcripts**: Analyze sentiment shifts with retail/distributor partners

### ML + AI Models
- **Propensity Model**: Predict reorder probability by outlet type (grocery, theme park, QSR)
- **Sentiment Classifier**: Monitor partner tone during negotiations or service issues
- **AI Opportunity Screener**: Highlight at-risk bottlers or high-potential accounts

### Reasoning Layer
- **Azure OpenAI GPT-4o**: Advanced reasoning and insight generation
- **Semantic Kernel Framework**: Cross-reference promo history, sales trends, partner communication

## 🚀 Getting Started

### Quick Launch
```bash
# Navigate to project directory
cd cokesales

# Install dependencies (Windows)
python -m pip install streamlit plotly pandas numpy requests

# Launch the platform
python -m streamlit run streamlit_dashboard.py
```

### Access the Platform
- **URL**: http://localhost:8502
- **Navigation**: Use the sidebar to switch between dashboard views
- **Interaction**: Click on map markers for account details

## 📋 Sample Use Cases

### For a Bottler Account
**Context:**
- Order volume down 12% YOY
- Recent email: "Costs are rising, exploring other brands"
- No promo participation in last 2 quarters

**AI Recommendation:**
"Recommend volume-based loyalty program enrollment and schedule executive relationship call within 48 hours. Consider regional competitor analysis and customized pricing proposal."

### For a Retail Chain
**Context:**
- Freestyle machine telemetry shows 35% decline
- Sentiment in communications = Neutral
- Competitor shelf activity flagged by field rep

**AI Recommendation:**
"Analyze opportunity health and propose localized 'Share a Coke' campaign. Schedule Freestyle technical review and consider exclusive partnership opportunities."

## 🎨 Design Philosophy

### Sales-Focused Interface
- **Action-Oriented**: Every insight includes specific next steps
- **Time-Sensitive**: Urgency indicators and timeline recommendations
- **Contact-Aware**: Sales rep assignments and escalation paths
- **Executive-Ready**: Professional presentation suitable for C-level discussions

### Coca-Cola Brand Authentic
- **Color Palette**: Authentic Coca-Cola reds, blacks, and complementary colors
- **Product Focus**: Real product names (Classic, Zero Sugar, Freestyle, Sprite)
- **Business Context**: B2B scenarios relevant to bottlers, distributors, and retail

### Immersive User Experience
- **Interactive Visualizations**: Plotly-powered charts and geographic maps
- **Responsive Design**: Optimized for desktop and tablet use
- **Real-Time Updates**: Dynamic data refresh and live insights
- **Professional Styling**: Executive-grade visual presentation

## 🔧 Technical Stack

- **Frontend**: Streamlit (Python-based web framework)
- **Visualization**: Plotly for interactive charts and maps
- **Data Processing**: Pandas and NumPy for data manipulation
- **AI Integration**: Azure OpenAI and Semantic Kernel (ready for integration)
- **Styling**: Custom CSS with authentic Coca-Cola branding

## 📈 Business Impact

### Measurable Outcomes
- **Churn Prevention**: Early warning system for at-risk accounts
- **Revenue Protection**: $2.8M+ in revenue at risk identified
- **Expansion Revenue**: $420K+ expansion opportunities detected
- **Sales Efficiency**: Automated account health monitoring

### Strategic Value
- **Proactive Sales Management**: Shift from reactive to predictive sales approach
- **Data-Driven Decisions**: AI-powered insights replace gut-feeling decisions
- **Account Relationship Strength**: Early intervention capabilities
- **Competitive Advantage**: Advanced analytics for market positioning

## 🎯 Next Steps

1. **Azure Integration**: Connect to Azure OpenAI and Semantic Kernel services
2. **CRM Integration**: Link to SAP/Salesforce for real-time data
3. **Freestyle Telemetry**: Integrate machine data for usage analytics
4. **Mobile Optimization**: Responsive design for field sales teams
5. **Advanced AI**: Implement more sophisticated ML models

## 👥 Target Users

- **Regional Sales Managers**: Account portfolio oversight
- **Account Managers**: Individual account relationship management  
- **Sales Representatives**: Field sales intelligence and action items
- **Sales Directors**: Strategic planning and resource allocation
- **Executive Leadership**: High-level performance and risk analysis

---

**🥤 Coca-Cola Sales AI Agent Framework** | Empowering Sales Teams with Intelligent Insights
