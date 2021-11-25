import numpy as np
import plotly.express as px
import csv

with open("TvVSSpendingHours.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Size of TV", y="\tAverage_time_spent_watching_TV_in_a_week")
    fig.show()

def getDataResources(data_path):
    size_of_tv = []
    average_time_spent_watching_tv_in_a_week = []
    with open(data_path) as f:
        df1 = csv.DictReader(f)
        for row in df1:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent_watching_tv_in_a_week.append(float(row["\tAverage_time_spent_watching_TV_in_a_week"]))
    
    return {"x":size_of_tv, "y":average_time_spent_watching_tv_in_a_week}


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of TV vs Average Time is :- \n--->", correlation[0,1])

def setup():
    data_path = "TvVSSpendingHours.csv"
    datasource = getDataResources(data_path)
    findCorrelation(datasource)

setup()


