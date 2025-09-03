'use client';

import React, { useState, useEffect } from 'react';
import { MapPin, TrendingUp, TrendingDown, AlertTriangle, Users, DollarSign } from 'lucide-react';

interface AccountMapData {
  id: string;
  name: string;
  latitude: number;
  longitude: number;
  health_score: number;
  annual_revenue: number;
  churn_risk_score: number;
  region: string;
  account_type: string;
  products: string[];
}

interface MapTooltipData {
  account: AccountMapData;
  x: number;
  y: number;
}

export default function InteractiveMap() {
  const [accounts, setAccounts] = useState<AccountMapData[]>([]);
  const [selectedRegion, setSelectedRegion] = useState<string>('all');
  const [tooltip, setTooltip] = useState<MapTooltipData | null>(null);
  const [loading, setLoading] = useState(true);

  const regions = [
    { id: 'all', name: 'All Regions', color: '#DC143C' },
    { id: 'northeast', name: 'Northeast', color: '#1E40AF' },
    { id: 'southeast', name: 'Southeast', color: '#059669' },
    { id: 'midwest', name: 'Midwest', color: '#D97706' },
    { id: 'southwest', name: 'Southwest', color: '#7C3AED' },
    { id: 'west', name: 'West', color: '#0D9488' }
  ];

  useEffect(() => {
    // Generate mock geographical data for US regions
    const mockAccounts: AccountMapData[] = [
      // Northeast
      { id: '1', name: 'New York Premium Bottlers', latitude: 40.7128, longitude: -74.0060, health_score: 92, annual_revenue: 45000000, churn_risk_score: 15, region: 'northeast', account_type: 'bottler', products: ['classic', 'zero', 'diet'] },
      { id: '2', name: 'Boston Market Leaders', latitude: 42.3601, longitude: -71.0589, health_score: 87, annual_revenue: 32000000, churn_risk_score: 25, region: 'northeast', account_type: 'retailer', products: ['classic', 'sprite', 'fanta'] },
      { id: '3', name: 'Philadelphia Distributors', latitude: 39.9526, longitude: -75.1652, health_score: 78, annual_revenue: 28000000, churn_risk_score: 35, region: 'northeast', account_type: 'distributor', products: ['classic', 'zero'] },
      
      // Southeast
      { id: '4', name: 'Atlanta Coca-Cola Bottling', latitude: 33.7490, longitude: -84.3880, health_score: 45, annual_revenue: 67000000, churn_risk_score: 87, region: 'southeast', account_type: 'bottler', products: ['classic', 'zero', 'sprite', 'freestyle'] },
      { id: '5', name: 'Miami Beach Resorts', latitude: 25.7617, longitude: -80.1918, health_score: 94, annual_revenue: 25000000, churn_risk_score: 12, region: 'southeast', account_type: 'qsr', products: ['classic', 'sprite', 'powerade'] },
      { id: '6', name: 'Charlotte Distribution Hub', latitude: 35.2271, longitude: -80.8431, health_score: 82, annual_revenue: 38000000, churn_risk_score: 28, region: 'southeast', account_type: 'distributor', products: ['classic', 'zero', 'diet', 'sprite'] },
      
      // Midwest
      { id: '7', name: 'Chicago Metro Bottlers', latitude: 41.8781, longitude: -87.6298, health_score: 89, annual_revenue: 52000000, churn_risk_score: 18, region: 'midwest', account_type: 'bottler', products: ['classic', 'zero', 'diet', 'freestyle'] },
      { id: '8', name: 'Detroit Auto District', latitude: 42.3314, longitude: -83.0458, health_score: 71, annual_revenue: 34000000, churn_risk_score: 42, region: 'midwest', account_type: 'retailer', products: ['classic', 'powerade'] },
      { id: '9', name: 'Milwaukee Brewers Concessions', latitude: 43.0389, longitude: -87.9065, health_score: 85, annual_revenue: 15000000, churn_risk_score: 22, region: 'midwest', account_type: 'stadium', products: ['classic', 'zero', 'powerade'] },
      
      // Southwest
      { id: '10', name: 'Dallas Mega Centers', latitude: 32.7767, longitude: -96.7970, health_score: 76, annual_revenue: 41000000, churn_risk_score: 38, region: 'southwest', account_type: 'retailer', products: ['classic', 'zero', 'sprite'] },
      { id: '11', name: 'Phoenix Desert Distributors', latitude: 33.4484, longitude: -112.0740, health_score: 91, annual_revenue: 29000000, churn_risk_score: 16, region: 'southwest', account_type: 'distributor', products: ['classic', 'zero', 'smartwater'] },
      { id: '12', name: 'Austin Music Venues', latitude: 30.2672, longitude: -97.7431, health_score: 88, annual_revenue: 18000000, churn_risk_score: 20, region: 'southwest', account_type: 'cinema', products: ['classic', 'sprite', 'fanta'] },
      
      // West
      { id: '13', name: 'Los Angeles Entertainment', latitude: 34.0522, longitude: -118.2437, health_score: 93, annual_revenue: 58000000, churn_risk_score: 14, region: 'west', account_type: 'theme_park', products: ['classic', 'zero', 'sprite', 'freestyle'] },
      { id: '14', name: 'San Francisco Tech Campus', latitude: 37.7749, longitude: -122.4194, health_score: 95, annual_revenue: 22000000, churn_risk_score: 8, region: 'west', account_type: 'qsr', products: ['zero', 'smartwater', 'sprite'] },
      { id: '15', name: 'Seattle Coffee & More', latitude: 47.6062, longitude: -122.3321, health_score: 72, annual_revenue: 31000000, churn_risk_score: 45, region: 'west', account_type: 'retailer', products: ['classic', 'zero'] }
    ];

    setAccounts(mockAccounts);
    setLoading(false);
  }, []);

  const getHealthColor = (score: number) => {
    if (score >= 90) return '#059669'; // Excellent - Green
    if (score >= 75) return '#D97706'; // Good - Amber
    if (score >= 60) return '#F59E0B'; // Fair - Yellow
    if (score >= 40) return '#DC143C'; // Poor - Red
    return '#8B0A14'; // Critical - Dark Red
  };

  const getAccountSize = (revenue: number) => {
    if (revenue > 50000000) return 16;
    if (revenue > 30000000) return 14;
    if (revenue > 20000000) return 12;
    return 10;
  };

  const filteredAccounts = selectedRegion === 'all' 
    ? accounts 
    : accounts.filter(account => account.region === selectedRegion);

  const handleAccountHover = (account: AccountMapData, event: React.MouseEvent) => {
    const rect = event.currentTarget.getBoundingClientRect();
    setTooltip({
      account,
      x: rect.left + rect.width / 2,
      y: rect.top - 10
    });
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0
    }).format(amount);
  };

  if (loading) {
    return (
      <div className="w-full h-96 bg-gray-100 rounded-xl flex items-center justify-center">
        <div className="loading-shimmer w-full h-full rounded-xl"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Region Filter */}
      <div className="flex flex-wrap gap-3">
        {regions.map((region) => (
          <button
            key={region.id}
            onClick={() => setSelectedRegion(region.id)}
            className={`px-4 py-2 rounded-lg font-medium transition-all duration-200 ${
              selectedRegion === region.id
                ? 'action-btn-primary'
                : 'action-btn-secondary'
            }`}
            style={selectedRegion === region.id ? {} : { borderColor: region.color, color: region.color }}
          >
            {region.name}
          </button>
        ))}
      </div>

      {/* Map Container */}
      <div className="map-container relative w-full h-96 bg-gradient-to-br from-blue-50 to-gray-100 rounded-xl overflow-hidden">
        <svg
          viewBox="0 0 800 400"
          className="w-full h-full"
          onMouseLeave={() => setTooltip(null)}
        >
          {/* US Map Background (Simplified) */}
          <rect x="0" y="0" width="800" height="400" fill="url(#mapGradient)" />
          
          <defs>
            <linearGradient id="mapGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#f8fafc" />
              <stop offset="100%" stopColor="#e2e8f0" />
            </linearGradient>
          </defs>

          {/* Account Markers */}
          {filteredAccounts.map((account) => {
            // Convert lat/lng to SVG coordinates (simplified projection)
            const x = ((account.longitude + 125) / 58) * 800; // Rough US longitude range
            const y = ((50 - account.latitude) / 25) * 400; // Rough US latitude range
            const size = getAccountSize(account.annual_revenue);
            const color = getHealthColor(account.health_score);
            
            return (
              <g key={account.id}>
                {/* Pulsing ring for critical accounts */}
                {account.churn_risk_score > 70 && (
                  <circle
                    cx={x}
                    cy={y}
                    r={size + 8}
                    fill="none"
                    stroke="#DC143C"
                    strokeWidth="2"
                    opacity="0.6"
                  >
                    <animate
                      attributeName="r"
                      values={`${size + 4};${size + 12};${size + 4}`}
                      dur="2s"
                      repeatCount="indefinite"
                    />
                    <animate
                      attributeName="opacity"
                      values="0.8;0.2;0.8"
                      dur="2s"
                      repeatCount="indefinite"
                    />
                  </circle>
                )}
                
                {/* Main account marker */}
                <circle
                  cx={x}
                  cy={y}
                  r={size}
                  fill={color}
                  stroke="white"
                  strokeWidth="2"
                  className="cursor-pointer transition-all duration-200"
                  onMouseEnter={(e) => handleAccountHover(account, e)}
                  style={{
                    filter: 'drop-shadow(0 4px 8px rgba(0,0,0,0.2))'
                  }}
                />
                
                {/* Account type icon */}
                <text
                  x={x}
                  y={y + 2}
                  textAnchor="middle"
                  fill="white"
                  fontSize="8"
                  fontWeight="bold"
                  className="pointer-events-none"
                >
                  {account.account_type === 'bottler' ? 'B' :
                   account.account_type === 'retailer' ? 'R' :
                   account.account_type === 'distributor' ? 'D' :
                   account.account_type === 'qsr' ? 'Q' : 'O'}
                </text>
              </g>
            );
          })}
        </svg>

        {/* Map Legend */}
        <div className="absolute bottom-4 left-4 bg-white rounded-lg p-4 shadow-lg border">
          <h4 className="font-semibold text-sm mb-2">Account Health</h4>
          <div className="space-y-1 text-xs">
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 rounded-full bg-green-600"></div>
              <span>Excellent (90-100)</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 rounded-full bg-yellow-600"></div>
              <span>Good (75-89)</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 rounded-full bg-orange-600"></div>
              <span>Fair (60-74)</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 rounded-full bg-red-600"></div>
              <span>Poor (40-59)</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 rounded-full" style={{backgroundColor: '#8B0A14'}}></div>
              <span>Critical (&lt;40)</span>
            </div>
          </div>
        </div>
      </div>

      {/* Tooltip */}
      {tooltip && (
        <div
          className="map-tooltip fixed z-50 pointer-events-none"
          style={{
            left: tooltip.x - 150,
            top: tooltip.y - 120,
            width: '300px'
          }}
        >
          <div className="bg-white rounded-lg shadow-xl border p-4">
            <h3 className="font-bold text-sm text-gray-900 mb-2">{tooltip.account.name}</h3>
            <div className="space-y-2 text-xs">
              <div className="flex justify-between">
                <span className="text-gray-600">Health Score:</span>
                <span className={`font-medium ${
                  tooltip.account.health_score >= 90 ? 'text-green-600' :
                  tooltip.account.health_score >= 75 ? 'text-yellow-600' :
                  tooltip.account.health_score >= 60 ? 'text-orange-600' : 'text-red-600'
                }`}>
                  {tooltip.account.health_score}%
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Annual Revenue:</span>
                <span className="font-medium">{formatCurrency(tooltip.account.annual_revenue)}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Churn Risk:</span>
                <span className={`font-medium ${
                  tooltip.account.churn_risk_score > 70 ? 'text-red-600' :
                  tooltip.account.churn_risk_score > 40 ? 'text-yellow-600' : 'text-green-600'
                }`}>
                  {tooltip.account.churn_risk_score}%
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Type:</span>
                <span className="font-medium capitalize">{tooltip.account.account_type}</span>
              </div>
              <div className="mt-2">
                <span className="text-gray-600 text-xs">Products:</span>
                <div className="flex flex-wrap gap-1 mt-1">
                  {tooltip.account.products.map((product) => (
                    <span
                      key={product}
                      className={`px-2 py-1 rounded text-xs font-medium product-${product}`}
                    >
                      {product.charAt(0).toUpperCase() + product.slice(1)}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Regional Summary */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        <div className="executive-card p-4 rounded-xl">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-green-100 rounded-lg">
              <Users className="h-5 w-5 text-green-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Active Accounts</p>
              <p className="text-xl font-bold text-gray-900">{filteredAccounts.length}</p>
            </div>
          </div>
        </div>
        
        <div className="executive-card p-4 rounded-xl">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-blue-100 rounded-lg">
              <DollarSign className="h-5 w-5 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Total Revenue</p>
              <p className="text-xl font-bold text-gray-900">
                {formatCurrency(filteredAccounts.reduce((sum, acc) => sum + acc.annual_revenue, 0))}
              </p>
            </div>
          </div>
        </div>
        
        <div className="executive-card p-4 rounded-xl">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-red-100 rounded-lg">
              <AlertTriangle className="h-5 w-5 text-red-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">High Risk Accounts</p>
              <p className="text-xl font-bold text-gray-900">
                {filteredAccounts.filter(acc => acc.churn_risk_score > 70).length}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
