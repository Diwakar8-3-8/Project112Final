import plotly.figure_factory as ff

fig = ff.create_distplot([df["quant_saved"].tolist()], ["wealthy"], show_hist=False)
fig.show()