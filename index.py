from app import app # main app
from apps import easy_dash, hard_dash, graph # two pages
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Beginner|', href='/apps/easy_dash'),
        dcc.Link('Advanced|', href='/apps/hard_dash'),
        dcc.Link('Graph', href='/apps/graph')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/easy_dash':
        return easy_dash.layout
    elif pathname == '/apps/hard_dash':
        return hard_dash.layout
    elif pathname == '/apps/graph':
        return graph.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
