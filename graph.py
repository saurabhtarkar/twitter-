import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
    Bar(
        x=['Positive', 'Negative', 'Irrelevant','Neutral'],
        y=[20, 14, 23, 34]
    )
])
plot_url = py.plot(data, filename='Micromax')
