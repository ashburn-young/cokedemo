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
  Zap
} from 'lucide-react';

import SalesMetrics from './SalesMetrics';
import OpportunityList from './OpportunityList';
import AccountHealthHeatmap from './AccountHealthHeatmap';
import AIInsights from './AIInsights';
import ApiService, { DashboardSummary } from '../lib/api';

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview');
  const [dashboardData, setDashboardData] = useState<DashboardSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<Date>(new Date());

  const tabs = [
    { id: 'overview', label: 'Overview', icon: BarChart3 },
    { id: 'opportunities', label: 'Opportunities', icon: Target },
    { id: 'accounts', label: 'Account Health', icon: Users },
    { id: 'heatmap', label: 'Geographic View', icon: MapPin },
    { id: 'insights', label: 'AI Insights', icon: Bot }
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
    <div className="min-h-screen bg-gradient-to-br from-red-50 to-white">
      {/* Header */}
      <div className="bg-white shadow-sm border-b border-red-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 bg-coca-red rounded-xl flex items-center justify-center">
                <Zap className="h-7 w-7 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">
                  Coca-Cola Sales AI Dashboard
                </h1>
                <p className="text-sm text-gray-600">
                  AI-powered insights for better sales performance
                  {error && (
                    <span className="text-amber-600 ml-2">
                      (Using offline data - {error})
                    </span>
                  )}
                </p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-sm text-gray-500">
                Last updated: {lastUpdated.toLocaleTimeString()}
              </div>
              <button
                onClick={refreshData}
                disabled={loading}
                className="flex items-center space-x-2 px-4 py-2 bg-coca-red text-white rounded-lg hover:bg-red-700 transition-colors disabled:opacity-50"
              >
                <RefreshCw className={`h-4 w-4 ${loading ? 'animate-spin' : ''}`} />
                <span>Refresh</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="-mb-px flex space-x-8" aria-label="Tabs">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm flex items-center space-x-2 transition-colors ${
                    activeTab === tab.id
                      ? 'border-coca-red text-coca-red'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'overview' && (
          <div className="space-y-8">
            {/* KPIs */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {kpis.map((kpi, index) => {
                const Icon = kpi.icon;
                return (
                  <div key={index} className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-3">
                        <div className={`p-2 rounded-lg ${
                          kpi.trend === 'up' ? 'bg-green-100' : 'bg-red-100'
                        }`}>
                          <Icon className={`h-5 w-5 ${
                            kpi.trend === 'up' ? 'text-green-600' : 'text-red-600'
                          }`} />
                        </div>
                        <div>
                          <p className="text-sm font-medium text-gray-600">{kpi.title}</p>
                          <p className="text-2xl font-bold text-gray-900">{kpi.value}</p>
                        </div>
                      </div>
                      <div className={`text-sm font-medium ${
                        kpi.trend === 'up' ? 'text-green-600' : 'text-red-600'
                      }`}>
                        {kpi.change}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Sales Metrics */}
            <SalesMetrics />

            {/* Recent AI Insights Preview */}
            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-900 flex items-center space-x-2">
                  <Bot className="h-5 w-5 text-coca-red" />
                  <span>Recent AI Insights</span>
                </h3>
                <button
                  onClick={() => setActiveTab('insights')}
                  className="text-coca-red hover:text-red-700 text-sm font-medium"
                >
                  View All
                </button>
              </div>
              <AIInsights preview={true} />
            </div>
          </div>
        )}

        {activeTab === 'opportunities' && <OpportunityList />}
        {activeTab === 'accounts' && <AccountHealthHeatmap />}
        {activeTab === 'heatmap' && <AccountHealthHeatmap geographic={true} />}
        {activeTab === 'insights' && <AIInsights />}
      </div>
    </div>
  );
}
