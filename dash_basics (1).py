# Basic Dash application that displays a heading, a table, and a plotly graph.

# Basic imports
from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd

# Create some data
data = [
    [1, 3, 5],
    [2, 4, 6],
    [3, 1, 8],
    [4, 2, 3],
    [5, 7, 1] 
]

# Create a plotly line graph
# Data must be in a pandas dataframe, so we convert it to a dataframe first
# The columns parameter is used to name the columns of the dataframe
data = pd.DataFrame(data, columns=["id", "height", "width"])

# Dash is a framework for building web applications. It is built on top of Flask, Plotly.js, and React.js.

# Create a Dash application instance
app = Dash(__name__)

# Dash apps are composed of HTML components. Some basic knowledge of HTML is ideal, but not necesarilly required. 
# The app layout represents the app components that will be displayed in the web browser, normally contained within a html.Div.

# Define the layout of the web application
app.layout = html.Div([
    # A div is a container for other HTML elements. These are usually stored in the children property.
    html.Div(
        # The children property is used to define the elements that will be displayed inside the div.
        children=[
            # The html.H1 component is used to display a heading. The style property is used to give the heading styling properties.
            # In this case, the style is used to center the heading.
            html.H1("Dash Basics", style={'text-align': 'center'}),

            # The dataTable component is used to display data in a table format.
            dash_table.DataTable(data = data.to_dict('records')),

            # The dcc.Graph component is used to display a plotly graph.
            dcc.Graph(figure=px.line(data, x='id', y=['height', 'width'], title="Line Graph with data from a dataframe")),
            dcc.Graph(figure=px.bar(x=["a", "b", "c"], y=[1, 3, 2], title="Bar Graph")),
            dcc.Graph(figure=px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], title="Scatter Plot"))
        ])
])

app.run_server(debug=True)
