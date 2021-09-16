from app import app
from apps import table, graph
from dash import dcc, html
from dash.dependencies import Input, Output



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Table|', href='/apps/table'),
        dcc.Link('Graph', href='/apps/graph')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/table':
        return table.layout
    elif pathname == '/apps/graph':
        return graph.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
