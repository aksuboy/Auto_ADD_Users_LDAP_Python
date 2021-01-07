#coding:utf-8

# Import du ou des modules nécessaire
import os
import sys



# On demande le nom de domaine, on formatera l'entrée en dc=xxx,dc=xxx'
print("Entrez le nom de domaine")
nom_de_domaine = input(">>>")
ndd_liste = nom_de_domaine.split(".")
DC = "dc={},dc={}".format(ndd_liste[0],ndd_liste[1])




# On demande où est le fichier?
reponse = False
while reponse == False:
    print("Entrez la direction du fichier CSV_type contenant la liste des utilisateurs à ajouter : ")
    listing = input(">>> ")

    #on verifie que le fichier existe
    if_exist = os.path.exists(listing)
    if_file = os.path.isfile(listing)

    if if_exist and if_file is True :#si le fichier existe on change la condition de la boucle
        print("Fichier {} trouvé".format(listing))
        reponse = True
    else :#sinon la condition ne change pas nous restons dans la condition
        print("Fichier non trouvé : veuillez indiquez le chemin absolu")
        reponse = False


# On définit une variable nb_users pour le nombre de comptes qui seront créés

nb_users = 0
#Création de la fonction ajoutAD
def ajoutAD():
    # On verifie si le compte existe
    utilisateur = "dsquery user "+DC+" -name {}"
    ajoutAD = utilisateur.format(value[1][:1]+value[0].lower())
    ajoutCMD = os.popen(ajoutAD).read()
    if ajoutCMD: #si le compte existe déjà
        check = "{} existe déjà".format(value[1][:1]+value[0].lower())
        print(check)
        
    if not ajoutCMD:#si le compte n'éxiste pas on doit le créé
        nb_users += 1 #on ajoute 1 au nombre d'utilisateurs créés
        ajoutAD = 'dsadd user "Cn={},ou={},{}" -mustchpwd yes -fn {} -ln {} -tel {} -pwd {}'
        ajout_synthaxe = ajoutAD.format(value[1][:1]+value[0].lower(),value[2],DC,value[1],value[0],value[3],value[4].strip())
        os.system(ajout_synthaxe)
        
        

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
  
    print("création du compte de ", value[1],value[0])
    ajoutAD()
    
    #print(value[2])

print("nombre de compte à créer :", nb_users)
listing_lu.close()
