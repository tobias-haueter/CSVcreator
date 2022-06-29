# --------------------------------------------------------------------------------
# webChart.py                                                           2022-06-05
# created by tobias(at)haueter.one
# Chart plotting software for .csv files on localhost web browser.
# --------------------------------------------------------------------------------

import pandas as pd
import plotly.graph_objects as go

# read csv file and choose the delimiter. -----------------------------------------------------------------------------
df = pd.read_csv('outputCSV/plotlyJS_data.csv', delimiter=',')  # <TAB>: delimiter='\t'

# Initialize figure with subplots -------------------------------------------------------------------------------------
fig = go.Figure()

config = dict({'scrollZoom': True})

# Plot 01 -------------------------------------------------------------------------------------------------------------
fig.add_scatter(
    x=df['time1'],
    y=df['amplitude1'],
    mode='lines',
    name='value1',
    line=dict(color="#1ca400")
)

# Plot 02 -------------------------------------------------------------------------------------------------------------
fig.add_scatter(
    x=df['time1'],
    y=df['amplitude2'],
    mode='lines',
    name='value2',
    line=dict(color="#0066ff")
)

# Plot 03 -------------------------------------------------------------------------------------------------------------
fig.add_scatter(
    x=df['time1'],
    y=df['amplitude3'],
    mode='lines',
    name='value3',
    line=dict(color="#ff0000")
)

# Plot 03 -------------------------------------------------------------------------------------------------------------
fig.add_scatter(
    x=df['time1'],
    y=df['amplitude4'],
    mode='lines',
    name='value4',
    line=dict(color="orange")
)

# Site properties -----------------------------------------------------------------------------------------------------
fig.update_layout(
    title='pyCHARTs - Plotly JS [180 Day / 30s / 507600',
    xaxis_title="x0_time = 30s",
    yaxis_title="y_value",
    legend_title="Legend Title",
    showlegend=True,
    plot_bgcolor='#e3ebff'
)

fig.show(config=config)
