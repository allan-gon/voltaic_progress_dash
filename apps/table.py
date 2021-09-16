from dash.dependencies import Input, Output
from apps.create_table import create_table
from dash import dcc, html
from app import app
import pathlib


PATH = pathlib.Path(__file__).parent

select_table = dcc.RadioItems(
    id='select_table',
    options=[
        {'label': 'Easy', 'value': 'Easy'},
        {'label': 'Hard', 'value': 'Hard'},
    ],
)

layout = html.Div(
    id='layout',
    children=[select_table]
)


@app.callback(
    Output(component_id='layout', component_property='children'),
    Input(component_id='select_table', component_property='value'),
    prevent_initial_call=True
)
def add_graph(value):
    if value == 'Easy':
        select_table.value = 'Easy'
        return [select_table, create_table(is_easy=True)]
    elif value == 'Hard':
        select_table.value = 'Hard'
        return [select_table, create_table(is_easy=False)]
    else:
        return [select_table]
