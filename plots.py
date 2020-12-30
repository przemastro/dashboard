from plotly.subplots import make_subplots
import plotly as plotly
import pandas as pd
from plotly.figure_factory import create_gantt
import plotly.graph_objects as go
import numpy as np


def linePlot():

    labels = ['Cycling', 'Running', 'Walking', 'Boxing', 'Squash', 'Kayaking', 'Weight']
    colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)',
              'rgb(78,23,250)', 'rgb(120,79,249)', 'rgb(174,150,250)']

    mode_size = [8, 8, 8, 8, 8, 8, 8]
    line_size = [2, 2, 2, 2, 2, 2, 2]

    x_data = np.vstack((np.arange(1, 12),)*7)

    y_data = np.array([
    [13, 21,   44.9, 62.4, 63.6, 63.3,  62.6,  63,   65.9, 64,    70,   65],
    [24, 10.4, 12.4, 0,    0,    0,     0,     0,    0,    0,     0,    0],
    [4,  0,    19.9, 0,    0,    0,     0,     0,    0,    15.7,  0,    0],
    [32, 24.9, 0,    3.3,  0,    0,     0,     0,    2.3,  0,     0,    0],
    [9, 12.8, 3.8,  0,    0,    0,     0,     0,    0,    6.2,   0,    0],
    [0,  0,    0,    0,    0,    0,     0,     5.9,  0,    0,     0,    0],
    [18, 30.9, 21.4, 34.4, 36.4, 36.7,  37.4,  31.1, 31.7, 14.1,  30,   35],
    ])

    fig = go.Figure()

    for i in range(0, 7):
       fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
                             name=labels[i],
                             line=dict(color=colors[i], width=line_size[i]),
                             connectgaps=True,
                             ))

    # endpoints
    fig.add_trace(go.Scatter(
        x=[x_data[i][0], x_data[i][-1]],
        y=[y_data[i][0], y_data[i][-1]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

    fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
    )

    annotations = []

    # Adding labels
    for y_trace, label, color in zip(y_data, labels, colors):
       # labeling the left_side of the plot
       annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                            xanchor='right', yanchor='middle',
                            text=label + ' {}%'.format(y_trace[0]),
                            font=dict(family='Arial',
                                      size=16),
                            showarrow=False))
       # labeling the right_side of the plot
       annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                            xanchor='left', yanchor='middle',
                            text='{}%'.format(y_trace[11]),
                            font=dict(family='Arial',
                                      size=16),
                            showarrow=False))
       # Source
       annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                        xanchor='center', yanchor='top',
                        text='',
                        font=dict(family='Arial',
                                  size=12,
                                  color='rgb(150,150,150)'),
                        showarrow=False))

       fig.update_layout(annotations=annotations, margin=dict(t=15))

       plotly.offline.plot(fig, filename ='static/linePlot.html', auto_open=False)
       plotly.offline.plot(fig, filename ='templates/linePlot.html', auto_open=False)

def testCenterComponentsPieChart():

    df = pd.DataFrame([['Automated Tests Framework', '2020-03-03', '2020-03-19', 95],
                       ['Dashboard', '2020-03-10', '2020-04-15', 80],
                       ['CI/CD', '2020-05-10', '2020-06-01', 90],
                       ['Android App', '2020-11-14', '2020-11-28', 50],
                       ['Farm of Devices', '2020-04-01', '2020-04-24', 75]],
                      columns=['Task', 'Start', 'Finish', 'Complete'])

    # Create a figure with Plotly colorscale

    fig = create_gantt(df, colors='Blues', index_col='Complete',
                   show_colorbar=True, bar_width=0.3,
                   showgrid_x=False, showgrid_y=False, height=450, width=600, title=None)
    fig.update_layout(margin=dict(t=15))
    fig.update_yaxes(autorange="reversed")

    try:
        plotly.offline.plot(fig, filename ='static/testCenterComponentsPieChart.html', auto_open=False)
        plotly.offline.plot(fig, filename ='templates/testCenterComponentsPieChart.html', auto_open=False)
    except (RuntimeError, TypeError, NameError):
        print("We experience some technical problems")

def diggingPieChart():

    labels = ["Done", "To Do"]

    colorsList = []
    for x in labels:
        for y in colorsdict:
            colorsList.append(colorsdict[y])
    colors = colorsList

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[55,45], marker_colors=colors), 1, 1)
    fig.update_layout(legend=dict(x=-.9, y=.4),width=380, height=380, margin=dict(l=215,r=0,b=155,t=0,pad=4))

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.6, hoverinfo="label+percent+name", textinfo='value')

    try:
        plotly.offline.plot(fig, filename ='static/diggingPieChart.html', auto_open=False)
        plotly.offline.plot(fig, filename ='templates/diggingPieChart.html', auto_open=False)
    except (RuntimeError, TypeError, NameError):
        print("We experience some technical problems")

def treesPieChart():

    labels = ["Picea Abies", "Pinus Sylvestris", "Abies Grandis", "Abiels Alba", "Larix Decidua"]

    colorsList = []
    for x in labels:
       for y in colorsdict:
          colorsList.append(colorsdict[y])
    colors = colorsList

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[61, 6, 2, 20, 16], marker_colors=colors), 1, 1)
    fig.update_layout(legend=dict(x=-.9, y=.4),width=380, height=380, margin=dict(l=215,r=0,b=175,t=0,pad=1))
    fig.update_layout(annotations=[dict(text='105', x=0.50, y=0.5, font_size=20, showarrow=False)])

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.6, hoverinfo="label+percent+name", textinfo='value')

    try:
        plotly.offline.plot(fig, filename ='static/treesPieChart.html', auto_open=False)
        plotly.offline.plot(fig, filename ='templates/treesPieChart.html', auto_open=False)
    except (RuntimeError, TypeError, NameError):
        print("We experience some technical problems")

def cyclingBarChart():

    labels = ["2016", "2017", "2018", "2019", "2020"]

    # Create subplots: use 'domain' type for Pie subplot
    fig = go.Figure([go.Bar(x=labels, y=[37, 137, 1104, 2205, 2361])])
    fig.update_layout(width=400, height=200, margin=dict(l=40, r=20, t=30, b=20))

    try:
        plotly.offline.plot(fig, filename ='static/cyclingBarChart.html', auto_open=False)
        plotly.offline.plot(fig, filename ='templates/cyclingBarChart.html', auto_open=False)
    except (RuntimeError, TypeError, NameError):
        print("We experience some technical problems")

def weightChart():

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=["January", "February", "March", "April", "May", "June",
                                "July", "August", "September", "October", "November", "December"],
                             y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 249.6, 2291.1, 0], fill='tozeroy')) # fill down to xaxis

    fig.update_layout(width=400, height=200, margin=dict(l=40, r=20, t=30, b=20), xaxis=dict(showgrid=False))

    try:
        plotly.offline.plot(fig, filename ='static/weightChart.html', auto_open=False)
        plotly.offline.plot(fig, filename ='templates/weightChart.html', auto_open=False)
    except (RuntimeError, TypeError, NameError):
        print("We experience some technical problems")



colorsdict =	{
  "Color1": "rgb(174,150,250)",
  "Color2": "rgb(78,23,250)",
  "Color3": "rgb(120,79,249)",
  "Color4": "rgb(189,189,189)",
  "Color5": "rgb(115,115,115)",
  "Color6": "rgb(49,130,189)",
  "Color7": "rgb(67,67,67)"
}
