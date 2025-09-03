"""
Enhanced Data Generator for Coca-Cola Sales AI Platform
Includes comprehensive customer data, engagement history, and proactive insights
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any

class EnhancedDataGenerator:
    """Enhanced data generator with detailed customer insights and proactive data"""
    
    def __init__(self):
        self.industries = [
            "Quick Service Restaurant", "Casual Dining", "Fine Dining", "Fast Casual",
            "Grocery Retail", "Convenience Store", "Gas Station", "Vending", 
            "Entertainment Venue", "Sports Stadium", "University", "Hospital",
            "Corporate Cafeteria", "Theme Park", "Airport"
        ]
        
        self.regions = [
            "North America - East", "North America - West", "North America - Central",
            "North America - Southeast", "North America - Southwest", "North America - Northwest",
            "Canada - Ontario", "Canada - Quebec", "Canada - Western", 
            "Mexico - North", "Mexico - Central", "Mexico - South"
        ]
        
        self.products = [
            {"name": "Coca-Cola Classic", "category": "Cola", "margin": 0.45},
            {"name": "Coca-Cola Zero Sugar", "category": "Cola", "margin": 0.48},
            {"name": "Diet Coke", "category": "Cola", "margin": 0.46},
            {"name": "Sprite", "category": "Lemon-Lime", "margin": 0.42},
            {"name": "Fanta Orange", "category": "Orange", "margin": 0.40},
            {"name": "Freestyle Classic Mix", "category": "Freestyle", "margin": 0.55},
            {"name": "Freestyle Zero Mix", "category": "Freestyle", "margin": 0.58},
            {"name": "Powerade", "category": "Sports Drink", "margin": 0.35},
            {"name": "Dasani Water", "category": "Water", "margin": 0.65},
            {"name": "Simply Orange", "category": "Juice", "margin": 0.38}
        ]
        
        self.sales_reps = [
            "Sarah Chen", "Mike Rodriguez", "Jennifer Smith", "David Kim", 
            "Lisa Johnson", "Carlos Martinez", "Emily Wang", "Robert Brown",
            "Maria Garcia", "James Wilson", "Ashley Davis", "Daniel Lee"
        ]
        
        self.engagement_types = [
            "Email", "Phone Call", "In-Person Meeting", "Video Call", 
            "Text Message", "Trade Show", "Presentation", "Contract Review"
        ]
        
    def generate_enhanced_accounts(self, num_accounts: int = 525) -> pd.DataFrame:
        """Generate enhanced account data with detailed insights"""
        accounts = []
        
        for i in range(num_accounts):
            # Basic account info
            account_id = f"ACC-{str(i+1).zfill(4)}"
            company_names = [
                "Metro Restaurant Group", "Golden Gate Grocers", "Summit Entertainment",
                "Riverside Convenience", "Pacific Stadium Corp", "Mountain View Dining",
                "Coastal Retail Chain", "Urban Food Services", "Valley Sports Complex",
                "Desert Oasis Hotels", "Northern Lights Cafeteria", "Eastern Seaboard Venues"
            ]
            
            company_name = f"{random.choice(company_names)} {random.choice(['Inc', 'LLC', 'Corp', 'Ltd'])}"
            if i < len(company_names):
                company_name = company_names[i] + f" {random.choice(['Inc', 'LLC', 'Corp', 'Ltd'])}"
            
            # Revenue and metrics
            annual_revenue = random.uniform(50000, 2500000)
            monthly_volume = random.uniform(500, 25000)
            
            # Health and sentiment scoring
            health_score = random.uniform(0.2, 1.0)
            sentiment_score = random.uniform(-1.0, 1.0)
            engagement_score = random.uniform(0.1, 1.0)
            
            # Risk indicators
            churn_risk = self._calculate_churn_risk(health_score, sentiment_score, engagement_score)
            payment_history = random.choice(["Excellent", "Good", "Fair", "Poor"])
            
            # Contract info
            contract_start = datetime.now() - timedelta(days=random.randint(30, 1095))
            contract_end = contract_start + timedelta(days=random.choice([365, 730, 1095]))
            
            account = {
                "account_id": account_id,
                "company_name": company_name,
                "industry": random.choice(self.industries),
                "region": random.choice(self.regions),
                "annual_revenue": annual_revenue,
                "monthly_volume": monthly_volume,
                "health_score": health_score,
                "sentiment_score": sentiment_score,
                "engagement_score": engagement_score,
                "churn_risk": churn_risk,
                "churn_probability": self._calculate_churn_probability(churn_risk),
                "payment_history": payment_history,
                "primary_contact": f"{random.choice(['John', 'Sarah', 'Mike', 'Lisa', 'David'])}"
                               f" {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Davis'])}",
                "contact_email": f"{random.choice(['john', 'sarah', 'mike', 'lisa', 'david'])}"
                               f".{random.choice(['smith', 'johnson', 'williams', 'brown', 'davis'])}"
                               f"@{company_name.split()[0].lower()}.com",
                "phone": f"+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}",
                "assigned_rep": random.choice(self.sales_reps),
                "contract_start": contract_start,
                "contract_end": contract_end,
                "days_to_renewal": (contract_end - datetime.now()).days,
                "primary_product": random.choice(self.products)["name"],
                "freestyle_machines": random.randint(0, 25),
                "last_order_date": datetime.now() - timedelta(days=random.randint(1, 90)),
                "avg_order_frequency": random.randint(7, 45),  # days
                "customer_since": contract_start.year,
                "total_locations": random.randint(1, 150),
                "growth_rate": random.uniform(-0.3, 0.8),  # YoY growth rate
                "competitive_threat": random.choice(["Low", "Medium", "High"]),
                "last_complaint_date": datetime.now() - timedelta(days=random.randint(30, 365)) if random.random() > 0.7 else None,
                "nps_score": random.randint(-100, 100),
                "expansion_potential": random.choice(["Low", "Medium", "High"]),
                "decision_maker": random.choice(["Procurement", "Operations", "C-Level", "Franchise Owner"]),
                "budget_cycle": random.choice(["Q1", "Q2", "Q3", "Q4", "Ongoing"]),
                "preferred_communication": random.choice(["Email", "Phone", "In-Person", "Text"]),
                "last_interaction": datetime.now() - timedelta(days=random.randint(1, 30)),
            }
            
            accounts.append(account)
        
        return pd.DataFrame(accounts)
    
    def generate_enhanced_opportunities(self, num_opportunities: int = 250, accounts_df: pd.DataFrame = None) -> pd.DataFrame:
        """Generate enhanced opportunities with pipeline stages and forecasting"""
        
        # Generate accounts if not provided
        if accounts_df is None:
            accounts_df = self.generate_enhanced_accounts(100)
            
        opportunities = []
        
        pipeline_stages = [
            {"name": "Prospecting", "probability": 0.1, "weight": 0.1},
            {"name": "Qualification", "probability": 0.25, "weight": 0.25},
            {"name": "Needs Analysis", "probability": 0.4, "weight": 0.4},
            {"name": "Proposal", "probability": 0.65, "weight": 0.65},
            {"name": "Negotiation", "probability": 0.8, "weight": 0.8},
            {"name": "Closing", "probability": 0.95, "weight": 0.95},
            {"name": "Closed-Won", "probability": 1.0, "weight": 1.0},
            {"name": "Closed-Lost", "probability": 0.0, "weight": 0.0}
        ]
        
        opportunity_types = [
            "New Product Launch", "Volume Increase", "Freestyle Installation",
            "Contract Renewal", "Competitive Displacement", "Seasonal Campaign",
            "Cross-Sell", "Upsell", "Expansion", "Partnership"
        ]
        
        for i in range(num_opportunities):
            account = accounts_df.sample(1).iloc[0]
            stage = random.choice(pipeline_stages)
            
            opp_id = f"OPP-{str(i+1).zfill(4)}"
            value = random.uniform(10000, 500000)
            
            # Create opportunity
            opportunity = {
                "opportunity_id": opp_id,
                "account_id": account["account_id"],
                "company_name": account["company_name"],
                "opportunity_name": f"{account['company_name']} - {random.choice(opportunity_types)}",
                "value": value,
                "weighted_value": value * stage["probability"],
                "stage": stage["name"],
                "probability": stage["probability"],
                "expected_close_date": datetime.now() + timedelta(days=random.randint(7, 180)),
                "created_date": datetime.now() - timedelta(days=random.randint(1, 90)),
                "last_activity_date": datetime.now() - timedelta(days=random.randint(0, 30)),
                "days_to_close": random.randint(7, 180),
                "assigned_rep": account["assigned_rep"],
                "region": account["region"],
                "industry": account["industry"],
                "opportunity_type": random.choice(opportunity_types),
                "priority": random.choice(["Low", "Medium", "High", "Critical"]),
                "competitor": random.choice(["Pepsi", "Dr Pepper", "Local Brand", "None"]) if random.random() > 0.3 else "None",
                "decision_maker": account["decision_maker"],
                "budget_confirmed": random.choice([True, False]),
                "pain_points": random.choice([
                    "High costs", "Poor service", "Limited variety", "Supply issues",
                    "Contract flexibility", "Technology upgrade", "Growth support"
                ]),
                "next_steps": self._generate_next_steps(stage["name"]),
                "days_in_stage": random.randint(1, 45),
                "source": random.choice(["Inbound", "Outbound", "Referral", "Trade Show", "Cold Call"]),
                "close_reason": random.choice([
                    "Price", "Product fit", "Relationship", "Service", "Contract terms"
                ]) if stage["name"] in ["Closed-Won", "Closed-Lost"] else None,
                "forecast_category": self._get_forecast_category(stage["probability"]),
                "risk_factors": self._generate_risk_factors(),
                "key_stakeholders": random.randint(2, 8),
                "engagement_level": random.choice(["Low", "Medium", "High"]),
                "product_interest": random.choice([p["name"] for p in self.products]),
            }
            
            opportunities.append(opportunity)
        
        return pd.DataFrame(opportunities)
    
    def generate_engagement_history(self, num_engagements: int = 1500, accounts_df: pd.DataFrame = None) -> pd.DataFrame:
        """Generate detailed engagement history for accounts"""
        
        # Generate accounts if not provided
        if accounts_df is None:
            accounts_df = self.generate_enhanced_accounts(100)
            
        engagements = []
        
        for i in range(num_engagements):
            account = accounts_df.sample(1).iloc[0]
            
            engagement_date = datetime.now() - timedelta(days=random.randint(0, 365))
            engagement_type = random.choice(self.engagement_types)
            
            engagement = {
                "engagement_id": f"ENG-{str(i+1).zfill(5)}",
                "account_id": account["account_id"],
                "company_name": account["company_name"],
                "engagement_date": engagement_date,
                "engagement_type": engagement_type,
                "duration_minutes": random.randint(15, 120) if engagement_type in ["Phone Call", "In-Person Meeting", "Video Call"] else 0,
                "participants": random.randint(1, 6),
                "initiated_by": random.choice(["Customer", "Sales Rep", "Support", "Marketing"]),
                "sentiment": random.choice(["Positive", "Neutral", "Negative"]),
                "outcome": random.choice([
                    "Information shared", "Follow-up scheduled", "Demo requested",
                    "Proposal requested", "Concerns raised", "Order placed",
                    "Issue resolved", "Meeting scheduled"
                ]),
                "topics_discussed": random.choice([
                    "Pricing", "Product features", "Service issues", "Contract renewal",
                    "New product launch", "Volume discounts", "Delivery schedules",
                    "Competitive comparison", "Expansion plans", "Payment terms"
                ]),
                "assigned_rep": account["assigned_rep"],
                "follow_up_required": random.choice([True, False]),
                "follow_up_date": engagement_date + timedelta(days=random.randint(1, 30)) if random.choice([True, False]) else None,
                "satisfaction_score": random.randint(1, 5) if engagement_type in ["Phone Call", "In-Person Meeting"] else None,
                "notes": f"Discussed {random.choice(['pricing options', 'product features', 'service improvements', 'contract terms'])} with customer. "
                        f"Customer expressed {random.choice(['interest', 'concerns', 'enthusiasm', 'skepticism'])} about our proposal.",
                "action_items": random.randint(0, 5),
                "opportunity_created": random.choice([True, False]) if random.random() > 0.8 else False,
                "effectiveness_score": random.uniform(0.3, 1.0),
            }
            
            engagements.append(engagement)
        
        return pd.DataFrame(engagements)
    
    def generate_product_performance(self, accounts_df: pd.DataFrame) -> pd.DataFrame:
        """Generate product performance data by account"""
        performance_data = []
        
        for _, account in accounts_df.iterrows():
            for product in self.products:
                # Not all accounts use all products
                if random.random() > 0.6:
                    continue
                    
                monthly_volume = random.uniform(100, 5000)
                monthly_revenue = monthly_volume * random.uniform(1.20, 3.50)
                
                performance = {
                    "account_id": account["account_id"],
                    "company_name": account["company_name"],
                    "product_name": product["name"],
                    "product_category": product["category"],
                    "monthly_volume": monthly_volume,
                    "monthly_revenue": monthly_revenue,
                    "margin_percentage": product["margin"],
                    "margin_dollars": monthly_revenue * product["margin"],
                    "growth_rate": random.uniform(-0.4, 0.6),
                    "market_share": random.uniform(0.1, 0.8),
                    "seasonality_factor": random.uniform(0.7, 1.3),
                    "competitive_pressure": random.choice(["Low", "Medium", "High"]),
                    "price_sensitivity": random.choice(["Low", "Medium", "High"]),
                    "trend": random.choice(["Growing", "Stable", "Declining"]),
                    "last_order_date": datetime.now() - timedelta(days=random.randint(1, 60)),
                    "avg_order_size": random.uniform(500, 3000),
                    "reorder_frequency": random.randint(7, 45),  # days
                    "stock_level": random.choice(["Low", "Normal", "High"]),
                    "customer_satisfaction": random.uniform(3.0, 5.0),
                }
                
                performance_data.append(performance)
        
        return pd.DataFrame(performance_data)
    
    def generate_regional_performance(self) -> pd.DataFrame:
        """Generate regional performance and insights data"""
        regional_data = []
        
        for region in self.regions:
            regional_performance = {
                "region": region,
                "total_accounts": random.randint(25, 80),
                "active_accounts": random.randint(20, 75),
                "total_revenue": random.uniform(2000000, 15000000),
                "revenue_growth": random.uniform(-0.15, 0.35),
                "avg_account_value": random.uniform(75000, 350000),
                "churn_rate": random.uniform(0.02, 0.18),
                "new_acquisitions": random.randint(2, 15),
                "market_penetration": random.uniform(0.15, 0.75),
                "competitive_wins": random.randint(1, 8),
                "competitive_losses": random.randint(0, 5),
                "top_product": random.choice([p["name"] for p in self.products]),
                "growth_opportunity": random.choice(["Low", "Medium", "High"]),
                "primary_challenge": random.choice([
                    "Competitive pressure", "Price sensitivity", "Supply chain",
                    "Market saturation", "Economic conditions", "Regulatory changes"
                ]),
                "key_success_factor": random.choice([
                    "Strong relationships", "Product innovation", "Competitive pricing",
                    "Service excellence", "Market positioning", "Distribution network"
                ]),
                "forecast_confidence": random.uniform(0.6, 0.95),
                "territory_manager": random.choice(self.sales_reps),
                "last_review_date": datetime.now() - timedelta(days=random.randint(7, 90)),
            }
            
            regional_data.append(regional_performance)
        
        return pd.DataFrame(regional_data)
    
    def generate_sales_rep_performance(self) -> pd.DataFrame:
        """Generate sales rep performance and gamification data"""
        rep_data = []
        
        for rep in self.sales_reps:
            rep_performance = {
                "sales_rep": rep,
                "total_accounts": random.randint(15, 55),
                "active_opportunities": random.randint(8, 35),
                "ytd_revenue": random.uniform(800000, 4500000),
                "revenue_target": random.uniform(1000000, 5000000),
                "target_achievement": random.uniform(0.65, 1.35),
                "deals_closed": random.randint(12, 48),
                "avg_deal_size": random.uniform(45000, 185000),
                "win_rate": random.uniform(0.35, 0.85),
                "pipeline_value": random.uniform(500000, 2500000),
                "forecast_accuracy": random.uniform(0.70, 0.95),
                "customer_satisfaction": random.uniform(3.5, 5.0),
                "activity_score": random.randint(65, 98),
                "engagement_score": random.uniform(0.6, 0.95),
                "last_activity": datetime.now() - timedelta(days=random.randint(0, 7)),
                "phone_calls": random.randint(45, 150),
                "emails_sent": random.randint(85, 300),
                "meetings_held": random.randint(15, 60),
                "proposals_sent": random.randint(5, 25),
                "rank_revenue": 0,  # Will be calculated
                "rank_deals": 0,    # Will be calculated
                "achievements": random.randint(2, 12),
                "badges_earned": random.choice([
                    ["Top Performer", "Customer Champion"], 
                    ["Rising Star", "Deal Closer"],
                    ["Relationship Builder", "Innovation Leader"],
                    ["Territory Master", "Growth Driver"]
                ]),
                "current_streak": random.randint(0, 15),  # consecutive successful weeks
                "region": random.choice(self.regions),
            }
            
            rep_data.append(rep_performance)
        
        # Calculate rankings
        df = pd.DataFrame(rep_data)
        df['rank_revenue'] = df['ytd_revenue'].rank(method='dense', ascending=False).astype(int)
        df['rank_deals'] = df['deals_closed'].rank(method='dense', ascending=False).astype(int)
        
        return df
    
    def _calculate_churn_risk(self, health_score: float, sentiment_score: float, engagement_score: float) -> str:
        """Calculate churn risk based on multiple factors"""
        risk_score = (health_score * 0.4) + ((sentiment_score + 1) / 2 * 0.3) + (engagement_score * 0.3)
        
        if risk_score < 0.3:
            return "High"
        elif risk_score < 0.6:
            return "Medium"
        else:
            return "Low"
    
    def _calculate_churn_probability(self, churn_risk: str) -> float:
        """Convert churn risk to probability"""
        risk_mapping = {"Low": random.uniform(0.02, 0.15), 
                       "Medium": random.uniform(0.15, 0.45), 
                       "High": random.uniform(0.45, 0.85)}
        return risk_mapping[churn_risk]
    
    def _generate_next_steps(self, stage: str) -> str:
        """Generate appropriate next steps based on opportunity stage"""
        steps_by_stage = {
            "Prospecting": ["Research decision makers", "Schedule discovery call", "Send introduction email"],
            "Qualification": ["Confirm budget", "Identify decision process", "Schedule needs assessment"],
            "Needs Analysis": ["Conduct product demo", "Prepare custom proposal", "Map stakeholders"],
            "Proposal": ["Present proposal", "Address questions", "Schedule follow-up"],
            "Negotiation": ["Finalize terms", "Get legal approval", "Prepare contracts"],
            "Closing": ["Sign contracts", "Schedule implementation", "Celebrate win"],
            "Closed-Won": ["Begin onboarding", "Schedule check-in", "Plan expansion"],
            "Closed-Lost": ["Conduct debrief", "Maintain relationship", "Plan re-engagement"]
        }
        return random.choice(steps_by_stage.get(stage, ["Follow up with customer"]))
    
    def _get_forecast_category(self, probability: float) -> str:
        """Categorize forecast based on probability"""
        if probability >= 0.75:
            return "Commit"
        elif probability >= 0.5:
            return "Best Case"
        elif probability >= 0.25:
            return "Pipeline"
        else:
            return "Upside"
    
    def _generate_risk_factors(self) -> str:
        """Generate realistic risk factors for opportunities"""
        risks = [
            "Budget constraints", "Competitive pressure", "Decision timeline",
            "Multiple stakeholders", "Economic uncertainty", "Internal changes",
            "Technical requirements", "Contract complexity", "Regulatory issues"
        ]
        return random.choice(risks)

# Global instance for easy access
enhanced_data_gen = EnhancedDataGenerator()
