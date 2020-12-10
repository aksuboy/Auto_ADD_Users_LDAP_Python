#coding:utf-8

# Import du ou des modules nécessaire
import os
import sys

# On définit une variable nb_users pour le nombre de comptes créés

nb_users = 0



# On demande ou est le fichier?
print("Entrez la direction du fichier contenant la liste : ")
listing = input(">>> ")

#on verifie que le fichier existe
if_exist = os.path.exists(listing)
if_file = os.path.isfile(listing)
if if_exist and if_file is True :
    print("Fichier trouvé")
else :
    print("Fichier non trouvé : le programme va quiter...")
    sys.exit()

#On extrait les valeurs du fichier
listing_lu = open(listing, "r")
print(listing_lu)
listing_lu.close()
# enregistrer toutes les valeurs du tableau AJOUTusers.csv dans une variable ajout_users


fichier_csv = open("AJOUTusers.csv", "r")
ajout_users = fichier_csv.read
fichier_csv.close()


"""
s'assurer que ajout_users est bien un objet de la classe dict"""
"""import csv
from pyad import *
def createuserfromcsv():
    #takes full file path
    file = input('please type your file path + file: ')
    data = open(file,encoding="utf-8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    #load admin information
    pyad.set_defaults(ldap_server="DC-01-Training.Udemy.training",username="Administrator",password="abc-123")

    for line in data_lines[1:]:
        user = line[0]
        oupath = line[2]
        ou = pyad.adcontainer.ADContainer.from_dn(oupath)
        pyad.aduser.ADUser.create(user,ou,password="abc-123")"""
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

"""