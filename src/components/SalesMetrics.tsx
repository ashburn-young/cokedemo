'use client'

import { useEffect, useRef } from 'react'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, LineElement, PointElement } from 'chart.js'
import { Bar } from 'react-chartjs-2'

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
)

interface SalesMetricsProps {
  data?: Array<{ month: string; value: number }>
}

export default function SalesMetrics({ data }: SalesMetricsProps) {
  // Default data if none provided
  const defaultData = [
    { month: 'Jan', value: 196000000 },
    { month: 'Feb', value: 220500000 },
    { month: 'Mar', value: 196000000 },
    { month: 'Apr', value: 220500000 },
    { month: 'May', value: 196000000 },
    { month: 'Jun', value: 220500000 }
  ];

  const chartData = data || defaultData;

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(value)
  }

  const chartConfig = {
    labels: chartData.map(item => item.month),
    datasets: [
      {
        label: 'Monthly Revenue',
        data: chartData.map(item => item.value),
        backgroundColor: 'rgba(220, 38, 38, 0.8)',
        borderColor: 'rgba(220, 38, 38, 1)',
        borderWidth: 2,
        borderRadius: 4,
        borderSkipped: false,
      }
    ]
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false
      },
      title: {
        display: true,
        text: 'Revenue Trend (6 Months)',
        font: {
          size: 16,
          weight: 'bold' as const
        },
        color: '#1f2937'
      },
      tooltip: {
        callbacks: {
          label: function(context: any) {
            return `Revenue: ${formatCurrency(context.parsed.y)}`
          }
        }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function(value: any) {
            return formatCurrency(value)
          }
        },
        grid: {
          color: 'rgba(0, 0, 0, 0.1)'
        }
      },
      x: {
        grid: {
          display: false
        }
      }
    }
  }

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
      <div className="h-80">
        <Bar data={chartConfig} options={options} />
      </div>
      
      {/* Summary stats below chart */}
      <div className="mt-4 pt-4 border-t border-gray-200">
        <div className="grid grid-cols-3 gap-4 text-center">
          <div>
            <div className="text-sm text-gray-500">Current Month</div>
            <div className="text-lg font-bold text-gray-900">
              {chartData.length > 0 ? formatCurrency(chartData[chartData.length - 1].value) : '$0'}
            </div>
          </div>
          <div>
            <div className="text-sm text-gray-500">6-Month Average</div>
            <div className="text-lg font-bold text-gray-900">
              {formatCurrency(chartData.reduce((sum, item) => sum + item.value, 0) / chartData.length)}
            </div>
          </div>
          <div>
            <div className="text-sm text-gray-500">Growth Rate</div>
            <div className="text-lg font-bold text-green-600">              {chartData.length >= 2 ?
                `+${(((chartData[chartData.length - 1].value - chartData[0].value) / chartData[0].value) * 100).toFixed(1)}%`
                : '+0%'
              }
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
