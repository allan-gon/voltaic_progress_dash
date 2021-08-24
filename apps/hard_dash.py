import dash_table
import pandas as pd
from apps.data import main, BENCHMARKS
import pathlib
import dash_html_components as html


PATH = pathlib.Path(__file__).parent

df, groups = main(easy=False)

table = {
    'Type': [], 'Subtype': [],
    'Scenario': [], 'High Score': [],
    'Average Score': [],
}

ranks = ["Jade", "Master", "Grandmaster", "Nova", "Astra"]

with open("./data/hard_bench.txt", "r") as f:
    content = f.readlines()
    for i in range(len(content)):
        table[ranks[i]] = [int(j) for j  in content[i].split(', ')]

for scenario in [i.strip(" Easy") for i in BENCHMARKS]:
    table['Type'].append(groups.get_group(scenario).scenario_type.iloc[0])
    table['Subtype'].append(groups.get_group(scenario).sub_type.iloc[0])
    table['Scenario'].append(scenario)
    table['High Score'].append(round(groups.get_group(scenario).score.max(), 2))
    table['Average Score'].append(round(groups.get_group(scenario).score.mean(), 2))

layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in table.keys()],
    data=pd.DataFrame.from_dict(table).to_dict('records'), # looks into dixing this, i think it works but is trash!!!
    style_cell={
        'textAlign': 'left', 'whiteSpace': 'normal',
        'height': 'auto',
    },
    style_data_conditional=[
        {
            'if': {'column_id': 'Scenario'},
            'fontWeight': 'bold'
        },
        # color for subtype
        {
            'if': {
                'filter_query': '{Subtype} = Dynamic',
                'column_id': ['Subtype','Scenario']
            },
            'backgroundColor': '#fff1aa'
        },
        {
            'if': {
                'filter_query': '{Subtype} = Static',
                'column_id': ['Subtype','Scenario']
            },
            'backgroundColor': '#EA9999'
        },
        {
            'if': {
                'filter_query': '{Subtype} = Precise',
                'column_id': ['Subtype','Scenario']
            },
            'backgroundColor': '#A2C4C9'
        },
        {
            'if': {
                'filter_query': '{Subtype} = Reactive',
                'column_id': ['Subtype','Scenario']
            },
            'backgroundColor': '#A4C2F4'
        },
        {
            'if': {
                'filter_query': '{Subtype} = Speed',
                'column_id': ['Subtype','Scenario']
            },
            'backgroundColor': '#D5A6BD'
        },
        {
            'if': {
                'filter_query': '{Subtype} = Evasive',
                'column_id': ['Subtype','Scenario']
            },
            'backgroundColor': '#B4A7D6'
        },
        # color for type
        {
            'if': {
                'filter_query': '{Type} = Clicking',
                'column_id': 'Type'
            },
            'backgroundColor': '#CC0000',
            'color': 'white'
        },
        {
            'if': {
                'filter_query': '{Type} = Tracking',
                'column_id': 'Type'
            },
            'backgroundColor': '#1155CC',
            'color': 'white'
        },
        {
            'if': {
                'filter_query': '{Type} = Switching',
                'column_id': 'Type'
            },
            'backgroundColor': '#351C75',
            'color': 'white'
        },
        # color of ranks
        {
            'if': {
                'column_id': 'Jade',
            },
            'backgroundColor': '#CEFDCE',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Master',
            },
            'backgroundColor': '#F8C0ED',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Grandmaster',
            },
            'backgroundColor': '#FFF1AA',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Nova',
            },
            'backgroundColor': '#C089FF',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Astra',
            },
            'backgroundColor': '#E786B0',
            'textAlign': 'center'
        },
        # color of high score
        {
            'if': {
                'filter_query': '{High Score} >= {Jade} && {High Score} < {Master}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#CEFDCE',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Master} && {High Score} < {Grandmaster}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#F8C0ED',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Grandmaster} && {High Score} < {Nova}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#FFF1AA',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Nova} && {High Score} < {Astra}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#C089FF',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Astra}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#E786B0',
        },
        # color of avg score
        {
            'if': {
                'filter_query': '{Average Score} >= {Jade} && {Average Score} < {Master}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#CEFDCE',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Master} && {Average Score} < {Grandmaster}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#F8C0ED',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Grandmaster} && {Average Score} < {Nova}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#FFF1AA',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Nova} && {Average Score} < {Astra}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#C089FF',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Astra}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#E786B0',
        },
        # width of columns
        {
            'if': {
                'column_id': 'Type'
            },
            'width': '10%',
            'textAlign': 'center'
        },
                {
            'if': {
                'column_id': 'Subtype'
            },
            'width': '10%',
            'textAlign': 'center'
        },
                {
            'if': {
                'column_id': 'Scenario'
            },
            'width': '20%',
            'textAlign': 'center'
        },
                {
            'if': {
                'column_id': 'High Score'
            },
            'textAlign': 'center'
        },
                {
            'if': {
                'column_id': 'Average Score'
            },
            'textAlign': 'center'
        },
    ],
    style_header_conditional=[
        {
            'if': {'column_id': 'Jade'},
            'backgroundColor': '#85FA85',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Master'},
            'backgroundColor': '#EC44CA',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Grandmaster'},
            'backgroundColor': '#FFD700',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Nova'},
            'backgroundColor': '#7900FF',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Astra'},
            'backgroundColor': '#FF2262',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': ['Type', 'Subtype', 'Scenario', 'High Score', 'Average Score']},
            'backgroundColor': '#0C343D',
            'color': 'white',
            'textAlign': 'center'
        },
    ]
)
