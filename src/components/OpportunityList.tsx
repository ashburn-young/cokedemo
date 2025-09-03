'use client'

import { useState, useEffect } from 'react'
import { DollarSign, Calendar, TrendingUp, AlertCircle, CheckCircle, Clock, Target } from 'lucide-react'

interface Opportunity {
  id: string
  account_id: string
  name: string
  description: string
  stage: string
  probability: number
  amount: number
  expected_close_date: string
  created_date: string
  product_lines: string[]
  account_name?: string
}

export default function OpportunityList() {
  const [opportunities, setOpportunities] = useState<Opportunity[]>([])
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState('all')
  const [sortBy, setSortBy] = useState('amount')

  useEffect(() => {
    fetchOpportunities()
  }, [])

  const fetchOpportunities = async () => {
    try {
      // Mock data for demonstration
      const mockOpportunities: Opportunity[] = [
        {
          id: '1',
          account_id: 'acc1',
          name: 'MovieMax Theaters - Freestyle Expansion',
          description: 'Installation of 15 new Freestyle machines across premium locations',
          stage: 'negotiation',
          probability: 78,
          amount: 2300000,
          expected_close_date: '2025-08-15',
          created_date: '2025-06-01',
          product_lines: ['freestyle', 'classic'],
          account_name: 'MovieMax Theaters'
        },
        {
          id: '2',
          account_id: 'acc2',
          name: 'SuperMax Grocery - Annual Contract Renewal',
          description: 'Renewal of annual beverage supply contract with 20% volume increase',
          stage: 'proposal',
          probability: 65,
          amount: 8500000,
          expected_close_date: '2025-07-30',
          created_date: '2025-05-15',
          product_lines: ['classic', 'zero', 'diet', 'sprite'],
          account_name: 'SuperMax Grocery Chain'
        },
        {
          id: '3',
          account_id: 'acc3',
          name: 'Burger Palace - Summer Promotion',
          description: 'Large-scale summer promotional campaign with co-marketing support',
          stage: 'qualification',
          probability: 45,
          amount: 1200000,
          expected_close_date: '2025-07-10',
          created_date: '2025-06-20',
          product_lines: ['classic', 'zero'],
          account_name: 'Burger Palace Chain'
        },
        {
          id: '4',
          account_id: 'acc4',
          name: 'Pacific Coast Bottlers - Territory Expansion',
          description: 'Expansion into 3 new territories with increased distribution rights',
          stage: 'closed_won',
          probability: 100,
          amount: 12000000,
          expected_close_date: '2025-06-30',
          created_date: '2025-03-01',
          product_lines: ['classic', 'zero', 'diet', 'sprite', 'fanta'],
          account_name: 'Pacific Coast Bottlers'
        },
        {
          id: '5',
          account_id: 'acc5',
          name: 'Grand Theater Chain - New Product Launch',
          description: 'Exclusive launch of new flavor variants in cinema locations',
          stage: 'prospecting',
          probability: 25,
          amount: 750000,
          expected_close_date: '2025-09-01',
          created_date: '2025-07-01',
          product_lines: ['freestyle'],
          account_name: 'Grand Theater Chain'
        },
        {
          id: '6',
          account_id: 'acc6',
          name: 'QuickStop Convenience - Freestyle Upgrade',
          description: 'Upgrade existing fountain systems to Freestyle technology',
          stage: 'negotiation',
          probability: 82,
          amount: 1850000,
          expected_close_date: '2025-08-20',
          created_date: '2025-05-20',
          product_lines: ['freestyle'],
          account_name: 'QuickStop Convenience'
        }
      ]
      
      setOpportunities(mockOpportunities)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching opportunities:', error)
      setLoading(false)
    }
  }

  const getStageColor = (stage: string) => {
    const colors = {
      'prospecting': 'bg-gray-100 text-gray-800',
      'qualification': 'bg-blue-100 text-blue-800',
      'proposal': 'bg-yellow-100 text-yellow-800',
      'negotiation': 'bg-orange-100 text-orange-800',
      'closed_won': 'bg-green-100 text-green-800',
      'closed_lost': 'bg-red-100 text-red-800'
    }
    return colors[stage as keyof typeof colors] || 'bg-gray-100 text-gray-800'
  }

  const getStageIcon = (stage: string) => {
    const icons = {
      'prospecting': Clock,
      'qualification': Target,
      'proposal': AlertCircle,
      'negotiation': TrendingUp,
      'closed_won': CheckCircle,
      'closed_lost': AlertCircle
    }
    const Icon = icons[stage as keyof typeof icons] || Clock
    return <Icon className="w-4 h-4" />
  }

  const getProbabilityColor = (probability: number) => {
    if (probability >= 80) return 'text-green-600'
    if (probability >= 60) return 'text-yellow-600'
    if (probability >= 40) return 'text-orange-600'
    return 'text-red-600'
  }

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(amount)
  }

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    })
  }

  const getDaysUntilClose = (dateString: string) => {
    const closeDate = new Date(dateString)
    const today = new Date()
    const diffTime = closeDate.getTime() - today.getTime()
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    return diffDays
  }

  const filteredOpportunities = opportunities.filter(opp => {
    if (filter === 'all') return true
    if (filter === 'closing_soon') {
      const daysUntil = getDaysUntilClose(opp.expected_close_date)
      return daysUntil <= 30 && daysUntil > 0
    }
    if (filter === 'high_value') return opp.amount >= 2000000
    if (filter === 'high_probability') return opp.probability >= 70
    return opp.stage === filter
  })

  const sortedOpportunities = [...filteredOpportunities].sort((a, b) => {
    if (sortBy === 'amount') return b.amount - a.amount
    if (sortBy === 'probability') return b.probability - a.probability
    if (sortBy === 'close_date') return new Date(a.expected_close_date).getTime() - new Date(b.expected_close_date).getTime()
    return 0
  })

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="animate-pulse">
          <div className="h-6 bg-gray-300 rounded w-1/3 mb-4"></div>
          <div className="space-y-3">
            {[1, 2, 3].map(i => (
              <div key={i} className="h-24 bg-gray-300 rounded"></div>
            ))}
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Header and Filters */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4">
          <h3 className="text-lg font-semibold text-gray-900">Sales Opportunities</h3>
          <div className="flex space-x-4 mt-4 sm:mt-0">
            <select
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
              className="border border-gray-300 rounded-md px-3 py-2 text-sm"
            >
              <option value="all">All Opportunities</option>
              <option value="closing_soon">Closing Soon (30 days)</option>
              <option value="high_value">High Value ($2M+)</option>
              <option value="high_probability">High Probability (70%+)</option>
              <option value="prospecting">Prospecting</option>
              <option value="qualification">Qualification</option>
              <option value="proposal">Proposal</option>
              <option value="negotiation">Negotiation</option>
            </select>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="border border-gray-300 rounded-md px-3 py-2 text-sm"
            >
              <option value="amount">Sort by Amount</option>
              <option value="probability">Sort by Probability</option>
              <option value="close_date">Sort by Close Date</option>
            </select>
          </div>
        </div>

        {/* Summary Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
          <div className="bg-blue-50 p-3 rounded">
            <div className="text-sm text-blue-600">Total Pipeline</div>
            <div className="text-xl font-bold text-blue-900">
              {formatCurrency(opportunities.reduce((sum, opp) => sum + opp.amount, 0))}
            </div>
          </div>
          <div className="bg-green-50 p-3 rounded">
            <div className="text-sm text-green-600">Weighted Pipeline</div>
            <div className="text-xl font-bold text-green-900">
              {formatCurrency(opportunities.reduce((sum, opp) => sum + (opp.amount * opp.probability / 100), 0))}
            </div>
          </div>
          <div className="bg-orange-50 p-3 rounded">
            <div className="text-sm text-orange-600">Closing This Month</div>
            <div className="text-xl font-bold text-orange-900">
              {opportunities.filter(opp => getDaysUntilClose(opp.expected_close_date) <= 30).length}
            </div>
          </div>
          <div className="bg-purple-50 p-3 rounded">
            <div className="text-sm text-purple-600">Avg Deal Size</div>
            <div className="text-xl font-bold text-purple-900">
              {formatCurrency(opportunities.reduce((sum, opp) => sum + opp.amount, 0) / opportunities.length)}
            </div>
          </div>
        </div>
      </div>

      {/* Opportunities List */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Opportunity
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Stage
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Amount
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Probability
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Close Date
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Products
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {sortedOpportunities.map((opportunity) => {
                const daysUntilClose = getDaysUntilClose(opportunity.expected_close_date)
                
                return (
                  <tr key={opportunity.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div>
                        <div className="text-sm font-medium text-gray-900">{opportunity.name}</div>
                        <div className="text-sm text-gray-500">{opportunity.account_name}</div>
                        <div className="text-xs text-gray-400 mt-1">{opportunity.description}</div>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-xs font-medium ${getStageColor(opportunity.stage)}`}>
                        {getStageIcon(opportunity.stage)}
                        <span className="capitalize">{opportunity.stage.replace('_', ' ')}</span>
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm font-medium text-gray-900">
                        {formatCurrency(opportunity.amount)}
                      </div>
                      <div className="text-xs text-gray-500">
                        Weighted: {formatCurrency(opportunity.amount * opportunity.probability / 100)}
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className={`text-sm font-medium ${getProbabilityColor(opportunity.probability)}`}>
                        {opportunity.probability}%
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm text-gray-900">{formatDate(opportunity.expected_close_date)}</div>
                      <div className={`text-xs ${daysUntilClose <= 7 ? 'text-red-600' : daysUntilClose <= 30 ? 'text-orange-600' : 'text-gray-500'}`}>
                        {daysUntilClose > 0 ? `${daysUntilClose} days` : 'Overdue'}
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="flex flex-wrap gap-1">
                        {opportunity.product_lines.map((product) => (
                          <span
                            key={product}
                            className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-red-100 text-red-800"
                          >
                            {product}
                          </span>
                        ))}
                      </div>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
