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

  const filteredInsights = insights.filter(insight => {
    if (filter === 'all') return true
    if (filter === 'high_priority') return insight.priority === 'high'
    if (filter === 'new') return insight.status === 'new'
    return insight.type === filter
  }).slice(0, preview ? 3 : undefined)  // Limit to 3 items in preview mode

  const updateInsightStatus = (insightId: string, newStatus: 'new' | 'reviewed' | 'actioned') => {
    setInsights(prev => prev.map(insight => 
      insight.id === insightId ? { ...insight, status: newStatus } : insight
    ))
  }

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="animate-pulse">
          <div className="h-6 bg-gray-300 rounded w-1/3 mb-4"></div>
          <div className="space-y-3">
            {[1, 2, 3].map(i => (
              <div key={i} className="h-20 bg-gray-300 rounded"></div>
            ))}
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Header and Controls */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4">
          <div className="flex items-center space-x-2">
            <Zap className="w-6 h-6 text-yellow-500" />
            <h3 className="text-lg font-semibold text-gray-900">AI-Powered Insights</h3>
          </div>
          <select
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
            className="border border-gray-300 rounded-md px-3 py-2 text-sm mt-4 sm:mt-0"
          >
            <option value="all">All Insights</option>
            <option value="high_priority">High Priority</option>
            <option value="new">New Insights</option>
            <option value="churn_risk">Churn Risk</option>
            <option value="growth_opportunity">Growth Opportunities</option>
            <option value="sentiment_alert">Sentiment Alerts</option>
            <option value="action_recommendation">Action Recommendations</option>
            <option value="performance_insight">Performance Insights</option>
          </select>
        </div>

        {/* Summary Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-red-50 p-3 rounded">
            <div className="text-sm text-red-600">High Priority</div>
            <div className="text-xl font-bold text-red-900">
              {insights.filter(i => i.priority === 'high').length}
            </div>
          </div>
          <div className="bg-blue-50 p-3 rounded">
            <div className="text-sm text-blue-600">New Insights</div>
            <div className="text-xl font-bold text-blue-900">
              {insights.filter(i => i.status === 'new').length}
            </div>
          </div>
          <div className="bg-green-50 p-3 rounded">
            <div className="text-sm text-green-600">Actions Taken</div>
            <div className="text-xl font-bold text-green-900">
              {insights.filter(i => i.status === 'actioned').length}
            </div>
          </div>
          <div className="bg-purple-50 p-3 rounded">
            <div className="text-sm text-purple-600">Avg Confidence</div>
            <div className="text-xl font-bold text-purple-900">
              {Math.round(insights.reduce((sum, i) => sum + i.confidence, 0) / insights.length * 100)}%
            </div>
          </div>
        </div>
      </div>

      {/* Insights List */}
      <div className="space-y-4">
        {filteredInsights.map((insight) => (
          <div
            key={insight.id}
            className={`bg-white rounded-lg shadow-sm border-2 p-6 cursor-pointer transition-all duration-200 ${
              selectedInsight === insight.id ? 'border-red-300 shadow-lg' : 'border-gray-200 hover:border-gray-300'
            }`}
            onClick={() => setSelectedInsight(selectedInsight === insight.id ? null : insight.id)}
          >
            <div className="flex items-start justify-between">
              <div className="flex items-start space-x-4 flex-1">
                <div className={`p-2 rounded-lg border ${getInsightColor(insight.type)}`}>
                  {getInsightIcon(insight.type)}
                </div>
                
                <div className="flex-1">
                  <div className="flex items-center space-x-3 mb-2">
                    <h4 className="font-semibold text-gray-900">{insight.title}</h4>
                    <div className={`w-2 h-2 rounded-full ${getPriorityColor(insight.priority)}`}></div>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(insight.status)}`}>
                      {insight.status}
                    </span>
                  </div>
                  
                  <div className="text-sm text-gray-600 mb-2">{insight.account_name}</div>
                  <p className="text-sm text-gray-700 mb-3">{insight.description}</p>
                  
                  <div className="flex items-center justify-between text-sm">
                    <div className="flex items-center space-x-4">
                      <span className="text-gray-500">Confidence: {Math.round(insight.confidence * 100)}%</span>
                      <span className="text-gray-500">{formatDate(insight.created_date)}</span>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="flex flex-col space-y-2 ml-4">
                {insight.status === 'new' && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation()
                      updateInsightStatus(insight.id, 'reviewed')
                    }}
                    className="px-3 py-1 bg-yellow-100 text-yellow-700 rounded text-xs hover:bg-yellow-200"
                  >
                    Mark Reviewed
                  </button>
                )}
                {insight.status === 'reviewed' && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation()
                      updateInsightStatus(insight.id, 'actioned')
                    }}
                    className="px-3 py-1 bg-green-100 text-green-700 rounded text-xs hover:bg-green-200"
                  >
                    Mark Actioned
                  </button>
                )}
                {insight.status === 'actioned' && (
                  <div className="flex items-center space-x-1 text-green-700">
                    <CheckCircle className="w-4 h-4" />
                    <span className="text-xs">Complete</span>
                  </div>
                )}
              </div>
            </div>
            
            {/* Expanded Details */}
            {selectedInsight === insight.id && (
              <div className="mt-4 pt-4 border-t border-gray-200">
                <div className="bg-gray-50 p-4 rounded-lg">
                  <h5 className="font-medium text-gray-900 mb-2">AI Recommendation:</h5>
                  <p className="text-sm text-gray-700">{insight.recommendation}</p>
                  
                  <div className="mt-4 flex space-x-3">
                    <button className="px-4 py-2 bg-red-600 text-white rounded text-sm hover:bg-red-700">
                      Take Action
                    </button>
                    <button className="px-4 py-2 bg-gray-200 text-gray-800 rounded text-sm hover:bg-gray-300">
                      Schedule Follow-up
                    </button>
                    <button className="px-4 py-2 bg-gray-200 text-gray-800 rounded text-sm hover:bg-gray-300">
                      View Account Details
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {filteredInsights.length === 0 && (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
          <Zap className="w-12 h-12 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No insights found</h3>
          <p className="text-gray-500">Try adjusting your filters or check back later for new AI insights.</p>
        </div>
      )}
    </div>
  )
}
