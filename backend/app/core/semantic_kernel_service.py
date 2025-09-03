"""
Semantic Kernel service for Coca-Cola Sales AI Agent Framework.

This module provides the core AI capabilities using Microsoft Semantic Kernel
integrated with Azure OpenAI GPT-4o for sales insights and recommendations.
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)

# Note: Semantic Kernel imports may need adjustment based on available packages
try:
    import semantic_kernel as sk
    from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureTextEmbedding
    from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
    from semantic_kernel.contents.chat_history import ChatHistory
    from semantic_kernel.functions.kernel_arguments import KernelArguments
    from semantic_kernel.prompt_template.input_variable import InputVariable
    from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig
    SEMANTIC_KERNEL_AVAILABLE = True
except ImportError:
    # Fallback for when Semantic Kernel is not available
    SEMANTIC_KERNEL_AVAILABLE = False
    sk = None
    logger.warning("Semantic Kernel not available, using fallback implementation")

from app.models.schemas import (
    Account, Opportunity, Communication, SentimentScore,
    AIInsight, ChurnPrediction, HeatmapData, DashboardSummary
)

# Import the new AI agents
from app.agents import SalesIntelligenceAgent, CustomerInsightsAgent, ForecastingAgent


class SemanticKernelService:
    """
    Main service class for AI operations using Semantic Kernel.
    
    This service orchestrates multiple AI agents for different sales functions:
    - Sales intelligence and opportunity analysis
    - Customer insights and sentiment tracking
    - Sales forecasting and pipeline analysis
    - Account health analysis
    - Churn prediction
    - Action recommendations
    """
    
    def __init__(
        self,
        azure_openai_api_key: str,
        azure_openai_endpoint: str,
        deployment_name: str = "gpt-4o",
        api_version: str = "2024-05-01-preview"
    ):
        self.azure_openai_api_key = azure_openai_api_key
        self.azure_openai_endpoint = azure_openai_endpoint
        self.deployment_name = deployment_name
        self.api_version = api_version
        
        self.kernel = None
        self.chat_service = None
        self.embedding_service = None
        
        # Initialize AI agents
        self.sales_agent = None
        self.customer_agent = None
        self.forecasting_agent = None
        
        # Legacy agent functions for backward compatibility
        self.agents = {}
        
        logger.info("SemanticKernelService initialized")
    
    async def initialize(self) -> None:
        """Initialize the Semantic Kernel and AI services."""
        try:
            if SEMANTIC_KERNEL_AVAILABLE:
                # Initialize kernel
                self.kernel = sk.Kernel()
                
                # Add Azure OpenAI chat completion service
                self.chat_service = AzureChatCompletion(
                    deployment_name=self.deployment_name,
                    endpoint=self.azure_openai_endpoint,
                    api_key=self.azure_openai_api_key,
                    api_version=self.api_version
                )
                
                self.kernel.add_service(self.chat_service)
                
                # Initialize AI agents with kernel
                self.sales_agent = SalesIntelligenceAgent(self.kernel)
                self.customer_agent = CustomerInsightsAgent(self.kernel)
                self.forecasting_agent = ForecastingAgent(self.kernel)
                
            else:
                # Initialize agents without kernel (fallback mode)
                self.sales_agent = SalesIntelligenceAgent(None)
                self.customer_agent = CustomerInsightsAgent(None)
                self.forecasting_agent = ForecastingAgent(None)
            
            # Initialize legacy agents for backward compatibility
            await self._initialize_agents()
            
            logger.info("Semantic Kernel service initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize Semantic Kernel service: {str(e)}")
            raise
    
    async def _initialize_agents(self) -> None:
        """Initialize specialized AI agents for different sales functions."""
        
        # Account Health Analyzer Agent
        self.agents["account_health"] = await self._create_account_health_agent()
        
        # Churn Prediction Agent
        self.agents["churn_prediction"] = await self._create_churn_prediction_agent()
        
        # Opportunity Scorer Agent
        self.agents["opportunity_scorer"] = await self._create_opportunity_scorer_agent()
        
        # Sentiment Analyzer Agent
        self.agents["sentiment_analyzer"] = await self._create_sentiment_analyzer_agent()
        
        # Action Recommender Agent
        self.agents["action_recommender"] = await self._create_action_recommender_agent()
        
        # Executive Summary Agent
        self.agents["executive_summary"] = await self._create_executive_summary_agent()
        
        logger.info("All AI agents initialized successfully")
    
    async def _create_account_health_agent(self):
        """Create the Account Health Analyzer agent."""
        prompt = """
        You are an expert Coca-Cola account health analyzer. Your role is to assess the overall health 
        of business relationships with bottlers, retailers, and distributors.
        
        Analyze the following account data and provide:
        1. Overall health score (0-100)
        2. Key health indicators (positive and negative)
        3. Trend analysis
        4. Risk assessment
        5. Recommendations for improvement
        
        Account Data:
        {{$account_data}}
        
        Recent Communications:
        {{$communications}}
        
        Sales Metrics:
        {{$sales_metrics}}
        
        Freestyle Machine Data (if applicable):
        {{$freestyle_data}}
        
        Provide your analysis in JSON format with clear reasoning for each score and recommendation.
        Focus on Coca-Cola-specific business factors like product mix, market share, promotional participation,
        and relationship strength with key decision makers.
        """
        
        return self.kernel.add_function(
            function_name="analyze_account_health",
            plugin_name="AccountHealthPlugin",
            prompt=prompt,
            description="Analyzes account health and provides insights"
        )
    
    async def _create_churn_prediction_agent(self):
        """Create the Churn Prediction agent."""
        prompt = """
        You are a specialized Coca-Cola churn prediction analyst. Your expertise is in identifying 
        early warning signs that indicate a customer might switch to competitors or reduce their business.
        
        Analyze the provided data and predict churn risk:
        
        Account Information:
        {{$account_data}}
        
        Historical Performance:
        {{$performance_history}}
        
        Communication Sentiment:
        {{$sentiment_data}}
        
        Competitive Intelligence:
        {{$competitive_data}}
        
        Provide:
        1. Churn probability (0-100%)
        2. Risk level (Low/Medium/High/Critical)
        3. Top 5 risk factors
        4. Early warning signals detected
        5. Recommended intervention strategies
        6. Timeline for action (urgent/30 days/90 days)
        
        Consider Coca-Cola-specific factors like:
        - Declining SKU diversity
        - Reduced promotional participation
        - Competitor shelf activity
        - Contract renewal timing
        - Freestyle machine performance issues
        - Payment delays or disputes
        
        Return analysis in JSON format.
        """
        
        return self.kernel.add_function(
            function_name="predict_churn_risk",
            plugin_name="ChurnPredictionPlugin", 
            prompt=prompt,
            description="Predicts customer churn risk and recommends interventions"
        )
    
    async def _create_opportunity_scorer_agent(self):
        """Create the Opportunity Scorer agent."""
        prompt = """
        You are a Coca-Cola opportunity scoring specialist. Your role is to evaluate sales opportunities
        and provide actionable insights to help sales teams prioritize and win deals.
        
        Opportunity Details:
        {{$opportunity_data}}
        
        Account Context:
        {{$account_context}}
        
        Historical Win/Loss Data:
        {{$historical_data}}
        
        Competitive Landscape:
        {{$competitive_landscape}}
        
        Provide:
        1. Win probability (0-100%)
        2. Deal quality score
        3. Key success factors
        4. Risk factors and mitigation strategies
        5. Next best actions
        6. Recommended timeline
        7. Required resources/support
        
        Consider Coca-Cola-specific opportunity factors:
        - Product portfolio fit
        - Volume potential vs. current capacity
        - Seasonal demand patterns
        - Regional market dynamics
        - Promotional calendar alignment
        - Freestyle integration opportunities
        - Long-term partnership potential
        
        Provide detailed scoring rationale in JSON format.
        """
        
        return self.kernel.add_function(
            function_name="score_opportunity",
            plugin_name="OpportunityScorerPlugin",
            prompt=prompt,
            description="Scores sales opportunities and provides win strategies"
        )
    
    async def _create_sentiment_analyzer_agent(self):
        """Create the Sentiment Analyzer agent."""
        prompt = """
        You are an expert in analyzing business communication sentiment for Coca-Cola partnerships.
        You understand the nuances of B2B relationships in the beverage industry.
        
        Communication Content:
        {{$communication_content}}
        
        Communication Type: {{$communication_type}}
        Relationship Context: {{$relationship_context}}
        
        Analyze and provide:
        1. Overall sentiment score (Very Positive/Positive/Neutral/Negative/Very Negative)
        2. Confidence level (0-100%)
        3. Key topics and themes identified
        4. Emotional indicators (satisfaction, frustration, urgency, etc.)
        5. Business implications
        6. Suggested response strategy
        7. Escalation recommendations if needed
        
        Look for Coca-Cola-specific sentiment indicators:
        - References to competitor activities
        - Concerns about pricing or margins
        - Satisfaction with product performance
        - Operational issues or supply chain concerns
        - Interest in new products or promotions
        - Contract or partnership satisfaction
        - Market or category performance discussions
        
        Return analysis in JSON format with specific evidence for your assessment.
        """
        
        return self.kernel.add_function(
            function_name="analyze_sentiment",
            plugin_name="SentimentAnalyzerPlugin",
            prompt=prompt,
            description="Analyzes communication sentiment and business implications"
        )
    
    async def _create_action_recommender_agent(self):
        """Create the Action Recommender agent."""
        prompt = """
        You are a strategic Coca-Cola sales action recommender. Your expertise is in prescribing 
        specific, actionable steps to improve account relationships and drive business growth.
        
        Current Situation:
        {{$current_situation}}
        
        Account Profile:
        {{$account_profile}}
        
        Available Resources:
        {{$available_resources}}
        
        Business Objectives:
        {{$business_objectives}}
        
        Based on the situation, recommend:
        1. Top 3 immediate actions (next 7 days)
        2. Medium-term strategies (next 30 days)
        3. Long-term initiatives (next 90 days)
        4. Required resources and budget
        5. Success metrics and KPIs
        6. Risk mitigation steps
        7. Stakeholder involvement needed
        
        Tailor recommendations to Coca-Cola's business context:
        - Promotional campaigns and timing
        - Product mix optimization
        - Freestyle machine opportunities
        - Volume incentives and rebates
        - Category management support
        - Marketing development funds
        - Field sales visit scheduling
        - Executive relationship building
        - Training and capability development
        
        Provide specific, executable recommendations with clear business rationale in JSON format.
        """
        
        return self.kernel.add_function(
            function_name="recommend_actions",
            plugin_name="ActionRecommenderPlugin",
            prompt=prompt,
            description="Recommends specific actions to improve business outcomes"
        )
    
    async def _create_executive_summary_agent(self):
        """Create the Executive Summary agent."""
        prompt = """
        You are a senior Coca-Cola business intelligence analyst creating executive summaries.
        Your role is to synthesize complex sales data into clear, actionable insights for leadership.
        
        Business Data:
        {{$business_data}}
        
        Performance Metrics:
        {{$performance_metrics}}
        
        Market Intelligence:
        {{$market_intelligence}}
        
        Risk Assessment:
        {{$risk_assessment}}
        
        Create an executive summary with:
        1. Key performance highlights
        2. Critical issues requiring attention
        3. Growth opportunities identified
        4. Risk mitigation priorities
        5. Resource allocation recommendations
        6. Strategic initiatives progress
        7. Market trends and competitive insights
        
        Focus on Coca-Cola business priorities:
        - Revenue growth and margin improvement
        - Market share expansion
        - Customer retention and acquisition
        - Operational efficiency
        - Innovation adoption (Freestyle, new products)
        - Partnership strength and satisfaction
        - Regional performance variations
        
        Present insights in clear, executive-friendly format with supporting data and recommended actions.
        """
        
        return self.kernel.add_function(
            function_name="create_executive_summary",
            plugin_name="ExecutiveSummaryPlugin",
            prompt=prompt,
            description="Creates executive summaries of business performance and insights"
        )
    
    async def analyze_account_health(
        self, 
        account: Account, 
        communications: List[Communication] = None,
        sales_metrics: Dict = None,
        freestyle_data: Dict = None
    ) -> Dict[str, Any]:
        """Analyze account health using the specialized agent."""
        try:
            arguments = KernelArguments(
                account_data=account.model_dump_json(),
                communications=json.dumps([c.model_dump() for c in communications] if communications else []),
                sales_metrics=json.dumps(sales_metrics) if sales_metrics else "{}",
                freestyle_data=json.dumps(freestyle_data) if freestyle_data else "{}"
            )
            
            result = await self.kernel.invoke(
                self.agents["account_health"],
                arguments
            )
            
            return json.loads(str(result))
            
        except Exception as e:
            logger.error(f"Error analyzing account health: {str(e)}")
            raise
    
    async def predict_churn_risk(
        self,
        account: Account,
        performance_history: Dict,
        sentiment_data: List[Dict],
        competitive_data: Dict = None
    ) -> ChurnPrediction:
        """Predict churn risk for an account."""
        try:
            arguments = KernelArguments(
                account_data=account.model_dump_json(),
                performance_history=json.dumps(performance_history),
                sentiment_data=json.dumps(sentiment_data),
                competitive_data=json.dumps(competitive_data) if competitive_data else "{}"
            )
            
            result = await self.kernel.invoke(
                self.agents["churn_prediction"],
                arguments
            )
            
            churn_data = json.loads(str(result))
            
            return ChurnPrediction(
                account_id=account.id,
                prediction_date=datetime.now(),
                churn_probability=churn_data.get("churn_probability", 0.0) / 100.0,
                risk_level=churn_data.get("risk_level", "low"),
                key_risk_factors=churn_data.get("risk_factors", []),
                recommended_interventions=churn_data.get("intervention_strategies", []),
                model_confidence=churn_data.get("confidence", 0.0) / 100.0,
                feature_importance=churn_data.get("feature_importance", {})
            )
            
        except Exception as e:
            logger.error(f"Error predicting churn risk: {str(e)}")
            raise
    
    async def score_opportunity(
        self,
        opportunity: Opportunity,
        account_context: Account,
        historical_data: Dict = None,
        competitive_landscape: Dict = None
    ) -> Dict[str, Any]:
        """Score a sales opportunity."""
        try:
            arguments = KernelArguments(
                opportunity_data=opportunity.model_dump_json(),
                account_context=account_context.model_dump_json(),
                historical_data=json.dumps(historical_data) if historical_data else "{}",
                competitive_landscape=json.dumps(competitive_landscape) if competitive_landscape else "{}"
            )
            
            result = await self.kernel.invoke(
                self.agents["opportunity_scorer"],
                arguments
            )
            
            return json.loads(str(result))
            
        except Exception as e:
            logger.error(f"Error scoring opportunity: {str(e)}")
            raise
    
    async def analyze_sentiment(
        self,
        communication: Communication,
        relationship_context: Dict = None
    ) -> Dict[str, Any]:
        """Analyze sentiment of a communication."""
        try:
            arguments = KernelArguments(
                communication_content=communication.content,
                communication_type=communication.communication_type,
                relationship_context=json.dumps(relationship_context) if relationship_context else "{}"
            )
            
            result = await self.kernel.invoke(
                self.agents["sentiment_analyzer"],
                arguments
            )
            
            return json.loads(str(result))
            
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {str(e)}")
            raise
    
    async def recommend_actions(
        self,
        current_situation: Dict,
        account_profile: Account,
        available_resources: Dict = None,
        business_objectives: Dict = None
    ) -> Dict[str, Any]:
        """Get action recommendations for a specific situation."""
        try:
            arguments = KernelArguments(
                current_situation=json.dumps(current_situation),
                account_profile=account_profile.model_dump_json(),
                available_resources=json.dumps(available_resources) if available_resources else "{}",
                business_objectives=json.dumps(business_objectives) if business_objectives else "{}"
            )
            
            result = await self.kernel.invoke(
                self.agents["action_recommender"],
                arguments
            )
            
            return json.loads(str(result))
            
        except Exception as e:
            logger.error(f"Error generating action recommendations: {str(e)}")
            raise
    
    async def create_executive_summary(
        self,
        business_data: Dict,
        performance_metrics: Dict,
        market_intelligence: Dict = None,
        risk_assessment: Dict = None
    ) -> Dict[str, Any]:
        """Create an executive summary."""
        try:
            arguments = KernelArguments(
                business_data=json.dumps(business_data),
                performance_metrics=json.dumps(performance_metrics),
                market_intelligence=json.dumps(market_intelligence) if market_intelligence else "{}",
                risk_assessment=json.dumps(risk_assessment) if risk_assessment else "{}"
            )
            
            result = await self.kernel.invoke(
                self.agents["executive_summary"],
                arguments
            )
            
            return json.loads(str(result))
            
        except Exception as e:
            logger.error(f"Error creating executive summary: {str(e)}")
            raise
    
    
    # New AI Agent Methods
    
    async def analyze_opportunity_with_ai(self, opportunity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze opportunity using AI sales agent."""
        try:
            if self.sales_agent:
                return await self.sales_agent.analyze_opportunity(opportunity_data)
            else:
                logger.warning("Sales agent not available, using fallback")
                return {
                    "risk_level": "Medium",
                    "risk_reasoning": "AI analysis not available",
                    "success_factors": ["Complete opportunity assessment"],
                    "obstacles": ["Limited AI capabilities"],
                    "next_actions": ["Manual review required"],
                    "strategic_value": "Standard opportunity",
                    "competitive_notes": "Monitor competition",
                    "opportunity_score": 50,
                    "urgency_level": "Medium"
                }
        except Exception as e:
            logger.error(f"Error in AI opportunity analysis: {e}")
            return {"error": str(e)}
    
    async def generate_account_insights_with_ai(self, account_data: Dict[str, Any], 
                                               opportunities: List[Dict[str, Any]], 
                                               communications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate account insights using AI sales agent."""
        try:
            if self.sales_agent:
                return await self.sales_agent.generate_account_insights(
                    account_data, opportunities, communications
                )
            else:
                logger.warning("Sales agent not available, using fallback")
                return {
                    "health_assessment": "Manual review required",
                    "growth_opportunities": ["Explore partnership expansion"],
                    "risk_factors": ["Limited AI analysis available"],
                    "relationship_strength": "Moderate",
                    "competitive_position": "Competitive market",
                    "recommendations": ["Schedule account review"],
                    "account_score": account_data.get('health_score', 50),
                    "pipeline_value": sum(o.get('value', 0) for o in opportunities),
                    "sentiment_trend": 50,
                    "engagement_level": "Medium"
                }
        except Exception as e:
            logger.error(f"Error in AI account insights: {e}")
            return {"error": str(e)}
    
    async def get_ai_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get AI-powered action recommendations."""
        try:
            if self.sales_agent:
                return await self.sales_agent.recommend_actions(context)
            else:
                logger.warning("Sales agent not available, using fallback")
                return [
                    {
                        "title": "Review Pipeline Health",
                        "description": "Conduct comprehensive pipeline review",
                        "priority": "High",
                        "impact": "Improved forecasting accuracy",
                        "timeline": "This week"
                    }
                ]
        except Exception as e:
            logger.error(f"Error in AI recommendations: {e}")
            return [{"error": str(e)}]
    
    async def analyze_customer_sentiment_with_ai(self, communications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze customer sentiment using AI customer agent."""
        try:
            if self.customer_agent:
                return await self.customer_agent.analyze_customer_sentiment(communications)
            else:
                logger.warning("Customer agent not available, using fallback")
                return {
                    "overall_sentiment": 0.5,
                    "sentiment_trend": "neutral",
                    "recent_sentiment": 0.5,
                    "key_themes": ["Manual analysis required"],
                    "risk_indicators": [],
                    "positive_signals": [],
                    "communication_volume": len(communications),
                    "engagement_score": 50
                }
        except Exception as e:
            logger.error(f"Error in AI sentiment analysis: {e}")
            return {"error": str(e)}
    
    async def predict_churn_with_ai(self, account_data: Dict[str, Any], 
                                   communications: List[Dict[str, Any]],
                                   opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Predict churn risk using AI customer agent."""
        try:
            if self.customer_agent:
                return await self.customer_agent.predict_churn_risk(
                    account_data, communications, opportunities
                )
            else:
                logger.warning("Customer agent not available, using fallback")
                return {
                    "risk_level": "Medium",
                    "risk_score": 50,
                    "risk_factors": ["AI analysis not available"],
                    "recommendations": ["Manual assessment required"],
                    "next_actions": ["Schedule customer review"],
                    "timeline": "30 days"
                }
        except Exception as e:
            logger.error(f"Error in AI churn prediction: {e}")
            return {"error": str(e)}
    
    async def analyze_buying_patterns_with_ai(self, account_data: Dict[str, Any],
                                             opportunities: List[Dict[str, Any]],
                                             telemetry: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze buying patterns using AI customer agent."""
        try:
            if self.customer_agent:
                return await self.customer_agent.analyze_buying_patterns(
                    account_data, opportunities, telemetry
                )
            else:
                logger.warning("Customer agent not available, using fallback")
                return {
                    "patterns": ["Manual analysis required"],
                    "preferences": [],
                    "seasonality": "Unknown",
                    "volume_trend": "Unknown",
                    "recommendations": ["Gather more transaction data"]
                }
        except Exception as e:
            logger.error(f"Error in AI buying pattern analysis: {e}")
            return {"error": str(e)}
    
    async def generate_sales_forecast_with_ai(self, opportunities: List[Dict[str, Any]], 
                                             historical_data: Optional[List[Dict[str, Any]]] = None,
                                             timeframe_months: int = 3) -> Dict[str, Any]:
        """Generate sales forecast using AI forecasting agent."""
        try:
            if self.forecasting_agent:
                return await self.forecasting_agent.generate_sales_forecast(
                    opportunities, historical_data, timeframe_months
                )
            else:
                logger.warning("Forecasting agent not available, using fallback")
                return {
                    "forecast_total": sum(o.get('value', 0) * o.get('probability', 50) / 100 
                                        for o in opportunities),
                    "confidence_level": "Low",
                    "monthly_breakdown": [],
                    "risk_adjusted_total": 0,
                    "forecast_accuracy": "Unknown"
                }
        except Exception as e:
            logger.error(f"Error in AI sales forecast: {e}")
            return {"error": str(e)}
    
    async def analyze_pipeline_health_with_ai(self, opportunities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze pipeline health using AI forecasting agent."""
        try:
            if self.forecasting_agent:
                return await self.forecasting_agent.analyze_pipeline_health(opportunities)
            else:
                logger.warning("Forecasting agent not available, using fallback")
                return {
                    "health_score": 50,
                    "velocity_score": 50,
                    "stage_distribution": {},
                    "total_pipeline_value": sum(o.get('value', 0) for o in opportunities),
                    "average_deal_size": 0,
                    "bottlenecks": ["AI analysis not available"],
                    "recommendations": ["Manual pipeline review required"],
                    "conversion_rates": {}
                }
        except Exception as e:
            logger.error(f"Error in AI pipeline analysis: {e}")
            return {"error": str(e)}
    
    async def predict_deal_outcomes_with_ai(self, opportunities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict deal outcomes using AI forecasting agent."""
        try:
            if self.forecasting_agent:
                return await self.forecasting_agent.predict_deal_outcomes(opportunities)
            else:
                logger.warning("Forecasting agent not available, using fallback")
                return [
                    {
                        "opportunity_id": opp.get('id', 'unknown'),
                        "account_name": opp.get('account_name', 'Unknown'),
                        "value": opp.get('value', 0),
                        "current_stage": opp.get('stage', 'Unknown'),
                        "predicted_outcome": "Manual Review Required",
                        "win_probability": opp.get('probability', 50),
                        "predicted_close_date": opp.get('close_date', 'Unknown'),
                        "risk_factors": ["AI analysis not available"],
                        "success_factors": [],
                        "next_actions": ["Manual assessment required"]
                    }
                    for opp in opportunities[:5]  # Limit to first 5 for fallback
                ]
        except Exception as e:
            logger.error(f"Error in AI deal prediction: {e}")
            return [{"error": str(e)}]

    async def health_check(self) -> bool:
        """Check if the service is healthy."""
        try:
            if not self.kernel or not self.chat_service:
                return False
            
            # Simple test to verify the service is working
            test_arguments = KernelArguments(test="health check")
            simple_prompt = "Return 'healthy' if you can process this request."
            
            # Create a simple function for health check
            health_function = self.kernel.add_function(
                function_name="health_check",
                plugin_name="HealthPlugin",
                prompt=simple_prompt
            )
            
            result = await self.kernel.invoke(health_function, test_arguments)
            return "healthy" in str(result).lower()
            
        except Exception as e:
            logger.error(f"Health check failed: {str(e)}")
            return False
    
    async def cleanup(self) -> None:
        """Cleanup resources."""
        try:
            # Cleanup any resources if needed
            logger.info("Semantic Kernel service cleanup completed")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")
