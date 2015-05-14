import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Bar(
    x=['Positive', 'Negative', 'Irrelevant','Neutral'],
    y=[20, 14, 23,49],
    name='Yureka'
)
trace2 = Bar(
    x=['Positive', 'Negative', 'Irrelevant','Neutral'],
    y=[12, 18, 29,56],
    name='One-plus-one'
)
data = Data([trace1, trace2])
layout = Layout(
    barmode='group'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Yureka Vs. One-plus-one')
