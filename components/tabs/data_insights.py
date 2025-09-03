"""
Data Insights Tab - Advanced Analytics, Market Intelligence, and Predictive Modeling
AI-powered data insights with GPT-4o driven analytics and business intelligence
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
import seaborn as sns
import matplotlib.pyplot as plt

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

def generate_market_intelligence():
    """Generate comprehensive market intelligence data"""
    return {
        "market_size": {
            "total_market": "$280B",
            "addressable_market": "$45B",
            "growth_rate": "3.2%",
            "coca_cola_share": "21.8%",
            "trends": [
                "Health-conscious consumption driving zero-sugar growth (+12%)",
                "Freestyle technology adoption accelerating (+34% QoQ)",
                "Sustainability concerns influencing purchase decisions (67% of consumers)",
                "Premium product segments outperforming (+8% vs standard)"
            ]
        },
        "competitive_landscape": {
            "market_leaders": {
                "coca_cola": {"share": 21.8, "change": "+0.3%"},
                "pepsi": {"share": 8.4, "change": "-0.1%"},
                "dr_pepper": {"share": 7.1, "change": "+0.2%"},
                "monster": {"share": 3.2, "change": "+0.8%"},
                "red_bull": {"share": 2.9, "change": "+0.4%"}
            },
            "emerging_threats": [
                "Local craft soda brands gaining regional traction",
                "Functional beverages (energy, health) expanding rapidly",
                "Private label expansion in grocery chains",
                "Plant-based and organic alternatives growing 15% YoY"
            ]
        },
        "consumer_insights": {
            "demographics": {
                "gen_z": {
                    "preference": "Zero-sugar and functional beverages",
                    "growth": "+18% engagement",
                    "influence": "Social media and sustainability focus"
                },
                "millennials": {
                    "preference": "Premium and craft options",
                    "growth": "+12% spending",
                    "influence": "Brand authenticity and experience"
                },
                "gen_x": {
                    "preference": "Classic flavors with health benefits",
                    "growth": "+5% loyalty",
                    "influence": "Convenience and family considerations"
                },
                "boomers": {
                    "preference": "Traditional products with familiar branding",
                    "growth": "+2% retention",
                    "influence": "Trust and consistency"
                }
            },
            "channels": {
                "convenience": {
                    "growth": "+8.3%",
                    "opportunity": "Freestyle machine expansion"
                },
                "foodservice": {
                    "growth": "+12.1%",
                    "opportunity": "Partnership with delivery platforms"
                },
                "retail": {
                    "growth": "+4.2%",
                    "opportunity": "Premium placement and displays"
                },
                "vending": {
                    "growth": "+6.7%",
                    "opportunity": "Smart vending technology adoption"
                }
            }
        }
    }

def generate_predictive_models():
    """Generate predictive analytics data"""
    return {
        "demand_forecasting": {
            "q4_prediction": {
                "coca_cola_classic": {"volume": "+3.2%", "confidence": "94%"},
                "coke_zero": {"volume": "+15.8%", "confidence": "89%"},
                "diet_coke": {"volume": "-2.1%", "confidence": "87%"},
                "sprite": {"volume": "+7.4%", "confidence": "91%"},
                "fanta": {"volume": "+4.6%", "confidence": "85%"}
            },
            "seasonal_patterns": {
                "summer_peak": "June-August +35% vs baseline",
                "holiday_surge": "November-December +22% vs baseline",
                "spring_growth": "March-May +18% vs baseline",
                "winter_stable": "January-February baseline performance"
            }
        },
        "customer_behavior": {
            "purchase_patterns": {
                "frequency": "Avg 2.3x per week",
                "basket_size": "Avg $12.50 per transaction",
                "loyalty_retention": "78% 12-month retention",
                "cross_sell_rate": "43% multi-product purchases"
            },
            "churn_indicators": [
                "Purchase frequency decline >30%",
                "Switch to competitor products",
                "Reduced promotional response",
                "Negative sentiment in social mentions"
            ]
        },
        "market_opportunities": {
            "expansion_markets": {
                "rural_penetration": {"potential": "$2.3B", "timeline": "18 months"},
                "college_campuses": {"potential": "$890M", "timeline": "12 months"},
                "healthcare_facilities": {"potential": "$1.2B", "timeline": "24 months"},
                "corporate_offices": {"potential": "$760M", "timeline": "15 months"}
            },
            "product_innovations": {
                "energy_variants": {"demand_score": 87, "launch_readiness": "Q2 2024"},
                "functional_additives": {"demand_score": 74, "launch_readiness": "Q4 2024"},
                "sustainability_packaging": {"demand_score": 92, "launch_readiness": "Q1 2024"},
                "local_flavor_variants": {"demand_score": 68, "launch_readiness": "Q3 2024"}
            }
        }
    }

def generate_advanced_analytics():
    """Generate advanced analytics insights"""
    return {
        "sentiment_analysis": {
            "overall_brand_sentiment": 0.78,
            "product_sentiment": {
                "coca_cola_classic": 0.82,
                "coke_zero": 0.85,
                "diet_coke": 0.71,
                "sprite": 0.79,
                "fanta": 0.75
            },
            "trending_topics": [
                "Sustainability initiatives (+0.12 sentiment)",
                "Freestyle technology (+0.18 sentiment)",
                "Zero sugar options (+0.15 sentiment)",
                "Local community support (+0.09 sentiment)"
            ]
        },
        "price_optimization": {
            "elasticity_analysis": {
                "premium_products": "Low elasticity (-0.3)",
                "core_products": "Moderate elasticity (-0.7)",
                "promotional_products": "High elasticity (-1.2)"
            },
            "optimization_opportunities": [
                "Increase premium pricing by 3-5% with minimal volume impact",
                "Bundle pricing strategies for multi-product purchases",
                "Dynamic pricing for vending and convenience channels",
                "Loyalty program pricing tiers for frequent purchasers"
            ]
        },
        "supply_chain": {
            "efficiency_metrics": {
                "delivery_performance": "96.2% on-time delivery",
                "inventory_turnover": "12.4x annual turnover",
                "cost_optimization": "8.3% reduction vs LY",
                "sustainability_score": "78/100 ESG rating"
            },
            "optimization_areas": [
                "Route optimization reducing delivery costs by 12%",
                "Predictive maintenance reducing downtime by 18%",
                "Sustainable packaging reducing costs by 6%",
                "Smart inventory management preventing 94% of stockouts"
            ]
        }
    }

def render_data_insights():
    """Render comprehensive data insights and analytics"""
    
    st.markdown("# 📊 Data Insights & Advanced Analytics")
    st.markdown("*AI-powered market intelligence, predictive modeling, and business analytics*")
    
    # Generate all data
    market_intel = generate_market_intelligence()
    predictive_models = generate_predictive_models()
    advanced_analytics = generate_advanced_analytics()
    
    # Create tabs for different insight categories
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌍 Market Intelligence", 
        "🔮 Predictive Analytics", 
        "🧠 Advanced Analytics",
        "📈 Performance Metrics"
    ])
    
    with tab1:
        st.markdown("### 🌍 Market Intelligence Dashboard")
        
        # Market size overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Market Size",
                market_intel["market_size"]["total_market"],
                market_intel["market_size"]["growth_rate"]
            )
        
        with col2:
            st.metric(
                "Addressable Market",
                market_intel["market_size"]["addressable_market"],
                "Opportunity"
            )
        
        with col3:
            st.metric(
                "Coca-Cola Share",
                market_intel["market_size"]["coca_cola_share"],
                "+0.3% vs LY"
            )
        
        with col4:
            st.metric(
                "Market Growth",
                market_intel["market_size"]["growth_rate"],
                "Annual"
            )
        
        st.markdown("---")
        
        # Competitive landscape
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🏆 Competitive Landscape")
            
            competitors = market_intel["competitive_landscape"]["market_leaders"]
            comp_df = pd.DataFrame([
                {"Brand": brand.replace("_", " ").title(), 
                 "Market Share": data["share"], 
                 "Change": data["change"]}
                for brand, data in competitors.items()
            ])
            
            fig = px.bar(
                comp_df,
                x="Brand",
                y="Market Share",
                color="Market Share",
                color_continuous_scale="Reds",
                title="Market Share by Brand"
            )
            fig.update_layout(height=300, font_color=COKE_COLORS['coke_black'])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### 📈 Market Trends")
            
            for trend in market_intel["market_size"]["trends"]:
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    border-left: 4px solid {COKE_COLORS['primary_red']};
                    padding: 10px;
                    margin: 8px 0;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <p style="margin: 0; color: {COKE_COLORS['coke_black']}; font-size: 14px; font-weight: 500;">{trend}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Consumer insights
        st.markdown("#### 👥 Consumer Demographics & Insights")
        
        demo_col1, demo_col2 = st.columns(2)
        
        with demo_col1:
            st.markdown("**Demographic Preferences**")
            for demo, data in market_intel["consumer_insights"]["demographics"].items():
                growth_color = COKE_COLORS['success_green'] if '+' in data['growth'] else COKE_COLORS['primary_red']
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']}; 
                    border: 2px solid {COKE_COLORS['light_gray']}; 
                    padding: 15px; 
                    margin: 8px 0; 
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h4 style="margin: 0 0 10px 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{demo.replace('_', ' ').title()}</h4>
                    <p style="margin: 5px 0; color: {COKE_COLORS['dark_gray']}; font-size: 14px;"><strong>Preference:</strong> {data['preference']}</p>
                    <p style="margin: 5px 0; color: {growth_color}; font-size: 14px; font-weight: 600;"><strong>Growth:</strong> {data['growth']}</p>
                    <p style="margin: 5px 0; color: {COKE_COLORS['dark_gray']}; font-size: 14px;"><strong>Influence:</strong> {data['influence']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with demo_col2:
            st.markdown("**Channel Performance**")
            for channel, data in market_intel["consumer_insights"]["channels"].items():
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']}; 
                    border: 2px solid {COKE_COLORS['light_gray']}; 
                    padding: 15px; 
                    margin: 8px 0; 
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h4 style="margin: 0 0 10px 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{channel.upper()}</h4>
                    <p style="margin: 5px 0; color: {COKE_COLORS['success_green']}; font-size: 14px; font-weight: 600;"><strong>Growth:</strong> {data['growth']}</p>
                    <p style="margin: 5px 0; color: {COKE_COLORS['dark_gray']}; font-size: 14px;"><strong>Opportunity:</strong> {data['opportunity']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🔮 Predictive Analytics Center")
        
        # Demand forecasting
        st.markdown("#### 📈 Demand Forecasting")
        
        forecast_data = predictive_models["demand_forecasting"]["q4_prediction"]
        
        products = list(forecast_data.keys())
        volumes = [forecast_data[prod]["volume"] for prod in products]
        confidences = [forecast_data[prod]["confidence"] for prod in products]
        
        # Forecast visualization
        fig_forecast = go.Figure()
        
        # Convert volume percentages to numeric for visualization
        volume_nums = [float(vol.replace("%", "").replace("+", "")) for vol in volumes]
        
        fig_forecast.add_trace(go.Bar(
            x=[prod.replace("_", " ").title() for prod in products],
            y=volume_nums,
            marker_color=[COKE_COLORS['success_green'] if vol > 0 else COKE_COLORS['primary_red'] for vol in volume_nums],
            text=volumes,
            textposition='auto',
        ))
        
        fig_forecast.update_layout(
            title="Q4 Volume Forecast by Product",
            yaxis_title="Forecast Change (%)",
            height=300,
            font_color=COKE_COLORS['coke_black']
        )
        
        st.plotly_chart(fig_forecast, use_container_width=True)
        
        # Market opportunities
        st.markdown("#### 🎯 Market Expansion Opportunities")
        
        opportunities = predictive_models["market_opportunities"]["expansion_markets"]
        
        opp_col1, opp_col2 = st.columns(2)
        
        with opp_col1:
            for market, data in opportunities.items():
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 15px;
                    border-radius: 8px;
                    margin: 10px 0;
                    border-left: 4px solid {COKE_COLORS['info_blue']};
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{market.replace('_', ' ').title()}</h5>
                    <p style="margin: 5px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;"><strong>Potential:</strong> {data['potential']}</p>
                    <p style="margin: 0; color: {COKE_COLORS['dark_gray']}; font-size: 12px;"><strong>Timeline:</strong> {data['timeline']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with opp_col2:
            # Customer behavior insights
            st.markdown("**Customer Behavior Patterns**")
            
            behavior = predictive_models["customer_behavior"]["purchase_patterns"]
            
            for metric, value in behavior.items():
                st.markdown(f"""
                <div style="
                    background: linear-gradient(90deg, {COKE_COLORS['light_gray']}, {COKE_COLORS['classic_white']});
                    padding: 10px;
                    border-radius: 8px;
                    margin: 5px 0;
                    border: 1px solid {COKE_COLORS['light_gray']};
                ">
                    <strong style="color: {COKE_COLORS['coke_black']};">{metric.replace('_', ' ').title()}:</strong>
                    <span style="color: {COKE_COLORS['primary_red']}; font-weight: 600;"> {value}</span>
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🧠 Advanced Analytics & AI Insights")
        
        # Sentiment analysis
        st.markdown("#### 💭 Brand Sentiment Analysis")
        
        sentiment_data = advanced_analytics["sentiment_analysis"]
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            overall_sentiment = sentiment_data["overall_brand_sentiment"]
            sentiment_color = COKE_COLORS['success_green'] if overall_sentiment > 0.7 else COKE_COLORS['warning_orange'] if overall_sentiment > 0.5 else COKE_COLORS['primary_red']
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                border: 3px solid {sentiment_color};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            ">
                <h2 style="margin: 0; color: {sentiment_color}; font-size: 48px;">{overall_sentiment:.2f}</h2>
                <p style="margin: 5px 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">Overall Brand Sentiment</p>
                <small style="color: {COKE_COLORS['dark_gray']};">Out of 1.0</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            product_sentiment = sentiment_data["product_sentiment"]
            
            sentiment_df = pd.DataFrame([
                {"Product": prod.replace("_", " ").title(), "Sentiment": score}
                for prod, score in product_sentiment.items()
            ])
            
            fig_sentiment = px.bar(
                sentiment_df,
                x="Product",
                y="Sentiment",
                color="Sentiment",
                color_continuous_scale="RdYlGn",
                title="Product Sentiment Scores"
            )
            
            fig_sentiment.update_layout(height=300, font_color=COKE_COLORS['coke_black'])
            st.plotly_chart(fig_sentiment, use_container_width=True)
        
        # Price optimization
        st.markdown("#### 💰 Price Optimization Insights")
        
        price_data = advanced_analytics["price_optimization"]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Price Elasticity Analysis**")
            for category, elasticity in price_data["elasticity_analysis"].items():
                elasticity_color = COKE_COLORS['success_green'] if "Low" in elasticity else COKE_COLORS['warning_orange'] if "Moderate" in elasticity else COKE_COLORS['primary_red']
                
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 12px;
                    border-radius: 8px;
                    margin: 8px 0;
                    border-left: 4px solid {elasticity_color};
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{category.replace('_', ' ').title()}</h5>
                    <p style="margin: 5px 0; color: {elasticity_color}; font-weight: 600;">{elasticity}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Optimization Opportunities**")
            for i, opportunity in enumerate(price_data["optimization_opportunities"]):
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 12px;
                    border-radius: 8px;
                    margin: 8px 0;
                    border: 1px solid {COKE_COLORS['light_gray']};
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <p style="margin: 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">
                        <strong>#{i+1}:</strong> {opportunity}
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 📈 Performance Metrics & KPIs")
        
        # Supply chain metrics
        st.markdown("#### 🚛 Supply Chain Performance")
        
        supply_chain = advanced_analytics["supply_chain"]["efficiency_metrics"]
        
        sc_col1, sc_col2, sc_col3, sc_col4 = st.columns(4)
        
        with sc_col1:
            st.metric("Delivery Performance", supply_chain["delivery_performance"], "+2.1%")
        
        with sc_col2:
            st.metric("Inventory Turnover", supply_chain["inventory_turnover"], "+0.8x")
        
        with sc_col3:
            st.metric("Cost Optimization", supply_chain["cost_optimization"], "vs LY")
        
        with sc_col4:
            st.metric("Sustainability Score", supply_chain["sustainability_score"], "+5 pts")
        
        # AI-Generated insights summary
        st.markdown("#### 🤖 AI-Generated Insights Summary")
        
        ai_insights = [
            {
                "category": "Market Opportunity",
                "insight": "Zero-sugar segment showing 15% growth trajectory",
                "action": "Accelerate Coke Zero marketing spend",
                "confidence": 94
            },
            {
                "category": "Competitive Threat", 
                "insight": "Energy drink category expanding into traditional soda space",
                "action": "Develop energy variant for Coca-Cola Classic",
                "confidence": 87
            },
            {
                "category": "Customer Behavior",
                "insight": "Convenience channel purchases correlate with mobile app usage",
                "action": "Integrate Freestyle app with convenience store partnerships",
                "confidence": 91
            },
            {
                "category": "Operational Efficiency",
                "insight": "Route optimization reducing delivery costs significantly",
                "action": "Expand AI-driven logistics to all regions",
                "confidence": 96
            }
        ]
        
        for insight in ai_insights:
            confidence_color = COKE_COLORS['success_green'] if insight['confidence'] > 90 else COKE_COLORS['warning_orange'] if insight['confidence'] > 80 else COKE_COLORS['primary_red']
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                padding: 15px;
                border-radius: 10px;
                margin: 10px 0;
                border-left: 6px solid {confidence_color};
                box-shadow: 0 3px 6px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h5 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{insight['category']}</h5>
                    <span style="
                        background: {confidence_color};
                        color: white;
                        padding: 4px 12px;
                        border-radius: 20px;
                        font-size: 12px;
                        font-weight: bold;
                    ">{insight['confidence']}% Confidence</span>
                </div>
                <p style="margin: 8px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px; line-height: 1.4;"><strong>Insight:</strong> {insight['insight']}</p>
                <p style="margin: 0; color: {COKE_COLORS['dark_gray']}; font-size: 13px;"><strong>Recommended Action:</strong> {insight['action']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Real-time data feeds simulation
        st.markdown("#### 📡 Real-Time Data Feeds")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Live Market Metrics**")
            
            # Simulate real-time updates
            current_time = datetime.now()
            
            live_metrics = [
                {"metric": "Social Media Mentions", "value": f"{random.randint(1200, 1800)}/hr", "trend": "+12%"},
                {"metric": "E-commerce Sales", "value": f"${random.randint(45, 75)}K/hr", "trend": "+8%"},
                {"metric": "Freestyle Dispenses", "value": f"{random.randint(850, 1200)}/min", "trend": "+15%"},
                {"metric": "Mobile App Interactions", "value": f"{random.randint(320, 480)}/min", "trend": "+22%"}
            ]
            
            for metric in live_metrics:
                trend_color = COKE_COLORS['success_green'] if '+' in metric['trend'] else COKE_COLORS['primary_red']
                
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 12px;
                    border-radius: 8px;
                    margin: 5px 0;
                    border: 1px solid {COKE_COLORS['light_gray']};
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                ">
                    <div>
                        <strong style="color: {COKE_COLORS['coke_black']};">{metric['metric']}</strong><br>
                        <span style="color: {COKE_COLORS['dark_gray']}; font-size: 12px;">Last updated: {current_time.strftime('%H:%M:%S')}</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="color: {COKE_COLORS['coke_black']}; font-weight: 600; font-size: 16px;">{metric['value']}</span><br>
                        <span style="color: {trend_color}; font-size: 12px; font-weight: 600;">{metric['trend']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**AI Model Performance**")
            
            model_metrics = [
                {"model": "Demand Forecasting", "accuracy": "94.2%", "last_trained": "2 hours ago"},
                {"model": "Sentiment Analysis", "accuracy": "91.7%", "last_trained": "4 hours ago"},
                {"model": "Churn Prediction", "accuracy": "88.9%", "last_trained": "6 hours ago"},
                {"model": "Price Optimization", "accuracy": "92.3%", "last_trained": "1 hour ago"}
            ]
            
            for model in model_metrics:
                accuracy_score = float(model['accuracy'].replace('%', ''))
                accuracy_color = COKE_COLORS['success_green'] if accuracy_score > 90 else COKE_COLORS['warning_orange']
                
                st.markdown(f"""
                <div style="
                    background: {COKE_COLORS['classic_white']};
                    padding: 12px;
                    border-radius: 8px;
                    margin: 5px 0;
                    border-left: 4px solid {accuracy_color};
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <h6 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{model['model']}</h6>
                    <div style="display: flex; justify-content: space-between; margin-top: 5px;">
                        <span style="color: {accuracy_color}; font-weight: 600;">Accuracy: {model['accuracy']}</span>
                        <small style="color: {COKE_COLORS['dark_gray']};">Updated: {model['last_trained']}</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)

def render():
    """Main render function for the data insights tab"""
    render_data_insights()
