"""
Forecasting Agent for Coca-Cola Sales Framework
Provides sales forecasting, pipeline analysis, and predictive insights
"""

from typing import List, Dict, Any, Optional, Tuple
import json
import logging
from datetime import datetime, timedelta
from statistics import mean, stdev
import random
from collections import defaultdict

logger = logging.getLogger(__name__)

class ForecastingAgent:
    """AI Agent for sales forecasting and pipeline analysis"""
    
    def __init__(self, kernel=None):
        self.kernel = kernel
        
    async def generate_sales_forecast(self, opportunities: List[Dict[str, Any]], 
                                     historical_data: Optional[List[Dict[str, Any]]] = None,
                                     timeframe_months: int = 3) -> Dict[str, Any]:
        """Generate comprehensive sales forecast"""
        
        if not opportunities:
            return {
                "forecast_total": 0,
                "confidence_level": "Low",
                "monthly_breakdown": [],
                "risk_adjusted_total": 0,
                "forecast_accuracy": "Unknown"
            }
        
        # Calculate weighted forecast
        forecast_total = 0
        monthly_forecast = defaultdict(float)
        
        for opp in opportunities:
            if opp.get('stage') in ['Closed Lost']:
                continue
                
            value = opp.get('value', 0)
            probability = opp.get('probability', 0) / 100
            weighted_value = value * probability
            
            # Distribute across months based on close date
            try:
                close_date = datetime.fromisoformat(opp.get('close_date', '').replace('Z', '+00:00'))
                month_key = close_date.strftime('%Y-%m')
                monthly_forecast[month_key] += weighted_value
                forecast_total += weighted_value
            except:
                # Default to current month if date parsing fails
                current_month = datetime.now().strftime('%Y-%m')
                monthly_forecast[current_month] += weighted_value
                forecast_total += weighted_value
        
        # Calculate confidence level
        confidence = self._calculate_forecast_confidence(opportunities)
        
        # Risk adjustment
        risk_factor = self._calculate_risk_factor(opportunities)
        risk_adjusted_total = forecast_total * (1 - risk_factor)
        
        # Generate monthly breakdown
        monthly_breakdown = []
        for i in range(timeframe_months):
            month_date = datetime.now() + timedelta(days=30 * i)
            month_key = month_date.strftime('%Y-%m')
            month_name = month_date.strftime('%B %Y')
            
            monthly_breakdown.append({
                "month": month_name,
                "forecast": round(monthly_forecast.get(month_key, 0), 2),
                "opportunity_count": len([o for o in opportunities 
                                        if o.get('close_date', '').startswith(month_key)])
            })
        
        return {
            "forecast_total": round(forecast_total, 2),
            "confidence_level": confidence,
            "monthly_breakdown": monthly_breakdown,
            "risk_adjusted_total": round(risk_adjusted_total, 2),
            "forecast_accuracy": self._estimate_accuracy(opportunities, historical_data),
            "key_assumptions": self._generate_forecast_assumptions(opportunities),
            "risk_factors": self._identify_forecast_risks(opportunities)
        }
    
    async def analyze_pipeline_health(self, opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze overall pipeline health and velocity"""
        
        if not opportunities:
            return {
                "health_score": 0,
                "velocity_score": 0,
                "stage_distribution": {},
                "bottlenecks": [],
                "recommendations": ["Build pipeline with new opportunities"]
            }
        
        # Pipeline composition analysis
        stage_distribution = defaultdict(lambda: {"count": 0, "value": 0})
        total_value = 0
        
        for opp in opportunities:
            if opp.get('stage') not in ['Closed Lost']:
                stage = opp.get('stage', 'Unknown')
                value = opp.get('value', 0)
                stage_distribution[stage]["count"] += 1
                stage_distribution[stage]["value"] += value
                total_value += value
        
        # Convert to percentages
        stage_percentages = {}
        for stage, data in stage_distribution.items():
            stage_percentages[stage] = {
                "count_percent": round((data["count"] / len(opportunities)) * 100, 1),
                "value_percent": round((data["value"] / total_value) * 100, 1) if total_value > 0 else 0,
                "count": data["count"],
                "value": data["value"]
            }
        
        # Calculate health score
        health_score = self._calculate_pipeline_health_score(opportunities, stage_distribution)
        
        # Calculate velocity
        velocity_score = self._calculate_pipeline_velocity(opportunities)
        
        # Identify bottlenecks
        bottlenecks = self._identify_pipeline_bottlenecks(opportunities, stage_distribution)
        
        # Generate recommendations
        recommendations = self._generate_pipeline_recommendations(health_score, velocity_score, bottlenecks)
        
        return {
            "health_score": health_score,
            "velocity_score": velocity_score,
            "stage_distribution": stage_percentages,
            "total_pipeline_value": round(total_value, 2),
            "average_deal_size": round(total_value / len(opportunities), 2) if opportunities else 0,
            "bottlenecks": bottlenecks,
            "recommendations": recommendations,
            "conversion_rates": self._calculate_conversion_rates(opportunities)
        }
    
    async def predict_deal_outcomes(self, opportunities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict outcomes for individual deals"""
        
        predictions = []
        
        for opp in opportunities:
            if opp.get('stage') in ['Closed Won', 'Closed Lost']:
                continue
                
            prediction = self._predict_single_deal(opp)
            predictions.append({
                "opportunity_id": opp.get('id'),
                "account_name": opp.get('account_name'),
                "value": opp.get('value'),
                "current_stage": opp.get('stage'),
                "predicted_outcome": prediction["outcome"],
                "win_probability": prediction["win_probability"],
                "predicted_close_date": prediction["close_date"],
                "risk_factors": prediction["risk_factors"],
                "success_factors": prediction["success_factors"],
                "next_actions": prediction["next_actions"]
            })
        
        # Sort by win probability (descending)
        predictions.sort(key=lambda x: x["win_probability"], reverse=True)
        
        return predictions
    
    async def analyze_win_loss_patterns(self, historical_opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze win/loss patterns to improve forecasting"""
        
        if not historical_opportunities:
            return {
                "overall_win_rate": 0,
                "win_factors": [],
                "loss_factors": [],
                "stage_conversion_rates": {},
                "insights": ["Insufficient historical data"]
            }
        
        won_deals = [o for o in historical_opportunities if o.get('stage') == 'Closed Won']
        lost_deals = [o for o in historical_opportunities if o.get('stage') == 'Closed Lost']
        
        overall_win_rate = len(won_deals) / len(historical_opportunities) * 100 if historical_opportunities else 0
        
        # Analyze winning factors
        win_factors = self._analyze_winning_factors(won_deals)
        
        # Analyze loss factors
        loss_factors = self._analyze_loss_factors(lost_deals)
        
        # Calculate stage conversion rates
        stage_conversions = self._calculate_stage_conversions(historical_opportunities)
        
        # Generate insights
        insights = self._generate_win_loss_insights(won_deals, lost_deals, overall_win_rate)
        
        return {
            "overall_win_rate": round(overall_win_rate, 1),
            "total_won": len(won_deals),
            "total_lost": len(lost_deals),
            "win_factors": win_factors,
            "loss_factors": loss_factors,
            "stage_conversion_rates": stage_conversions,
            "average_deal_cycle": self._calculate_average_cycle_time(won_deals),
            "insights": insights,
            "recommendations": self._generate_win_loss_recommendations(win_factors, loss_factors)
        }
    
    def _calculate_forecast_confidence(self, opportunities: List[Dict[str, Any]]) -> str:
        """Calculate confidence level for forecast"""
        if not opportunities:
            return "Low"
        
        confidence_score = 0
        
        # Pipeline size factor
        if len(opportunities) >= 20:
            confidence_score += 30
        elif len(opportunities) >= 10:
            confidence_score += 20
        else:
            confidence_score += 10
        
        # Stage distribution factor
        advanced_stage_count = len([o for o in opportunities 
                                  if o.get('stage') in ['Proposal', 'Negotiation']])
        if advanced_stage_count >= len(opportunities) * 0.3:
            confidence_score += 30
        elif advanced_stage_count >= len(opportunities) * 0.2:
            confidence_score += 20
        else:
            confidence_score += 10
        
        # Data quality factor
        complete_data_count = len([o for o in opportunities 
                                 if all(o.get(field) for field in ['value', 'probability', 'close_date'])])
        data_quality = complete_data_count / len(opportunities)
        confidence_score += int(data_quality * 40)
        
        if confidence_score >= 80:
            return "High"
        elif confidence_score >= 60:
            return "Medium"
        else:
            return "Low"
    
    def _calculate_risk_factor(self, opportunities: List[Dict[str, Any]]) -> float:
        """Calculate risk adjustment factor"""
        if not opportunities:
            return 0.3  # Default 30% risk
        
        risk_factors = 0
        
        # Long stale deals
        stale_deals = len([o for o in opportunities if o.get('days_in_stage', 0) > 60])
        risk_factors += (stale_deals / len(opportunities)) * 0.2
        
        # Low probability deals
        low_prob_deals = len([o for o in opportunities if o.get('probability', 0) < 30])
        risk_factors += (low_prob_deals / len(opportunities)) * 0.15
        
        # Concentration risk (single large deal)
        values = [o.get('value', 0) for o in opportunities]
        if values:
            max_deal = max(values)
            total_value = sum(values)
            if max_deal > total_value * 0.5:  # One deal is >50% of pipeline
                risk_factors += 0.15
        
        return min(risk_factors, 0.4)  # Cap at 40% risk
    
    def _estimate_accuracy(self, opportunities: List[Dict[str, Any]], 
                          historical_data: Optional[List[Dict[str, Any]]]) -> str:
        """Estimate forecast accuracy based on historical performance"""
        if not historical_data:
            return "Unknown - No historical data"
        
        # Simplified accuracy estimation
        # In a real implementation, this would compare past forecasts to actual results
        pipeline_quality = self._assess_pipeline_quality(opportunities)
        
        if pipeline_quality >= 80:
            return "High (±10%)"
        elif pipeline_quality >= 60:
            return "Medium (±20%)"
        else:
            return "Low (±30%)"
    
    def _generate_forecast_assumptions(self, opportunities: List[Dict[str, Any]]) -> List[str]:
        """Generate key forecast assumptions"""
        assumptions = [
            "Probabilities reflect actual likelihood of closure",
            "No major market disruptions expected",
            "Current sales velocity continues"
        ]
        
        if opportunities:
            avg_cycle = mean([o.get('days_in_stage', 30) for o in opportunities])
            assumptions.append(f"Average sales cycle: {avg_cycle:.0f} days")
        
        return assumptions
    
    def _identify_forecast_risks(self, opportunities: List[Dict[str, Any]]) -> List[str]:
        """Identify key risks to forecast"""
        risks = []
        
        if not opportunities:
            return ["No active pipeline"]
        
        # Concentration risk
        values = [o.get('value', 0) for o in opportunities]
        if values and max(values) > sum(values) * 0.4:
            risks.append("High concentration in single deal")
        
        # Stale pipeline
        stale_count = len([o for o in opportunities if o.get('days_in_stage', 0) > 60])
        if stale_count > len(opportunities) * 0.3:
            risks.append("High number of stale opportunities")
        
        # Low probability deals
        low_prob = len([o for o in opportunities if o.get('probability', 0) < 30])
        if low_prob > len(opportunities) * 0.5:
            risks.append("Many low-probability opportunities")
        
        return risks[:3]  # Return top 3 risks
    
    def _calculate_pipeline_health_score(self, opportunities: List[Dict[str, Any]], 
                                       stage_distribution: Dict) -> int:
        """Calculate overall pipeline health score"""
        if not opportunities:
            return 0
        
        score = 0
        
        # Stage distribution health (30 points)
        total_count = len(opportunities)
        early_stage_ratio = (stage_distribution.get('Prospecting', {}).get('count', 0) + 
                           stage_distribution.get('Qualification', {}).get('count', 0)) / total_count
        
        if 0.3 <= early_stage_ratio <= 0.6:  # Healthy range
            score += 30
        else:
            score += int(30 * (1 - abs(early_stage_ratio - 0.45) / 0.45))
        
        # Pipeline size (25 points)
        if total_count >= 20:
            score += 25
        elif total_count >= 10:
            score += 20
        else:
            score += total_count
        
        # Average deal size (20 points)
        avg_deal = mean([o.get('value', 0) for o in opportunities])
        if avg_deal >= 50000:
            score += 20
        elif avg_deal >= 25000:
            score += 15
        else:
            score += 10
        
        # Velocity (25 points)
        avg_days_in_stage = mean([o.get('days_in_stage', 30) for o in opportunities])
        if avg_days_in_stage <= 30:
            score += 25
        elif avg_days_in_stage <= 45:
            score += 20
        else:
            score += 10
        
        return min(score, 100)
    
    def _calculate_pipeline_velocity(self, opportunities: List[Dict[str, Any]]) -> int:
        """Calculate pipeline velocity score"""
        if not opportunities:
            return 0
        
        # Calculate based on days in stage
        avg_days = mean([o.get('days_in_stage', 30) for o in opportunities])
        
        if avg_days <= 20:
            return 90
        elif avg_days <= 30:
            return 80
        elif avg_days <= 45:
            return 60
        elif avg_days <= 60:
            return 40
        else:
            return 20
    
    def _identify_pipeline_bottlenecks(self, opportunities: List[Dict[str, Any]], 
                                     stage_distribution: Dict) -> List[str]:
        """Identify pipeline bottlenecks"""
        bottlenecks = []
        
        if not opportunities:
            return ["No pipeline to analyze"]
        
        total_count = len(opportunities)
        
        # Check for stage concentrations
        for stage, data in stage_distribution.items():
            if stage == 'Closed Won':
                continue
                
            stage_ratio = data["count"] / total_count
            if stage_ratio > 0.4:  # More than 40% in one stage
                bottlenecks.append(f"Too many deals stuck in {stage}")
        
        # Check for stale deals
        stale_deals = len([o for o in opportunities if o.get('days_in_stage', 0) > 60])
        if stale_deals > total_count * 0.3:
            bottlenecks.append("High number of stale opportunities")
        
        # Check for low conversion
        qualified_deals = stage_distribution.get('Qualification', {}).get('count', 0)
        proposal_deals = stage_distribution.get('Proposal', {}).get('count', 0)
        
        if qualified_deals > 0 and proposal_deals / qualified_deals < 0.3:
            bottlenecks.append("Low qualification to proposal conversion")
        
        return bottlenecks[:3]  # Return top 3 bottlenecks
    
    def _generate_pipeline_recommendations(self, health_score: int, velocity_score: int, 
                                         bottlenecks: List[str]) -> List[str]:
        """Generate pipeline improvement recommendations"""
        recommendations = []
        
        if health_score < 60:
            recommendations.append("Focus on building a healthier pipeline mix")
        
        if velocity_score < 60:
            recommendations.append("Accelerate deal progression through stages")
        
        if "stale" in " ".join(bottlenecks).lower():
            recommendations.append("Review and action stale opportunities")
        
        if "stuck" in " ".join(bottlenecks).lower():
            recommendations.append("Implement stage-specific coaching")
        
        if not recommendations:
            recommendations.append("Continue current pipeline management practices")
        
        return recommendations[:3]
    
    def _calculate_conversion_rates(self, opportunities: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculate conversion rates between stages"""
        stage_counts = defaultdict(int)
        
        for opp in opportunities:
            stage = opp.get('stage', 'Unknown')
            stage_counts[stage] += 1
        
        total_opps = len(opportunities)
        conversion_rates = {}
        
        if total_opps > 0:
            for stage, count in stage_counts.items():
                conversion_rates[stage] = round((count / total_opps) * 100, 1)
        
        return conversion_rates
    
    def _predict_single_deal(self, opportunity: Dict[str, Any]) -> Dict[str, Any]:
        """Predict outcome for a single deal"""
        # Base probability
        base_prob = opportunity.get('probability', 50)
        
        # Adjust based on various factors
        adjusted_prob = base_prob
        
        # Stage factor
        stage = opportunity.get('stage', '')
        stage_multipliers = {
            'Prospecting': 0.8,
            'Qualification': 0.9,
            'Proposal': 1.1,
            'Negotiation': 1.2
        }
        adjusted_prob *= stage_multipliers.get(stage, 1.0)
        
        # Days in stage factor
        days_in_stage = opportunity.get('days_in_stage', 0)
        if days_in_stage > 60:
            adjusted_prob *= 0.7
        elif days_in_stage > 30:
            adjusted_prob *= 0.9
        
        # Value factor (larger deals may be harder to close)
        value = opportunity.get('value', 0)
        if value > 100000:
            adjusted_prob *= 0.9
        
        adjusted_prob = max(10, min(95, adjusted_prob))  # Keep between 10-95%
        
        # Determine outcome
        outcome = "Win" if adjusted_prob > 50 else "At Risk"
        
        # Risk factors
        risk_factors = []
        if days_in_stage > 45:
            risk_factors.append("Deal has been stalled")
        if adjusted_prob < 40:
            risk_factors.append("Low win probability")
        if value > 100000:
            risk_factors.append("High-value deal complexity")
        
        # Success factors
        success_factors = []
        if stage in ['Proposal', 'Negotiation']:
            success_factors.append("Advanced sales stage")
        if adjusted_prob > 70:
            success_factors.append("High win probability")
        
        # Next actions
        next_actions = []
        if stage == 'Prospecting':
            next_actions.append("Qualify decision makers")
        elif stage == 'Qualification':
            next_actions.append("Present proposal")
        elif stage == 'Proposal':
            next_actions.append("Address objections")
        elif stage == 'Negotiation':
            next_actions.append("Finalize terms")
        
        # Predicted close date
        try:
            current_close = datetime.fromisoformat(opportunity.get('close_date', '').replace('Z', '+00:00'))
            if days_in_stage > 45:
                # Likely to slip
                predicted_close = current_close + timedelta(days=30)
            else:
                predicted_close = current_close
            predicted_close_str = predicted_close.strftime('%Y-%m-%d')
        except:
            predicted_close_str = opportunity.get('close_date', 'Unknown')
        
        return {
            "outcome": outcome,
            "win_probability": round(adjusted_prob, 1),
            "close_date": predicted_close_str,
            "risk_factors": risk_factors,
            "success_factors": success_factors,
            "next_actions": next_actions
        }
    
    def _analyze_winning_factors(self, won_deals: List[Dict[str, Any]]) -> List[str]:
        """Analyze common factors in won deals"""
        if not won_deals:
            return []
        
        factors = []
        
        # Average deal size
        avg_won_value = mean([d.get('value', 0) for d in won_deals])
        factors.append(f"Average won deal size: ${avg_won_value:,.0f}")
        
        # Common product lines
        product_counts = defaultdict(int)
        for deal in won_deals:
            product = deal.get('product_line', 'Unknown')
            product_counts[product] += 1
        
        if product_counts:
            top_product = max(product_counts, key=product_counts.get)
            factors.append(f"Most successful product: {top_product}")
        
        # Fast closers
        quick_wins = len([d for d in won_deals if d.get('days_in_stage', 0) <= 30])
        if quick_wins > len(won_deals) * 0.5:
            factors.append("Fast deal progression increases win rate")
        
        return factors[:3]
    
    def _analyze_loss_factors(self, lost_deals: List[Dict[str, Any]]) -> List[str]:
        """Analyze common factors in lost deals"""
        if not lost_deals:
            return []
        
        factors = []
        
        # Stale deals
        stale_losses = len([d for d in lost_deals if d.get('days_in_stage', 0) > 60])
        if stale_losses > len(lost_deals) * 0.4:
            factors.append("Stale deals more likely to be lost")
        
        # Size factor
        avg_lost_value = mean([d.get('value', 0) for d in lost_deals])
        factors.append(f"Average lost deal size: ${avg_lost_value:,.0f}")
        
        # Common loss reasons (if available in data)
        factors.append("Price competition frequently cited")
        
        return factors[:3]
    
    def _calculate_stage_conversions(self, historical_deals: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculate conversion rates between stages"""
        stage_order = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation', 'Closed Won']
        conversions = {}
        
        for i in range(len(stage_order) - 1):
            current_stage = stage_order[i]
            next_stage = stage_order[i + 1]
            
            current_count = len([d for d in historical_deals if d.get('stage') == current_stage])
            next_count = len([d for d in historical_deals if d.get('stage') == next_stage])
            
            if current_count > 0:
                conversion_rate = (next_count / current_count) * 100
                conversions[f"{current_stage} to {next_stage}"] = round(conversion_rate, 1)
        
        return conversions
    
    def _calculate_average_cycle_time(self, won_deals: List[Dict[str, Any]]) -> int:
        """Calculate average sales cycle time for won deals"""
        if not won_deals:
            return 0
        
        # Simplified calculation - in reality, this would track from opportunity creation to close
        cycle_times = [d.get('days_in_stage', 30) for d in won_deals]
        return int(mean(cycle_times))
    
    def _generate_win_loss_insights(self, won_deals: List[Dict[str, Any]], 
                                  lost_deals: List[Dict[str, Any]], 
                                  win_rate: float) -> List[str]:
        """Generate insights from win/loss analysis"""
        insights = []
        
        if win_rate > 60:
            insights.append("Strong win rate indicates effective sales process")
        elif win_rate < 30:
            insights.append("Low win rate suggests need for process improvement")
        else:
            insights.append("Moderate win rate with room for improvement")
        
        if won_deals and lost_deals:
            won_avg = mean([d.get('value', 0) for d in won_deals])
            lost_avg = mean([d.get('value', 0) for d in lost_deals])
            
            if won_avg > lost_avg * 1.2:
                insights.append("Larger deals have higher success rate")
            elif lost_avg > won_avg * 1.2:
                insights.append("Smaller deals close more successfully")
        
        return insights[:3]
    
    def _generate_win_loss_recommendations(self, win_factors: List[str], 
                                         loss_factors: List[str]) -> List[str]:
        """Generate recommendations based on win/loss analysis"""
        recommendations = []
        
        if "Fast deal progression" in " ".join(win_factors):
            recommendations.append("Focus on accelerating deal velocity")
        
        if "Stale deals" in " ".join(loss_factors):
            recommendations.append("Implement regular pipeline reviews")
        
        if "Price competition" in " ".join(loss_factors):
            recommendations.append("Strengthen value proposition messaging")
        
        recommendations.append("Continue tracking win/loss patterns")
        
        return recommendations[:3]
    
    def _assess_pipeline_quality(self, opportunities: List[Dict[str, Any]]) -> int:
        """Assess overall pipeline quality score"""
        if not opportunities:
            return 0
        
        quality_score = 0
        
        # Data completeness
        complete_opps = len([o for o in opportunities 
                           if all(o.get(field) for field in ['value', 'probability', 'close_date'])])
        quality_score += (complete_opps / len(opportunities)) * 40
        
        # Stage distribution
        advanced_opps = len([o for o in opportunities 
                           if o.get('stage') in ['Proposal', 'Negotiation']])
        quality_score += min((advanced_opps / len(opportunities)) * 30, 30)
        
        # Freshness
        fresh_opps = len([o for o in opportunities if o.get('days_in_stage', 0) <= 45])
        quality_score += (fresh_opps / len(opportunities)) * 30
        
        return int(quality_score)
