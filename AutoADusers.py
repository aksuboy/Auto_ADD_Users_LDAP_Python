#coding:utf-8

# Import du ou des modules nécessaire
import os

# On définit une variable nb_users pour le nombre de comptes créés

nb_users = 0


# enregistrer toutes les valeurs du tableau AJOUTusers.csv dans une variable ajout_users

os.chdir("chemin du dossier contenant le CSV)
fichier_csv = open("AJOUTusers.csv", "r")
ajout_users = fichier_csv.read
fichier_csv.close()
"""
s'assurer que ajout_users est bien un objet de la classe dict"""
# boucle for pour récupérer chaque données contenues dans la variable ajout_users dans des variables séparés
for users in fichier_csv
    # lire chaque colonne de chaque ligne afin d'en extraire les donnees sous forme de dictionnaire avec les variable en [string]
    {
    username =
    password =
    Firstname =
    Lastname =
    email =
    streetaddress =
    city =
    zipcode =
    state =
    country =
    telephone =
    jobtitle =
    compagny =
    department =

}


# verification si l'utilisateur existe avant de lancer la création
"""si user existe deja, signalez que """

