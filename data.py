import pandas as pd
import csv
import plotly.figure_factory as ff
#read_csv converts the data into data frame
df = pd.read_csv("data.csv")


p = df["Avg Rating"].to_list()  
g = ff.create_distplot([p],["Avg Rating"],show_hist = False) 
g.show()