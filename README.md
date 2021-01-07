# monpremierprojet
Ajout utilisateur dans le répertoire active directory automatiquement à partir d'une liste


Ce script permet l'ajout d'utilisateur dans un répertoire LDAP


Il suffit de compléter le fichier list.csv

Vous avez donc besoin du fichier list.csv et du script AutoADusers.py



Démarrage
Entrez vos données dans le fichier csv au préalable.

Executer le script à partir de votre serveur qui fait controleur de domaine. 
Il vous demandera en premier lieu l'adresse du domaine. exemple : lab.local
Il vous sera demandé ensuite d'indiquer le chemin du fichier list.csv, s'il n'est pas dans le meme dossier entrez le chemin absolu. ex : list.csv
l'identifiant créé automatiquement sera constitué de la première lettre du prénom suivi du nom de famille.
Auteur : CIFTCI Veli
Versions 1.0


License Opensource
Ce script rédigé en python par l'auteur est mis à contribution de la communauté gratuitement. Vous avez accès également accès au script pour le modifier.
