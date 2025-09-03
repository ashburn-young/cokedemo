'use client'

import { useState, useEffect } from 'react'
import { 
  Zap, TrendingUp, AlertTriangle, Target, Users, MessageSquare, Brain, 
  CheckCircle, Clock, ArrowRight, DollarSign, BarChart3, Sparkles,
  TrendingDown, Calendar, Phone, Mail, FileText
} from 'lucide-react'

interface AIInsight {
  id: string
  type: 'churn_risk' | 'growth_opportunity' | 'sentiment_alert' | 'action_recommendation' | 'performance_insight' | 'product_opportunity' | 'competitive_threat'
  title: string
  description: string
  confidence: number
  priority: 'high' | 'medium' | 'low'
  account_name: string
  recommendation: string
  impact_value?: number
  timeline?: string
  products_involved?: string[]
  next_actions?: string[]
  created_date: string
  status: 'new' | 'reviewed' | 'actioned' | 'dismissed'
  roi_potential?: number
  executive_summary?: string
}

interface AIInsightsProps {
  preview?: boolean;
}

export default function AIInsights({ preview = false }: AIInsightsProps) {
  const [insights, setInsights] = useState<AIInsight[]>([])
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState('all')
  const [selectedInsight, setSelectedInsight] = useState<string | null>(null)
  const [actioningInsight, setActioningInsight] = useState<string | null>(null)

  useEffect(() => {
    fetchAIInsights()
  }, [])

  const fetchAIInsights = async () => {
    try {
      // Enhanced AI insights with real Coca-Cola products and business context
      const mockInsights: AIInsight[] = [
        {
          id: '1',
          type: 'churn_risk',
          title: 'Critical Churn Risk: Atlanta Coca-Cola Bottling',
          description: 'Atlanta Coca-Cola Bottling shows 87% churn probability based on declining communication sentiment, 35% reduction in Coca-Cola Classic orders, and delayed payments. Their Freestyle machine utilization dropped 42% in Q4.',
          confidence: 0.87,
          priority: 'high',
          account_name: 'Atlanta Coca-Cola Bottling',
          recommendation: 'Immediate executive intervention required. Schedule C-level meeting within 48 hours.',
          impact_value: 3200000,
          timeline: '72 hours',
          products_involved: ['Coca-Cola Classic', 'Coca-Cola Zero Sugar', 'Freestyle Systems'],
          next_actions: [
            'Schedule emergency meeting with CEO & CFO',
            'Prepare retention package with volume incentives',
            'Analyze competitive threats in Atlanta market',
            'Review payment terms and credit facilities'
          ],
          created_date: '2025-07-06T08:30:00Z',
          status: 'new',
          roi_potential: 15600000,
          executive_summary: 'Lost revenue risk of $3.2M this quarter, $15.6M annually. Immediate action required to preserve largest Southeast bottling partnership.'
        },
        {
          id: '2',
          type: 'product_opportunity',
          title: 'Freestyle Expansion: MovieMax Theaters',
          description: 'MovieMax Theaters (142 locations) showing optimal conditions for Coca-Cola Freestyle expansion. Their current beverage mix analysis indicates 67% revenue increase potential with Freestyle deployment.',
          confidence: 0.82,
          priority: 'high',
          account_name: 'MovieMax Theaters',
          recommendation: 'Present comprehensive Freestyle ROI analysis with pilot program proposal.',
          impact_value: 2800000,
          timeline: '90 days',
          products_involved: ['Coca-Cola Freestyle', 'Coca-Cola Classic', 'Sprite', 'Fanta Orange'],
          next_actions: [
            'Develop customized ROI presentation',
            'Propose 10-location pilot program',
            'Arrange Freestyle demo at flagship theater',
            'Negotiate volume-based pricing structure'
          ],
          created_date: '2025-07-05T14:15:00Z',
          status: 'reviewed',
          roi_potential: 12400000,
          executive_summary: 'Freestyle expansion opportunity across 142 theater locations. Projected $2.8M immediate revenue, $12.4M 3-year impact.'
        },
        {
          id: '3',
          type: 'growth_opportunity',
          title: 'Cross-Sell Success: Powerade in QSR Segment',
          description: 'Burger Palace Chain analysis reveals untapped Powerade opportunity. Their sports drink sales increased 45% post-pandemic while they only carry competitor products. High potential for Powerade Zero Sugar introduction.',
          confidence: 0.78,
          priority: 'medium',
          account_name: 'Burger Palace Chain',
          recommendation: 'Propose Powerade product trial with promotional support and athlete endorsement tie-ins.',
          impact_value: 1200000,
          timeline: '120 days',
          products_involved: ['Powerade', 'Powerade Zero Sugar', 'Powerade Ion4'],
          next_actions: [
            'Analyze competitor pricing and placement',
            'Develop trial program with promotional support',
            'Coordinate with athlete endorsement team',
            'Design custom POS materials and training'
          ],
          created_date: '2025-07-05T11:20:00Z',
          status: 'new',
          roi_potential: 5200000,
          executive_summary: 'Cross-sell opportunity for Powerade in 420 QSR locations. Conservative estimate: $1.2M Year 1, $5.2M potential over 3 years.'
        },
        {
          id: '4',
          type: 'competitive_threat',
          title: 'Competitive Pressure: Southwest Regional Decline',
          description: 'Southwest region showing 18% volume decline despite market growth. Competitive analysis indicates aggressive pricing from regional competitor affecting Coca-Cola Classic and Sprite market share.',
          confidence: 0.84,
          priority: 'high',
          account_name: 'Southwest Region Portfolio',
          recommendation: 'Implement defensive pricing strategy and enhanced promotional support for key accounts.',
          impact_value: 4100000,
          timeline: '60 days',
          products_involved: ['Coca-Cola Classic', 'Sprite', 'Fanta Orange'],
          next_actions: [
            'Conduct comprehensive competitive pricing analysis',
            'Develop regional promotional campaign',
            'Negotiate volume incentives with key distributors',
            'Launch consumer loyalty programs'
          ],
          created_date: '2025-07-04T16:45:00Z',
          status: 'reviewed',
          roi_potential: 18500000,
          executive_summary: 'Competitive threat causing $4.1M quarterly impact. Strategic response needed to protect $18.5M annual revenue base.'
        },
        {
          id: '5',
          type: 'action_recommendation',
          title: 'Contract Renewal Optimization: Pacific Coast Bottlers',
          description: 'Pacific Coast Bottlers contract renewal in 90 days. Historical data shows early engagement increases renewal probability by 23% and average contract value by 12%. Current relationship health: 89%.',
          confidence: 0.91,
          priority: 'medium',
          account_name: 'Pacific Coast Bottlers',
          recommendation: 'Initiate renewal discussions with performance review showcasing mutual growth opportunities.',
          impact_value: 1800000,
          timeline: '30 days',
          products_involved: ['Coca-Cola Classic', 'Coca-Cola Zero Sugar', 'smartwater', 'Minute Maid'],
          next_actions: [
            'Prepare 3-year performance analytics report',
            'Schedule renewal strategy meeting',
            'Develop expansion opportunity proposals',
            'Negotiate multi-year volume commitments'
          ],
          created_date: '2025-07-04T09:30:00Z',
          status: 'actioned',
          roi_potential: 8900000,
          executive_summary: 'Strategic contract renewal opportunity. Early engagement projected to increase contract value by $1.8M annually, $8.9M over 5 years.'
        },
        {
          id: '6',
          type: 'sentiment_alert',
          title: 'Communication Sentiment Decline: SuperMax Grocery',
          description: 'SuperMax Grocery Chain communications show 40% increase in negative sentiment over 30 days. Key concerns: delivery scheduling, product mix optimization, and promotional support effectiveness.',
          confidence: 0.74,
          priority: 'medium',
          account_name: 'SuperMax Grocery Chain',
          recommendation: 'Conduct immediate relationship health assessment and address operational concerns.',
          impact_value: 850000,
          timeline: '21 days',
          products_involved: ['Coca-Cola Classic', 'Diet Coke', 'Sprite'],
          next_actions: [
            'Schedule relationship review call with key stakeholders',
            'Audit delivery and logistics performance',
            'Review promotional effectiveness metrics',
            'Propose enhanced account management model'
          ],
          created_date: '2025-07-03T13:10:00Z',
          status: 'new',
          roi_potential: 3400000,
          executive_summary: 'Relationship risk indicators suggest potential $850K quarterly impact. Proactive intervention needed to maintain $3.4M annual account value.'
        }
      ]
      
      setInsights(mockInsights)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching AI insights:', error)
      setLoading(false)
    }
  }

  const getInsightIcon = (type: string) => {
    const icons = {
      'churn_risk': AlertTriangle,
      'growth_opportunity': TrendingUp,
      'sentiment_alert': MessageSquare,
      'action_recommendation': Target,
      'performance_insight': Brain,
      'product_opportunity': Sparkles,
      'competitive_threat': TrendingDown
    }
    const Icon = icons[type as keyof typeof icons] || Zap
    return <Icon className="w-5 h-5" />
  }

  const getInsightColor = (type: string) => {
    const colors = {
      'churn_risk': 'status-critical',
      'growth_opportunity': 'status-excellent',
      'sentiment_alert': 'status-fair',
      'action_recommendation': 'status-good',
      'performance_insight': 'bg-purple-100 text-purple-700 border-purple-200',
      'product_opportunity': 'bg-blue-100 text-blue-700 border-blue-200',
      'competitive_threat': 'status-poor'
    }
    return colors[type as keyof typeof colors] || 'bg-gray-100 text-gray-700 border-gray-200'
  }

  const getPriorityColor = (priority: string) => {
    const colors = {
      'high': 'priority-high',
      'medium': 'priority-medium',
      'low': 'priority-low'
    }
    return colors[priority as keyof typeof colors] || 'bg-gray-500'
  }

  const getStatusIcon = (status: string) => {
    const icons = {
      'new': Clock,
      'reviewed': Users,
      'actioned': CheckCircle,
      'dismissed': Users
    }
    const Icon = icons[status as keyof typeof icons] || Clock
    return Icon
  }

  const getStatusColor = (status: string) => {
    const colors = {
      'new': 'bg-blue-100 text-blue-800',
      'reviewed': 'bg-yellow-100 text-yellow-800',
      'actioned': 'bg-green-100 text-green-800',
      'dismissed': 'bg-gray-100 text-gray-800'
    }
    return colors[status as keyof typeof colors] || 'bg-gray-100 text-gray-800'
  }

  const handleTakeAction = async (insightId: string) => {
    setActioningInsight(insightId);
    
    // Simulate API call
    setTimeout(() => {
      setInsights(prev => prev.map(insight => 
        insight.id === insightId 
          ? { ...insight, status: 'actioned' as const }
          : insight
      ));
      setActioningInsight(null);
    }, 1500);
  }

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0
    }).format(amount);
  }

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  }

  const filteredInsights = filter === 'all' 
    ? insights 
    : insights.filter(insight => insight.priority === filter || insight.status === filter || insight.type === filter);

  const displayInsights = preview ? insights.slice(0, 3) : filteredInsights;

  if (loading) {
    return (
      <div className="executive-card p-6 rounded-xl">
        <div className="loading-shimmer h-64 rounded-lg"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {!preview && (
        <div className="executive-card p-6 rounded-xl">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-gradient-to-r from-red-500 to-purple-600 rounded-lg">
                <Brain className="w-6 h-6 text-white" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-gray-900">AI-Powered Executive Insights</h3>
                <p className="text-sm text-gray-600">Powered by Azure AI Agents</p>
              </div>
            </div>
            <select
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
              className="action-btn-secondary text-sm mt-4 sm:mt-0"
            >
              <option value="all">All Insights</option>
              <option value="high">High Priority</option>
              <option value="new">New Insights</option>
              <option value="churn_risk">Churn Risk</option>
              <option value="growth_opportunity">Growth Opportunities</option>
              <option value="product_opportunity">Product Opportunities</option>
              <option value="competitive_threat">Competitive Threats</option>
            </select>
          </div>

          {/* Executive Summary Stats */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
            <div className="metric-card p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">High Priority</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {insights.filter(i => i.priority === 'high').length}
                  </p>
                </div>
                <AlertTriangle className="h-8 w-8 text-red-500" />
              </div>
            </div>
            <div className="metric-card p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">Revenue Impact</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {formatCurrency(insights.reduce((sum, i) => sum + (i.impact_value || 0), 0))}
                  </p>
                </div>
                <DollarSign className="h-8 w-8 text-green-500" />
              </div>
            </div>
            <div className="metric-card p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">Pending Actions</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {insights.filter(i => i.status === 'new').length}
                  </p>
                </div>
                <Clock className="h-8 w-8 text-amber-500" />
              </div>
            </div>
            <div className="metric-card p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">Avg Confidence</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {Math.round(insights.reduce((sum, i) => sum + i.confidence, 0) / insights.length * 100)}%
                  </p>
                </div>
                <BarChart3 className="h-8 w-8 text-blue-500" />
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Insights List */}
      <div className="space-y-4">
        {displayInsights.map((insight) => {
          const StatusIcon = getStatusIcon(insight.status);
          const isExpanded = selectedInsight === insight.id;
          
          return (
            <div key={insight.id} className="ai-insight-executive p-6 rounded-xl">
              <div className={`priority-indicator ${getPriorityColor(insight.priority)}`}></div>
              
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-start space-x-4 flex-1">
                  <div className={`p-3 rounded-lg border ${getInsightColor(insight.type)}`}>
                    {getInsightIcon(insight.type)}
                  </div>
                  <div className="flex-1">
                    <div className="flex items-center space-x-3 mb-2">
                      <h4 className="text-lg font-bold text-gray-900">{insight.title}</h4>
                      <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(insight.status)}`}>
                        {insight.status.charAt(0).toUpperCase() + insight.status.slice(1)}
                      </span>
                    </div>
                    <p className="text-sm text-gray-600 mb-3">{insight.description}</p>
                    
                    {insight.executive_summary && (
                      <div className="bg-gradient-to-r from-red-50 to-purple-50 p-3 rounded-lg mb-3">
                        <p className="text-sm font-medium text-gray-900">
                          <Sparkles className="w-4 h-4 inline mr-2 text-purple-600" />
                          Executive Summary: {insight.executive_summary}
                        </p>
                      </div>
                    )}

                    <div className="flex flex-wrap items-center gap-4 text-sm text-gray-600">
                      <div className="flex items-center space-x-1">
                        <Target className="w-4 h-4" />
                        <span>Confidence: {Math.round(insight.confidence * 100)}%</span>
                      </div>
                      {insight.impact_value && (
                        <div className="flex items-center space-x-1">
                          <DollarSign className="w-4 h-4" />
                          <span>Impact: {formatCurrency(insight.impact_value)}</span>
                        </div>
                      )}
                      {insight.timeline && (
                        <div className="flex items-center space-x-1">
                          <Calendar className="w-4 h-4" />
                          <span>Timeline: {insight.timeline}</span>
                        </div>
                      )}
                      <div className="flex items-center space-x-1">
                        <Clock className="w-4 h-4" />
                        <span>{formatDate(insight.created_date)}</span>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div className="flex items-center space-x-2">
                  <button
                    onClick={() => setSelectedInsight(isExpanded ? null : insight.id)}
                    className="action-btn-secondary text-sm px-3 py-2"
                  >
                    {isExpanded ? 'Less' : 'Details'}
                  </button>
                  {insight.status === 'new' && (
                    <button
                      onClick={() => handleTakeAction(insight.id)}
                      disabled={actioningInsight === insight.id}
                      className="action-btn-primary text-sm px-4 py-2 flex items-center space-x-2"
                    >
                      {actioningInsight === insight.id ? (
                        <>
                          <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                          <span>Processing...</span>
                        </>
                      ) : (
                        <>
                          <ArrowRight className="w-4 h-4" />
                          <span>Take Action</span>
                        </>
                      )}
                    </button>
                  )}
                </div>
              </div>

              {isExpanded && (
                <div className="border-t border-gray-200 pt-4 mt-4 space-y-4">
                  <div>
                    <h5 className="font-semibold text-gray-900 mb-2">Recommendation</h5>
                    <p className="text-sm text-gray-700 bg-gray-50 p-3 rounded-lg">{insight.recommendation}</p>
                  </div>

                  {insight.products_involved && insight.products_involved.length > 0 && (
                    <div>
                      <h5 className="font-semibold text-gray-900 mb-2">Products Involved</h5>
                      <div className="flex flex-wrap gap-2">
                        {insight.products_involved.map((product) => {
                          const productKey = product.toLowerCase().replace(/[^a-z]/g, '');
                          return (
                            <span
                              key={product}
                              className={`px-3 py-1 rounded-lg text-sm font-medium product-${productKey}`}
                            >
                              {product}
                            </span>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  {insight.next_actions && insight.next_actions.length > 0 && (
                    <div>
                      <h5 className="font-semibold text-gray-900 mb-2">Next Actions</h5>
                      <ul className="space-y-2">
                        {insight.next_actions.map((action, index) => (
                          <li key={index} className="flex items-start space-x-2 text-sm text-gray-700">
                            <CheckCircle className="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" />
                            <span>{action}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {insight.roi_potential && (
                    <div className="bg-green-50 p-4 rounded-lg">
                      <h5 className="font-semibold text-green-900 mb-1">ROI Potential</h5>
                      <p className="text-lg font-bold text-green-700">{formatCurrency(insight.roi_potential)}</p>
                      <p className="text-sm text-green-600">Long-term revenue opportunity</p>
                    </div>
                  )}

                  <div className="flex space-x-3 pt-4">
                    <button className="action-btn-primary flex items-center space-x-2">
                      <Phone className="w-4 h-4" />
                      <span>Schedule Call</span>
                    </button>
                    <button className="action-btn-secondary flex items-center space-x-2">
                      <Mail className="w-4 h-4" />
                      <span>Send Email</span>
                    </button>
                    <button className="action-btn-secondary flex items-center space-x-2">
                      <FileText className="w-4 h-4" />
                      <span>Generate Report</span>
                    </button>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {displayInsights.length === 0 && (
        <div className="executive-card p-12 rounded-xl text-center">
          <Brain className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">No insights found</h3>
          <p className="text-gray-600">Try adjusting your filter to see more insights.</p>
        </div>
      )}
    </div>
  );
}
