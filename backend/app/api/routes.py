"""
API Routes for Coca-Cola Sales AI Agent Framework.
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Dict, Any, Optional
import logging

from app.core.semantic_kernel_service import SemanticKernelService
from app.services.data_generator import DataGeneratorService
from app.models.schemas import Account, Opportunity, Communication, AIInsight, ChurnPrediction

logger = logging.getLogger(__name__)

# Global service instances (will be set by main.py)
_data_service: DataGeneratorService = None
_semantic_kernel_service: SemanticKernelService = None

def set_data_service(service: DataGeneratorService):
    """Set the global data service instance."""
    global _data_service
    _data_service = service

def set_semantic_kernel_service(service: SemanticKernelService):
    """Set the global semantic kernel service instance."""
    global _semantic_kernel_service
    _semantic_kernel_service = service

def get_data_service() -> DataGeneratorService:
    """Dependency to get the data generator service."""
    if not _data_service:
        raise HTTPException(status_code=503, detail="Data service not available")
    return _data_service

def get_semantic_kernel_service() -> SemanticKernelService:
    """Dependency to get the semantic kernel service."""
    if not _semantic_kernel_service:
        raise HTTPException(status_code=503, detail="Semantic kernel service not available")
    return _semantic_kernel_service

# Create routers
sales_router = APIRouter()
agents_router = APIRouter()
dashboard_router = APIRouter()


# Sales Routes
@sales_router.get("/accounts", response_model=List[Dict[str, Any]])
async def get_accounts(
    limit: int = Query(50, ge=1, le=200),
    risk_level: Optional[str] = Query(None, description="Filter by risk level: low, medium, high"),
    account_type: Optional[str] = Query(None, description="Filter by account type"),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get list of accounts with optional filtering."""
    try:
        # For demo, we'll use the data generator service
        # In production, this would query the database
        accounts = data_service.get_accounts() if data_service else []
        
        # Apply filters
        if risk_level:
            if risk_level == "high":
                accounts = [acc for acc in accounts if acc.churn_risk_score > 70]
            elif risk_level == "medium":
                accounts = [acc for acc in accounts if 40 <= acc.churn_risk_score <= 70]
            elif risk_level == "low":
                accounts = [acc for acc in accounts if acc.churn_risk_score < 40]
        
        if account_type:
            accounts = [acc for acc in accounts if acc.account_type.value == account_type]
        
        # Limit results
        accounts = accounts[:limit]
        
        return [acc.model_dump() for acc in accounts]
        
    except Exception as e:
        logger.error(f"Error fetching accounts: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch accounts")


