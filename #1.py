#Ouvrir et lire le fichier d'inputs
fichier=open("input#1.txt", "r")
lignes=fichier.readlines()

#Lister chaque ligne du fichier
lignes_fichier=[]
for ligne in lignes :
    lignes_fichier.append(ligne[:len(ligne)-1])

#Créer une liste pour chaque elf indiquant leur numéro et le nombre de calories qu'ils transportent
nb_calories = 0
nb_elf = 1
list=[]
for i in lignes_fichier :
    if i != '' :
        nb_calories+=int(i)
    else :
        list.append((nb_elf,nb_calories))
        nb_calories=0
        nb_elf += 1      
print(list)

#Créer la liste des calories transportées et trouver le maximum
list_calories=[]
for i in range(0,len(list)) :
    list_calories.append(list[i][1])

print(max(list_calories))

for i in range(0,len(list)) :
    if list[i][1] == max(list_calories) :
        print(list[i][0])


