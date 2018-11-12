from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid,
                          Range1d)
from bokeh.models.glyphs import VBar
from bokeh.plotting import figure
#from bokeh.charts import Bar
from bokeh.embed import components
from bokeh.models.sources import ColumnDataSource

import pandas as pd


def generate_plot(data):
    p = figure(x_axis_type="datetime", plot_width=800, plot_height=350)
    p.line(x=range(0, len(data)), y=data)
    return p
