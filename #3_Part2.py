#Compter le nombre de lignes du fichier
with open(r"Input#3.txt", 'r') as fichier:
    nb_lines = len(fichier.readlines())
    
#Ouvrir et lire le fichier d'inputs
fichier=open("Rucksacks#3.txt", "r")
lignes=fichier.readlines()

#Créer et remplir la liste des badges :
list_badges=[]
for i in range(0,nb_lines,3) :
    list_badges_ici=[]
    for j in lignes[i] :
        if j in lignes[i+1] and j in lignes[i+2] and j!= '\n':
            list_badges_ici.append(j)
        
    list_badges_ici=list(set(list_badges_ici))
    print(list_badges_ici)
        
    for k in list_badges_ici :
        list_badges.append(k)
print(list_badges)


#Convertir la liste des badges en priorities :
liste_priorities=[]
for i in list_badges :
    
    """Traiter le cas des majuscules"""
    if ord(i)>=65 and ord(i)<=90 :
        liste_priorities.append(ord(i)-38)
    
    """Traiter le cas des minuscules"""
    if ord(i)>=97 and ord(i)<=122 :
        liste_priorities.append(ord(i)-96)

print(liste_priorities)

#Calculer la sommme des priorities :    
sum_priorities = 0    
for i in liste_priorities :
    sum_priorities += i

print(len(liste_priorities))
print(sum_priorities)
    


