import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import pandas as pd


dataSource = pd.read_csv('./data/data.csv')
X = list(dataSource.values[:, 0])
Y = list(dataSource.values[:, 1])

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
                {'label': 'Cos', 'value': 'Cos'}
            ],
            value='Linear'
        ),
        dcc.Graph(id='myGraph'),
        dcc.Graph(id='myGraph2')
])


@app.callback(Output('myGraph', 'figure'), [Input('myDropDown', 'value')])
def update_graph(selected_dropdown_value):
    datas = []
    if selected_dropdown_value == 'Linear':
        datas.append(dict(x=X, y=Y, type='scatter', mode='markers+lines'))
    if selected_dropdown_value == 'Sin':
        datas.append(dict(x=X, y=Y, type='scatter', mode='markers'))
    if selected_dropdown_value == 'Cos':
        datas.append(dict(x=X, y=Y, type='scatter', mode='lines'))

    layout = dict(
        paper_bgcolor='#171717',
        plot_bgcolor='#171717',
        xaxis=dict(gridcolor='#ffffff', gridwidth=1,
                   zerolinecolor='#ffffff', zerolinewidth=2, zeroline='true'),
        yaxis=dict(gridcolor='#ffffff', gridwidth=1,
                   zerolinecolor='#ffffff', zerolinewidth=2, zeroline='true'),
        clickmode='none'
    )
    figure = dict(data=datas, layout=layout)
    return figure


@app.callback(Output('myGraph2', 'figure'), [Input('myDropDown', 'value')])
def update_graph(selected_dropdown_value):
    datas = []
    if selected_dropdown_value == 'Linear':
        datas.append(dict(x=X, y=Y, type='scatter', mode='markers+lines'))
    if selected_dropdown_value == 'Sin':
        datas.append(dict(x=X, y=Y, type='scatter', mode='markers'))
    if selected_dropdown_value == 'Cos':
        datas.append(dict(x=X, y=Y, type='scatter', mode='lines'))

    layout = dict(
        paper_bgcolor='#171717',
        plot_bgcolor='#171717',
        xaxis=dict(gridcolor='#ffffff', gridwidth=1,
                   zerolinecolor='#ffffff', zerolinewidth=2, zeroline='true'),
        yaxis=dict(gridcolor='#ffffff', gridwidth=1,
                   zerolinecolor='#ffffff', zerolinewidth=2, zeroline='true'),
        clickmode='none'
    )
    figure = dict(data=datas, layout=layout)
    return figure


if __name__ == '__main__':
    app.run_server()
