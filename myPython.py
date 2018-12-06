import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import dash


X = list(np.linspace(-5, 5))
Y = list(map(lambda x: x, X))
Y1 = list(map(lambda x: np.sin(x), X))
Y2 = list(map(lambda x: np.cos(x), X))
#  external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
colors = {
    'background': "#000000",
    'text': '#0000FF',
    'foreground': '#BCDFAA'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(children="This is a dash demo", style={'testAlign': 'center', 'color': colors['text']}),
        dcc.Dropdown(
            id='myDropDown',
            style={'backgroundColor': colors['foreground']},
            options=[
                {'label': 'Linear', 'value': 'Linear'},
                {'label': 'Sin', 'value': 'Sin'},
                {'label': 'Cos', 'value': 'Cos'}
            ],
            value='Linear'
        ),
        dcc.Graph(id='myGraph', style={'backgroundColor': colors['foreground']})
])


@app.callback(Output('myGraph', 'figure'), [Input('myDropDown', 'value')])
def update_graph(selected_dropdown_value):
    if selected_dropdown_value == 'Linear':
        return {
            'data': [{
                'x': X,
                'y': Y
            }]
        }
    if selected_dropdown_value == 'Sin':
        return {
            'data': [{
                'x': X,
                'y': Y1
            }]
        }
    if selected_dropdown_value == 'Cos':
        return {
            'data': [{
                'x': X,
                'y': Y2
            }]
        }


if __name__ == '__main__':
    app.run_server()

