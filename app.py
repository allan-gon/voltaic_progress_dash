import dash

app = dash.Dash(__name__, prevent_initial_callbacks=True, )

server = app.server
