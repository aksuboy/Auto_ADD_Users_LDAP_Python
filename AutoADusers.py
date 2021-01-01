#coding:utf-8
#On désigne l'adresse du controleur de domaine
DC = "dc=lab,dc=local"
# Import du ou des modules nécessaire
import os
import sys

# On définit une variable nb_users pour le nombre de comptes créés

nb_users = 0



# On demande ou est le fichier?
print("Entrez la direction du fichier contenant la liste des utilisateurs à ajouter : ")
listing = input(">>> ")

#on verifie que le fichier existe
if_exist = os.path.exists(listing)
if_file = os.path.isfile(listing)
if if_exist and if_file is True :
    print("Fichier {} trouvé".format(listing))
else :
    print("Fichier non trouvé : le programme va quiter...")
    sys.exit()



#Création de la fonction ajoutAD
def ajoutAD():
    # On verifie si le compte existe
    utilisateur = "dsquery user "+DC+" -name {}"
    ajoutAD = utilisateur.format(value[1][:1]+value[0].lower())
    ajoutCMD = os.popen(ajoutAD).read()
    if ajoutCMD: #si le compte existe déjà
        check = "{} éxiste déjà".format(value[1][:1]+value[0].lower())
        print(check)
        
    if not ajoutCMD:#si le compte n'éxiste pas on doit le créé
        ajoutAD = 'dsadd user "Cn={},ou={},{}" -pwd Openclass57 -mustchpwd yes -fn {} -ln {} '
        ajout_synthaxe = ajoutAD.format(value[1][:1]+value[0].lower(),value[2],DC,value[1],value[0])
        os.system(ajout_synthaxe)
        
"""
print("création des comptes utilisateurs suivants : \n"+ listing_ok)
with open(listing) as l_u:
    for i in range(nb_lignes):
        line = l_u.readline()
        ajoutAD()
        print ("compte",line,"créé")
"""
#On enregistre les données du fichier et le une variable
listing_lu = open(listing, "r")

# Lit la première ligne du fichier (entête de colonnes)
# pour avancer jusqu'à la ligne 2
listing_lu.readline()

while True:
    #Lecture d'une nouvelle ligne dans le fichier
    line = listing_lu.readline()
    
    # Si la ligne est vide, ma fin du fichier a été atteinte
    if line == "":
        break

    # Extraction des cellules de la ligne courante
    value = line.split(";")
  
    print("création du compte : ", value[1][:1]+value[0].lower())
    ajoutAD()
    #print(value[2])
"""
nb_lignes = len(listing_lu.readlines())
#print("compte(s) à créer :\n", value)
print("nombre de compte à créer :", nb_lignes)
listing_lu.close()
"""