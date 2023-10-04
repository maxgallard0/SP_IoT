# This file contains some basic examples of how to use plotly express to create graphs.

# Basic imports
import plotly.express as px
import pandas as pd

# Create some data
data = [
    (1, 3, 5),
    (2, 4, 6),
    (3, 1, 8),
    (4, 2, 3),
    (5, 7, 1) 
]

# Create a plotly line graph
# Data must be in a pandas dataframe, so we convert it to a dataframe first
# The columns parameter is used to name the columns of the dataframe
data = pd.DataFrame(data, columns=["id", "height", "width"])

# Plotly is a Python graphing library that makes it easy to create interactive plots.
# Plotly Express is a high-level interface for Plotly. It is easy to use and allows you to create interactive plots with a single line of code.

# Create the plot using plotly express and the dataframe as the data source
fig = px.line(data_frame=data, x="id", y=["height", "width"], title="Line Graph")

# Update the x and y axis titles
fig.update_layout(xaxis_title='Id', yaxis_title='Height and Width')

# Show the plot
fig.show()

# You could also create a bar graph using data from lists instead of a dataframe
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2], title="Bar Graph")

fig.show()

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], title="Scatter Plot")

fig.show()