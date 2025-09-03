import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Architecture Diagram Test", layout="wide")

# Coca-Cola Color Palette
COKE_COLORS = {
    'primary_red': '#DC143C',
    'dark_red': '#B91C1C',
    'light_red': '#EF4444',
    'coke_black': '#1F2937',
    'coke_white': '#FFFFFF',
    'coke_gold': '#F59E0B',
    'executive_green': '#10B981',
    'executive_blue': '#3B82F6',
    'executive_amber': '#F59E0B',
    'executive_purple': '#8B5CF6',
    'warning_orange': '#F97316',
    'critical_red': '#DC2626',
    'success_green': '#059669',
    'neutral_gray': '#6B7280',
    'dark_gray': '#374151',
    'light_gray': '#F9FAFB'
}

def create_test_architecture_diagram():
    """Create a test architecture diagram using Plotly"""
    # Define nodes
    nodes = {
        "Streamlit Dashboard": {"x": 0.5, "y": 0.9, "color": COKE_COLORS['primary_red']},
        "FastAPI Backend": {"x": 0.5, "y": 0.7, "color": COKE_COLORS['executive_blue']},
        "Azure OpenAI": {"x": 0.8, "y": 0.5, "color": COKE_COLORS['executive_green']},
        "Account Data": {"x": 0.2, "y": 0.5, "color": COKE_COLORS['coke_gold']},
        "AI Agents": {"x": 0.9, "y": 0.3, "color": COKE_COLORS['executive_purple']}
    }
    
    # Define connections
    edges = [
        ("Streamlit Dashboard", "FastAPI Backend"),
        ("FastAPI Backend", "Azure OpenAI"),
        ("FastAPI Backend", "Account Data"),
        ("Azure OpenAI", "AI Agents"),
    ]
    
    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in edges:
        x0, y0 = nodes[edge[0]]["x"], nodes[edge[0]]["y"]
        x1, y1 = nodes[edge[1]]["x"], nodes[edge[1]]["y"]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(x=edge_x, y=edge_y,
                           line=dict(width=3, color='#ffffff'),
                           hoverinfo='none',
                           mode='lines')
    
    # Create node traces
    node_x = [nodes[node]["x"] for node in nodes]
    node_y = [nodes[node]["y"] for node in nodes]
    node_colors = [nodes[node]["color"] for node in nodes]
    node_text = list(nodes.keys())
    
    node_trace = go.Scatter(x=node_x, y=node_y,
                           mode='markers+text',
                           hoverinfo='text',
                           text=node_text,
                           textposition="middle center",
                           textfont=dict(color="white", size=14, family="Arial Black"),
                           marker=dict(size=80,
                                     color=node_colors,
                                     line=dict(width=3, color='white')))
    
    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                        title=dict(text='🏗️ Coca-Cola Architecture Diagram Test',
                                  font=dict(size=24, color='white')),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=60),
                        annotations=[ dict(
                            text="✅ Interactive Architecture Diagram - Hover over components",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.5, y=-0.1,
                            xanchor='center', yanchor='bottom',
                            font=dict(color='white', size=14)
                        )],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        plot_bgcolor='#1F2937',
                        paper_bgcolor='#1F2937',
                        height=500
                    ))
    
    return fig

st.markdown("# 🏗️ Architecture Diagram Test")
st.markdown("Testing Plotly-based architecture diagrams for Coca-Cola platform")

# Test basic Plotly functionality
st.markdown("## Test 1: Basic Plotly Chart")
test_fig = go.Figure()
test_fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='lines+markers', name='Test Line'))
test_fig.update_layout(title="Basic Plotly Test", plot_bgcolor='#1F2937', paper_bgcolor='#1F2937')
st.plotly_chart(test_fig, use_container_width=True)

# Test architecture diagram
st.markdown("## Test 2: Architecture Diagram")
try:
    arch_fig = create_test_architecture_diagram()
    st.plotly_chart(arch_fig, use_container_width=True)
    st.success("✅ Architecture diagram rendered successfully!")
except Exception as e:
    st.error(f"❌ Error rendering architecture diagram: {e}")
    import traceback
    st.code(traceback.format_exc())

# Test Mermaid fallback
st.markdown("## Test 3: Mermaid Code Display")
mermaid_code = """
graph TD
    A[Streamlit] --> B[FastAPI]
    B --> C[Azure OpenAI]
    C --> D[AI Agents]
"""
st.code(mermaid_code, language="mermaid")
