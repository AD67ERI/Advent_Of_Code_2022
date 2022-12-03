#Ouvrir et lire le fichier d'inputs
fichier=open("Input#2.txt", "r")
lignes=fichier.readlines()

points = 0
for ligne in lignes :
    
    if ligne[0]=='A' and ligne[2]=='X' or ligne[0]=='B' and ligne[2]=='Y' or ligne[0]=='C' and ligne[2]=='Z':
        if ligne[2] == 'X' :
            points += 4
        elif ligne[2] == 'Y' :
            points += 5
        else :
            points += 6
    
    elif ligne[2] == 'X' :
        if ligne[0] == 'C' :
            points += 7
        else :
            points += 1
    
    elif ligne[2] == 'Y' :
        if ligne[0] == 'A' :
            points += 8
        else :
            points += 2
    
    else :
        if ligne[0] == 'B' :
            points += 9
        else :
            points += 3

print(points)
