#Ouvrir et lire le fichier d'inputs
fichier=open("Input#3.txt", "r")
lignes=fichier.readlines()

#Créer et remplir la liste des doubles :
liste_double = []
for ligne in lignes :
    compartment_1=[]
    compartment_2=[]
    liste_double_ici=[]
    for i in range(0,int(len(ligne)/2)) :
        compartment_1.append(ligne[i])
    for i in range(int(len(ligne)/2),len(ligne)) :
        compartment_2.append(ligne[i])
    del compartment_2[int(len(compartment_2))-1]
    
    for i in compartment_1 :
        if i in compartment_2 :
            liste_double_ici.append(i)
    liste_double_ici=list(set(liste_double_ici))

    for i in liste_double_ici :
        liste_double.append(i)

#Convertir la liste_double en priorities :
liste_priorities=[]
for i in liste_double :
    
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
    