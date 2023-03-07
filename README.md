# Securite


# Installation cia le script sh
Pour installer l'application il faut télécharger le projet en zip ou via un git clone puis éxecuter le code suiant à la racide du projet

# INFORMATION IMPORTENTE
Le fochier build_n_run.sh suppose le fait que le container ma-mariadb fourni existe et tourne sur la machine avant le lancement des fichiers .sh

## sous LINUX
A la racine du projet 
```bash
source build_n_run.sh
```


## sous WINDOWS
Pour installer l'application il faut télécharger le projet en zip ou via un git clone puis éxecuter le code suiant à la racide du projet

```bash
docker build -t groupe5challenges .
```

puis pour lancer le container il faut executer la commande suivant en modifiant les variables d'environement après chaque `-e VAR_NAME=VALUE` selon les informations de votre base de donnée
```bash
docker run --link ma-mariadb:localhost -p 8050:8050 -e HOST=0.0.0.0 -e DB_HOST=localhost -e DB_TABLE=FW -e DB_USERNAME=root -e DB_PASSWORD=mypass123 -e DB_DATABASE=Logs_fw groupe5challenges
```
