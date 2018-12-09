import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import numpy as np


dataSource = pd.read_csv('./data/data.csv')
X = list(dataSource.values[:, 0])
Y = list(dataSource.values[:, 1])

# mapbox_access_token = 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2lxMnVvdm5iMDA4dnhsbTQ5aHJzcGs0MyJ9.X9o_rzNLNesDxdra4neC_A'
# create
# mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'
# github
mapbox_access_token = 'pk.eyJ1IjoibGl1anAyMDA2IiwiYSI6ImNqcGZoajlpcDBiMGYzd250dWlpOWM2dXgifQ.j3KwQmlPytRkLpPCMhHzjw'

'''
map layout

'''
lon = 115 + (117 - 115) * np.random.random(size=200)
lat = 40 + (41 - 40) * np.random.random(size=200)
layout = dict(
    autosize=True,
    height=1000,
    font=dict(color='#CCCCCC'),
    titlefont=dict(color='#CCCCCC', size='14'),
    hovermode="closest",
    plot_bgcolor="#191A1A",
    paper_bgcolor="#020202",
    legend=dict(font=dict(size=10), orientation='h'),
    title='Satellite Overview',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="dark",  # basic
        center=dict(
            lon=116.5,
            lat=39.9
        ),
        zoom=5,
    )
)
'''
X = list(np.linspace(-5, 5))
Y = list(map(lambda x: x, X))
Y1 = list(map(lambda x: np.sin(x), X))
Y2 = list(map(lambda x: np.cos(x), X))
'''
#  external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)
colors = {
    'background': "#404040",
    'text': '#0000FF',
    'foreground': '#BCDFAA'
}

app.layout = html.Div(style={'backgroundColor': colors['foreground']}, children=[
        html.H1(children="Information Display System ", style={'textAlign': 'center', 'color': colors['text']}),
        dcc.Dropdown(
            id='myDropDown',
            options=[
                {'label': 'Linear', 'value': 'Linear'},
                {'label': 'Sin', 'value': 'Sin'},
                {'label': 'Pie', 'value': 'Pie'}
            ],
            value='Linear'
        ),
        html.Div(
            [dcc.Graph(id='myGraph'),
             dcc.Interval(id='myInterval', interval=1000, n_intervals=0)]
        ),
        html.Div(
            [dcc.Graph(id="myMap")]
        )
])


@app.callback(Output('myGraph', 'figure'), [Input('myDropDown', 'value')])
def update_graph(selected_dropdown_value):
    datas = []
    if selected_dropdown_value == 'Linear':
        datas.append(dict(x=X, y=Y, type='scatter', mode='markers+lines'))
    if selected_dropdown_value == 'Sin':
        datas.append(dict(type='choropleth', mode='markers', geo='geo'))
    if selected_dropdown_value == 'Pie':
        datas.append(dict(values=X, type='pie'))

    layout = dict(
        paper_bgcolor='#171717',
        plot_bgcolor='#171717',
        xaxis=dict(gridcolor='#ffffff', gridwidth=1,
                   zerolinecolor='#ffffff', zerolinewidth=2, zeroline='true'),
        yaxis=dict(gridcolor='#ffffff', gridwidth=1,
                   zerolinecolor='#ffffff', zerolinewidth=2, zeroline='true'),
        clickmode='none'
    )
    figure = dict(data=datas)
    return figure


@app.callback(Output('myMap', 'figure'), [Input('myInterval', 'n_intervals')])
def update_graph(interval):
    trace = []
    if interval % 2 == 0:
        trace = [dict(lat=lat, lon=lon, type='scattermapbox', mode='markers', subplot='mapbox',
                      marker=dict(color='#ff0000', size=10,))]
    if interval % 2 == 1:
        trace = [dict(lat=lat, lon=lon, type='scattermapbox', mode='markers', subplot='mapbox',
                      marker=dict(color='#00ff00', size=10, ))]
    figure = dict(data=trace, layout=layout)
    return figure


if __name__ == '__main__':
    app.run_server()
