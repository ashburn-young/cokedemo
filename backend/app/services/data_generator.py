"""
Data Generator Service for Coca-Cola Sales AI Agent Framework.

This service generates realistic sample data that simulates a real CRM system
with accounts, opportunities, communications, and Freestyle machine telemetry.
"""

import asyncio
import logging
import random
import json
from datetime import datetime, date, timedelta
from typing import List, Dict, Any
from faker import Faker
import uuid

from app.models.schemas import (
    Account, Contact, Opportunity, Communication, FreestyleMachineData,
    SalesMetrics, AccountType, ProductLine, OpportunityStage, SentimentScore
)

logger = logging.getLogger(__name__)
fake = Faker()


class DataGeneratorService:
    """Service for generating realistic Coca-Cola sales data."""
    
    def __init__(self):
        self.accounts: List[Account] = []
        self.contacts: List[Contact] = []
        self.opportunities: List[Opportunity] = []
        self.communications: List[Communication] = []
        self.freestyle_data: List[FreestyleMachineData] = []
        self.sales_metrics: List[SalesMetrics] = []
        
        # Realistic data sets for generation
        # Real Coca-Cola business partner names and realistic scenarios
        self.bottler_names = [
            "Atlanta Coca-Cola Bottling", "Coca-Cola Consolidated", "Swire Coca-Cola USA",
            "Great Lakes Coca-Cola", "Coca-Cola Bottling Co. United", "Buffalo Rock Company",
            "Coca-Cola Refreshments", "Texas Coca-Cola Bottling", "Florida Coca-Cola Bottling",
            "Liberty Coca-Cola Beverages", "Carolinas Coca-Cola", "Rocky Mountain Bottling"
        ]
        
        self.retailer_names = [
            "Walmart Supercenters", "Target Corporation", "Kroger Grocery Chain",
            "Safeway Supermarkets", "Publix Super Markets", "Meijer Supercenters",
            "H-E-B Grocery Company", "Wegmans Food Markets", "WinCo Foods",
            "Food Lion Supermarkets", "Giant Eagle Markets", "ShopRite Supermarkets"
        ]
        
        self.qsr_names = [
            "McDonald's Corporation", "Burger King", "Subway Restaurants",
            "KFC Restaurants", "Pizza Hut", "Taco Bell",
            "Wendy's Company", "Domino's Pizza", "Papa John's Pizza",
            "Chipotle Mexican Grill", "Panera Bread", "Five Guys Burgers"
        ]
        
        self.cinema_names = [
            "AMC Entertainment", "Regal Cinemas", "Cinemark Theatres",
            "Marcus Theatres", "Harkins Theatres", "Showcase Cinemas",
            "Alamo Drafthouse", "iPic Entertainment", "Studio Movie Grill",
            "Bow Tie Cinemas", "Landmark Theatres", "B&B Theatres"
        ]
        
        self.stadium_names = [
            "Mercedes-Benz Stadium", "AT&T Stadium", "MetLife Stadium",
            "Soldier Field", "Lambeau Field", "Arrowhead Stadium",
            "State Farm Stadium", "Hard Rock Stadium", "NRG Stadium",
            "U.S. Bank Stadium", "Allegiant Stadium", "SoFi Stadium"
        ]
        
        self.qsr_names = [
            "Burger Palace Chain", "Taco Fiesta Restaurants", "Pizza Corner", "Chicken Express",
            "Sandwich Station", "Grill Master", "Fast Bites", "Quick Eats", "Speedy Meals",
            "Comfort Kitchen", "Drive-Thru Delights", "Express Diner"
        ]
        
        self.cinema_names = [
            "MovieMax Theaters", "CinemaWorld", "Premium Pictures", "Starlight Cinemas",
            "Grand Theater Chain", "FilmFest Theaters", "Screen Palace", "Vista Cinemas",
            "Regal Entertainment", "AMC Partner Theaters", "Independent Cinema Group"
        ]
        
        self.regions = [
            "North America - East", "North America - Central", "North America - West",
            "North America - Southeast", "North America - Southwest", "North America - Northwest"
        ]
        
        self.countries = ["United States", "Canada", "Mexico"]
        
        # Business-specific data
        self.job_titles = [
            "CEO", "President", "VP of Operations", "General Manager", "Operations Director",
            "Purchasing Manager", "Category Manager", "Store Manager", "Regional Manager",
            "Marketing Director", "Sales Director", "Procurement Specialist", "Buyer"
        ]
        
        self.communication_subjects = [
            "Q4 Volume Commitment Discussion", "New Product Launch Collaboration",
            "Promotional Calendar Review", "Freestyle Machine Performance",
            "Contract Renewal Terms", "Market Share Analysis", "Competitive Response Strategy",
            "Category Management Support", "Supply Chain Optimization", "Pricing Discussion",
            "Marketing Development Fund Request", "Performance Review Meeting"
        ]
        
        logger.info("DataGeneratorService initialized")
    
    async def generate_sample_data(self) -> None:
        """Generate comprehensive sample data for the system."""
        try:
            logger.info("Starting sample data generation...")
            
            # Generate accounts first (foundation for all other data)
            await self._generate_accounts(50)
            
            # Generate contacts for each account
            await self._generate_contacts()
            
            # Generate opportunities
            await self._generate_opportunities(200)
            
            # Generate communications
            await self._generate_communications(500)
            
            # Generate Freestyle machine data for applicable accounts
            await self._generate_freestyle_data()
            
            # Generate sales metrics
            await self._generate_sales_metrics()
            
            logger.info(f"Sample data generation completed: {len(self.accounts)} accounts, "
                       f"{len(self.opportunities)} opportunities, {len(self.communications)} communications")
            
        except Exception as e:
            logger.error(f"Error generating sample data: {str(e)}")
            raise
    
    async def _generate_accounts(self, count: int) -> None:
        """Generate realistic account data."""
        for i in range(count):
            account_type = random.choice(list(AccountType))
            
            # Select appropriate name based on account type
            if account_type == AccountType.BOTTLER:
                name = random.choice(self.bottler_names)
            elif account_type in [AccountType.RETAILER, AccountType.GROCERY, AccountType.CONVENIENCE]:
                name = random.choice(self.retailer_names)
            elif account_type == AccountType.QSR:
                name = random.choice(self.qsr_names)
            elif account_type == AccountType.CINEMA:
                name = random.choice(self.cinema_names)
            else:
                name = f"{fake.company()} {account_type.value.title()}"
            
            # Generate realistic business metrics based on account type
            if account_type == AccountType.BOTTLER:
                annual_revenue = random.uniform(50_000_000, 500_000_000)
                employee_count = random.randint(200, 2000)
                lifetime_value = random.uniform(5_000_000, 50_000_000)
            elif account_type in [AccountType.RETAILER, AccountType.GROCERY]:
                annual_revenue = random.uniform(10_000_000, 100_000_000)
                employee_count = random.randint(100, 1000)
                lifetime_value = random.uniform(1_000_000, 10_000_000)
            elif account_type == AccountType.QSR:
                annual_revenue = random.uniform(5_000_000, 50_000_000)
                employee_count = random.randint(50, 500)
                lifetime_value = random.uniform(500_000, 5_000_000)
            else:
                annual_revenue = random.uniform(1_000_000, 20_000_000)
                employee_count = random.randint(20, 200)
                lifetime_value = random.uniform(100_000, 2_000_000)
            
            # Health and risk scores with some correlation
            base_health = random.uniform(60, 95)
            health_score = base_health
            churn_risk_score = max(0, 100 - base_health + random.uniform(-10, 10))
            
            # Product portfolio - more diverse for larger accounts
            product_count = random.randint(2, 6) if annual_revenue > 10_000_000 else random.randint(1, 3)
            current_products = random.sample(list(ProductLine), product_count)
            
            # Freestyle data for applicable account types
            freestyle_machines = None
            avg_daily_pours = None
            machine_uptime = None
            
            if account_type in [AccountType.QSR, AccountType.CINEMA, AccountType.CONVENIENCE]:
                freestyle_machines = random.randint(1, 10)
                avg_daily_pours = random.uniform(200, 1500)
                machine_uptime = random.uniform(85, 99)
            
            account = Account(
                name=name,
                account_type=account_type,
                region=random.choice(self.regions),
                country=random.choice(self.countries),
                annual_revenue=annual_revenue,
                employee_count=employee_count,
                created_date=fake.date_time_between(start_date="-2y", end_date="-6m"),
                last_activity_date=fake.date_time_between(start_date="-30d", end_date="now"),
                health_score=health_score,
                churn_risk_score=churn_risk_score,
                lifetime_value=lifetime_value,
                current_products=current_products,
                freestyle_machines_count=freestyle_machines,
                avg_daily_pours=avg_daily_pours,
                machine_uptime_percentage=machine_uptime,
                credit_rating=random.choice(["A+", "A", "A-", "B+", "B", "B-"]),
                payment_terms=random.choice(["Net 30", "Net 45", "Net 60", "2/10 Net 30"]),
                discount_tier=random.choice(["Platinum", "Gold", "Silver", "Bronze"]),
                latitude=fake.latitude(),
                longitude=fake.longitude()
            )
            
            self.accounts.append(account)
    
    async def _generate_contacts(self) -> None:
        """Generate contacts for each account."""
        for account in self.accounts:
            # Generate 2-5 contacts per account
            contact_count = random.randint(2, 5)
            
            for i in range(contact_count):
                is_decision_maker = i == 0  # First contact is always decision maker
                
                contact = Contact(
                    account_id=account.id,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    title=random.choice(self.job_titles),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    department=random.choice(["Operations", "Purchasing", "Marketing", "Sales", "Executive"]),
                    decision_maker=is_decision_maker,
                    influence_level=random.randint(7, 10) if is_decision_maker else random.randint(3, 8),
                    last_contact_date=fake.date_time_between(start_date="-60d", end_date="now"),
                    preferred_communication=random.choice(["email", "phone", "in_person"])
                )
                
                self.contacts.append(contact)
                
                # Set primary contact for account
                if is_decision_maker:
                    account.primary_contact_id = contact.id
    
    async def _generate_opportunities(self, count: int) -> None:
        """Generate sales opportunities."""
        opportunity_names = [
            "Annual Contract Renewal", "Q1 Volume Expansion", "Coca-Cola Freestyle Installation",
            "New Product Line Introduction", "Promotional Campaign Partnership", "Category Reset Optimization",
            "Market Share Growth Initiative", "Summer Beverage Program", "Holiday Season Partnership",
            "Back-to-School Campaign", "Sports Season Sponsorship", "Premium Product Placement",
            "smartwater Portfolio Expansion", "Powerade Distribution Agreement", "Exclusive Partnership Deal"
        ]
        
        for i in range(count):
            account = random.choice(self.accounts)
            stage = random.choice(list(OpportunityStage))
            
            # Probability based on stage
            stage_probabilities = {
                OpportunityStage.PROSPECTING: random.uniform(10, 30),
                OpportunityStage.QUALIFICATION: random.uniform(25, 45),
                OpportunityStage.PROPOSAL: random.uniform(40, 70),
                OpportunityStage.NEGOTIATION: random.uniform(60, 85),
                OpportunityStage.CLOSED_WON: 100,
                OpportunityStage.CLOSED_LOST: 0
            }
            
            # Amount based on account size
            base_amount = account.annual_revenue * 0.1  # 10% of annual revenue
            amount = random.uniform(base_amount * 0.5, base_amount * 1.5)
            
            opportunity = Opportunity(
                account_id=account.id,
                name=f"{account.name} - {random.choice(opportunity_names)}",
                description=self._generate_opportunity_description(account, stage),
                stage=stage,
                probability=stage_probabilities[stage],
                amount=amount,
                expected_close_date=fake.date_between(start_date="today", end_date="+6m"),
                created_date=fake.date_time_between(start_date="-90d", end_date="-10d"),
                last_modified_date=fake.date_time_between(start_date="-10d", end_date="now"),
                owner_id=str(uuid.uuid4()),  # Sales rep ID
                product_lines=random.sample(account.current_products, random.randint(1, len(account.current_products)))
            )
            
            self.opportunities.append(opportunity)
    
    def _generate_opportunity_description(self, account: Account, stage: OpportunityStage) -> str:
        """Generate realistic opportunity descriptions."""
        descriptions = {
            OpportunityStage.PROSPECTING: [
                f"Initial discussions with {account.name} about expanding beverage program.",
                f"Exploring partnership opportunities with {account.name} for enhanced product placement.",
                f"Assessing potential for Freestyle machine installation at {account.name} locations."
            ],
            OpportunityStage.QUALIFICATION: [
                f"Qualified opportunity with {account.name} for 15% volume increase next quarter.",
                f"Decision makers identified and engaged for new product line introduction.",
                f"Budget confirmed for promotional campaign with {account.name}."
            ],
            OpportunityStage.PROPOSAL: [
                f"Submitted comprehensive proposal for {account.name} annual contract renewal.",
                f"Presented Freestyle installation plan with ROI projections.",
                f"Detailed marketing partnership proposal under review."
            ],
            OpportunityStage.NEGOTIATION: [
                f"Negotiating final terms for volume commitments and pricing structure.",
                f"Working through contract details and implementation timeline.",
                f"Finalizing promotional calendar and marketing support terms."
            ],
            OpportunityStage.CLOSED_WON: [
                f"Successfully renewed annual contract with {account.name} - 20% volume increase.",
                f"Completed Freestyle installation across 5 locations.",
                f"Launched successful promotional campaign generating 25% lift."
            ],
            OpportunityStage.CLOSED_LOST: [
                f"Lost opportunity to competitor due to pricing constraints.",
                f"Account decided to delay expansion plans due to budget cuts.",
                f"Unable to meet technical requirements for installation timeline."
            ]
        }
        
        return random.choice(descriptions[stage])
    
    async def _generate_communications(self, count: int) -> None:
        """Generate communication records."""
        communication_types = ["email", "call", "meeting", "visit"]
        directions = ["inbound", "outbound"]
        
        for i in range(count):
            account = random.choice(self.accounts)
            account_contacts = [c for c in self.contacts if c.account_id == account.id]
            contact = random.choice(account_contacts) if account_contacts else None
            
            comm_type = random.choice(communication_types)
            subject = random.choice(self.communication_subjects)
            
            # Generate content based on sentiment
            sentiment = random.choice(list(SentimentScore))
            content = self._generate_communication_content(subject, sentiment, account)
            
            # Get opportunities for this account safely
            account_opportunities = [opp.id for opp in self.opportunities if opp.account_id == account.id]
            opportunity_id = random.choice(account_opportunities) if account_opportunities and random.random() < 0.3 else None
            
            communication = Communication(
                account_id=account.id,
                contact_id=contact.id if contact else None,
                opportunity_id=opportunity_id,
                communication_type=comm_type,
                subject=subject,
                content=content,
                date=fake.date_time_between(start_date="-90d", end_date="now"),
                direction=random.choice(directions),
                sentiment_score=sentiment,
                sentiment_confidence=random.uniform(0.7, 0.95),
                key_topics=self._extract_key_topics(content),
                action_items=self._generate_action_items(sentiment, comm_type)
            )
            
            self.communications.append(communication)
    
    def _generate_communication_content(self, subject: str, sentiment: SentimentScore, account: Account) -> str:
        """Generate realistic communication content based on sentiment."""
        if sentiment == SentimentScore.VERY_POSITIVE:
            return f"Excellent meeting about {subject.lower()}. {account.name} is very excited about the partnership opportunities and wants to move forward quickly. They're particularly interested in expanding the product mix and increasing volume commitments."
        
        elif sentiment == SentimentScore.POSITIVE:
            return f"Good discussion regarding {subject.lower()}. {account.name} team is supportive of the initiative and we're making solid progress. They have some questions about implementation timeline but overall very receptive."
        
        elif sentiment == SentimentScore.NEUTRAL:
            return f"Standard review meeting for {subject.lower()}. {account.name} provided updates on current performance. No major issues raised but also no significant enthusiasm for new initiatives at this time."
        
        elif sentiment == SentimentScore.NEGATIVE:
            return f"Challenging conversation about {subject.lower()}. {account.name} expressed concerns about current performance and questioned some aspects of our partnership. They're looking for better terms and improved support."
        
        else:  # VERY_NEGATIVE
            return f"Difficult meeting regarding {subject.lower()}. {account.name} is frustrated with recent issues and considering alternatives. They mentioned competitor offers and expressed dissatisfaction with current service levels."
    
    def _extract_key_topics(self, content: str) -> List[str]:
        """Extract key topics from communication content."""
        topics = []
        if "volume" in content.lower():
            topics.append("Volume Commitments")
        if "price" in content.lower() or "pricing" in content.lower():
            topics.append("Pricing")
        if "freestyle" in content.lower():
            topics.append("Freestyle Machines")
        if "competitor" in content.lower():
            topics.append("Competitive Pressure")
        if "partnership" in content.lower():
            topics.append("Partnership")
        if "product" in content.lower():
            topics.append("Product Mix")
        if "performance" in content.lower():
            topics.append("Performance Review")
        
        return topics if topics else ["General Discussion"]
    
    def _generate_action_items(self, sentiment: SentimentScore, comm_type: str) -> List[str]:
        """Generate action items based on communication sentiment."""
        if sentiment in [SentimentScore.VERY_POSITIVE, SentimentScore.POSITIVE]:
            return ["Follow up with proposal", "Schedule implementation meeting", "Prepare contract terms"]
        elif sentiment == SentimentScore.NEUTRAL:
            return ["Send additional information", "Schedule follow-up call"]
        else:
            return ["Address concerns raised", "Escalate to management", "Prepare retention strategy"]
    
    async def _generate_freestyle_data(self) -> None:
        """Generate Freestyle machine telemetry data."""
        freestyle_accounts = [acc for acc in self.accounts if acc.freestyle_machines_count and acc.freestyle_machines_count > 0]
        
        for account in freestyle_accounts:
            machine_count = account.freestyle_machines_count
            
            for machine_num in range(machine_count):
                # Generate daily data for last 30 days
                for day in range(30):
                    date_point = datetime.now() - timedelta(days=day)
                    
                    freestyle_data = FreestyleMachineData(
                        account_id=account.id,
                        machine_id=f"{account.id}-machine-{machine_num:02d}",
                        location_name=f"{account.name} Location {machine_num + 1}",
                        timestamp=date_point,
                        total_pours=random.randint(150, 800),
                        unique_customers=random.randint(50, 300),
                        avg_pour_size=random.uniform(12, 24),
                        popular_flavors=random.sample([
                            "Classic Coke", "Coke Zero", "Diet Coke", "Sprite", "Fanta Orange",
                            "Cherry Coke", "Vanilla Coke", "Lime Coke", "Raspberry Sprite"
                        ], 3),
                        uptime_percentage=random.uniform(85, 99),
                        error_count=random.randint(0, 5),
                        maintenance_alerts=["Low syrup level"] if random.random() < 0.1 else [],
                        revenue=random.uniform(300, 1500),
                        cost_per_pour=random.uniform(0.15, 0.35),
                        profit_margin=random.uniform(0.60, 0.75)
                    )
                    
                    self.freestyle_data.append(freestyle_data)
    
    async def _generate_sales_metrics(self) -> None:
        """Generate sales metrics for each account."""
        for account in self.accounts:
            # Generate quarterly metrics for last year
            for quarter in range(4):
                period_start = date(2024, quarter * 3 + 1, 1)
                if quarter == 3:
                    period_end = date(2024, 12, 31)
                else:
                    period_end = date(2024, (quarter + 1) * 3, 28)
                
                # Base volume and revenue on account size
                base_volume = account.annual_revenue * 0.0001  # Convert to volume units
                volume_variation = random.uniform(0.8, 1.2)
                total_volume = base_volume * volume_variation
                
                total_revenue = account.annual_revenue * 0.25  # Quarterly revenue
                revenue_variation = random.uniform(0.85, 1.15)
                total_revenue *= revenue_variation
                
                # Product mix based on account's current products
                product_mix = {}
                for product in account.current_products:
                    product_mix[product] = random.uniform(0.1, 0.4)
                
                # Normalize product mix to sum to 1.0
                total_mix = sum(product_mix.values())
                product_mix = {k: v/total_mix for k, v in product_mix.items()}
                
                metrics = SalesMetrics(
                    account_id=account.id,
                    period_start=period_start,
                    period_end=period_end,
                    total_volume=total_volume,
                    volume_change_percent=random.uniform(-10, 15),
                    volume_trend=random.choice(["increasing", "decreasing", "stable"]),
                    total_revenue=total_revenue,
                    revenue_change_percent=random.uniform(-8, 20),
                    avg_order_value=total_revenue / random.randint(10, 50),
                    product_mix=product_mix,
                    on_time_delivery_rate=random.uniform(92, 99),
                    quality_score=random.uniform(85, 98),
                    customer_satisfaction=random.uniform(80, 95)
                )
                
                self.sales_metrics.append(metrics)
    
    def get_sample_data(self) -> Dict[str, Any]:
        """Return all generated sample data."""
        return {
            "accounts": [acc.model_dump() for acc in self.accounts],
            "contacts": [contact.model_dump() for contact in self.contacts],
            "opportunities": [opp.model_dump() for opp in self.opportunities],
            "communications": [comm.model_dump() for comm in self.communications],
            "freestyle_data": [fs.model_dump() for fs in self.freestyle_data],
            "sales_metrics": [sm.model_dump() for sm in self.sales_metrics]
        }
    
    def get_accounts(self) -> List[Account]:
        """Get all generated accounts."""
        return self.accounts
    
    def get_high_risk_accounts(self) -> List[Account]:
        """Get accounts with high churn risk."""
        return [acc for acc in self.accounts if acc.churn_risk_score > 70]
    
    def get_top_opportunities(self, limit: int = 10) -> List[Opportunity]:
        """Get top opportunities by amount."""
        return sorted(self.opportunities, key=lambda x: x.amount, reverse=True)[:limit]
    
    def get_opportunities(self) -> List[Opportunity]:
        """Get all generated opportunities."""
        return self.opportunities
    
    def get_communications(self) -> List[Communication]:
        """Get all generated communications."""
        return self.communications
