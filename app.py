import dash
from dash import html

# Required for Azure App Service to find the app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Hello from Azure!"),
    html.P("This is a Dash app deployed via GitHub Actions.")
])

if __name__ == '__main__':
    app.run(debug=True)