@sales_router.get("/accounts/{account_id}", response_model=Dict[str, Any])
async def get_account_details(
    account_id: str,
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get detailed account information including related data."""
    try:
        accounts = data_service.get_accounts() if data_service else []
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        return account.model_dump()
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching account details: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch account details")


@sales_router.get("/opportunities", response_model=List[Dict[str, Any]])
async def get_opportunities(
    account_id: Optional[str] = Query(None),
    stage: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=200),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get sales opportunities with optional filtering."""
    try:
        # This would query the database in production
        opportunities = data_service.opportunities if data_service else []
        
        # Apply filters
        if account_id:
            opportunities = [opp for opp in opportunities if opp.account_id == account_id]
        
        if stage:
            opportunities = [opp for opp in opportunities if opp.stage.value == stage]
        
        # Sort by amount descending and limit
        opportunities = sorted(opportunities, key=lambda x: x.amount, reverse=True)[:limit]
        
        return [opp.model_dump() for opp in opportunities]
        
    except Exception as e:
        logger.error(f"Error fetching opportunities: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch opportunities")


# AI Agents Routes
@agents_router.post("/analyze-account-health")
async def analyze_account_health(
    account_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Analyze account health using AI agent."""
    try:
        # Get account data
        accounts = data_service.get_accounts() if data_service else []
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        # Get related communications
        communications = [comm for comm in data_service.communications if comm.account_id == account_id] if data_service else []
        
        # Use AI to analyze account health
        if sk_service:
            analysis = await sk_service.analyze_account_health(
                account=account,
                communications=communications[:10],  # Last 10 communications
                sales_metrics={"quarterly_growth": 5.2, "satisfaction_score": 87},
                freestyle_data={"avg_daily_pours": account.avg_daily_pours} if account.avg_daily_pours else None
            )
            return analysis
        else:
            # Return mock analysis if service not available
            return {
                "account_id": account_id,
                "health_score": account.health_score,
                "risk_factors": ["Declining communication frequency", "Competitive pressure"],
                "recommendations": ["Schedule executive meeting", "Propose volume incentive"],
                "confidence": 0.85
            }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error analyzing account health: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze account health")


@agents_router.post("/predict-churn")
async def predict_churn_risk(
    account_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Predict churn risk for an account."""
    try:
        # Get account data
        accounts = data_service.get_accounts() if data_service else []
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        # Prepare historical data
        performance_history = {
            "revenue_trend": [-2.1, 1.5, -0.8, 3.2],  # Last 4 quarters
            "volume_trend": [-1.5, 2.1, -1.2, 2.8],
            "satisfaction_scores": [88, 85, 82, 87]
        }
        
        # Get sentiment data from communications
        communications = [comm for comm in data_service.communications if comm.account_id == account_id] if data_service else []
        sentiment_data = [
            {
                "date": comm.date.isoformat(),
                "sentiment": comm.sentiment_score.value,
                "confidence": comm.sentiment_confidence
            }
            for comm in communications[-5:]  # Last 5 communications
        ]
        
        if sk_service:
            prediction = await sk_service.predict_churn_risk(
                account=account,
                performance_history=performance_history,
                sentiment_data=sentiment_data,
                competitive_data={"competitor_activity": "moderate"}
            )
            return prediction.model_dump()
        else:
            # Return mock prediction
            return {
                "account_id": account_id,
                "churn_probability": account.churn_risk_score / 100,
                "risk_level": "high" if account.churn_risk_score > 70 else "medium" if account.churn_risk_score > 40 else "low",
                "key_risk_factors": ["Payment delays", "Reduced order frequency", "Competitor meetings"],
                "recommended_interventions": ["Executive outreach", "Volume incentive offer", "Account review meeting"],
                "model_confidence": 0.82
            }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error predicting churn risk: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to predict churn risk")


@agents_router.post("/score-opportunity")
async def score_opportunity(
    opportunity_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Score a sales opportunity using AI."""
    try:
        # Get opportunity data
        opportunities = data_service.opportunities if data_service else []
        opportunity = next((opp for opp in opportunities if opp.id == opportunity_id), None)
        
        if not opportunity:
            raise HTTPException(status_code=404, detail="Opportunity not found")
        
        # Get account context
        accounts = data_service.get_accounts() if data_service else []
        account = next((acc for acc in accounts if acc.id == opportunity.account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Associated account not found")
        
        if sk_service:
            scoring = await sk_service.score_opportunity(
                opportunity=opportunity,
                account_context=account,
                historical_data={"win_rate": 0.68, "avg_sales_cycle": 45},
                competitive_landscape={"competitive_intensity": "medium"}
            )
            return scoring
        else:
            # Return mock scoring
            return {
                "opportunity_id": opportunity_id,
                "win_probability": opportunity.probability,
                "deal_quality_score": 7.5,
                "success_factors": ["Strong relationship", "Budget confirmed", "Technical fit"],
                "risk_factors": ["Competitive pressure", "Extended timeline"],
                "next_actions": ["Submit final proposal", "Schedule decision maker meeting"],
                "confidence": 0.78
            }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error scoring opportunity: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to score opportunity")


@agents_router.post("/recommend-actions")
async def recommend_actions(
    account_id: str,
    situation_type: str = Query(..., description="Type of situation: churn_risk, growth_opportunity, relationship_issue"),
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get AI-powered action recommendations."""
    try:
        # Get account data
        accounts = data_service.get_accounts() if data_service else []
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        # Prepare situation context
        current_situation = {
            "type": situation_type,
            "account_health": account.health_score,
            "churn_risk": account.churn_risk_score,
            "last_activity": account.last_activity_date.isoformat()
        }
        
        available_resources = {
            "budget": 50000,
            "promotional_programs": ["Volume incentive", "Marketing support", "Freestyle upgrade"],
            "sales_team": ["Field rep", "Account manager", "Technical specialist"]
        }
        
        business_objectives = {
            "revenue_growth": 15,
            "retention_rate": 95,
            "market_share_increase": 5
        }
        
        if sk_service:
            recommendations = await sk_service.recommend_actions(
                current_situation=current_situation,
                account_profile=account,
                available_resources=available_resources,
                business_objectives=business_objectives
            )
            return recommendations
        else:
            # Return mock recommendations
            return {
                "immediate_actions": [
                    "Schedule face-to-face meeting with decision maker",
                    "Prepare competitive analysis presentation",
                    "Review contract terms for improvement opportunities"
                ],
                "medium_term_strategies": [
                    "Propose volume incentive program",
                    "Introduce new product samples",
                    "Organize executive dinner meeting"
                ],
                "long_term_initiatives": [
                    "Develop strategic partnership plan",
                    "Explore Freestyle machine expansion",
                    "Create co-marketing opportunities"
                ],
                "success_metrics": ["Revenue retention", "Order frequency", "Satisfaction score"],
                "confidence": 0.88
            }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating action recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate recommendations")


# Enhanced AI Agent Routes

@agents_router.post("/ai/analyze-opportunity")
async def ai_analyze_opportunity(
    opportunity_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Analyze opportunity using enhanced AI sales agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get opportunity data
        opportunities = data_service.get_opportunities()
        opportunity = next((opp for opp in opportunities if opp.id == opportunity_id), None)
        
        if not opportunity:
            raise HTTPException(status_code=404, detail="Opportunity not found")
        
        # Convert to dict for AI analysis
        opportunity_data = opportunity.model_dump()
        
        if sk_service:
            analysis = await sk_service.analyze_opportunity_with_ai(opportunity_data)
            return analysis
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in AI opportunity analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze opportunity with AI")


@agents_router.post("/ai/account-insights")
async def ai_account_insights(
    account_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Generate comprehensive account insights using AI sales agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get account data
        accounts = data_service.get_accounts()
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        # Get related data
        opportunities = [opp for opp in data_service.get_opportunities() if opp.account_id == account_id]
        communications = [comm for comm in data_service.communications if comm.account_id == account_id]
        
        # Convert to dicts for AI analysis
        account_data = account.model_dump()
        opportunity_data = [opp.model_dump() for opp in opportunities]
        communication_data = [comm.model_dump() for comm in communications]
        
        if sk_service:
            insights = await sk_service.generate_account_insights_with_ai(
                account_data, opportunity_data, communication_data
            )
            return insights
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating AI account insights: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate account insights")


@agents_router.post("/ai/sentiment-analysis")
async def ai_sentiment_analysis(
    account_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Analyze customer sentiment using AI customer agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get communications for the account
        communications = [comm for comm in data_service.communications if comm.account_id == account_id]
        
        if not communications:
            raise HTTPException(status_code=404, detail="No communications found for account")
        
        # Convert to dicts for AI analysis
        communication_data = [comm.model_dump() for comm in communications]
        
        if sk_service:
            sentiment_analysis = await sk_service.analyze_customer_sentiment_with_ai(communication_data)
            return sentiment_analysis
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in AI sentiment analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze sentiment")


@agents_router.post("/ai/churn-prediction")
async def ai_churn_prediction(
    account_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Predict churn risk using AI customer agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get account data
        accounts = data_service.get_accounts()
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        # Get related data
        opportunities = [opp for opp in data_service.get_opportunities() if opp.account_id == account_id]
        communications = [comm for comm in data_service.communications if comm.account_id == account_id]
        
        # Convert to dicts for AI analysis
        account_data = account.model_dump()
        opportunity_data = [opp.model_dump() for opp in opportunities]
        communication_data = [comm.model_dump() for comm in communications]
        
        if sk_service:
            churn_prediction = await sk_service.predict_churn_with_ai(
                account_data, communication_data, opportunity_data
            )
            return churn_prediction
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in AI churn prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to predict churn risk")


@agents_router.post("/ai/buying-patterns")
async def ai_buying_patterns(
    account_id: str,
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Analyze buying patterns using AI customer agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get account data
        accounts = data_service.get_accounts()
        account = next((acc for acc in accounts if acc.id == account_id), None)
        
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        # Get related data
        opportunities = [opp for opp in data_service.get_opportunities() if opp.account_id == account_id]
        telemetry = data_service.get_telemetry_data()  # Get telemetry for the account
        
        # Convert to dicts for AI analysis
        account_data = account.model_dump()
        opportunity_data = [opp.model_dump() for opp in opportunities]
        telemetry_data = [tel.model_dump() for tel in telemetry if tel.account_id == account_id]
        
        if sk_service:
            pattern_analysis = await sk_service.analyze_buying_patterns_with_ai(
                account_data, opportunity_data, telemetry_data
            )
            return pattern_analysis
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in AI buying pattern analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze buying patterns")


@agents_router.post("/ai/sales-forecast")
async def ai_sales_forecast(
    timeframe_months: int = Query(3, ge=1, le=12, description="Forecast timeframe in months"),
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Generate sales forecast using AI forecasting agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get opportunity data
        opportunities = data_service.get_opportunities()
        active_opportunities = [opp for opp in opportunities if opp.stage not in ["Closed Lost"]]
        
        # Convert to dicts for AI analysis
        opportunity_data = [opp.model_dump() for opp in active_opportunities]
        
        if sk_service:
            forecast = await sk_service.generate_sales_forecast_with_ai(
                opportunity_data, None, timeframe_months
            )
            return forecast
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating AI sales forecast: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate sales forecast")


@agents_router.get("/ai/pipeline-health")
async def ai_pipeline_health(
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Analyze pipeline health using AI forecasting agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get opportunity data
        opportunities = data_service.get_opportunities()
        active_opportunities = [opp for opp in opportunities if opp.stage not in ["Closed Lost", "Closed Won"]]
        
        # Convert to dicts for AI analysis
        opportunity_data = [opp.model_dump() for opp in active_opportunities]
        
        if sk_service:
            pipeline_analysis = await sk_service.analyze_pipeline_health_with_ai(opportunity_data)
            return pipeline_analysis
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error analyzing pipeline health: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze pipeline health")


@agents_router.post("/ai/deal-predictions")
async def ai_deal_predictions(
    limit: int = Query(10, ge=1, le=50, description="Number of deals to predict"),
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Predict deal outcomes using AI forecasting agent."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Get opportunity data
        opportunities = data_service.get_opportunities()
        active_opportunities = [opp for opp in opportunities 
                               if opp.stage not in ["Closed Lost", "Closed Won"]][:limit]
        
        # Convert to dicts for AI analysis
        opportunity_data = [opp.model_dump() for opp in active_opportunities]
        
        if sk_service:
            predictions = await sk_service.predict_deal_outcomes_with_ai(opportunity_data)
            return predictions
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error predicting deal outcomes: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to predict deal outcomes")


@agents_router.post("/ai/recommendations")
async def ai_recommendations(
    context_type: str = Query(..., description="Context type: pipeline, account, churn_risk, growth"),
    sk_service: SemanticKernelService = Depends(get_semantic_kernel_service),
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get AI-powered recommendations based on context."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        # Build context based on type
        opportunities = data_service.get_opportunities()
        accounts = data_service.get_accounts()
        
        if context_type == "pipeline":
            context = {
                "opportunity_count": len(opportunities),
                "pipeline_value": sum(opp.value for opp in opportunities),
                "at_risk_count": len([opp for opp in opportunities if opp.probability < 30]),
                "overdue_count": len([opp for opp in opportunities if opp.days_in_stage > 60]),
                "avg_cycle_days": sum(opp.days_in_stage for opp in opportunities) / len(opportunities) if opportunities else 0
            }
        elif context_type == "account":
            context = {
                "total_accounts": len(accounts),
                "healthy_accounts": len([acc for acc in accounts if acc.health_score > 70]),
                "at_risk_accounts": len([acc for acc in accounts if acc.churn_risk_score > 70]),
                "avg_health_score": sum(acc.health_score for acc in accounts) / len(accounts) if accounts else 0
            }
        else:
            context = {
                "general_metrics": True,
                "context_type": context_type
            }
        
        if sk_service:
            recommendations = await sk_service.get_ai_recommendations(context)
            return {"recommendations": recommendations, "context": context}
        else:
            raise HTTPException(status_code=503, detail="AI service not available")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating AI recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate recommendations")


# Dashboard Routes
@dashboard_router.get("/summary")
async def get_dashboard_summary(
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get executive dashboard summary."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        accounts = data_service.get_accounts()
        opportunities = data_service.opportunities
        
        # Calculate summary metrics
        total_accounts = len(accounts)
        total_revenue = sum(acc.annual_revenue for acc in accounts)
        high_risk_accounts = len([acc for acc in accounts if acc.churn_risk_score > 70])
        
        # Opportunities metrics
        closing_this_month = [opp for opp in opportunities if opp.expected_close_date.month == 7]  # July 2025
        avg_deal_size = sum(opp.amount for opp in opportunities) / len(opportunities) if opportunities else 0
        won_opportunities = [opp for opp in opportunities if opp.stage.value == "closed_won"]
        win_rate = len(won_opportunities) / len(opportunities) * 100 if opportunities else 0
        
        # Regional performance
        regional_revenue = {}
        for acc in accounts:
            if acc.region not in regional_revenue:
                regional_revenue[acc.region] = 0
            regional_revenue[acc.region] += acc.annual_revenue
        
        top_regions = sorted(regional_revenue.items(), key=lambda x: x[1], reverse=True)[:3]
        
        summary = {
            "total_accounts": total_accounts,
            "total_revenue": total_revenue,
            "revenue_growth_percent": 8.5,  # Mock growth
            "high_risk_accounts": high_risk_accounts,
            "opportunities_closing_this_month": len(closing_this_month),
            "avg_deal_size": avg_deal_size,
            "win_rate": win_rate,
            "top_performing_regions": [region[0] for region in top_regions],
            "at_risk_revenue": sum(acc.lifetime_value for acc in accounts if acc.churn_risk_score > 70),
            "revenue_trend": [
                {"month": "Jan", "value": total_revenue * 0.08},
                {"month": "Feb", "value": total_revenue * 0.09},
                {"month": "Mar", "value": total_revenue * 0.08},
                {"month": "Apr", "value": total_revenue * 0.09},
                {"month": "May", "value": total_revenue * 0.10},
                {"month": "Jun", "value": total_revenue * 0.11}
            ],
            "health_score_trend": [
                {"month": "Jan", "value": 82},
                {"month": "Feb", "value": 84},
                {"month": "Mar", "value": 83},
                {"month": "Apr", "value": 85},
                {"month": "May", "value": 87},
                {"month": "Jun", "value": 88}
            ]
        }
        
        return summary
        
    except Exception as e:
        logger.error(f"Error generating dashboard summary: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate dashboard summary")


@dashboard_router.get("/heatmap-data")
async def get_heatmap_data(
    data_service: DataGeneratorService = Depends(get_data_service)
):
    """Get data for geographic heatmap visualization."""
    try:
        if not data_service:
            raise HTTPException(status_code=503, detail="Data service not available")
        
        accounts = data_service.get_accounts()
        
        # Group accounts by region
        regional_data = {}
        for acc in accounts:
            if acc.region not in regional_data:
                regional_data[acc.region] = {
                    "accounts": [],
                    "total_revenue": 0,
                    "churn_risk_accounts": 0
                }
            
            regional_data[acc.region]["accounts"].append(acc)
            regional_data[acc.region]["total_revenue"] += acc.annual_revenue
            if acc.churn_risk_score > 70:
                regional_data[acc.region]["churn_risk_accounts"] += 1
        
        # Convert to heatmap format
        heatmap_data = []
        for region, data in regional_data.items():
            avg_health = sum(acc.health_score for acc in data["accounts"]) / len(data["accounts"])
            
            # Mock coordinates for regions
            coordinates = {
                "North America - East": {"lat": 40.7128, "lng": -74.0060},
                "North America - Central": {"lat": 41.8781, "lng": -87.6298},
                "North America - West": {"lat": 34.0522, "lng": -118.2437},
                "North America - Southeast": {"lat": 33.4484, "lng": -84.3917},
                "North America - Southwest": {"lat": 32.7767, "lng": -96.7970},
                "North America - Northwest": {"lat": 47.6062, "lng": -122.3321}
            }.get(region, {"lat": 39.8283, "lng": -98.5795})
            
            heatmap_data.append({
                "region": region,
                "account_count": len(data["accounts"]),
                "total_revenue": data["total_revenue"],
                "avg_health_score": avg_health,
                "churn_risk_accounts": data["churn_risk_accounts"],
                "growth_opportunity_score": avg_health * (data["total_revenue"] / 1000000),
                "coordinates": coordinates
            })
        
        return heatmap_data
        
    except Exception as e:
        logger.error(f"Error generating heatmap data: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate heatmap data")
