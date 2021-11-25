import plotly.express as px
import csv

with open('iceCreamVSTemperature.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Temperature", y="Ice_cream_Sales", color="Cold drink sales")
    fig.show()
    