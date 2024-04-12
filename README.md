
# Simulateur de Botnet avec Docker et Python

Ce projet utilise Docker pour créer un environnement de test sécurisé pour simuler un botnet à des fins éducatives. Le simulateur se compose de trois composants principaux: une image Docker configurée avec Kali Linux et hping3, un script de serveur en Python (`server.py`), et un script de bot en Python (`botnet.py`). Ce projet est destiné à des fins éducatives pour comprendre le fonctionnement des botnets et les stratégies pour les mitiger.

## Composants

- **Dockerfile**: Crée une image Docker basée sur `kalilinux/kali-rolling` avec `hping3` installé.
- **botnet.py**: Script de bot qui se connecte au serveur de commande et contrôle (C&C) pour exécuter des commandes.
- **server.py**: Script du serveur C&C pour gérer les bots connectés et envoyer des commandes.
- **LICENSE**: Détails de la licence sous laquelle ce projet est distribué.
- **README.md**: Ce fichier, fournissant une documentation sur le projet.

## Prérequis

- Docker installé sur votre machine.
- Python 3 installé sur votre machine (pour exécuter les scripts `botnet` et `serveur`).

## Mise en place

### Construction de l'image Docker

Pour construire l'image Docker à partir du Dockerfile:

```
docker build -t kali-hping3 .
```

### Exécution de l'environnement Docker

Pour exécuter un conteneur à partir de cette image:

```
docker run -it kali-hping3
```

Vous serez alors dans un shell à l'intérieur du conteneur, avec `hping3` prêt à être utilisé.

### Exécution du Serveur C&C

Pour démarrer le serveur C&C, exécutez:

```
python server.py
```

Assurez-vous que le script `server.py` est configuré pour écouter sur l'interface et le port appropriés.

### Connexion des Bots

Sur chaque bot, exécutez:

```
python botnet.py
```

Assurez-vous que `botnet.py` est configuré pour se connecter à l'adresse IP et au port corrects du serveur C&C.

## Utilisation

### Serveur C&C

Le serveur attendra les connexions des bots et pourra leur envoyer des commandes arbitraires à exécuter.

### Botnet

Chaque bot connecté au serveur exécutera les commandes reçues et enverra les résultats au serveur.

## Sécurité et Éthique

Ce projet est uniquement à des fins éducatives et ne doit être utilisé que dans un environnement de test sécurisé. Ne l'utilisez jamais sur des réseaux ou des systèmes sans autorisation explicite.

## Contribution

Vos contributions sont les bienvenues. Si vous avez des suggestions d'amélioration ou des corrections, veuillez soumettre une pull request ou une issue sur GitHub.
