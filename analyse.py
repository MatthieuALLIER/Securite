# Execution du module format pour récupérer le fichier issu de la base de données
exec(open("format.py").read())

#Import des modules de graphiques
import plotly.express as px
import plotly.io as pio
pio.renderers.default="browser" 

# Graphique 1 : Classement des règles les plus utilisées

regles = df.policyid.value_counts()
regles  = pd.DataFrame(regles.reset_index())

fig_regles = px.bar(regles,x="index", y="policyid", title="Classement des règles")
fig_regles.show()

# Graphique 2 : Utilisation des différents protocoles 

protocoles = df.proto.value_counts()
protocoles = pd.DataFrame(protocoles.reset_index())

fig_protocoles = px.bar(protocoles,x="index", y="proto", title="Utilisation des différents protocoles")
fig_protocoles.show()

# Graphique 3 : Top 10 des règles avec le protocole UDP

df_ucp = df.loc[df.proto=="UDP"]

regles_udp = df.policyid.value_counts()
regles_udp  = pd.DataFrame(regles.reset_index())

top_10_regles_udp = regles_udp.head(10)

fig_10_regles_udp = px.bar(top_10_regles_udp,x="index", y="policyid", title="Classement des 5 règles les plus utilisées pour le protocoles TCP")
fig_10_regles_udp.show()

# Graphique 4 : Top 5 des règles avec le protocole TCP

df_tcp = df.loc[df.proto=="TCP"]

regles_tcp = df.policyid.value_counts()
regles_tcp  = pd.DataFrame(regles.reset_index())

top_5_regles_tcp = regles_tcp.head(5)

fig_5_regles_tcp = px.bar(top_5_regles_tcp,x="index", y="policyid", title="Classement des 5 règles les plus utilisées pour le protocoles TCP")
fig_5_regles_tcp.show()

# Graphique 6 : action en fonction du protocole

proto_action = df.groupby(["proto","action"]).size()
proto_action  = pd.DataFrame(proto_action.reset_index())

proto_action.columns= ["proto","action","valeur"]

fig_proto_action = px.bar(proto_action,x="proto", y="valeur", color="action", title="Action en fonction du protocole")
fig_proto_action.show()

# Graphique 7 : Distribution des Ipsource 

ipsource = df.ipsrc.value_counts()
ipsource  = pd.DataFrame(ipsource.reset_index())

top10_ipsource=ipsource.head(10)
fig_ipsource = px.pie(top10_ipsource,values="ipsrc", names="index", title="Distribution des différents Ip Sources")
fig_ipsource.show()

# Graphique 8 : Action en fonction de l'adresse IP source 

df_action_top1_ipsource=df.loc[df.ipsrc=="109.234.162.235"] 

action_top1_ipsource=df_action_top1_ipsource.action.value_counts()
action_top1_ipsource=pd.DataFrame(action_top1_ipsource.reset_index())

fig_ipsource_action = px.pie(action_top1_ipsource,values="action", names="index", title="Distribution des différents Ip Sources")
fig_ipsource_action.show()

# Graphique 9 : Nombre d'action par jour 

df_daily = df.groupby([df['datetime'].dt.date,"action"]).size()
df_daily  = pd.DataFrame(df_hourly.reset_index())

df_daily.columns= ["datetime","action","valeur"]

df_daily['date_str'] = df_daily['datetime'].dt.strftime('%Y/%m/%d')

fig_date_action = px.line(df_daily,x="date_str", y="valeur", color="action", title="Action en fonction de la journée")
fig_date_action.show()

