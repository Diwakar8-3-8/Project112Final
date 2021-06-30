import plotly.express as pe
import pandas as pd
import statistics

df = pd.read_csv("data.csv") 
fig = pe.scatter(df, y="quant_saved", color="wealthy") 
fig.show()