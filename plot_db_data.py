import mysql.connector
from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd

def createConnection(user_name, database_name, user_password, host, port):
    cnx = mysql.connector.connect(user=user_name, database=database_name, password=user_password, host=host, port=port)
    cursor = cnx.cursor()
    return (cnx, cursor)

def select_data():
    try:
        # Create a connection to the database - # Dont forget to pass in the correct parameters
        cnx, cursor = createConnection('root', 'iot_situacion_problema', 'R_carlos2002mb.', 'localhost', '3306')

        # Query the database
        query = ("SELECT ID, humidity, temperatura FROM dht_data")

        # Execute the query
        cursor.execute(query)

        # Get the data
        data = cursor.fetchall()
        # Return the data
        return data
    
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if ('cnx' in locals() or 'cnx' in globals()) and ('cursor' in locals() or 'cursor' in globals()):
            cnx.close()
            cursor.close()

def create_page(data):

    # Create a plotly line graph
    # Data must be in a pandas dataframe, so we convert it to a dataframe first
    # The columns parameter is used to name the columns of the dataframe
    data = pd.DataFrame(data, columns=["id", "humidity", "temperatura"])

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
                html.H1("Temperatura and Humidity", style={'text-align': 'center','font-family': 'Times New Roman','font-size': '28px','margin-bottom': '20px'}),
                html.P("This graph shows the temperature and humidity of the room over time. The data is from DHT11 sensor. The data is stored in a MySQL database. The data is retrieved from the database using a Python script. The data is then plotted using Plotly Express. The graph is then displayed using Dash"),
                dcc.Graph(figure=px.line(data, x='id', y=['humidity', 'temperatura'], title="Gráfica de Variación en Temperatura y Humedad")),

            ])
    ])

    app.run_server(debug=True)

    mess = str("Well done")

    return mess

createConnection('root', 'iot_situacion_problema', 'R_carlos2002mb.', 'localhost', '3306')
data = select_data()
print(create_page(data))
        