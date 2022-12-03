#Ouvrir et lire le fichier d'inputs
fichier=open("Input#2.txt", "r")
lignes=fichier.readlines()

points = 0
for ligne in lignes :
    
    if ligne[2] == 'X' : #Lose
        if ligne[0] == 'A' :
            points += 3
        elif ligne[0] == 'B' :
            points += 1
        else :
            points += 2
            
    elif ligne[2] == 'Y' : #Draw
        if ligne[0] == 'A' :
            points += 4
        elif ligne[0] == 'B' :
            points += 5
        else :
            points += 6
            
    else : #Win
        if ligne[0] == 'A' :
            points += 8
        elif ligne[0] == 'B' :
            points += 9
        else :
            points += 7

print(points)