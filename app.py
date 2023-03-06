#Import des modules Dash
from dash import Dash, dash_table, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from connexion import connexion
import pandas as pd 
import plotly.express as px
import numpy as np


con = connexion("localhost", "root", "", "securite")
req = "SELECT * FROM fw"
df = pd.read_sql(req,con)

df_der = df.tail(100000)

#Création de l'interface
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE], title='Challenge sécurité')
server = app.server  

#Menu de l'interface
head = dbc.Container([
    html.H1("Securité", style=({"margin":"5px","text-align":"center"})),
    html.Hr(),
    dbc.Tabs(
        [
            dbc.Tab(label="Accueil", tab_id="Accueil"),
            dbc.Tab(label="Statistiques", tab_id="Statistiques"),
            dbc.Tab(label="Historique", tab_id="Historique")
        ],
        id="tabPanel",
        active_tab="Accueil",
    )
])


#instrancation graphique 
# Graphique 1 : Classement des règles les plus utilisées

regles = df.policyid.value_counts()
regles  = pd.DataFrame(regles.reset_index())

fig_regles = px.bar(regles,x="index", y="policyid", title="Classement des règles")

# Graphique 2 : Utilisation des différents protocoles 

protocoles = df.proto.value_counts()
protocoles = pd.DataFrame(protocoles.reset_index())

fig_protocoles = px.bar(protocoles,x="index", y="proto", title="Utilisation des différents protocoles")

# Graphique 3 : Top 10 des règles avec le protocole UDP

df_ucp = df.loc[df.proto=="UDP"]

regles_udp = df.policyid.value_counts()
regles_udp  = pd.DataFrame(regles.reset_index())

top_10_regles_udp = regles_udp.head(10)

fig_10_regles_udp = px.bar(top_10_regles_udp,x="index", y="policyid", title="Classement des 5 règles les plus utilisées pour le protocoles TCP")

# Graphique 4 : Top 5 des règles avec le protocole TCP

df_tcp = df.loc[df.proto=="TCP"]

regles_tcp = df.policyid.value_counts()
regles_tcp  = pd.DataFrame(regles.reset_index())

top_5_regles_tcp = regles_tcp.head(5)

fig_5_regles_tcp = px.bar(top_5_regles_tcp,x="index", y="policyid", title="Classement des 5 règles les plus utilisées pour le protocoles TCP")

# Graphique 6 : action en fonction du protocole

proto_action = df.groupby(["proto","action"]).size()
proto_action  = pd.DataFrame(proto_action.reset_index())

proto_action.columns= ["proto","action","valeur"]

fig_proto_action = px.bar(proto_action,x="proto", y="valeur", color="action", title="Action en fonction du protocole")

# Graphique 7 : Distribution des Ipsource 

ipsource = df.ipsrc.value_counts()
ipsource  = pd.DataFrame(ipsource.reset_index())

top10_ipsource=ipsource.head(10)
fig_ipsource = px.pie(top10_ipsource,values="ipsrc", names="index", title="Distribution des différents Ip Sources")

# Graphique 8 : Action en fonction de l'adresse IP source 

df_action_top1_ipsource=df.loc[df.ipsrc=="109.234.162.235"] 

action_top1_ipsource=df_action_top1_ipsource.action.value_counts()
action_top1_ipsource=pd.DataFrame(action_top1_ipsource.reset_index())

fig_ipsource_action = px.pie(action_top1_ipsource,values="action", names="index", title="Distribution des différents Ip Sources")

# Graphique 9 : Nombre d'action par jour 

df_daily = df.groupby([df['datetime'].dt.date,"action"]).size()
df_daily  = pd.DataFrame(df_daily.reset_index())

df_daily.columns= ["datetime","action","valeur"]

fig_date_action = px.line(df_daily,x="datetime", y="valeur", color="action", title="Action en fonction de la journée")


colors = {
    'background': 'rgb(50, 50, 50)',
    'text': 'rgb(210, 210, 210)'
}

