'use client'

import { useState, useEffect } from 'react'
import { MapPin, TrendingUp, TrendingDown, AlertTriangle } from 'lucide-react'

interface HeatmapDataPoint {
  region: string
  account_count: number
  total_revenue: number
  avg_health_score: number
  churn_risk_accounts: number
  growth_opportunity_score: number
  coordinates: { lat: number; lng: number }
}

interface AccountHealthHeatmapProps {
  geographic?: boolean;
}

export default function AccountHealthHeatmap({ geographic = false }: AccountHealthHeatmapProps) {
  const [heatmapData, setHeatmapData] = useState<HeatmapDataPoint[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedRegion, setSelectedRegion] = useState<string | null>(null)

  useEffect(() => {
    fetchHeatmapData()
  }, [])

  const fetchHeatmapData = async () => {
    try {
      // Mock data for demonstration
      const mockData: HeatmapDataPoint[] = [
        {
          region: 'North America - East',
          account_count: 145,
          total_revenue: 650000000,
          avg_health_score: 88.5,
          churn_risk_accounts: 3,
          growth_opportunity_score: 92.3,
          coordinates: { lat: 40.7128, lng: -74.0060 }
        },
        {
          region: 'North America - Central',
          account_count: 178,
          total_revenue: 720000000,
          avg_health_score: 85.2,
          churn_risk_accounts: 8,
          growth_opportunity_score: 87.1,
          coordinates: { lat: 41.8781, lng: -87.6298 }
        },
        {
          region: 'North America - West',
          account_count: 134,
          total_revenue: 580000000,
          avg_health_score: 82.1,
          churn_risk_accounts: 12,
          growth_opportunity_score: 78.5,
          coordinates: { lat: 34.0522, lng: -118.2437 }
        },
        {
          region: 'North America - Southeast',
          account_count: 156,
          total_revenue: 480000000,
          avg_health_score: 91.3,
          churn_risk_accounts: 2,
          growth_opportunity_score: 89.7,
          coordinates: { lat: 33.4484, lng: -84.3917 }
        },
        {
          region: 'North America - Southwest',
          account_count: 142,
          total_revenue: 420000000,
          avg_health_score: 79.8,
          churn_risk_accounts: 15,
          growth_opportunity_score: 72.4,
          coordinates: { lat: 32.7767, lng: -96.7970 }
        },
        {
          region: 'North America - Northwest',
          account_count: 92,
          total_revenue: 280000000,
          avg_health_score: 86.7,
          churn_risk_accounts: 4,
          growth_opportunity_score: 84.2,
          coordinates: { lat: 47.6062, lng: -122.3321 }
        }
      ]
      
      setHeatmapData(mockData)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching heatmap data:', error)
      setLoading(false)
    }
  }

  const getHealthColor = (score: number) => {
    if (score >= 85) return 'bg-green-500'
    if (score >= 75) return 'bg-yellow-500'
    if (score >= 65) return 'bg-orange-500'
    return 'bg-red-500'
  }

  const getHealthTextColor = (score: number) => {
    if (score >= 85) return 'text-green-700'
    if (score >= 75) return 'text-yellow-700'
    if (score >= 65) return 'text-orange-700'
    return 'text-red-700'
  }

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(amount)
  }

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="animate-pulse">
          <div className="h-6 bg-gray-300 rounded w-1/3 mb-4"></div>
          <div className="space-y-3">
            <div className="h-20 bg-gray-300 rounded"></div>
            <div className="h-20 bg-gray-300 rounded"></div>
            <div className="h-20 bg-gray-300 rounded"></div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-lg font-semibold text-gray-900">Regional Account Health</h3>
        <div className="flex items-center space-x-4 text-sm">
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-green-500 rounded-full"></div>
            <span className="text-gray-600">Excellent (85+)</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-yellow-500 rounded-full"></div>
            <span className="text-gray-600">Good (75-84)</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-orange-500 rounded-full"></div>
            <span className="text-gray-600">Fair (65-74)</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-red-500 rounded-full"></div>
            <span className="text-gray-600">Poor (&lt;65)</span>
          </div>
        </div>
      </div>

      {/* Regional Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {heatmapData.map((region) => (
          <div
            key={region.region}
            className={`border-2 rounded-lg p-4 cursor-pointer transition-all duration-200 ${
              selectedRegion === region.region
                ? 'border-red-500 shadow-lg'
                : 'border-gray-200 hover:border-gray-300 hover:shadow-md'
            }`}
            onClick={() => setSelectedRegion(selectedRegion === region.region ? null : region.region)}
          >
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center space-x-2">
                <MapPin className="w-4 h-4 text-gray-500" />
                <h4 className="font-medium text-gray-900 text-sm">{region.region}</h4>
              </div>
              <div className={`w-3 h-3 rounded-full ${getHealthColor(region.avg_health_score)}`}></div>
            </div>

            <div className="space-y-2">
              <div className="flex justify-between items-center">
                <span className="text-xs text-gray-500">Health Score</span>
                <span className={`text-sm font-medium ${getHealthTextColor(region.avg_health_score)}`}>
                  {region.avg_health_score.toFixed(1)}
                </span>
              </div>

              <div className="flex justify-between items-center">
                <span className="text-xs text-gray-500">Accounts</span>
                <span className="text-sm font-medium text-gray-900">{region.account_count}</span>
              </div>

              <div className="flex justify-between items-center">
                <span className="text-xs text-gray-500">Revenue</span>
                <span className="text-sm font-medium text-gray-900">
                  {formatCurrency(region.total_revenue)}
                </span>
              </div>

              {region.churn_risk_accounts > 0 && (
                <div className="flex items-center justify-between bg-red-50 px-2 py-1 rounded">
                  <div className="flex items-center space-x-1">
                    <AlertTriangle className="w-3 h-3 text-red-500" />
                    <span className="text-xs text-red-700">At Risk</span>
                  </div>
                  <span className="text-xs font-medium text-red-700">{region.churn_risk_accounts}</span>
                </div>
              )}

              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-500">Growth Potential</span>
                <div className="flex items-center space-x-1">
                  {region.growth_opportunity_score > 80 ? (
                    <TrendingUp className="w-3 h-3 text-green-500" />
                  ) : (
                    <TrendingDown className="w-3 h-3 text-yellow-500" />
                  )}
                  <span className={`text-xs font-medium ${
                    region.growth_opportunity_score > 80 ? 'text-green-700' : 'text-yellow-700'
                  }`}>
                    {region.growth_opportunity_score.toFixed(1)}
                  </span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Detailed View for Selected Region */}
      {selectedRegion && (
        <div className="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
          {(() => {
            const region = heatmapData.find(r => r.region === selectedRegion)
            if (!region) return null

            return (
              <div>
                <h4 className="font-semibold text-gray-900 mb-3">{region.region} - Detailed Analysis</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div className="bg-white p-3 rounded border">
                    <div className="text-sm text-gray-500">Total Revenue</div>
                    <div className="text-lg font-bold text-gray-900">{formatCurrency(region.total_revenue)}</div>
                    <div className="text-xs text-gray-500">
                      Average per account: {formatCurrency(region.total_revenue / region.account_count)}
                    </div>
                  </div>
                  <div className="bg-white p-3 rounded border">
                    <div className="text-sm text-gray-500">Health Metrics</div>
                    <div className="text-lg font-bold text-gray-900">{region.avg_health_score.toFixed(1)}%</div>
                    <div className="text-xs text-gray-500">
                      {region.account_count - region.churn_risk_accounts} healthy accounts
                    </div>
                  </div>
                  <div className="bg-white p-3 rounded border">
                    <div className="text-sm text-gray-500">Growth Potential</div>
                    <div className="text-lg font-bold text-gray-900">{region.growth_opportunity_score.toFixed(1)}%</div>
                    <div className="text-xs text-gray-500">
                      {region.growth_opportunity_score > 80 ? 'High potential' : 'Moderate potential'}
                    </div>
                  </div>
                </div>

                {region.churn_risk_accounts > 0 && (
                  <div className="mt-4 p-3 bg-red-50 border border-red-200 rounded">
                    <div className="flex items-center space-x-2 mb-2">
                      <AlertTriangle className="w-4 h-4 text-red-500" />
                      <span className="font-medium text-red-700">Immediate Attention Required</span>
                    </div>
                    <p className="text-sm text-red-600">
                      {region.churn_risk_accounts} accounts in this region show high churn risk. 
                      Recommend immediate account manager outreach and retention strategy activation.
                    </p>
                  </div>
                )}
              </div>
            )
          })()}
        </div>
      )}
    </div>
  )
}
