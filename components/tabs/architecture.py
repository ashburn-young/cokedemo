"""
Architecture Tab - System Architecture, Technical Documentation, and Platform Overview
AI-enhanced architecture visualization with GPT-4o insights
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
from datetime import datetime, timedelta
import time

# Coca-Cola Brand Colors
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000', 
    'classic_white': '#FFFFFF',
    'coke_gold': '#FFC72C',
    'success_green': '#28a745',
    'warning_orange': '#ffc107',
    'info_blue': '#17a2b8',
    'light_gray': '#f8f9fa',
    'dark_gray': '#6c757d'
}

def generate_system_components():
    """Generate system architecture components"""
    return {
        "frontend": {
            "name": "Frontend Layer",
            "components": [
                {"name": "Next.js App Router", "type": "Framework", "status": "Active", "version": "14.0"},
                {"name": "React Components", "type": "UI Library", "status": "Active", "version": "18.2"},
                {"name": "Tailwind CSS", "type": "Styling", "status": "Active", "version": "3.3"},
                {"name": "TypeScript", "type": "Language", "status": "Active", "version": "5.0"},
                {"name": "Plotly/Chart.js", "type": "Visualization", "status": "Active", "version": "5.17"}
            ],
            "description": "Modern React-based frontend with responsive design and interactive visualizations"
        },
        "backend": {
            "name": "Backend Services",
            "components": [
                {"name": "Python FastAPI", "type": "API Framework", "status": "Active", "version": "0.104"},
                {"name": "Semantic Kernel", "type": "AI Orchestration", "status": "Active", "version": "0.9"},
                {"name": "Azure OpenAI", "type": "AI Service", "status": "Active", "version": "GPT-4o"},
                {"name": "SQLite Database", "type": "Data Storage", "status": "Active", "version": "3.44"},
                {"name": "Pydantic", "type": "Data Validation", "status": "Active", "version": "2.5"}
            ],
            "description": "High-performance Python backend with AI integration and robust data handling"
        },
        "ai_layer": {
            "name": "AI & Intelligence",
            "components": [
                {"name": "GPT-4o Engine", "type": "LLM", "status": "Active", "version": "Latest"},
                {"name": "Semantic Kernel", "type": "AI Framework", "status": "Active", "version": "0.9"},
                {"name": "Custom AI Agents", "type": "Business Logic", "status": "Active", "version": "Custom"},
                {"name": "Predictive Models", "type": "ML Models", "status": "Active", "version": "v2.1"},
                {"name": "Natural Language Processing", "type": "Text Analysis", "status": "Active", "version": "Latest"}
            ],
            "description": "Advanced AI layer with GPT-4o integration for intelligent business insights"
        },
        "data_layer": {
            "name": "Data & Analytics",
            "components": [
                {"name": "Enhanced Data Generator", "type": "Data Source", "status": "Active", "version": "2.0"},
                {"name": "Pandas Analytics", "type": "Data Processing", "status": "Active", "version": "2.1"},
                {"name": "Streamlit Dashboard", "type": "Analytics UI", "status": "Active", "version": "1.28"},
                {"name": "Real-time Metrics", "type": "Monitoring", "status": "Active", "version": "Live"},
                {"name": "Export Capabilities", "type": "Data Export", "status": "Active", "version": "Multi-format"}
            ],
            "description": "Comprehensive data management with real-time analytics and reporting"
        }
    }

def generate_architecture_metrics():
    """Generate architecture performance metrics"""
    return {
        "performance": {
            "response_time": "< 200ms",
            "uptime": "99.9%",
            "concurrent_users": "500+",
            "api_calls_per_minute": "1,200",
            "data_processing_speed": "10K records/sec"
        },
        "scalability": {
            "horizontal_scaling": "Auto-scaling enabled",
            "vertical_scaling": "Dynamic resource allocation",
            "load_balancing": "Multi-region deployment",
            "caching_strategy": "Redis + CDN",
            "database_scaling": "Read replicas + sharding"
        },
        "security": {
            "authentication": "OAuth 2.0 + JWT",
            "authorization": "Role-based access control",
            "data_encryption": "AES-256 at rest, TLS 1.3 in transit",
            "api_security": "Rate limiting + API keys",
            "compliance": "SOC 2 Type II + GDPR"
        },
        "reliability": {
            "backup_strategy": "Automated daily backups",
            "disaster_recovery": "Multi-region failover",
            "monitoring": "24/7 application monitoring",
            "alerting": "Real-time incident detection",
            "sla": "99.9% availability guarantee"
        }
    }

def generate_technical_stack():
    """Generate detailed technical stack information"""
    return {
        "languages": [
            {"name": "TypeScript", "percentage": 45, "purpose": "Frontend development"},
            {"name": "Python", "percentage": 35, "purpose": "Backend services & AI"},
            {"name": "SQL", "percentage": 10, "purpose": "Database queries"},
            {"name": "HTML/CSS", "percentage": 8, "purpose": "Markup & styling"},
            {"name": "JavaScript", "percentage": 2, "purpose": "Legacy components"}
        ],
        "frameworks": [
            {"category": "Frontend", "technologies": ["Next.js", "React", "Tailwind CSS"]},
            {"category": "Backend", "technologies": ["FastAPI", "Semantic Kernel", "Pydantic"]},
            {"category": "AI/ML", "technologies": ["Azure OpenAI", "GPT-4o", "Custom Agents"]},
            {"category": "Data", "technologies": ["Pandas", "NumPy", "Plotly"]},
            {"category": "UI/UX", "technologies": ["Streamlit", "Chart.js", "Responsive Design"]}
        ],
        "infrastructure": [
            {"component": "Hosting", "technology": "Azure App Service", "tier": "Production"},
            {"component": "Database", "technology": "Azure SQL Database", "tier": "Standard"},
            {"component": "AI Services", "technology": "Azure OpenAI", "tier": "Enterprise"},
            {"component": "CDN", "technology": "Azure CDN", "tier": "Premium"},
            {"component": "Monitoring", "technology": "Azure Monitor", "tier": "Standard"}
        ]
    }

def generate_deployment_architecture():
    """Generate deployment and DevOps information"""
    return {
        "environments": [
            {"name": "Development", "status": "Active", "url": "dev-cokesales.azurewebsites.net", "version": "latest"},
            {"name": "Staging", "status": "Active", "url": "staging-cokesales.azurewebsites.net", "version": "v2.1.0"},
            {"name": "Production", "status": "Active", "url": "cokesales.azurewebsites.net", "version": "v2.0.5"},
            {"name": "Demo", "status": "Active", "url": "demo-cokesales.azurewebsites.net", "version": "v2.1.0-rc"}
        ],
        "cicd_pipeline": {
            "source_control": "GitHub",
            "build_system": "GitHub Actions",
            "testing": "Automated unit & integration tests",
            "deployment": "Azure DevOps Pipelines",
            "monitoring": "Application Insights + Custom dashboards"
        },
        "data_flow": [
            {"step": 1, "process": "Data Ingestion", "description": "CRM data from multiple sources"},
            {"step": 2, "process": "Data Processing", "description": "Clean, transform, and enrich data"},
            {"step": 3, "process": "AI Analysis", "description": "GPT-4o generates insights and recommendations"},
            {"step": 4, "process": "Real-time Updates", "description": "Live dashboard updates and alerts"},
            {"step": 5, "process": "User Interaction", "description": "Interactive dashboards and reports"}
        ]
    }

def generate_ai_architecture():
    """Generate AI-specific architecture details"""
    return {
        "ai_workflow": [
            {"stage": "Data Ingestion", "ai_component": "Data Quality Assessment", "description": "AI validates and scores data quality"},
            {"stage": "Processing", "ai_component": "Intelligent ETL", "description": "ML-driven data transformation and enrichment"},
            {"stage": "Analysis", "ai_component": "GPT-4o Reasoning", "description": "Advanced language model for business insights"},
            {"stage": "Prediction", "ai_component": "Custom ML Models", "description": "Specialized models for sales forecasting"},
            {"stage": "Recommendation", "ai_component": "Decision Engine", "description": "AI-powered strategic recommendations"},
            {"stage": "Interaction", "ai_component": "Conversational AI", "description": "Natural language query interface"}
        ],
        "model_architecture": {
            "primary_llm": {
                "name": "GPT-4o",
                "provider": "Azure OpenAI",
                "context_window": "128K tokens",
                "capabilities": ["Text generation", "Analysis", "Code generation", "Reasoning"]
            },
            "specialized_models": [
                {"name": "Sentiment Analysis", "type": "BERT-based", "accuracy": "94%"},
                {"name": "Churn Prediction", "type": "XGBoost", "accuracy": "89%"},
                {"name": "Demand Forecasting", "type": "Time Series LSTM", "accuracy": "92%"},
                {"name": "Price Optimization", "type": "Reinforcement Learning", "accuracy": "87%"}
            ]
        },
        "ai_capabilities": [
            "Natural language query processing",
            "Automated insight generation",
            "Predictive analytics and forecasting",
            "Intelligent recommendation engine",
            "Real-time anomaly detection",
            "Conversational business intelligence"
        ]
    }

def render_architecture():
    """Main function to render the Architecture tab"""
    
    st.markdown("# 🏗️ System Architecture & Technical Documentation")
    st.markdown("*Comprehensive platform architecture, technical stack, and AI integration details*")
    
    # Generate data
    system_components = generate_system_components()
    arch_metrics = generate_architecture_metrics()
    tech_stack = generate_technical_stack()
    deployment_arch = generate_deployment_architecture()
    ai_architecture = generate_ai_architecture()
    
    # Key architecture metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("System Components", "47", "+3")
    
    with col2:
        st.metric("Uptime", arch_metrics["performance"]["uptime"], "+0.1%")
    
    with col3:
        st.metric("Response Time", arch_metrics["performance"]["response_time"], "-15ms")
    
    with col4:
        st.metric("AI Accuracy", "91.2%", "+2.3%")
    
    st.divider()
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏗️ System Overview", 
        "⚙️ Technical Stack", 
        "🤖 AI Architecture", 
        "🚀 Deployment",
        "📊 Performance Metrics",
        "📚 Documentation"
    ])
    
    with tab1:
        st.markdown("### 🏗️ System Architecture Overview")
        
        # Architecture diagram using text-based representation
        st.markdown("#### 🎯 High-Level Architecture")
        
        st.markdown("""
        ```
        ┌─────────────────────────────────────────────────────────────────┐
        │                         User Interface Layer                     │
        │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
        │  │   Next.js Web   │  │  Streamlit      │  │   Mobile Apps   │  │
        │  │   Application   │  │  Dashboard      │  │   (Future)      │  │
        │  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
        └─────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
        ┌─────────────────────────────────────────────────────────────────┐
        │                      API Gateway & Load Balancer                 │
        │              ┌─────────────────────────────────────┐              │
        │              │         Azure API Management        │              │
        │              └─────────────────────────────────────┘              │
        └─────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
        ┌─────────────────────────────────────────────────────────────────┐
        │                      Business Logic Layer                        │
        │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
        │  │  Sales Agent    │  │ Customer Agent  │  │Forecasting Agent│  │
        │  │   (GPT-4o)      │  │   (GPT-4o)      │  │   (GPT-4o)      │  │
        │  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
        └─────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
        ┌─────────────────────────────────────────────────────────────────┐
        │                         AI & ML Layer                            │
        │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
        │  │  Azure OpenAI   │  │ Semantic Kernel │  │ Custom Models   │  │
        │  │    (GPT-4o)     │  │   Framework     │  │  (Scikit-learn) │  │
        │  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
        └─────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
        ┌─────────────────────────────────────────────────────────────────┐
        │                        Data Layer                                │
        │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
        │  │   Azure SQL     │  │    Redis Cache  │  │   Blob Storage  │  │
        │  │   Database      │  │                 │  │                 │  │
        │  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
        └─────────────────────────────────────────────────────────────────┘
        ```
        """)
        
        # System components overview
        st.markdown("#### 🔧 System Components")
        
        for layer_key, layer_data in system_components.items():
            with st.expander(f"🏗️ {layer_data['name']} - {len(layer_data['components'])} Components"):
                st.markdown(f"**Description:** {layer_data['description']}")
                
                # Components table
                components_df = pd.DataFrame(layer_data['components'])
                st.dataframe(components_df, use_container_width=True)
                
                # Component status visualization
                status_counts = components_df['status'].value_counts()
                
                fig_status = px.pie(
                    values=status_counts.values,
                    names=status_counts.index,
                    title=f"{layer_data['name']} - Component Status",
                    color_discrete_map={'Active': '#28a745', 'Maintenance': '#ffc107', 'Inactive': '#dc3545'}
                )
                
                st.plotly_chart(fig_status, use_container_width=True)
        
        # Data flow visualization
        st.markdown("#### 🔄 Data Flow Architecture")
        
        flow_steps = deployment_arch["data_flow"]
        
        # Create flow diagram
        fig_flow = go.Figure()
        
        x_positions = list(range(len(flow_steps)))
        y_position = [1] * len(flow_steps)
        
        # Add nodes
        for i, step in enumerate(flow_steps):
            fig_flow.add_trace(go.Scatter(
                x=[i],
                y=[1],
                mode='markers+text',
                marker=dict(size=60, color='#007bff'),
                text=str(step['step']),
                textposition='middle center',
                textfont=dict(color='white', size=16),
                showlegend=False,
                hovertemplate=f"<b>{step['process']}</b><br>{step['description']}<extra></extra>"
            ))
        
        # Add arrows
        for i in range(len(flow_steps) - 1):
            fig_flow.add_annotation(
                x=i + 0.5,
                y=1,
                ax=i,
                ay=1,
                xref='x',
                yref='y',
                axref='x',
                ayref='y',
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor='#007bff'
            )
        
        # Add step labels
        for i, step in enumerate(flow_steps):
            fig_flow.add_annotation(
                x=i,
                y=0.7,
                text=f"<b>{step['process']}</b><br><span style='font-size:10px'>{step['description']}</span>",
                showarrow=False,
                font=dict(size=10),
                align='center'
            )
        
        fig_flow.update_layout(
            title="Data Processing Flow",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 1.5]),
            height=300,
            margin=dict(l=50, r=50, t=50, b=100)
        )
        
        st.plotly_chart(fig_flow, use_container_width=True)
    
    with tab2:
        st.markdown("### ⚙️ Technical Stack Details")
        
        # Programming languages
        st.markdown("#### 💻 Programming Languages")
        
        languages_df = pd.DataFrame(tech_stack["languages"])
        
        fig_languages = px.pie(
            languages_df,
            values='percentage',
            names='name',
            title="Codebase Composition",
            hover_data=['purpose']
        )
        
        st.plotly_chart(fig_languages, use_container_width=True)
        
        # Display languages table
        st.dataframe(languages_df, use_container_width=True)
        
        # Frameworks and technologies
        st.markdown("#### 🛠️ Frameworks & Technologies")
        
        for framework in tech_stack["frameworks"]:
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                border-left: 5px solid {COKE_COLORS['info_blue']};
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h4 style="margin: 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{framework['category']}</h4>
                <p style="margin: 10px 0; color: {COKE_COLORS['coke_black']}; font-size: 14px;">
                    {' • '.join(framework['technologies'])}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Infrastructure
        st.markdown("#### ☁️ Infrastructure & Hosting")
        
        infra_df = pd.DataFrame(tech_stack["infrastructure"])
        
        # Infrastructure visualization
        fig_infra = px.bar(
            infra_df,
            x='component',
            y=[1] * len(infra_df),  # Same height for all
            color='tier',
            title="Infrastructure Components by Tier",
            text='technology',
            color_discrete_map={
                'Production': '#dc3545',
                'Enterprise': '#28a745', 
                'Premium': '#6f42c1',
                'Standard': '#007bff'
            }
        )
        
        fig_infra.update_traces(textposition='inside')
        fig_infra.update_layout(showlegend=True, yaxis_title="")
        
        st.plotly_chart(fig_infra, use_container_width=True)
        
        # Technology version tracking
        st.markdown("#### 📦 Version Management")
        
        version_data = [
            {"Component": "Next.js", "Current": "14.0.3", "Latest": "14.0.4", "Status": "Up to date"},
            {"Component": "React", "Current": "18.2.0", "Latest": "18.2.0", "Status": "Current"},
            {"Component": "Python", "Current": "3.11.5", "Latest": "3.12.0", "Status": "Upgrade available"},
            {"Component": "FastAPI", "Current": "0.104.1", "Latest": "0.104.1", "Status": "Current"},
            {"Component": "Streamlit", "Current": "1.28.1", "Latest": "1.29.0", "Status": "Upgrade available"}
        ]
        
        version_df = pd.DataFrame(version_data)
        
        # Color code based on status
        def get_status_color(status):
            if status == "Current":
                return "#28a745"
            elif status == "Up to date":
                return "#007bff"
            else:
                return "#ffc107"
        
        for _, version in version_df.iterrows():
            color = get_status_color(version['Status'])
            
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border: 2px solid {color};
                border-radius: 8px;
                padding: 12px;
                margin: 8px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <div>
                    <strong>{version['Component']}</strong><br>
                    <small>Current: {version['Current']} | Latest: {version['Latest']}</small>
                </div>
                <span style="color: {color}; font-weight: bold;">{version['Status']}</span>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🤖 AI Architecture & Integration")
        
        # AI workflow
        st.markdown("#### 🔄 AI Processing Workflow")
        
        ai_workflow = ai_architecture["ai_workflow"]
        
        # Create AI workflow visualization
        workflow_fig = go.Figure()
        
        for i, stage in enumerate(ai_workflow):
            # Add workflow step
            workflow_fig.add_trace(go.Scatter(
                x=[i],
                y=[2],
                mode='markers+text',
                marker=dict(size=80, color='#6f42c1'),
                text=stage['stage'],
                textposition='middle center',
                textfont=dict(color='white', size=10),
                showlegend=False,
                name=stage['stage']
            ))
            
            # Add AI component
            workflow_fig.add_trace(go.Scatter(
                x=[i],
                y=[1],
                mode='markers+text',
                marker=dict(size=60, color='#007bff'),
                text=stage['ai_component'][:15] + '...' if len(stage['ai_component']) > 15 else stage['ai_component'],
                textposition='middle center',
                textfont=dict(color='white', size=8),
                showlegend=False,
                hovertemplate=f"<b>{stage['ai_component']}</b><br>{stage['description']}<extra></extra>"
            ))
            
            # Add connection
            workflow_fig.add_trace(go.Scatter(
                x=[i, i],
                y=[2, 1],
                mode='lines',
                line=dict(color='#6c757d', width=2),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Add arrows between stages
        for i in range(len(ai_workflow) - 1):
            workflow_fig.add_annotation(
                x=i + 0.5,
                y=2,
                ax=i,
                ay=2,
                xref='x',
                yref='y',
                axref='x',
                ayref='y',
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor='#6f42c1'
            )
        
        workflow_fig.update_layout(
            title="AI Processing Workflow",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 2.5]),
            height=400,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        
        st.plotly_chart(workflow_fig, use_container_width=True)
        
        # Model architecture
        st.markdown("#### 🧠 AI Model Architecture")
        
        model_arch = ai_architecture["model_architecture"]
        
        # Primary LLM details
        st.markdown("##### 🎯 Primary Language Model")
        
        primary_llm = model_arch["primary_llm"]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Model:** {primary_llm['name']}")
            st.markdown(f"**Provider:** {primary_llm['provider']}")
            st.markdown(f"**Context Window:** {primary_llm['context_window']}")
            st.markdown(f"**Capabilities:** {', '.join(primary_llm['capabilities'])}")
        
        with col2:
            # Capability visualization
            capabilities = primary_llm['capabilities']
            capability_scores = [95, 92, 88, 94]  # Mock scores
            
            fig_capabilities = go.Figure(go.Bar(
                x=capability_scores,
                y=capabilities,
                orientation='h',
                marker_color='#6f42c1'
            ))
            
            fig_capabilities.update_layout(
                title="Capability Scores",
                xaxis_title="Performance %",
                height=300
            )
            
            st.plotly_chart(fig_capabilities, use_container_width=True)
        
        # Specialized models
        st.markdown("##### 🎯 Specialized ML Models")
        
        specialized_models = model_arch["specialized_models"]
        specialized_df = pd.DataFrame(specialized_models)
        
        # Model accuracy comparison
        fig_models = px.bar(
            specialized_df,
            x='name',
            y='accuracy',
            color='type',
            title="Specialized Model Performance",
            text='accuracy'
        )
        
        fig_models.update_traces(texttemplate='%{text}', textposition='outside')
        fig_models.update_layout(xaxis_tickangle=-45)
        
        st.plotly_chart(fig_models, use_container_width=True)
        
        # AI capabilities
        st.markdown("#### 🚀 AI Platform Capabilities")
        
        capabilities = ai_architecture["ai_capabilities"]
        
        for i, capability in enumerate(capabilities):
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #6f42c1 0%, #007bff 100%);
                color: white;
                padding: 12px;
                margin: 8px 0;
                border-radius: 8px;
                border-left: 5px solid #ffc107;
            ">
                <strong>#{i+1}: {capability}</strong>
            </div>
            """, unsafe_allow_html=True)
        
        # AI integration patterns
        st.markdown("#### 🔗 AI Integration Patterns")
        
        integration_patterns = [
            {"pattern": "Function Calling", "usage": "Structured data retrieval and processing", "frequency": "High"},
            {"pattern": "Prompt Engineering", "usage": "Optimized AI responses for business context", "frequency": "High"},
            {"pattern": "Chain of Thought", "usage": "Complex reasoning and analysis tasks", "frequency": "Medium"},
            {"pattern": "Retrieval Augmented Generation", "usage": "Context-aware responses using business data", "frequency": "High"},
            {"pattern": "Few-Shot Learning", "usage": "Quick adaptation to new business scenarios", "frequency": "Medium"},
            {"pattern": "Multi-Agent Orchestration", "usage": "Coordinated AI agents for complex workflows", "frequency": "High"}
        ]
        
        for pattern in integration_patterns:
            frequency_color = COKE_COLORS['success_green'] if pattern["frequency"] == "High" else COKE_COLORS['warning_orange'] if pattern["frequency"] == "Medium" else COKE_COLORS['primary_red']
            
            st.markdown(f"""
            <div style="
                background: {COKE_COLORS['classic_white']};
                border-left: 6px solid {frequency_color};
                padding: 20px;
                margin: 12px 0;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0 0 8px 0; color: {COKE_COLORS['coke_black']}; font-weight: 600;">{pattern['pattern']}</h4>
                        <p style="margin: 0; color: {COKE_COLORS['dark_gray']}; font-size: 14px; line-height: 1.4;">{pattern['usage']}</p>
                    </div>
                    <span style="
                        color: {frequency_color}; 
                        font-weight: bold; 
                        font-size: 16px;
                        background: {frequency_color}20;
                        padding: 8px 12px;
                        border-radius: 20px;
                        white-space: nowrap;
                    ">{pattern['frequency']} Usage</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 🚀 Deployment Architecture")
        
        # Environment overview
        st.markdown("#### 🌍 Environment Overview")
        
        environments = deployment_arch["environments"]
        env_df = pd.DataFrame(environments)
        
        # Environment status visualization
        fig_env = px.bar(
            env_df,
            x='name',
            y=[1] * len(env_df),  # Same height
            color='status',
            title="Environment Status",
            text='version',
            color_discrete_map={'Active': '#28a745', 'Maintenance': '#ffc107', 'Inactive': '#dc3545'}
        )
        
        fig_env.update_traces(textposition='inside')
        fig_env.update_layout(yaxis_title="", showlegend=False)
        
        st.plotly_chart(fig_env, use_container_width=True)
        
        # Environment details
        for env in environments:
            status_color = "#28a745" if env['status'] == "Active" else "#ffc107" if env['status'] == "Maintenance" else "#dc3545"
            
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border: 2px solid {status_color};
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0; color: #333;">{env['name']} Environment</h4>
                        <small style="color: #666;">URL: {env['url']}</small>
                    </div>
                    <div style="text-align: right;">
                        <span style="color: {status_color}; font-weight: bold;">{env['status']}</span><br>
                        <small style="color: #666;">{env['version']}</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # CI/CD Pipeline
        st.markdown("#### 🔄 CI/CD Pipeline")
        
        cicd = deployment_arch["cicd_pipeline"]
        
        pipeline_steps = [
            {"step": "Source Control", "tool": cicd["source_control"], "description": "Code versioning and collaboration"},
            {"step": "Build", "tool": cicd["build_system"], "description": "Automated builds and testing"},
            {"step": "Testing", "tool": cicd["testing"], "description": "Quality assurance and validation"},
            {"step": "Deployment", "tool": cicd["deployment"], "description": "Automated deployment to environments"},
            {"step": "Monitoring", "tool": cicd["monitoring"], "description": "Performance and health monitoring"}
        ]
        
        # Pipeline visualization
        pipeline_fig = go.Figure()
        
        for i, step in enumerate(pipeline_steps):
            pipeline_fig.add_trace(go.Scatter(
                x=[i],
                y=[1],
                mode='markers+text',
                marker=dict(size=80, color='#007bff'),
                text=step['step'],
                textposition='middle center',
                textfont=dict(color='white', size=10),
                showlegend=False,
                hovertemplate=f"<b>{step['step']}</b><br>Tool: {step['tool']}<br>{step['description']}<extra></extra>"
            ))
        
        # Add arrows
        for i in range(len(pipeline_steps) - 1):
            pipeline_fig.add_annotation(
                x=i + 0.5,
                y=1,
                ax=i,
                ay=1,
                xref='x',
                yref='y',
                axref='x',
                ayref='y',
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor='#007bff'
            )
        
        pipeline_fig.update_layout(
            title="CI/CD Pipeline Flow",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 1.5]),
            height=300
        )
        
        st.plotly_chart(pipeline_fig, use_container_width=True)
        
        # Deployment strategy
        st.markdown("#### 📋 Deployment Strategy")
        
        deployment_strategies = [
            {"strategy": "Blue-Green Deployment", "benefit": "Zero-downtime deployments", "status": "Implemented"},
            {"strategy": "Rolling Updates", "benefit": "Gradual feature rollout", "status": "Implemented"},
            {"strategy": "Feature Flags", "benefit": "Safe feature testing", "status": "Planned"},
            {"strategy": "Canary Releases", "benefit": "Risk mitigation", "status": "In Progress"},
            {"strategy": "Automated Rollback", "benefit": "Quick recovery", "status": "Implemented"}
        ]
        
        for strategy in deployment_strategies:
            status_color = "#28a745" if strategy["status"] == "Implemented" else "#007bff" if strategy["status"] == "In Progress" else "#ffc107"
            
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border-left: 5px solid {status_color};
                padding: 12px;
                margin: 8px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>{strategy['strategy']}</strong><br>
                        <small style="color: #666;">{strategy['benefit']}</small>
                    </div>
                    <span style="color: {status_color}; font-weight: bold;">{strategy['status']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 📊 Performance Metrics & Monitoring")
        
        # Performance metrics overview
        st.markdown("#### ⚡ Performance Metrics")
        
        performance = arch_metrics["performance"]
        
        perf_col1, perf_col2, perf_col3 = st.columns(3)
        
        with perf_col1:
            st.metric("Response Time", performance["response_time"], "-15ms")
            st.metric("Uptime", performance["uptime"], "+0.1%")
        
        with perf_col2:
            st.metric("Concurrent Users", performance["concurrent_users"], "+50")
            st.metric("API Calls/Min", performance["api_calls_per_minute"], "+200")
        
        with perf_col3:
            st.metric("Processing Speed", performance["data_processing_speed"], "+2K/sec")
        
        # Performance trends (mock data)
        st.markdown("#### 📈 Performance Trends")
        
        # Generate trend data
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        
        perf_trends = pd.DataFrame({
            'Date': dates,
            'Response_Time': np.random.normal(180, 20, 30),
            'Throughput': np.random.normal(1200, 100, 30),
            'Error_Rate': np.random.exponential(0.01, 30),
            'CPU_Usage': np.random.normal(65, 10, 30)
        })
        
        # Multi-metric performance chart
        fig_perf = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Response Time (ms)', 'API Throughput', 'Error Rate (%)', 'CPU Usage (%)'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        fig_perf.add_trace(
            go.Scatter(x=perf_trends['Date'], y=perf_trends['Response_Time'], name='Response Time'),
            row=1, col=1
        )
        
        fig_perf.add_trace(
            go.Scatter(x=perf_trends['Date'], y=perf_trends['Throughput'], name='Throughput'),
            row=1, col=2
        )
        
        fig_perf.add_trace(
            go.Scatter(x=perf_trends['Date'], y=perf_trends['Error_Rate']*100, name='Error Rate'),
            row=2, col=1
        )
        
        fig_perf.add_trace(
            go.Scatter(x=perf_trends['Date'], y=perf_trends['CPU_Usage'], name='CPU Usage'),
            row=2, col=2
        )
        
        fig_perf.update_layout(height=600, showlegend=False, title_text="30-Day Performance Trends")
        st.plotly_chart(fig_perf, use_container_width=True)
        
        # System health categories
        st.markdown("#### 🏥 System Health Categories")
        
        health_categories = ["Performance", "Scalability", "Security", "Reliability"]
        
        for category in health_categories:
            category_data = arch_metrics[category.lower()]
            
            with st.expander(f"🔍 {category} Metrics"):
                for metric, value in category_data.items():
                    st.markdown(f"**{metric.replace('_', ' ').title()}:** {value}")
        
        # Monitoring dashboard
        st.markdown("#### 📡 Real-Time Monitoring")
        
        monitoring_data = [
            {"Service": "Frontend", "Status": "Healthy", "Response": "145ms", "Load": "Low"},
            {"Service": "API Gateway", "Status": "Healthy", "Response": "89ms", "Load": "Medium"},
            {"Service": "AI Services", "Status": "Healthy", "Response": "234ms", "Load": "High"},
            {"Service": "Database", "Status": "Healthy", "Response": "12ms", "Load": "Low"},
            {"Service": "Cache", "Status": "Healthy", "Response": "3ms", "Load": "Medium"}
        ]
        
        for service in monitoring_data:
            status_color = "#28a745" if service["Status"] == "Healthy" else "#ffc107" if service["Status"] == "Warning" else "#dc3545"
            load_color = "#dc3545" if service["Load"] == "High" else "#ffc107" if service["Load"] == "Medium" else "#28a745"
            
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 12px;
                margin: 8px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <div>
                    <strong>{service['Service']}</strong><br>
                    <small style="color: #666;">Response: {service['Response']}</small>
                </div>
                <div style="text-align: right;">
                    <span style="color: {status_color}; font-weight: bold;">{service['Status']}</span><br>
                    <small style="color: {load_color};">Load: {service['Load']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab6:
        st.markdown("### 📚 Technical Documentation")
        
        # Documentation sections
        st.markdown("#### 📖 Documentation Index")
        
        docs_sections = [
            {
                "title": "API Documentation",
                "description": "Complete REST API reference with examples",
                "status": "Complete",
                "last_updated": "2024-01-15"
            },
            {
                "title": "Deployment Guide",
                "description": "Step-by-step deployment instructions",
                "status": "Complete",
                "last_updated": "2024-01-12"
            },
            {
                "title": "AI Integration Guide",
                "description": "How to configure and use AI features",
                "status": "In Progress",
                "last_updated": "2024-01-10"
            },
            {
                "title": "Architecture Decisions",
                "description": "Technical decision records and rationale",
                "status": "Complete",
                "last_updated": "2024-01-08"
            },
            {
                "title": "Security Guidelines",
                "description": "Security best practices and compliance",
                "status": "Complete",
                "last_updated": "2024-01-14"
            },
            {
                "title": "Troubleshooting Guide",
                "description": "Common issues and solutions",
                "status": "In Progress",
                "last_updated": "2024-01-11"
            }
        ]
        
        for doc in docs_sections:
            status_color = "#28a745" if doc["status"] == "Complete" else "#ffc107" if doc["status"] == "In Progress" else "#dc3545"
            
            with st.expander(f"📄 {doc['title']} ({doc['status']})"):
                st.markdown(f"**Description:** {doc['description']}")
                st.markdown(f"**Status:** <span style='color: {status_color}'>{doc['status']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Last Updated:** {doc['last_updated']}")
                
                if st.button(f"📖 View Documentation", key=f"doc_{doc['title']}"):
                    st.success(f"✅ Opening {doc['title']} documentation...")
        
        # Quick reference
        st.markdown("#### ⚡ Quick Reference")
        
        quick_ref = {
            "🔗 Repository": "https://github.com/company/coke-sales-ai",
            "📊 Live Dashboard": "https://cokesales.azurewebsites.net",
            "🚀 CI/CD Pipeline": "https://dev.azure.com/company/coke-sales",
            "📡 Monitoring": "https://portal.azure.com/monitoring",
            "🔧 API Docs": "https://api.cokesales.com/docs",
            "📚 Wiki": "https://wiki.company.com/coke-sales-ai"
        }
        
        for name, url in quick_ref.items():
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border: 1px solid #007bff;
                border-radius: 5px;
                padding: 10px;
                margin: 5px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <span>{name}</span>
                <a href="{url}" target="_blank" style="
                    background: #007bff;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 3px;
                    text-decoration: none;
                    font-size: 12px;
                ">Open ↗</a>
            </div>
            """, unsafe_allow_html=True)
        
        # Architecture decisions log
        st.markdown("#### 📋 Architecture Decision Records (ADRs)")
        
        adrs = [
            {
                "id": "ADR-001",
                "title": "Choice of Next.js for Frontend",
                "date": "2024-01-05",
                "status": "Accepted",
                "summary": "Selected Next.js for better SEO, performance, and developer experience"
            },
            {
                "id": "ADR-002", 
                "title": "Azure OpenAI for AI Services",
                "date": "2024-01-03",
                "status": "Accepted",
                "summary": "Chose Azure OpenAI for enterprise compliance and integration"
            },
            {
                "id": "ADR-003",
                "title": "Semantic Kernel for AI Orchestration",
                "date": "2024-01-02",
                "status": "Accepted",
                "summary": "Adopted Semantic Kernel for structured AI agent development"
            },
            {
                "id": "ADR-004",
                "title": "Streamlit for Analytics Dashboard",
                "date": "2023-12-28",
                "status": "Accepted",
                "summary": "Selected Streamlit for rapid analytics dashboard development"
            }
        ]
        
        for adr in adrs:
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border-left: 5px solid #28a745;
                padding: 12px;
                margin: 8px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>{adr['id']}: {adr['title']}</strong><br>
                        <small style="color: #666;">{adr['summary']}</small>
                    </div>
                    <div style="text-align: right;">
                        <span style="color: #28a745; font-weight: bold;">{adr['status']}</span><br>
                        <small style="color: #666;">{adr['date']}</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_architecture()
