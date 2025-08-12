# Discord Bot + Flask API

## Déploiement sur Render
1. Créer un dépôt GitHub avec ces fichiers.
2. Aller sur https://render.com et créer un **nouveau Web Service**.
3. Connecter le dépôt GitHub.
4. Ajouter les variables d'environnement :
   - DISCORD_TOKEN : token de ton bot
   - OWNER_ID : ton ID Discord
   - PORT : 10000 (Render attribue un port automatiquement)
5. Choisir **Build Command** : `pip install -r requirements.txt`
6. Choisir **Start Command** : `bash start.sh`
7. Déployer et récupérer ton URL publique.
