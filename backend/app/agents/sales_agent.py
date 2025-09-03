"""
Sales Intelligence Agent for Coca-Cola Sales Framework
Provides sales insights, opportunity analysis, and strategic recommendations
"""

from typing import List, Dict, Any, Optional
from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig
from semantic_kernel.functions.kernel_function_decorator import kernel_function
import json
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class SalesIntelligenceAgent:
    """AI Agent for sales intelligence and opportunity analysis"""
    
    def __init__(self, kernel: Kernel):
        self.kernel = kernel
        self.service_id = "sales_service"
        
    async def analyze_opportunity(self, opportunity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a sales opportunity and provide insights"""
        
        prompt = f"""
        You are a senior sales analyst for Coca-Cola with deep expertise in B2B sales, market dynamics, and customer behavior.
        
        Analyze the following sales opportunity and provide strategic insights:
        
        Opportunity Details:
        - Account: {opportunity_data.get('account_name', 'Unknown')}
        - Value: ${opportunity_data.get('value', 0):,.2f}
        - Stage: {opportunity_data.get('stage', 'Unknown')}
        - Product Line: {opportunity_data.get('product_line', 'Unknown')}
        - Close Date: {opportunity_data.get('close_date', 'Unknown')}
        - Probability: {opportunity_data.get('probability', 0)}%
        - Days in Stage: {opportunity_data.get('days_in_stage', 0)}
        
        Provide a comprehensive analysis including:
        1. Risk Assessment (High/Medium/Low with reasoning)
        2. Key Success Factors
        3. Potential Obstacles
        4. Recommended Next Actions
        5. Strategic Value to Coca-Cola
        6. Competitive Considerations
        
        Format your response as a JSON object with these keys: risk_level, risk_reasoning, success_factors, obstacles, next_actions, strategic_value, competitive_notes.
        """
        
        try:
            result = await self.kernel.invoke_prompt(
                prompt,
                arguments=KernelArguments()
            )
            
            # Parse the AI response
            analysis = json.loads(str(result))
            
            # Add calculated metrics
            analysis['opportunity_score'] = self._calculate_opportunity_score(opportunity_data)
            analysis['urgency_level'] = self._assess_urgency(opportunity_data)
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing opportunity: {e}")
            return {
                "risk_level": "Medium",
                "risk_reasoning": "Unable to complete full analysis",
                "success_factors": ["Follow up with customer"],
                "obstacles": ["Analysis incomplete"],
                "next_actions": ["Schedule customer meeting"],
                "strategic_value": "Standard opportunity value",
                "competitive_notes": "Monitor competitive activity",
                "opportunity_score": 50,
                "urgency_level": "Medium"
            }
    
    async def generate_account_insights(self, account_data: Dict[str, Any], 
                                       opportunities: List[Dict[str, Any]], 
                                       communications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive account insights"""
        
        # Calculate account metrics
        total_pipeline = sum(opp.get('value', 0) for opp in opportunities)
        avg_deal_size = total_pipeline / len(opportunities) if opportunities else 0
        win_rate = len([o for o in opportunities if o.get('stage') == 'Closed Won']) / len(opportunities) * 100 if opportunities else 0
        
        # Analyze communication sentiment
        positive_comms = len([c for c in communications if c.get('sentiment', 0) > 0.5])
        sentiment_score = positive_comms / len(communications) * 100 if communications else 50
        
        prompt = f"""
        You are a strategic account manager for Coca-Cola analyzing a key B2B account.
        
        Account Analysis:
        - Account: {account_data.get('name', 'Unknown')}
        - Industry: {account_data.get('industry', 'Unknown')}
        - Size: {account_data.get('size', 'Unknown')}
        - Health Score: {account_data.get('health_score', 50)}/100
        - Total Pipeline: ${total_pipeline:,.2f}
        - Average Deal Size: ${avg_deal_size:,.2f}
        - Win Rate: {win_rate:.1f}%
        - Communication Sentiment: {sentiment_score:.1f}% positive
        - Active Opportunities: {len(opportunities)}
        - Recent Communications: {len(communications)}
        
        Provide strategic account insights including:
        1. Account Health Assessment
        2. Growth Opportunities
        3. Risk Factors
        4. Relationship Strength
        5. Competitive Position
        6. Strategic Recommendations
        
        Format as JSON with keys: health_assessment, growth_opportunities, risk_factors, relationship_strength, competitive_position, recommendations.
        """
        
        try:
            result = await self.kernel.invoke_prompt(
                prompt,
                arguments=KernelArguments()
            )
            
            insights = json.loads(str(result))
            
            # Add calculated metrics
            insights['account_score'] = account_data.get('health_score', 50)
            insights['pipeline_value'] = total_pipeline
            insights['sentiment_trend'] = sentiment_score
            insights['engagement_level'] = self._calculate_engagement_level(communications)
            
            return insights
            
        except Exception as e:
            logger.error(f"Error generating account insights: {e}")
            return {
                "health_assessment": "Requires detailed review",
                "growth_opportunities": ["Expand product portfolio", "Increase order frequency"],
                "risk_factors": ["Limited recent engagement"],
                "relationship_strength": "Moderate",
                "competitive_position": "Competitive market",
                "recommendations": ["Schedule executive meeting", "Review pricing strategy"],
                "account_score": account_data.get('health_score', 50),
                "pipeline_value": total_pipeline,
                "sentiment_trend": sentiment_score,
                "engagement_level": "Medium"
            }
    
    async def recommend_actions(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate actionable recommendations based on sales context"""
        
        prompt = f"""
        You are a Coca-Cola sales AI assistant providing actionable recommendations.
        
        Current Sales Context:
        - Active Opportunities: {context.get('opportunity_count', 0)}
        - Pipeline Value: ${context.get('pipeline_value', 0):,.2f}
        - At-Risk Deals: {context.get('at_risk_count', 0)}
        - Overdue Follow-ups: {context.get('overdue_count', 0)}
        - Average Deal Cycle: {context.get('avg_cycle_days', 30)} days
        
        Generate 5 specific, actionable recommendations to improve sales performance.
        Each recommendation should include:
        - Action title
        - Description
        - Priority (High/Medium/Low)
        - Expected impact
        - Timeline
        
        Format as JSON array with objects containing: title, description, priority, impact, timeline.
        """
        
        try:
            result = await self.kernel.invoke_prompt(
                prompt,
                arguments=KernelArguments()
            )
            
            recommendations = json.loads(str(result))
            
            # Add system-generated recommendations
            system_recs = self._generate_system_recommendations(context)
            
            return recommendations + system_recs
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            return [
                {
                    "title": "Review Pipeline Health",
                    "description": "Conduct comprehensive pipeline review",
                    "priority": "High",
                    "impact": "Improved forecasting accuracy",
                    "timeline": "This week"
                }
            ]
    
    def _calculate_opportunity_score(self, opportunity: Dict[str, Any]) -> int:
        """Calculate opportunity score based on various factors"""
        score = 50  # Base score
        
        # Value factor
        value = opportunity.get('value', 0)
        if value > 100000:
            score += 20
        elif value > 50000:
            score += 10
        
        # Probability factor
        probability = opportunity.get('probability', 0)
        score += probability * 0.3
        
        # Stage factor
        stage = opportunity.get('stage', '')
        stage_scores = {
            'Prospecting': -10,
            'Qualification': 0,
            'Proposal': 10,
            'Negotiation': 20,
            'Closed Won': 50,
            'Closed Lost': -50
        }
        score += stage_scores.get(stage, 0)
        
        # Days in stage factor (penalize stalled deals)
        days_in_stage = opportunity.get('days_in_stage', 0)
        if days_in_stage > 60:
            score -= 20
        elif days_in_stage > 30:
            score -= 10
        
        return max(0, min(100, int(score)))
    
    def _assess_urgency(self, opportunity: Dict[str, Any]) -> str:
        """Assess opportunity urgency"""
        close_date = opportunity.get('close_date')
        if not close_date:
            return "Medium"
        
        try:
            close_dt = datetime.fromisoformat(close_date.replace('Z', '+00:00'))
            days_to_close = (close_dt - datetime.now()).days
            
            if days_to_close < 7:
                return "High"
            elif days_to_close < 30:
                return "Medium"
            else:
                return "Low"
        except:
            return "Medium"
    
    def _calculate_engagement_level(self, communications: List[Dict[str, Any]]) -> str:
        """Calculate engagement level based on communication frequency"""
        if not communications:
            return "Low"
        
        recent_comms = len([c for c in communications 
                           if (datetime.now() - datetime.fromisoformat(c.get('date', '2024-01-01'))).days < 30])
        
        if recent_comms >= 10:
            return "High"
        elif recent_comms >= 5:
            return "Medium"
        else:
            return "Low"
    
    def _generate_system_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate system-based recommendations"""
        recommendations = []
        
        if context.get('at_risk_count', 0) > 0:
            recommendations.append({
                "title": "Address At-Risk Opportunities",
                "description": f"Focus on {context['at_risk_count']} opportunities showing risk indicators",
                "priority": "High",
                "impact": "Prevent revenue loss",
                "timeline": "Immediate"
            })
        
        if context.get('overdue_count', 0) > 0:
            recommendations.append({
                "title": "Complete Overdue Follow-ups",
                "description": f"Address {context['overdue_count']} overdue customer interactions",
                "priority": "Medium",
                "impact": "Improved customer relationships",
                "timeline": "This week"
            })
        
        return recommendations
