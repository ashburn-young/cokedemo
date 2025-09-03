/**
 * API service for Coca-Cola Sales AI Agent Framework
 * Handles all communication with the backend FastAPI server
 */

import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

// Types for API responses
export interface Account {
  id: string;
  name: string;
  account_type: string;
  industry: string;
  region: string;
  health_score: number;
  churn_risk_score: number;
  annual_revenue: number;
  last_activity_date: string;
  assigned_rep: string;
  avg_daily_pours?: number;
}

export interface Opportunity {
  id: string;
  account_id: string;
  account_name: string;
  title: string;
  value: number;
  stage: string;
  probability: number;
  close_date: string;
  product_line: string;
  days_in_stage: number;
}

export interface Communication {
  id: string;
  account_id: string;
  type: string;
  content: string;
  sentiment: number;
  date: string;
  rep_name: string;
}

export interface AIInsight {
  id: string;
  insight_type: string;
  title: string;
  description: string;
  confidence: number;
  impact: string;
  recommended_actions: string[];
  created_at: string;
}

export interface DashboardSummary {
  total_accounts: number;
  healthy_accounts: number;
  at_risk_accounts: number;
  total_opportunities: number;
  pipeline_value: number;
  forecasted_revenue: number;
  avg_deal_size: number;
  win_rate: number;
  recent_activities: number;
}

export interface HeatmapData {
  region: string;
  account_count: number;
  total_revenue: number;
  avg_health_score: number;
  churn_risk_accounts: number;
  growth_opportunity_score: number;
  coordinates: {
    lat: number;
    lng: number;
  };
}

// API Service Class
export class ApiService {
  // Account endpoints
  static async getAccounts(limit = 50, riskLevel?: string): Promise<Account[]> {
    const params = new URLSearchParams({ limit: limit.toString() });
    if (riskLevel) params.append('risk_level', riskLevel);
    
    const response = await api.get(`/api/v1/sales/accounts?${params}`);
    return response.data;
  }

  static async getAccount(accountId: string): Promise<Account> {
    const response = await api.get(`/api/v1/sales/accounts/${accountId}`);
    return response.data;
  }

  // Opportunity endpoints
  static async getOpportunities(limit = 50, stage?: string): Promise<Opportunity[]> {
    const params = new URLSearchParams({ limit: limit.toString() });
    if (stage) params.append('stage', stage);
    
    const response = await api.get(`/api/v1/sales/opportunities?${params}`);
    return response.data;
  }

  // Dashboard endpoints
  static async getDashboardSummary(): Promise<DashboardSummary> {
    const response = await api.get('/api/v1/dashboard/summary');
    return response.data;
  }

  static async getHeatmapData(): Promise<HeatmapData[]> {
    const response = await api.get('/api/v1/dashboard/heatmap-data');
    return response.data;
  }

  static async getAIInsights(limit = 10): Promise<AIInsight[]> {
    const response = await api.get(`/api/v1/dashboard/ai-insights?limit=${limit}`);
    return response.data;
  }

  // Enhanced AI Agent endpoints
  static async analyzeOpportunity(opportunityId: string) {
    const response = await api.post(`/api/v1/agents/ai/analyze-opportunity?opportunity_id=${opportunityId}`);
    return response.data;
  }

  static async getAccountInsights(accountId: string) {
    const response = await api.post(`/api/v1/agents/ai/account-insights?account_id=${accountId}`);
    return response.data;
  }

  static async analyzeSentiment(accountId: string) {
    const response = await api.post(`/api/v1/agents/ai/sentiment-analysis?account_id=${accountId}`);
    return response.data;
  }

  static async predictChurn(accountId: string) {
    const response = await api.post(`/api/v1/agents/ai/churn-prediction?account_id=${accountId}`);
    return response.data;
  }

  static async analyzeBuyingPatterns(accountId: string) {
    const response = await api.post(`/api/v1/agents/ai/buying-patterns?account_id=${accountId}`);
    return response.data;
  }

  static async getSalesForecast(timeframeMonths = 3) {
    const response = await api.post(`/api/v1/agents/ai/sales-forecast?timeframe_months=${timeframeMonths}`);
    return response.data;
  }

  static async getPipelineHealth() {
    const response = await api.get('/api/v1/agents/ai/pipeline-health');
    return response.data;
  }

  static async getDealPredictions(limit = 10) {
    const response = await api.post(`/api/v1/agents/ai/deal-predictions?limit=${limit}`);
    return response.data;
  }

  static async getAIRecommendations(contextType: 'pipeline' | 'account' | 'churn_risk' | 'growth') {
    const response = await api.post(`/api/v1/agents/ai/recommendations?context_type=${contextType}`);
    return response.data;
  }

  // Health check
  static async healthCheck(): Promise<boolean> {
    try {
      const response = await api.get('/health');
      return response.status === 200;
    } catch (error) {
      return false;
    }
  }
}

export default ApiService;
