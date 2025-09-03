"""
Enhanced Architecture Diagram Renderer for Coca-Cola Sales Platform
Provides multiple rendering methods with robust fallbacks
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Coca-Cola Color Palette
COKE_COLORS = {
    'primary_red': '#DC143C',
    'executive_blue': '#3B82F6',
    'executive_green': '#10B981',
    'coke_gold': '#F59E0B',
    'executive_purple': '#8B5CF6',
    'warning_orange': '#F97316',
    'coke_black': '#1F2937',
    'dark_gray': '#374151',
    'white': '#FFFFFF'
}

class ArchitectureDiagramRenderer:
    """Enhanced diagram renderer with multiple fallback methods"""
    
    @staticmethod
    def create_high_level_architecture_plotly():
        """Create high-level architecture diagram using Plotly"""
        fig = go.Figure()
        
        # Define components and their positions
        components = [
            # Frontend Layer
            {"name": "Next.js Dashboard", "x": 1, "y": 4, "color": COKE_COLORS['primary_red'], "layer": "Frontend"},
            {"name": "Streamlit Analytics", "x": 3, "y": 4, "color": COKE_COLORS['primary_red'], "layer": "Frontend"},
            
            # API Gateway
            {"name": "FastAPI Gateway", "x": 2, "y": 3, "color": COKE_COLORS['executive_blue'], "layer": "API"},
            
            # AI Layer
            {"name": "Semantic Kernel", "x": 1, "y": 2, "color": COKE_COLORS['executive_green'], "layer": "AI"},
            {"name": "Azure OpenAI", "x": 2, "y": 2, "color": COKE_COLORS['executive_green'], "layer": "AI"},
            {"name": "GPT-4o Agents", "x": 3, "y": 2, "color": COKE_COLORS['executive_green'], "layer": "AI"},
            
            # Data Layer
            {"name": "CRM Data", "x": 0.5, "y": 1, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            {"name": "Freestyle Telemetry", "x": 1.5, "y": 1, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            {"name": "Sales Analytics", "x": 2.5, "y": 1, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            {"name": "Market Intelligence", "x": 3.5, "y": 1, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
        ]
        
        # Add components as scatter points
        for comp in components:
            fig.add_trace(go.Scatter(
                x=[comp["x"]], y=[comp["y"]],
                mode='markers+text',
                marker=dict(size=60, color=comp["color"], line=dict(width=2, color='white')),
                text=comp["name"],
                textposition="middle center",
                textfont=dict(color='white', size=10, family="Arial Black"),
                name=comp["layer"],
                showlegend=True if comp == components[0] or 
                         (comp["layer"] not in [c["layer"] for c in components[:components.index(comp)]]) else False
            ))
        
        # Add connections
        connections = [
            # Frontend to API
            ([1, 2], [4, 3]), ([3, 2], [4, 3]),
            # API to AI
            ([2, 1], [3, 2]), ([2, 2], [3, 2]), ([2, 3], [3, 2]),
            # AI to Data
            ([1, 0.5], [2, 1]), ([2, 1.5], [2, 1]), ([3, 2.5], [2, 1]), ([2, 3.5], [2, 1])
        ]
        
        for conn in connections:
            fig.add_trace(go.Scatter(
                x=conn[0], y=conn[1],
                mode='lines',
                line=dict(color='rgba(255,255,255,0.3)', width=2),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        fig.update_layout(
            title={
                'text': "🏗️ Coca-Cola Sales AI Platform - High-Level Architecture",
                'x': 0.5,
                'font': {'size': 20, 'color': 'white', 'family': 'Arial Black'}
            },
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.5, 4.5]),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 4.5]),
            plot_bgcolor=COKE_COLORS['coke_black'],
            paper_bgcolor=COKE_COLORS['coke_black'],
            font=dict(color='white'),
            height=600,
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        return fig
    
    @staticmethod
    def create_ai_agent_ecosystem_plotly():
        """Create AI agent ecosystem diagram using Plotly"""
        fig = go.Figure()
        
        # Central orchestrator
        fig.add_trace(go.Scatter(
            x=[2], y=[2.5],
            mode='markers+text',
            marker=dict(size=80, color=COKE_COLORS['primary_red'], line=dict(width=3, color='white')),
            text="Semantic<br>Kernel<br>Orchestrator",
            textposition="middle center",
            textfont=dict(color='white', size=12, family="Arial Black"),
            name="Orchestrator"
        ))
        
        # AI Agents around the orchestrator
        agents = [
            {"name": "Sales<br>Performance<br>Agent", "x": 0.5, "y": 4, "color": COKE_COLORS['executive_blue']},
            {"name": "Customer<br>Intelligence<br>Agent", "x": 3.5, "y": 4, "color": COKE_COLORS['executive_green']},
            {"name": "Market<br>Analytics<br>Agent", "x": 0.5, "y": 1, "color": COKE_COLORS['coke_gold']},
            {"name": "Forecasting<br>Agent", "x": 3.5, "y": 1, "color": COKE_COLORS['executive_purple']},
            {"name": "Churn<br>Prevention<br>Agent", "x": 1, "y": 3.5, "color": COKE_COLORS['warning_orange']},
            {"name": "Opportunity<br>Scoring<br>Agent", "x": 3, "y": 3.5, "color": COKE_COLORS['executive_blue']},
        ]
        
        for agent in agents:
            fig.add_trace(go.Scatter(
                x=[agent["x"]], y=[agent["y"]],
                mode='markers+text',
                marker=dict(size=70, color=agent["color"], line=dict(width=2, color='white')),
                text=agent["name"],
                textposition="middle center",
                textfont=dict(color='white', size=10, family="Arial Black"),
                name="AI Agents",
                showlegend=False
            ))
            
            # Add connection to orchestrator
            fig.add_trace(go.Scatter(
                x=[agent["x"], 2], y=[agent["y"], 2.5],
                mode='lines',
                line=dict(color='rgba(255,255,255,0.4)', width=2, dash='dash'),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Add GPT-4o models
        models = [
            {"name": "GPT-4o<br>Reasoning", "x": 1, "y": 1.5, "color": COKE_COLORS['dark_gray']},
            {"name": "GPT-4o<br>Analysis", "x": 3, "y": 1.5, "color": COKE_COLORS['dark_gray']},
        ]
        
        for model in models:
            fig.add_trace(go.Scatter(
                x=[model["x"]], y=[model["y"]],
                mode='markers+text',
                marker=dict(size=50, color=model["color"], line=dict(width=2, color='white')),
                text=model["name"],
                textposition="middle center",
                textfont=dict(color='white', size=9, family="Arial"),
                name="AI Models",
                showlegend=False
            ))
        
        fig.update_layout(
            title={
                'text': "🤖 AI Agent Ecosystem - Coca-Cola Sales Intelligence",
                'x': 0.5,
                'font': {'size': 20, 'color': 'white', 'family': 'Arial Black'}
            },
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 4]),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 4.5]),
            plot_bgcolor=COKE_COLORS['coke_black'],
            paper_bgcolor=COKE_COLORS['coke_black'],
            font=dict(color='white'),
            height=600,
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        return fig
    
    @staticmethod
    def create_data_integration_plotly():
        """Create data integration flow diagram using Plotly"""
        fig = go.Figure()
        
        # Data Sources (Left)
        sources = [
            {"name": "SAP ERP", "x": 0.5, "y": 4, "color": COKE_COLORS['executive_blue']},
            {"name": "Salesforce CRM", "x": 0.5, "y": 3.5, "color": COKE_COLORS['executive_green']},
            {"name": "Freestyle Machines", "x": 0.5, "y": 3, "color": COKE_COLORS['primary_red']},
            {"name": "Market Data APIs", "x": 0.5, "y": 2.5, "color": COKE_COLORS['coke_gold']},
            {"name": "Communication Logs", "x": 0.5, "y": 2, "color": COKE_COLORS['executive_purple']},
        ]
        
        # Integration Layer (Center)
        integration = [
            {"name": "Data<br>Ingestion<br>Pipeline", "x": 2, "y": 3.5, "color": COKE_COLORS['dark_gray']},
            {"name": "Real-time<br>ETL<br>Processor", "x": 2, "y": 2.5, "color": COKE_COLORS['dark_gray']},
        ]
        
        # AI Processing (Right)
        ai_processing = [
            {"name": "Sentiment<br>Analysis", "x": 3.5, "y": 4, "color": COKE_COLORS['warning_orange']},
            {"name": "Churn<br>Prediction", "x": 3.5, "y": 3.5, "color": COKE_COLORS['primary_red']},
            {"name": "Opportunity<br>Scoring", "x": 3.5, "y": 3, "color": COKE_COLORS['executive_green']},
            {"name": "Forecasting<br>Models", "x": 3.5, "y": 2.5, "color": COKE_COLORS['executive_blue']},
            {"name": "Market<br>Intelligence", "x": 3.5, "y": 2, "color": COKE_COLORS['coke_gold']},
        ]
        
        # Add all components
        all_components = sources + integration + ai_processing
        for comp in all_components:
            size = 80 if "Pipeline" in comp["name"] or "ETL" in comp["name"] else 60
            fig.add_trace(go.Scatter(
                x=[comp["x"]], y=[comp["y"]],
                mode='markers+text',
                marker=dict(size=size, color=comp["color"], line=dict(width=2, color='white')),
                text=comp["name"],
                textposition="middle center",
                textfont=dict(color='white', size=9, family="Arial Black"),
                showlegend=False
            ))
        
        # Add data flow arrows
        flows = [
            # Sources to Integration
            ([0.5, 2], [4, 3.5]), ([0.5, 2], [3.5, 3.5]), ([0.5, 2], [3, 3.5]), 
            ([0.5, 2], [2.5, 3.5]), ([0.5, 2], [2, 3.5]),
            ([0.5, 2], [4, 2.5]), ([0.5, 2], [3.5, 2.5]), ([0.5, 2], [3, 2.5]), 
            ([0.5, 2], [2.5, 2.5]), ([0.5, 2], [2, 2.5]),
            # Integration to AI Processing
            ([2, 3.5], [3.5, 4]), ([2, 3.5], [3.5, 3.5]), ([2, 3.5], [3.5, 3]), 
            ([2, 2.5], [3.5, 2.5]), ([2, 2.5], [3.5, 2]),
        ]
        
        for flow in flows:
            fig.add_trace(go.Scatter(
                x=flow[0], y=flow[1],
                mode='lines',
                line=dict(color='rgba(255,255,255,0.3)', width=1.5),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Add section labels
        fig.add_annotation(x=0.5, y=4.5, text="📊 Data Sources", 
                          showarrow=False, font=dict(size=14, color='white', family='Arial Black'))
        fig.add_annotation(x=2, y=4.5, text="⚙️ Integration Layer", 
                          showarrow=False, font=dict(size=14, color='white', family='Arial Black'))
        fig.add_annotation(x=3.5, y=4.5, text="🤖 AI Processing", 
                          showarrow=False, font=dict(size=14, color='white', family='Arial Black'))
        
        fig.update_layout(
            title={
                'text': "📈 Data Integration & AI Processing Pipeline",
                'x': 0.5,
                'font': {'size': 20, 'color': 'white', 'family': 'Arial Black'}
            },
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 4]),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[1.5, 5]),
            plot_bgcolor=COKE_COLORS['coke_black'],
            paper_bgcolor=COKE_COLORS['coke_black'],
            font=dict(color='white'),
            height=600,
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        return fig
    
    @staticmethod
    def render_architecture_diagram(diagram_type="high_level"):
        """Main method to render architecture diagrams with fallbacks"""
        try:
            if diagram_type == "high_level":
                fig = ArchitectureDiagramRenderer.create_high_level_architecture_plotly()
                st.plotly_chart(fig, use_container_width=True)
                return True
            elif diagram_type == "ai_agents":
                fig = ArchitectureDiagramRenderer.create_ai_agent_ecosystem_plotly()
                st.plotly_chart(fig, use_container_width=True)
                return True
            elif diagram_type == "data_integration":
                fig = ArchitectureDiagramRenderer.create_data_integration_plotly()
                st.plotly_chart(fig, use_container_width=True)
                return True
            else:
                st.error(f"Unknown diagram type: {diagram_type}")
                return False
                
        except Exception as e:
            st.error(f"Error rendering diagram: {str(e)}")
            return False
    
    @staticmethod
    def create_mermaid_fallback_html(mermaid_code, title="Architecture Diagram"):
        """Create a simple HTML fallback for Mermaid diagrams"""
        # Create a basic HTML representation with ASCII-style layout
        html_content = f"""
        <div style="background-color: #1F2937; color: white; padding: 20px; border-radius: 10px; font-family: monospace;">
            <h3 style="color: #DC143C; text-align: center; margin-bottom: 20px;">{title}</h3>
            <div style="background-color: #374151; padding: 15px; border-radius: 5px; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
{mermaid_code}
            </div>
            <p style="text-align: center; margin-top: 15px; color: #9CA3AF; font-size: 11px;">
                📝 Mermaid Diagram Code (Visual rendering in development)
            </p>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

# Quick test function
def test_diagrams():
    """Test all diagram rendering methods"""
    st.title("🔬 Diagram Renderer Test Suite")
    
    st.header("1. High-Level Architecture")
    ArchitectureDiagramRenderer.render_architecture_diagram("high_level")
    
    st.header("2. AI Agent Ecosystem")
    ArchitectureDiagramRenderer.render_architecture_diagram("ai_agents")
    
    st.header("3. Data Integration")
    ArchitectureDiagramRenderer.render_architecture_diagram("data_integration")

if __name__ == "__main__":
    test_diagrams()
