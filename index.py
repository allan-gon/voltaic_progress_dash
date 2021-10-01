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


def main(is_exec=True):
    if is_exec:
        app.run_server(host='0.0.0.0', port=8080, debug=False, use_reloader=False)
    else:
        app.run_server()


if __name__ == '__main__':
    main()
