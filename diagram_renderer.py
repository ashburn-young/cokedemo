"""
Enhanced Architecture Diagram Renderer for Coca-Cola Sales Platform
Provides multiple rendering methods with robust fallbacks - Now matching README.md structure
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from math import cos, sin, pi

# Coca-Cola brand colors
COKE_COLORS = {
    'primary_red': '#FF0000',
    'coke_black': '#000000', 
    'classic_white': '#FFFFFF',
    'executive_blue': '#0078D4',
    'executive_green': '#00BCF2',
    'coke_gold': '#FFC72C',
    'dark_red': '#CC0000',
    'light_gray': '#F5F5F5'
}

class ArchitectureDiagramRenderer:
    """Enhanced diagram renderer matching README.md architecture structure"""
    
    @staticmethod
    def create_high_level_architecture_plotly():
        """Create layered high-level architecture matching README.md structure"""
        
        fig = go.Figure()
        
        # Background
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.95)',
            paper_bgcolor='rgba(0,0,0,0.95)',
            font=dict(color='white', family="Arial"),
            title=dict(
                text="🏢 High-Level Architecture - Coca-Cola Sales AI Platform",
                font=dict(size=20, color=COKE_COLORS['primary_red'], family="Arial Black"),
                x=0.5
            ),
            showlegend=True,
            width=1000,
            height=700,
            xaxis=dict(range=[-0.5, 4.5], showgrid=False, showticklabels=False, zeroline=False),
            yaxis=dict(range=[-0.5, 4.5], showgrid=False, showticklabels=False, zeroline=False)
        )
        
        # Layer labels
        layer_labels = [
            {"text": "PRESENTATION LAYER", "x": 2, "y": 4.2, "color": COKE_COLORS['primary_red']},
            {"text": "API LAYER", "x": 1, "y": 3.2, "color": COKE_COLORS['executive_blue']},
            {"text": "AI LAYER", "x": 3.5, "y": 3.2, "color": COKE_COLORS['executive_green']},
            {"text": "DATA LAYER", "x": 2, "y": 1.2, "color": COKE_COLORS['coke_gold']},
            {"text": "DATA SOURCES", "x": 2, "y": 0.4, "color": COKE_COLORS['light_gray']},
        ]
        
        for label in layer_labels:
            fig.add_annotation(
                x=label["x"], y=label["y"],
                text=label["text"],
                showarrow=False,
                font=dict(size=12, color=label["color"], family="Arial Black")
            )
        
        # Components
        components = [
            # Presentation Layer
            {"name": "Streamlit Executive Dashboard<br>• KPI Analytics • Visualizations<br>• Interactive Charts • Risk Alerts", 
             "x": 2, "y": 4, "size": 80, "color": COKE_COLORS['primary_red'], "layer": "Presentation"},
            
            # API Layer  
            {"name": "FastAPI REST API<br>• Agent Orchestration<br>• Data Services<br>• Business Logic", 
             "x": 1, "y": 3, "size": 60, "color": COKE_COLORS['executive_blue'], "layer": "API"},
            
            # AI Layer
            {"name": "Azure OpenAI GPT-4o<br>Semantic Kernel<br>• 6 AI Agents<br>• Prompt Engineering<br>• Function Calling", 
             "x": 3.5, "y": 3, "size": 70, "color": COKE_COLORS['executive_green'], "layer": "AI"},
            
            # Data Layer - Aggregated Data
            {"name": "Account Data<br>(523)", "x": 0.5, "y": 1, "size": 40, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            {"name": "Opportunity Data<br>(247)", "x": 1.5, "y": 1, "size": 40, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            {"name": "Product Performance<br>Data", "x": 2.5, "y": 1, "size": 40, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            {"name": "Regional Data<br>(12 regions)", "x": 3.5, "y": 1, "size": 40, "color": COKE_COLORS['coke_gold'], "layer": "Data"},
            
            # Data Sources
            {"name": "CRM System", "x": 0.5, "y": 0.2, "size": 25, "color": COKE_COLORS['light_gray'], "layer": "Sources"},
            {"name": "Freestyle Telemetry", "x": 1.5, "y": 0.2, "size": 25, "color": COKE_COLORS['light_gray'], "layer": "Sources"},
            {"name": "Communication Analysis", "x": 2.5, "y": 0.2, "size": 25, "color": COKE_COLORS['light_gray'], "layer": "Sources"},
            {"name": "Competitive Intelligence", "x": 3.5, "y": 0.2, "size": 25, "color": COKE_COLORS['light_gray'], "layer": "Sources"},
        ]
        
        # Add components
        for comp in components:
            fig.add_trace(go.Scatter(
                x=[comp["x"]], y=[comp["y"]],
                mode='markers+text',
                marker=dict(size=comp["size"], color=comp["color"], 
                           line=dict(width=2, color='white'),
                           opacity=0.9),
                text=comp["name"],
                textposition="middle center",
                textfont=dict(color='white' if comp["layer"] != "Sources" else 'black', 
                             size=9, family="Arial"),
                name=comp["layer"],
                showlegend=False
            ))
        
        # Add connections showing data flow
        connections = [
            # Bidirectional between presentation and API
            {"from": (2, 4), "to": (1, 3), "color": "rgba(255,0,0,0.6)", "width": 4},
            
            # Bidirectional between API and AI
            {"from": (1, 3), "to": (3.5, 3), "color": "rgba(0,120,212,0.6)", "width": 4},
            
            # API to Data Layer
            {"from": (1, 3), "to": (0.5, 1), "color": "rgba(0,188,242,0.4)", "width": 2},
            {"from": (1, 3), "to": (1.5, 1), "color": "rgba(0,188,242,0.4)", "width": 2},
            {"from": (1, 3), "to": (2.5, 1), "color": "rgba(0,188,242,0.4)", "width": 2},
            {"from": (1, 3), "to": (3.5, 1), "color": "rgba(0,188,242,0.4)", "width": 2},
            
            # Data Sources to Data Layer
            {"from": (0.5, 0.2), "to": (0.5, 1), "color": "rgba(255,199,44,0.4)", "width": 2},
            {"from": (1.5, 0.2), "to": (1.5, 1), "color": "rgba(255,199,44,0.4)", "width": 2},
            {"from": (2.5, 0.2), "to": (2.5, 1), "color": "rgba(255,199,44,0.4)", "width": 2},
            {"from": (3.5, 0.2), "to": (3.5, 1), "color": "rgba(255,199,44,0.4)", "width": 2},
        ]
        
        for conn in connections:
            fig.add_trace(go.Scatter(
                x=[conn["from"][0], conn["to"][0]], 
                y=[conn["from"][1], conn["to"][1]],
                mode='lines',
                line=dict(color=conn["color"], width=conn["width"]),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        return fig

    @staticmethod
    def create_ai_agent_ecosystem_plotly():
        """Create hub-and-spoke AI agent ecosystem matching README.md structure"""
        
        fig = go.Figure()
        
        # Background
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.95)',
            paper_bgcolor='rgba(0,0,0,0.95)',
            font=dict(color='white', family="Arial"),
            title=dict(
                text="🤖 AI Agent Ecosystem - Semantic Kernel Orchestration",
                font=dict(size=20, color=COKE_COLORS['executive_green'], family="Arial Black"),
                x=0.5
            ),
            showlegend=False,
            width=1000,
            height=700,
            xaxis=dict(range=[-3, 3], showgrid=False, showticklabels=False, zeroline=False),
            yaxis=dict(range=[-3, 3], showgrid=False, showticklabels=False, zeroline=False)
        )
        
        # Central Semantic Kernel
        center = {"x": 0, "y": 0, "size": 100, "color": COKE_COLORS['executive_green']}
        fig.add_trace(go.Scatter(
            x=[center["x"]], y=[center["y"]],
            mode='markers+text',
            marker=dict(size=center["size"], color=center["color"], 
                       line=dict(width=4, color='white')),
            text="Semantic Kernel<br>Orchestrator<br><br>• Agent Coordination<br>• Context Management<br>• Function Calling<br>• Memory",
            textposition="middle center",
            textfont=dict(color='white', size=11, family="Arial Black"),
            showlegend=False
        ))
        
        # AI Agents positioned in a circle around the center
        agents = [
            {"name": "Customer Risk<br>Assessment Agent<br><br>• Churn Risk<br>• Health Score<br>• Early Warning", 
             "angle": 0, "color": COKE_COLORS['primary_red']},
            {"name": "Opportunity<br>Intelligence Agent<br><br>• Revenue Opportunities<br>• Cross-sell<br>• Freestyle", 
             "angle": pi/3, "color": COKE_COLORS['executive_blue']},
            {"name": "Competitive Threat<br>Monitoring Agent<br><br>• Market Share<br>• Pricing<br>• Competitive Analysis", 
             "angle": 2*pi/3, "color": COKE_COLORS['coke_gold']},
            {"name": "Product Portfolio<br>Optimization Agent<br><br>• Mix Analysis<br>• Performance<br>• Forecasting", 
             "angle": pi, "color": COKE_COLORS['dark_red']},
            {"name": "Communication<br>Sentiment Intelligence<br><br>• NLP Analysis<br>• Relationship<br>• Escalation", 
             "angle": 4*pi/3, "color": COKE_COLORS['executive_green']},
            {"name": "Regional Performance<br>Intelligence Agent<br><br>• Geographic Analysis<br>• Territory<br>• Optimization", 
             "angle": 5*pi/3, "color": COKE_COLORS['coke_black']},
        ]
        
        radius = 2.2
        for agent in agents:
            x = radius * cos(agent["angle"])
            y = radius * sin(agent["angle"])
            
            # Add agent node
            fig.add_trace(go.Scatter(
                x=[x], y=[y],
                mode='markers+text',
                marker=dict(size=70, color=agent["color"], 
                           line=dict(width=3, color='white'),
                           opacity=0.9),
                text=agent["name"],
                textposition="middle center",
                textfont=dict(color='white', size=9, family="Arial"),
                showlegend=False
            ))
            
            # Add connection to center
            fig.add_trace(go.Scatter(
                x=[0, x], y=[0, y],
                mode='lines',
                line=dict(color='rgba(255,255,255,0.4)', width=3),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Add Azure OpenAI and Data Integration connections
        additional_nodes = [
            {"name": "Azure OpenAI<br>GPT-4o<br><br>• Advanced Reasoning<br>• Context Understanding", 
             "x": 0, "y": -2.8, "color": COKE_COLORS['executive_blue']},
            {"name": "Data Integration<br>Services<br><br>• Account Data<br>• Opportunity<br>• Performance<br>• AI Insights", 
             "x": 0, "y": 2.8, "color": COKE_COLORS['coke_gold']},
        ]
        
        for node in additional_nodes:
            fig.add_trace(go.Scatter(
                x=[node["x"]], y=[node["y"]],
                mode='markers+text',
                marker=dict(size=60, color=node["color"], 
                           line=dict(width=3, color='white')),
                text=node["name"],
                textposition="middle center",
                textfont=dict(color='white', size=9, family="Arial"),
                showlegend=False
            ))
            
            # Connect to center
            fig.add_trace(go.Scatter(
                x=[0, node["x"]], y=[0, node["y"]],
                mode='lines',
                line=dict(color='rgba(255,255,255,0.5)', width=4),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        return fig

    @staticmethod
    def create_data_integration_plotly():
        """Create data integration flow diagram matching README.md structure"""
        
        fig = go.Figure()
        
        # Background
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.95)',
            paper_bgcolor='rgba(0,0,0,0.95)',
            font=dict(color='white', family="Arial"),
            title=dict(
                text="🔄 Data Integration & Intelligence Flow",
                font=dict(size=20, color=COKE_COLORS['coke_gold'], family="Arial Black"),
                x=0.5
            ),
            showlegend=True,
            width=1000,
            height=700,
            xaxis=dict(range=[-0.5, 6.5], showgrid=False, showticklabels=False, zeroline=False),
            yaxis=dict(range=[-0.5, 4.5], showgrid=False, showticklabels=False, zeroline=False)
        )
        
        # Data Sources (Left side)
        data_sources = [
            {"name": "CRM System (SAP)<br>• 523 Accounts<br>• Contact Hierarchy<br>• Real-time Updates", 
             "x": 0.5, "y": 3.5, "color": COKE_COLORS['primary_red'], "layer": "External Systems"},
            {"name": "Freestyle Machines<br>• 1,200+ Machines<br>• IoT Telemetry<br>• 5-min Aggregation", 
             "x": 0.5, "y": 2.5, "color": COKE_COLORS['executive_blue'], "layer": "External Systems"},
            {"name": "Sales Performance DB<br>• 3+ Years History<br>• Daily ETL<br>• Monthly Reconciliation", 
             "x": 0.5, "y": 1.5, "color": COKE_COLORS['executive_green'], "layer": "External Systems"},
            {"name": "Communication Platform<br>• 10K+ Monthly Comms<br>• Real-time NLP<br>• Sentiment Scoring", 
             "x": 0.5, "y": 0.5, "color": COKE_COLORS['coke_gold'], "layer": "External Systems"},
        ]
        
        # Integration Layer (Center)
        integration_layer = [
            {"name": "Data Integration Hub<br>• API Gateway<br>• Real-time Processing<br>• Quality Validation", 
             "x": 3, "y": 2, "color": COKE_COLORS['coke_black'], "layer": "Integration"},
        ]
        
        # Analytics & AI Layer (Right side)
        analytics_layer = [
            {"name": "AI Agent Analytics<br>• Sentiment Analysis<br>• Churn Prediction<br>• Opportunity Scoring", 
             "x": 5.5, "y": 3, "color": COKE_COLORS['dark_red'], "layer": "AI Analytics"},
            {"name": "Executive Dashboard<br>• Real-time KPIs<br>• Interactive Visualizations<br>• Alert System", 
             "x": 5.5, "y": 1, "color": COKE_COLORS['primary_red'], "layer": "Presentation"},
        ]
        
        # Add all components
        all_components = data_sources + integration_layer + analytics_layer
        
        for comp in all_components:
            fig.add_trace(go.Scatter(
                x=[comp["x"]], y=[comp["y"]],
                mode='markers+text',
                marker=dict(size=70, color=comp["color"], 
                           line=dict(width=3, color='white'),
                           opacity=0.9),
                text=comp["name"],
                textposition="middle center",
                textfont=dict(color='white', size=9, family="Arial"),
                name=comp["layer"],
                showlegend=True if comp == all_components[0] or 
                         comp["layer"] not in [c["layer"] for c in all_components[:all_components.index(comp)]] else False
            ))
        
        # Add data flow connections
        connections = [
            # Data sources to integration hub
            {"from": (0.5, 3.5), "to": (3, 2), "color": "rgba(255,0,0,0.6)", "width": 3},
            {"from": (0.5, 2.5), "to": (3, 2), "color": "rgba(0,120,212,0.6)", "width": 3},
            {"from": (0.5, 1.5), "to": (3, 2), "color": "rgba(0,188,242,0.6)", "width": 3},
            {"from": (0.5, 0.5), "to": (3, 2), "color": "rgba(255,199,44,0.6)", "width": 3},
            
            # Integration hub to analytics
            {"from": (3, 2), "to": (5.5, 3), "color": "rgba(204,0,0,0.6)", "width": 4},
            {"from": (3, 2), "to": (5.5, 1), "color": "rgba(255,0,0,0.6)", "width": 4},
        ]
        
        for conn in connections:
            fig.add_trace(go.Scatter(
                x=[conn["from"][0], conn["to"][0]], 
                y=[conn["from"][1], conn["to"][1]],
                mode='lines',
                line=dict(color=conn["color"], width=conn["width"]),
                showlegend=False,
                hoverinfo='skip'
            ))
            
            # Add arrow markers for flow direction
            mid_x = (conn["from"][0] + conn["to"][0]) / 2
            mid_y = (conn["from"][1] + conn["to"][1]) / 2
            fig.add_annotation(
                x=mid_x, y=mid_y,
                text="▶",
                showarrow=False,
                font=dict(size=16, color=conn["color"])
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

def get_diagram(diagram_type):
    """Get the specified diagram for backwards compatibility"""
    diagrams = {
        "high_level": ArchitectureDiagramRenderer.create_high_level_architecture_plotly,
        "ai_agents": ArchitectureDiagramRenderer.create_ai_agent_ecosystem_plotly, 
        "data_integration": ArchitectureDiagramRenderer.create_data_integration_plotly
    }
    
    if diagram_type in diagrams:
        return diagrams[diagram_type]()
    else:
        return None
