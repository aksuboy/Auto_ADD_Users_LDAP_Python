#coding:utf-8
#On désigne l'adresse du controleur de domaine
DC = "dc=lab,dc=local"
# Import du ou des modules nécessaire
import os
import sys

# On définit une variable nb_users pour le nombre de comptes créés

nb_users = 0



# On demande ou est le fichier?
print("Entrez le chemin du fichier contenant la liste des utilisateurs à ajouter : ")
listing = input(">>> ")

#on verifie que le fichier existe
if_exist = os.path.exists(listing)
if_file = os.path.isfile(listing)
if if_exist and if_file is True :
    print("Fichier {} trouvé".format(listing))
else :
    print("Fichier non trouvé : le programme va quiter...")
    sys.exit()
#On enregistre les données du fichier et le une variable
listing_lu = open(listing, "r")
listing_ok = listing_lu.read()
listing_lu = open(listing, "r")
nb_lignes = len(listing_lu.readlines())
print("génération de la liste des comptes à créer : \n_______________\n"+listing_ok+"\n_______________")
listing_lu.close()

#Création de la fonction ajoutAD
def ajoutAD():
    # On verifie si le compte existe
    utilisateur = "dsquery user "+DC+" -name {}"
    ajoutAD = utilisateur.format(line.strip())
    ajoutCMD = os.popen(ajoutAD).read()
    if ajoutCMD: #si le compte existe déjà
        check = "{} existe déjà".format(line.strip())
        print(check)
        
    if not ajoutCMD:#si le compte n'éxiste pas on doit le créé
        ajoutAD = 'dsadd user "Cn={},{}" -disabled yes'
        ajout_synthaxe = ajoutAD.format(line.strip(), DC.strip())
        os.system(ajout_synthaxe)
        

with open(listing) as l_u:
    for i in range(nb_lignes):
        line = l_u.readline()
        ajoutAD()
        