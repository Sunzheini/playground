# Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


# Sample Data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

# 1. Create the Dash app instance
app = Dash(__name__)

# 2. Define the Layout (the UI)
app.layout = html.Div([
    html.H1("My First Fruit Dashboard"),  # A heading

    dcc.Dropdown(  # A dropdown
        id='city-dropdown',
        options=[{'label': city, 'value': city} for city in df['City'].unique()],
        value='SF'  # Default value
    ),

    dcc.Graph(  # An empty graph, waiting for data
        id='example-graph'
    )
])


# 3. Define the Callback (the Interactivity)
@app.callback(
    Output('example-graph', 'figure'),  # The output is the 'figure' property of the component with id 'example-graph'
    Input('city-dropdown', 'value')  # The input is the 'value' property of the component with id 'city-dropdown'
)
def update_graph(selected_city):
    # Filter the dataframe based on the selected city from the dropdown
    filtered_df = df[df["City"] == selected_city]

    # Create a bar chart figure using the filtered data
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City")

    return fig  # This returned object updates the output (the graph)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)