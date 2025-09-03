'use client';

import React, { useState, useEffect } from 'react';
import { 
  BarChart3, 
  Users, 
  TrendingUp, 
  DollarSign, 
  AlertTriangle,
  RefreshCw,
  Bot,
  Target,
  MapPin,
  Zap,
  ArrowRight
} from 'lucide-react';

import SalesMetrics from './SalesMetrics';
import OpportunityList from './OpportunityList';
import AccountHealthHeatmap from './AccountHealthHeatmap';
import AIInsights from './AIInsights_Enhanced';
import InteractiveMap from './InteractiveMap';
import ApiService, { DashboardSummary } from '../lib/api';

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview');
  const [dashboardData, setDashboardData] = useState<DashboardSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<Date>(new Date());

  const tabs = [
    { id: 'overview', label: 'Executive Overview', icon: BarChart3 },
    { id: 'opportunities', label: 'Revenue Opportunities', icon: Target },
    { id: 'accounts', label: 'Account Portfolio', icon: Users },
    { id: 'geographic', label: 'Geographic Intelligence', icon: MapPin },
    { id: 'insights', label: 'AI Strategic Insights', icon: Bot }
  ];

  const fetchDashboardData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Check if backend is available
      const isHealthy = await ApiService.healthCheck();
      if (!isHealthy) {
        throw new Error('Backend service is not available');
      }

      const data = await ApiService.getDashboardSummary();
      setDashboardData(data);
      setLastUpdated(new Date());
    } catch (err) {
      console.error('Failed to fetch dashboard data:', err);
      setError(err instanceof Error ? err.message : 'Failed to load dashboard data');
      
      // Use mock data as fallback
      setDashboardData({
        total_accounts: 127,
        healthy_accounts: 89,
        at_risk_accounts: 23,
        total_opportunities: 89,
        pipeline_value: 2847293,
        forecasted_revenue: 1923847,
        avg_deal_size: 31854,
        win_rate: 67.3,
        recent_activities: 34
      });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDashboardData();
    
    // Auto-refresh every 5 minutes
    const interval = setInterval(fetchDashboardData, 5 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  const refreshData = () => {
    fetchDashboardData();
  };

  if (loading && !dashboardData) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-red-50 to-white flex items-center justify-center">
        <div className="flex flex-col items-center space-y-4">
          <RefreshCw className="h-8 w-8 text-coca-red animate-spin" />
          <p className="text-gray-600">Loading Coca-Cola Sales Dashboard...</p>
        </div>
      </div>
    );
  }

  // Create KPIs from dashboard data
  const kpis = dashboardData ? [
    {
      title: 'Pipeline Value',
      value: `$${(dashboardData.pipeline_value / 1000000).toFixed(1)}M`,
      change: '+8.7%',
      icon: DollarSign,
      trend: 'up' as const
    },
    {
      title: 'Active Accounts',
      value: dashboardData.total_accounts.toString(),
      change: '+3.2%',
      icon: Users,
      trend: 'up' as const
    },
    {
      title: 'Win Rate',
      value: `${dashboardData.win_rate.toFixed(1)}%`,
      change: '+2.1%',
      icon: TrendingUp,
      trend: 'up' as const
    },
    {
      title: 'At-Risk Accounts',
      value: dashboardData.at_risk_accounts.toString(),
      change: '-5.1%',
      icon: AlertTriangle,
      trend: 'down' as const
    }
  ] : [];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-red-50">
      {/* Executive Header */}
      <div className="dashboard-header">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-8">
            <div className="flex items-center space-x-4">
              <div className="w-14 h-14 bg-gradient-to-br from-red-600 to-red-800 rounded-xl flex items-center justify-center shadow-lg">
                <Zap className="h-8 w-8 text-white" />
              </div>
              <div>
                <h1 className="text-3xl font-bold bg-gradient-to-r from-red-600 to-red-800 bg-clip-text text-transparent">
                  Coca-Cola Sales Dashboard, Powered by Azure AI Agents
                </h1>
                <p className="text-sm text-gray-600 flex items-center space-x-2">
                  <span>Real-time insights for strategic decision making</span>
                  {error && (
                    <span className="text-amber-600 ml-2">
                      (Using offline data - {error})
                    </span>
                  )}
                </p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-sm text-gray-500 bg-white px-3 py-2 rounded-lg border">
                Last updated: {lastUpdated.toLocaleTimeString()}
              </div>
              <button
                onClick={refreshData}
                disabled={loading}
                className="action-btn-primary flex items-center space-x-2"
              >
                <RefreshCw className={`h-4 w-4 ${loading ? 'animate-spin' : ''}`} />
                <span>Refresh Data</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Executive Navigation */}
      <div className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="-mb-px flex space-x-8" aria-label="Tabs">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`whitespace-nowrap py-6 px-1 border-b-3 font-semibold text-sm flex items-center space-x-3 transition-all duration-200 ${
                    activeTab === tab.id
                      ? 'border-red-600 text-red-600 bg-red-50'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 hover:bg-gray-50'
                  }`}
                >
                  <Icon className="h-5 w-5" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </nav>
        </div>
      </div>

      {/* Main Dashboard Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'overview' && (
          <div className="space-y-8">
            {/* Executive KPIs */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {kpis.map((kpi, index) => {
                const Icon = kpi.icon;
                return (
                  <div key={index} className="executive-metric-card p-6 rounded-xl">
                    <div className="flex items-center justify-between mb-4">
                      <div className={`p-3 rounded-xl ${
                        kpi.trend === 'up' ? 'bg-green-100' : 'bg-red-100'
                      }`}>
                        <Icon className={`h-6 w-6 ${
                          kpi.trend === 'up' ? 'text-green-600' : 'text-red-600'
                        }`} />
                      </div>
                      <div className={`text-lg font-bold px-3 py-1 rounded-lg ${
                        kpi.trend === 'up' ? 'trend-up' : 'trend-down'
                      }`}>
                        {kpi.change}
                      </div>
                    </div>
                    <div>
                      <p className="text-sm font-medium text-gray-600 mb-1">{kpi.title}</p>
                      <p className="text-3xl font-bold text-gray-900">{kpi.value}</p>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Enhanced Sales Metrics */}
            <div className="executive-card p-6 rounded-xl">
              <h3 className="text-xl font-bold text-gray-900 mb-6 flex items-center space-x-2">
                <BarChart3 className="h-6 w-6 text-red-600" />
                <span>Performance Analytics</span>
              </h3>
              <SalesMetrics />
            </div>

            {/* AI Insights Preview */}
            <div className="executive-card p-6 rounded-xl">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-bold text-gray-900 flex items-center space-x-2">
                  <Bot className="h-6 w-6 text-purple-600" />
                  <span>Strategic AI Insights</span>
                </h3>
                <button
                  onClick={() => setActiveTab('insights')}
                  className="action-btn-secondary flex items-center space-x-2"
                >
                  <ArrowRight className="h-4 w-4" />
                  <span>View All Insights</span>
                </button>
              </div>
              <AIInsights preview={true} />
            </div>
          </div>
        )}

        {activeTab === 'opportunities' && <OpportunityList />}
        {activeTab === 'accounts' && <AccountHealthHeatmap />}
        {activeTab === 'geographic' && <InteractiveMap />}
        {activeTab === 'insights' && <AIInsights />}
      </div>
    </div>
  );
}