content = dbc.Container([ 
html.Div([
    html.Br(),
    html.H1("Acceuil"),
    
    
    html.P("Ce projet à été réalisé dans le carde d'une collaboration entre les étudiants de la formation SISE et d'OPSIE mélangeant l'aspect technique de la sécurisation, récupération de données à partir de logs ainsi l'analyse de celles-ci. En effet les étudiant d'OPSIE ont du dans, un premier temps, récupérer les données. Dans un second temps, les étudiants de SISE ont du les réaliser un traitement et analyse sur ces dernières. Nous avions 1 jour et demie pour réaliser ce projet avec par la suite comme critère d'évaluation : une soutenance et un rapport pdf.")
    
    
    
], id="Accueil-tab"),
html.Div([
    html.Br(),
    html.H1("Quelques statistiques..."),
    html.Div([
        
        html.Div(dcc.Graph(figure=fig_regles,style = {'width': '600px'})),

        html.Div(dcc.Graph(figure=fig_protocoles,style = {'width': '600px'}))
    ], style = {'display': 'flex', "border" : "10px black solid",'width': '30%',"margin-left" : "40px"}), 
    
    
    html.Div([
        
        dcc.Graph(figure=fig_10_regles_udp,style = {'width': '160%'}),

        dcc.Graph(figure=fig_5_regles_tcp,style = {'width': '160%'})
    ] ,  style = {'display': 'flex', 'width': '30%', "margin-left" : "40px", "border" : "10px black solid"}), 
    
     html.Div([
        
        dcc.Graph(figure=fig_proto_action, style = {'width': '160%'}),

        dcc.Graph(figure=fig_ipsource, style = {'width': '160%'})
    ] , style = {'display': 'flex', 'width': '30%', "margin-left" : "40px", "border" : "10px black solid"}), 
    
    
     html.Div([
        
        dcc.Graph(figure=fig_ipsource_action,style = {'width': '160%'}),

        dcc.Graph(figure=fig_date_action, style = {'width': '160%'})
    ] ,style = {'display': 'flex', 'width': '30%', "margin-left" : "40px", "border" : "10px black solid"}), 
    
], id="Statistique-tab"),
html.Div([
    
    html.Br(),
    html.H1("Historique"),
    dash_table.DataTable(df_der.to_dict('records'),[{"name": i, "id": i} for i in df_der.columns],
                         filter_action='native', page_size=10, style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'rgb(210, 210, 210)'
    },
    style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'rgb(210, 210, 210)'
    },),
    
    html.Br(),
    
    dcc.Dropdown(
       id='dropdown', options = list(df_der.ipsrc.unique()), value = "167.94.146.7"
    ),
    
    html.Br(),
    
    html.Div([
        
        dcc.Graph(id='pieregle', style = {'width': '160%'}),

        dcc.Graph(id='pieAction', style = {'width': '160%'})
    ] , style = {'display': 'flex', 'width': '30%', "margin-left" : "40px"}), 
    
    html.Div(dcc.Graph(id='traffic'), style = {'display': 'inline-block', 'width': '80%', "margin-left" : "130px", "border" : "10px black solid"}),
    html.Br(),
    
    
], id="Historique-tab")
])


#Rendus de l'application
app.layout = html.Div([head, content])

@app.callback([Output("Accueil-tab", "style"),Output("Statistique-tab", "style"), Output("Historique-tab", "style")],
                                                                [Input("tabPanel","active_tab")])
def render_tab_content(active_tab):

    on = {"display":"block"}

    off = {"display":"none"}

    if active_tab is not None:

        if active_tab == "Accueil":

            return [on, off, off]

        elif active_tab == "Statistiques":

            return [off, on, off]

        elif active_tab == "Historique":

            return [off, off,on]

    return "No tab selected"


@app.callback([Output('pieregle', 'figure'), Output('pieAction', 'figure'), Output('traffic', 'figure')],
    [Input('dropdown','value')])

def Graph(value): 
    
    
    regles = df[df.ipsrc == value].policyid.value_counts()
    regles  = pd.DataFrame(regles.reset_index())

    fig_regles = px.bar(regles,x="index", y="policyid", title="Classement des règles")
    
    fig_action = px.pie(df[df.ipsrc == value], values = df[df.ipsrc == value].action.value_counts(), names =df[df.ipsrc == value].action.unique(), title="Proportion des actions")
    
    df2 = df[df.ipsrc == value]
    
    df_daily = df2.groupby([df2['datetime'].dt.date]).size()
     
    df_daily  = pd.DataFrame(df_daily.reset_index())

    df_daily.columns= ["datetime","valeur"]
    
    print(df_daily)

    fig_date_action = px.line(df_daily,x="datetime", y="valeur", title="Nb de ping l'utilisateur dans la journée")

    return fig_regles, fig_action, fig_date_action

    
    


#Lancement de l'application
if __name__ == '__main__':
    app.run_server(debug = True)