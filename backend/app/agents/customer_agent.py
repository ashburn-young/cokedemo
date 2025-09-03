"""
Customer Insights Agent for Coca-Cola Sales Framework
Provides customer behavior analysis, sentiment tracking, and relationship insights
"""

from typing import List, Dict, Any, Optional
import json
import logging
from datetime import datetime, timedelta
from statistics import mean

logger = logging.getLogger(__name__)

class CustomerInsightsAgent:
    """AI Agent for customer insights and relationship analysis"""
    
    def __init__(self, kernel=None):
        self.kernel = kernel
        
    async def analyze_customer_sentiment(self, communications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze customer sentiment from communications"""
        
        if not communications:
            return {
                "overall_sentiment": 0.5,
                "sentiment_trend": "neutral",
                "key_themes": ["No recent communications"],
                "risk_indicators": [],
                "positive_signals": []
            }
        
        # Calculate sentiment metrics
        sentiments = [comm.get('sentiment', 0.5) for comm in communications]
        overall_sentiment = mean(sentiments)
        
        # Recent sentiment trend
        recent_comms = sorted(communications, key=lambda x: x.get('date', ''), reverse=True)[:5]
        recent_sentiments = [comm.get('sentiment', 0.5) for comm in recent_comms]
        recent_avg = mean(recent_sentiments) if recent_sentiments else 0.5
        
        # Determine trend
        if recent_avg > overall_sentiment + 0.1:
            trend = "improving"
        elif recent_avg < overall_sentiment - 0.1:
            trend = "declining"
        else:
            trend = "stable"
        
        # Extract themes and indicators
        key_themes = self._extract_themes(communications)
        risk_indicators = self._identify_risk_indicators(communications)
        positive_signals = self._identify_positive_signals(communications)
        
        return {
            "overall_sentiment": round(overall_sentiment, 2),
            "sentiment_trend": trend,
            "recent_sentiment": round(recent_avg, 2),
            "key_themes": key_themes,
            "risk_indicators": risk_indicators,
            "positive_signals": positive_signals,
            "communication_volume": len(communications),
            "engagement_score": self._calculate_engagement_score(communications)
        }
    
    async def predict_churn_risk(self, account_data: Dict[str, Any], 
                                communications: List[Dict[str, Any]],
                                opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Predict customer churn risk based on multiple factors"""
        
        risk_score = 0
        risk_factors = []
        
        # Communication frequency analysis
        recent_comms = len([c for c in communications 
                           if (datetime.now() - datetime.fromisoformat(c.get('date', '2024-01-01'))).days < 30])
        
        if recent_comms == 0:
            risk_score += 30
            risk_factors.append("No recent communications (30 days)")
        elif recent_comms < 3:
            risk_score += 15
            risk_factors.append("Low communication frequency")
        
        # Sentiment analysis
        if communications:
            avg_sentiment = mean([c.get('sentiment', 0.5) for c in communications])
            if avg_sentiment < 0.3:
                risk_score += 25
                risk_factors.append("Negative customer sentiment")
            elif avg_sentiment < 0.5:
                risk_score += 10
                risk_factors.append("Below-average sentiment")
        
        # Opportunity pipeline analysis
        active_opps = [o for o in opportunities if o.get('stage') not in ['Closed Won', 'Closed Lost']]
        if not active_opps:
            risk_score += 20
            risk_factors.append("No active opportunities")
        
        # Account health score
        health_score = account_data.get('health_score', 50)
        if health_score < 30:
            risk_score += 20
            risk_factors.append("Low account health score")
        elif health_score < 50:
            risk_score += 10
            risk_factors.append("Below-average account health")
        
        # Deal velocity analysis
        stalled_deals = len([o for o in opportunities if o.get('days_in_stage', 0) > 45])
        if stalled_deals > 0:
            risk_score += stalled_deals * 5
            risk_factors.append(f"{stalled_deals} stalled opportunities")
        
        # Determine risk level
        if risk_score >= 60:
            risk_level = "High"
        elif risk_score >= 30:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        return {
            "risk_level": risk_level,
            "risk_score": min(risk_score, 100),
            "risk_factors": risk_factors,
            "recommendations": self._generate_retention_recommendations(risk_level, risk_factors),
            "next_actions": self._suggest_retention_actions(risk_level),
            "timeline": "30 days" if risk_level == "High" else "60 days"
        }
    
    async def analyze_buying_patterns(self, account_data: Dict[str, Any],
                                     opportunities: List[Dict[str, Any]],
                                     telemetry: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze customer buying patterns and preferences"""
        
        if not opportunities and not telemetry:
            return {
                "patterns": [],
                "preferences": [],
                "seasonality": "Unknown",
                "volume_trend": "Unknown",
                "recommendations": ["Gather more transaction data"]
            }
        
        patterns = []
        preferences = []
        
        # Analyze opportunity patterns
        if opportunities:
            # Product preferences
            product_counts = {}
            for opp in opportunities:
                product = opp.get('product_line', 'Unknown')
                product_counts[product] = product_counts.get(product, 0) + 1
            
            if product_counts:
                preferred_product = max(product_counts, key=product_counts.get)
                preferences.append(f"Prefers {preferred_product}")
            
            # Deal size patterns
            deal_values = [opp.get('value', 0) for opp in opportunities if opp.get('value')]
            if deal_values:
                avg_deal = mean(deal_values)
                patterns.append(f"Average deal size: ${avg_deal:,.0f}")
            
            # Seasonal patterns (simplified)
            monthly_counts = {}
            for opp in opportunities:
                date_str = opp.get('close_date', '')
                try:
                    month = datetime.fromisoformat(date_str.replace('Z', '+00:00')).month
                    monthly_counts[month] = monthly_counts.get(month, 0) + 1
                except:
                    continue
            
            if monthly_counts:
                peak_month = max(monthly_counts, key=monthly_counts.get)
                month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                patterns.append(f"Peak activity in {month_names[peak_month]}")
        
        # Analyze telemetry patterns
        if telemetry:
            volume_data = [t.get('volume', 0) for t in telemetry if t.get('volume')]
            if volume_data:
                avg_volume = mean(volume_data)
                patterns.append(f"Average daily volume: {avg_volume:.0f} units")
        
        return {
            "patterns": patterns,
            "preferences": preferences,
            "seasonality": self._determine_seasonality(opportunities),
            "volume_trend": self._calculate_volume_trend(telemetry),
            "recommendations": self._generate_buying_recommendations(patterns, preferences)
        }
    
    def _extract_themes(self, communications: List[Dict[str, Any]]) -> List[str]:
        """Extract key themes from communications"""
        themes = []
        
        # Simple keyword-based theme extraction
        keywords = {
            "pricing": ["price", "cost", "budget", "expensive", "cheap"],
            "quality": ["quality", "taste", "fresh", "flavor"],
            "delivery": ["delivery", "shipping", "logistics", "late"],
            "service": ["service", "support", "help", "issue", "problem"],
            "volume": ["volume", "quantity", "amount", "increase", "decrease"]
        }
        
        for comm in communications:
            content = comm.get('content', '').lower()
            for theme, words in keywords.items():
                if any(word in content for word in words):
                    if theme not in themes:
                        themes.append(theme)
        
        return themes[:5]  # Return top 5 themes
    
    def _identify_risk_indicators(self, communications: List[Dict[str, Any]]) -> List[str]:
        """Identify risk indicators from communications"""
        indicators = []
        
        risk_keywords = ["complaint", "issue", "problem", "unhappy", "disappointed", 
                        "cancel", "terminate", "competitor", "cheaper", "alternative"]
        
        for comm in communications:
            content = comm.get('content', '').lower()
            sentiment = comm.get('sentiment', 0.5)
            
            if sentiment < 0.3:
                indicators.append("Low sentiment in recent communication")
            
            for keyword in risk_keywords:
                if keyword in content:
                    indicators.append(f"Mentioned: {keyword}")
                    break
        
        return list(set(indicators))[:3]  # Return unique indicators, max 3
    
    def _identify_positive_signals(self, communications: List[Dict[str, Any]]) -> List[str]:
        """Identify positive signals from communications"""
        signals = []
        
        positive_keywords = ["satisfied", "happy", "excellent", "great", "love", 
                           "expand", "increase", "more", "additional", "recommend"]
        
        for comm in communications:
            content = comm.get('content', '').lower()
            sentiment = comm.get('sentiment', 0.5)
            
            if sentiment > 0.7:
                signals.append("High satisfaction in recent communication")
            
            for keyword in positive_keywords:
                if keyword in content:
                    signals.append(f"Positive indicator: {keyword}")
                    break
        
        return list(set(signals))[:3]  # Return unique signals, max 3
    
    def _calculate_engagement_score(self, communications: List[Dict[str, Any]]) -> int:
        """Calculate customer engagement score"""
        if not communications:
            return 0
        
        score = 0
        
        # Frequency score (30 days)
        recent_comms = len([c for c in communications 
                           if (datetime.now() - datetime.fromisoformat(c.get('date', '2024-01-01'))).days < 30])
        score += min(recent_comms * 10, 40)  # Max 40 points for frequency
        
        # Sentiment score
        avg_sentiment = mean([c.get('sentiment', 0.5) for c in communications])
        score += int(avg_sentiment * 30)  # Max 30 points for sentiment
        
        # Response rate (simplified assumption)
        score += 30  # Base response engagement
        
        return min(score, 100)
    
    def _generate_retention_recommendations(self, risk_level: str, risk_factors: List[str]) -> List[str]:
        """Generate retention recommendations based on risk"""
        recommendations = []
        
        if risk_level == "High":
            recommendations.extend([
                "Schedule immediate executive meeting",
                "Conduct customer satisfaction survey",
                "Review and adjust pricing if needed",
                "Assign dedicated account manager"
            ])
        elif risk_level == "Medium":
            recommendations.extend([
                "Increase communication frequency",
                "Schedule quarterly business review",
                "Explore upselling opportunities",
                "Monitor account health closely"
            ])
        else:
            recommendations.extend([
                "Maintain regular touchpoints",
                "Continue value-based selling",
                "Monitor for expansion opportunities"
            ])
        
        # Add specific recommendations based on risk factors
        if "No recent communications" in risk_factors:
            recommendations.append("Establish regular communication cadence")
        
        if "Negative customer sentiment" in risk_factors:
            recommendations.append("Address customer concerns immediately")
        
        return recommendations[:5]  # Limit to 5 recommendations
    
    def _suggest_retention_actions(self, risk_level: str) -> List[str]:
        """Suggest immediate retention actions"""
        if risk_level == "High":
            return [
                "Call customer within 24 hours",
                "Schedule face-to-face meeting",
                "Escalate to senior management"
            ]
        elif risk_level == "Medium":
            return [
                "Schedule call within week",
                "Send customer satisfaction survey",
                "Review account performance"
            ]
        else:
            return [
                "Continue regular check-ins",
                "Monitor account metrics",
                "Look for growth opportunities"
            ]
    
    def _determine_seasonality(self, opportunities: List[Dict[str, Any]]) -> str:
        """Determine seasonal buying patterns"""
        if not opportunities:
            return "Unknown"
        
        # Simplified seasonality detection
        monthly_values = {}
        for opp in opportunities:
            try:
                date_str = opp.get('close_date', '')
                month = datetime.fromisoformat(date_str.replace('Z', '+00:00')).month
                value = opp.get('value', 0)
                monthly_values[month] = monthly_values.get(month, 0) + value
            except:
                continue
        
        if not monthly_values:
            return "Unknown"
        
        # Simple peak detection
        max_month = max(monthly_values, key=monthly_values.get)
        if max_month in [12, 1, 2]:
            return "Winter peak"
        elif max_month in [6, 7, 8]:
            return "Summer peak"
        else:
            return "Moderate seasonality"
    
    def _calculate_volume_trend(self, telemetry: List[Dict[str, Any]]) -> str:
        """Calculate volume trend from telemetry data"""
        if len(telemetry) < 2:
            return "Insufficient data"
        
        # Sort by date and calculate trend
        sorted_data = sorted(telemetry, key=lambda x: x.get('date', ''))
        if len(sorted_data) < 5:
            return "Insufficient data"
        
        recent_avg = mean([t.get('volume', 0) for t in sorted_data[-5:]])
        earlier_avg = mean([t.get('volume', 0) for t in sorted_data[:5]])
        
        if recent_avg > earlier_avg * 1.1:
            return "Increasing"
        elif recent_avg < earlier_avg * 0.9:
            return "Decreasing"
        else:
            return "Stable"
    
    def _generate_buying_recommendations(self, patterns: List[str], preferences: List[str]) -> List[str]:
        """Generate recommendations based on buying patterns"""
        recommendations = []
        
        if patterns:
            recommendations.append("Leverage identified buying patterns for timing")
        
        if preferences:
            recommendations.append("Focus on preferred product lines")
        
        recommendations.extend([
            "Optimize order scheduling based on patterns",
            "Develop targeted promotions",
            "Monitor volume trends for forecasting"
        ])
        
        return recommendations[:5]
