
# Dockerfile pour Kali Linux avec hping3

Ce Dockerfile crée une image Docker basée sur `kalilinux/kali-rolling`, la version roulante de Kali Linux, qui est une distribution Linux orientée vers les tests de pénétration et la sécurité informatique. `hping3`, un outil puissant de génération et d'analyse de paquets, est également installé dans cette image.

## Fonctionnalités

- **Base de Kali Linux**: Profitez des outils et de l'environnement de Kali Linux directement dans un conteneur Docker.
- **hping3 inclus**: `hping3` est préinstallé, permettant la manipulation de paquets pour tester la sécurité des réseaux.

## Comment utiliser cette image Docker

Pour construire l'image Docker à partir de ce Dockerfile, naviguez dans le répertoire contenant le Dockerfile et exécutez la commande suivante:

```
docker build -t kali-hping3 .
```

Cela construira une image Docker locale nommée `kali-hping3`.

Pour exécuter un conteneur à partir de cette image, utilisez:

```
docker run -it kali-hping3
```

Vous serez alors dans un shell à l'intérieur du conteneur, avec `hping3` prêt à être utilisé.

## Exemple d'utilisation de hping3

Pour envoyer des paquets SYN vers un hôte cible (par exemple, `exemple.com`), vous pouvez utiliser:

```
hping3 -S exemple.com -p 80
```

Remplacez `exemple.com` par l'adresse de votre cible et ajustez les options de `hping3` selon vos besoins.

## Contribution

Si vous avez des suggestions d'amélioration ou des corrections, n'hésitez pas à soumettre une pull request ou une issue sur GitHub.
