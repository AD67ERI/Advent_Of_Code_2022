#Ouvrir et lire le fichier d'inputs
fichier=open("Input#5.txt", "r")
lignes=fichier.readlines()

#Calculer le nombre de lignes et colonnes 
nb_lignes = -2
for ligne in lignes :
    if 'move' not in ligne :
        nb_lignes += 1
nb_colonnes = len(lignes[0])//4

#Créer et remplir la liste qui représente la composition de chaque colonne
colonnes_de_crates=[[] for i in range(nb_colonnes)]
for i in range(0,nb_lignes) :
    for j in range(1,nb_colonnes*4,4) :
        if lignes[i][j] != ' ' :
            colonnes_de_crates[j//4].append(lignes[i][j])
for i in range(0,len(colonnes_de_crates)) :
    colonnes_de_crates[i].reverse()
print(colonnes_de_crates)


for i in range(nb_lignes+2,len(lignes)) :
    
    #Convertir chaque instruction en une liste de 3 entiers
    instruction=lignes[i].split()
    
    #Déplacer les crates selon chaque instruction      
    for j in range(0,int(instruction[1])) : 
        colonnes_de_crates[int(instruction[5])-1].append(colonnes_de_crates[int(instruction[3])-1][len(colonnes_de_crates[int(instruction[3])-1])-int(instruction[1])+j])
    for j in range(0,int(instruction[1])) :
        del colonnes_de_crates[int(instruction[3])-1][len(colonnes_de_crates[int(instruction[3])-1])-1]

output=''
for i in range(0,len(colonnes_de_crates)) :
    output += colonnes_de_crates[i][len(colonnes_de_crates[i])-1]
print(output)
    
    
    
    

