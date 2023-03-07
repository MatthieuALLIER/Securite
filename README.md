# Securite

#Pour l'application :

# Installation via le script sh
Pour installer l'application il faut télécharger le projet en zip ou via un git clone puis éxecuter le code suivant à la racine du projet.

# INFORMATION IMPORTANTE
Le fichier build_n_run.sh suppose le fait que le container ma-mariadb fourni existe et tourne sur la machine avant le lancement des fichiers .sh

![image](https://user-images.githubusercontent.com/81558595/223493761-68f76252-cea3-4fd0-88bb-5eba5e4ba969.png)
![image](https://user-images.githubusercontent.com/81558595/223493965-fd7759f4-976b-4547-9366-f5a3abc44b92.png)

La base de données Logs_fw doit être créée comme indiqué dans l'énoncé du projet.

![image](https://user-images.githubusercontent.com/81558595/223494091-779a851e-338d-4656-9346-c87b8fdcb4ff.png)

Il faut aussi que la table FW soit bien remplie via les fichiers sur le drive (FW.sql ou FW_full_length.sql)

## sous LINUX
A la racine du projet 
```bash
source build_n_run.sh
```

## sous WINDOWS
Pour installer l'application il faut télécharger le projet en zip ou via un git clone puis éxecuter le code suivant à la racide du projet

```bash
docker build -t groupe5challenges .
```
puis pour lancer le container il faut executer la commande suivante en modifiant les variables d'environement après chaque `-e VAR_NAME=VALUE` selon les informations de votre base de donnée (normalement pas besoin de changer)
```bash
docker run --link ma-mariadb:localhost -p 8050:8050 -e HOST=0.0.0.0 -e DB_HOST=localhost -e DB_TABLE=FW -e DB_USERNAME=root -e DB_PASSWORD=mypass123 -e DB_DATABASE=Logs_fw groupe5challenges
```
On accède à l'application en cliquant sur le port visible à côté du container créé dans Docker desktop

#Pour le modèle : 

Il suffit d'aller dans le fichier model.py, modifier les informations d'acces à la base (une base en local via xampp suffit) et lance le script
La base aura alors une nouvelle table composée des prédictions (0 pour flux licites et 1 pour flux illicite)
