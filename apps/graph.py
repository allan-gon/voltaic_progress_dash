import pathlib
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
from apps.wrangle import main, SCENARIOS
from app import app


PATH = pathlib.Path(__file__).parent

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
        return [{'label': i, 'value': i} for i in SCENARIOS['Easy']]
    elif val == 'hard':
        bench = [i.strip(" Easy") for i in SCENARIOS['Hard']]
        return [{'label': i, 'value': i} for i in bench]
    return []


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='scenario_drop', component_property='value'),
    State(component_id='choice', component_property='value')
)
def create_graph(scenario, dropdown):
    if dropdown == 'easy':
        df, groups = main(m_easy=True)
    else:
        df, groups = main(m_easy=False)

    if scenario in df.scenario_name.unique():
        temp = groups.get_group(scenario).sort_values(by='date').groupby('date')
        x = []
        y = []
        for name, group in temp:
            x.append(name)
            y.append(group.score.mean())
        fig = px.line(
            x=x,y=y, title='Avg Score by Day'
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(
            xaxis_title='Day',
            yaxis_title='Score'
        )
    else:
        fig = px.line(title='YOU HAVEN"T PLAYED THIS SCENARIOS YET!')
    return fig


layout = html.Div(
    id='temp',
    children=[
        choice, drop, graph,
    ]
)
