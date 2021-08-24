import dash_table
import pandas as pd
from apps.data_handle import main, BENCHMARKS
import pathlib
import dash_html_components as html


PATH = pathlib.Path(__file__).parent

df, groups = main()

table = {
    'Type': [], 'Subtype': [],
    'Scenario': [], 'High Score': [],
    'Average Score': [],
}

ranks = ["Bronze", "Silver", "Gold", "Platinum", "Diamond"]

with open("./data/easy_bench.txt", "r") as f:
    content = f.readlines()
    for i in range(len(content)):
        table[ranks[i]] = [int(j) for j  in content[i].split(', ')]

for scenario in BENCHMARKS:
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
                'column_id': 'Bronze',
            },
            'backgroundColor': '#FCE5CD',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Silver',
            },
            'backgroundColor': '#DCE5EC',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Gold',
            },
            'backgroundColor': '#E4DAB0',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Platinum',
            },
            'backgroundColor': '#B9EFEA',
            'textAlign': 'center'
        },
        {
            'if': {
                'column_id': 'Diamond',
            },
            'backgroundColor': '#E7FAFF',
            'textAlign': 'center'
        },
        # color of high score
        {
            'if': {
                'filter_query': '{High Score} < {Silver}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#FCE5CD',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Silver} && {High Score} < {Gold}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#DCE5EC',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Gold} && {High Score} < {Platinum}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#E4DAB0',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Platinum} && {High Score} < {Diamond}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#B9EFEA',
        },
        {
            'if': {
                'filter_query': '{High Score} >= {Diamond}',
                'column_id': 'High Score'
            },
            'backgroundColor': '#E7FAFF',
        },
        # color of avg score
        {
            'if': {
                'filter_query': '{Average Score} < {Silver}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#FCE5CD',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Silver} && {Average Score} < {Gold}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#DCE5EC',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Gold} && {Average Score} < {Platinum}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#E4DAB0',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Platinum} && {Average Score} < {Diamond}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#B9EFEA',
        },
        {
            'if': {
                'filter_query': '{Average Score} >= {Diamond}',
                'column_id': 'Average Score'
            },
            'backgroundColor': '#E7FAFF',
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
            'if': {'column_id': 'Bronze'},
            'backgroundColor': '#FF9900',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Silver'},
            'backgroundColor': '#CBD9E6',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Gold'},
            'backgroundColor': '#CAB148',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Platinum'},
            'backgroundColor': '#2FCFC2',
            'textAlign': 'center'
        },
        {
            'if': {'column_id': 'Diamond'},
            'backgroundColor': '#B9F2FF',
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
