import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('./data.csv')
fig = ff.create_distplot([df["Mobile Brand"].tolist()], ["Mobile Brand"], show_hist = True)
fig.show()