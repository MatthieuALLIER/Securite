# Securite

Pour installer l'application il faut télécharger le projet en zip ou via un git clone puis éxecuter le code suiant à la racide du projet

```bash
docker build -t groupe5challenges .
```

puis pour lancer le container il faut executer la commande suivant en modifiant les variables d'environement après chaque `-e VAR_NAME=VALUE` selon les informations de votre base de donnée
```bash
docker run --link ma-mariadb:localhost -p 8050:8050 -e HOST=0.0.0.0 -e DB_HOST=localhost -e DB_TABLE=FW -e DB_USERNAME=root -e DB_PASSWORD=mypass123 -e DB_DATABASE=Logs_fw groupe5challenges
```
