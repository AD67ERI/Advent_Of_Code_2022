#Ouvrir et lire le fichier d'inputs
fichier=open("Input#4.txt", "r")
lignes=fichier.readlines()

nb_overlaps = 0

for ligne in lignes :
    
    #Création des listes de sections assignées à chacun des deux elfs
    l=ligne.split(',')
    l[1]=l[1][:(len(l[1])-1)]
    list=l[0].split('-') + l[1].split('-')
    sections=[i for i in range(int(list[0]),int(list[1])+1)] + [i for i in range(int(list[2]),int(list[3])+1)]
    
    #Concaténation des deux listes et test d'overlap :
    nb_doubles = 0
    for i in sections :
        if sections.count(i) >= 2 :
            nb_doubles += 1
    if nb_doubles >= 1 :
        nb_overlaps += 1 
    
print(nb_overlaps)
