import numpy as np
import plotly.express as px
import csv

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Temperature", y="Ice_cream_Sales", color="Cold drink sales")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    coldDrinkSales = []
    with open(data_path) as f:
        df1 = csv.DictReader(f)
        for row in df1:
            ice_cream_sales.append(float(row["Temperature"]))
            coldDrinkSales.append(float(row["Ice_cream_Sales"]))
        
    return {"x": ice_cream_sales, "y":coldDrinkSales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream is :- \n--->", correlation[0,1])

def setup():
    data_path = "iceCreamVSTemperature.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
