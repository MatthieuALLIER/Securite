#Import des modules Dash
from dash import Dash, dash_table, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

#Création de l'interface
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE], title='Challenge sécurité')
server = app.server  

#Menu de l'interface
content = [
dbc.Container([
    html.H1("Securité", style=({"margin":"5px","text-align":"center"})),
    html.Hr(),
    dbc.Tabs(
        [
            dbc.Tab(label="Accueil", tab_id="Accueil"),
            dbc.Tab(label="Statistique", tab_id="Statistique"),
            dbc.Tab(label="Historique", tab_id="Historique")
        ],
        id="tabPanel",
        active_tab="Accueil",
    )
]),
html.Div([
    html.P("acceuil")
], id="Accueil-tab", style= {'display': 'none'}),
html.Div([
    html.P("Stats robin")
], id="Statistique-tab", style= {'display': 'none'}),
html.Div([
    dash_table.DataTable("dt_logs",
                         )
], id="Historique-tab", style= {'display': 'none'})
]

#Rendus de l'application
app.layout = content

#Lancement de l'application
if __name__ == '__main__':
    app.run_server()