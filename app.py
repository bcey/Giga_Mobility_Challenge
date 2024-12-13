import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load vulnerable_areas_reset from CSV
vulnerable_areas_reset = pd.read_csv('vulnerable_areas_reset.csv')

# Reset the index and use it as a column
vulnerable_areas_reset.reset_index(inplace=True)

# Initialize Dash app
app = dash.Dash(__name__)

# Create a Plotly bar plot
fig = px.bar(vulnerable_areas_reset, 
             x='index',  # Use the reset index column
             y='Absolute Change', 
             title='Vulnerable Areas - Mobility Change',
             labels={'index': 'Area ID', 'Absolute Change': 'Absolute Change in Mobility'},
             color_discrete_sequence=['red'])

# Define layout for the app
app.layout = html.Div([
    html.H1("Vulnerable Areas - Mobility Change Dashboard"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
