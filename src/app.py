from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load and sort the data
df = pd.read_csv('C:\\dev\\quantium-starter-repo\\data\\task2.csv')
df = df.sort_values(by='date')

# The layout with our new radio buttons and some fresh CSS
app.layout = html.Div(
    style={'backgroundColor': '#2b2b2b', 'fontFamily': 'Arial, sans-serif', 'padding': '40px', 'minHeight': '100vh'},
    children=[
        html.H1(
            "Pink Morsel Sales Explorer", 
            style={'textAlign': 'center', 'color': '#FF69B4', 'marginBottom': '30px'}
        ),
        
        html.Div(
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All Regions', 'value': 'all'}
                ],
                value='all',
                inline=True,
                style={'color': '#ffffff', 'fontSize': '18px', 'display': 'flex', 'justifyContent': 'center', 'gap': '20px'}
            ),
            style={'marginBottom': '30px'}
        ),

        dcc.Graph(id='sales-graph')
    ]
)

# Callback to update the graph when a radio button is clicked
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter the dataframe based on the selection
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    # Build the chart
    fig = px.line(filtered_df, x="date", y="sales")
    
    # Styling the chart to match the dark theme
    fig.update_traces(line_color='#FF69B4', line_width=3) 
    fig.update_layout(
        plot_bgcolor='#333333',
        paper_bgcolor='#2b2b2b',
        font_color='#ffffff',
        font_family="Arial, sans-serif",
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)