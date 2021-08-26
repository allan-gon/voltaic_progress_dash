import pandas as pd
from apps.data_handle import main, BENCHMARKS
import pathlib
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc
from app import app
import plotly.express as px


PATH = pathlib.Path(__file__).parent

df, groups = main()

choice = dcc.RadioItems(
    id='choice',
    options=[
        {'label': 'Easy', 'value': 'easy'},
        {'label': 'Hard', 'value': 'hard'}
    ],
    value=None,
    labelStyle={'display': 'inline-block'}
)

drop = dcc.Dropdown(
    id='scenario_drop',
    options = [],
    value=None
)

graph = dcc.Graph(
    id='graph',
    figure={}
)


@app.callback(
    Output(component_id='scenario_drop', component_property='options'),
    Input(component_id='choice', component_property='value'),
)
def gen_drop(val):
    if val == 'easy':
        return [{'label': i, 'value': i} for i in BENCHMARKS]
    elif val == 'hard':
        bench = [i.strip(" Easy") for i in BENCHMARKS]
        return [{'label': i, 'value': i} for i in bench]
    return []


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='scenario_drop', component_property='value')
)
def create_graph(val):
    if val:
        fig = px.line(
            data_frame=groups.get_group(val).sort_values(by='date'),
            x='date',y='score', title=val
        )
        fig.update_traces(mode='lines+markers')
        return fig
    else:
        return {}


layout = html.Div(
    id='temp',
    children=[
        choice, drop, graph,
    ]
)

# TODO: Find a way to fix the fucked up lines in the graph
# they exist because mutiple plays of a scenario are within a short time of one another