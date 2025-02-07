import plotly.graph_objects as go
import plotly.io as pio

# Define the custom template
pio.templates["unhcr_style"] = go.layout.Template(
    layout=dict(
        # General layout settings
        paper_bgcolor="#FFFFFF",  # Background color of the entire chart
        plot_bgcolor='#FFFFFF',   # Background color of the plotting area
        font=dict(
            family="Lato, Sans-serif",  # Default font family
            color="#222222",            # Default font color
            size=12,                    # Default font size
        ),
        title=dict(
            font=dict(
                family="Lato Bold, Sans-serif",  # Title font family
                size=20,                         # Title font size
                color="#333333",                 # Title font color
            ),
            xanchor="left",                      # Title horizontal alignment
            xref='paper',                        # Title reference to the paper
            yref='paper',                        # Title reference to the paper
            x=0,                                 # Title x position
        ),
        uniformtext_minsize=12,                  # Minimum size for uniform text
        uniformtext_mode='hide',                 # Hide text if it doesn't fit
        colorway=['#0072BC', '#8EBEFF', '#18375F', "#666666", '#E1CC0D', '#EF4A60', '#00A876', '#FF6F61'],  # Color palette
        showlegend=True,                         # Show legend
        legend=dict(
            itemclick="toggleothers",            # Toggle other items when one is clicked
            bgcolor="rgba(0,0,0,0)",             # Legend background color (transparent)
            itemdoubleclick="toggle",            # Toggle item on double click
            itemsizing="constant",               # Keep legend item size constant
            title_text="",                       # Legend title (empty)
            orientation="h",                     # Horizontal legend orientation
            xanchor="left",                      # Legend horizontal alignment
            x=0,                                 # Legend x position
            yanchor="bottom",                    # Legend vertical alignment
            y=1.02,                              # Legend y position (slightly above the plot)
        ),
        xaxis=dict(
            gridcolor='#CCCCCC',                 # Grid line color
            gridwidth=0.5,                       # Grid line width
            ticks="",                            # Hide ticks
            tickcolor='#CCCCCC',                 # Tick color
            zerolinecolor='#333333',             # Zero line color
            zerolinewidth=1,                     # Zero line width
            ticklabelstep=1,                     # Step between tick labels               
            showticklabels=True,                 # Show tick labels
            side="bottom",                       # Position of the axis
            title=dict(
                text="",                         # Axis title (empty)
                standoff=12,                     # Distance between title and axis
                font=dict(size=14, color="#666666"),  # Title font settings
            ),
        ),
        yaxis=dict(
            automargin=True,                     # Automatically adjust margins
            gridcolor='#CCCCCC',                 # Grid line color
            gridwidth=0.5,                       # Grid line width
            ticks='outside',                     # Position of ticks
            ticklen=3,                          # Length of ticks
            tickcolor='#FFFFFF',                 # Tick color
            tickmode='array',                    # Tick mode
            zerolinecolor='#333333',             # Zero line color
            zerolinewidth=1,                     # Zero line width
            title=dict(
                text='',                         # Axis title (empty)
                standoff=12,                     # Distance between title and axis
                font=dict(size=12, color="#666666"),  # Title font settings
            ),
        ),
        margin=dict(l=40, r=0, t=100, b=60),     # Chart margins
        modebar_remove=["autoScale", "lasso2d", "select"],  # Remove unnecessary modebar buttons
        modebar_activecolor="#F39C12",           # Active color for modebar buttons
        hoverlabel=dict(
            bgcolor="#444444",
            font_size=14,
            font_family="Lato, Sans-serif",
            font_color="#FFFFFF",
            bordercolor="rgba(255,255,255,0.3)",  # White transparent border
            namelength=-1,
            align="left",
        ),
    
        hovermode="closest",                   # Unified hover mode for multiple traces
        annotations=[],                          # List of annotations (empty by default)
        shapes=[],                               # List of shapes (empty by default)
    ),
    data=dict(
        bar=[go.Bar(
            textangle=0,                         # Text angle for bar labels
            texttemplate='%{y:,.0f}', 
            hovertemplate="%{x}<br>%{y:,.0f}<extra></extra>", 
            text=None,
            textposition="none",
        )],
        scatter=[go.Scatter(
            mode='lines+markers',                # Default mode for scatter plots
            marker=dict(size=8),                 # Default marker size
            hovertemplate="%{x}<br>%{y:,.0f}<extra></extra>",
            line=dict(width=2),                  # Default line width
        )],
    ),
)

# Set the template as default
pio.templates.default = "unhcr_style"