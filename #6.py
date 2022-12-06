#Ouvrir et lire le fichier d'inputs
fichier=open("Input#6.txt", "r")
ligne=fichier.readlines()

i=0
nb_double = 1
while nb_double != 0 :
    seq = ligne[0][i:i+4]
    nb_caractere_unique = 0
    for j in seq :
        if seq.count(j)==1 :
            nb_caractere_unique +=1
    if nb_caractere_unique == 4 :
        print(i+4)
        nb_double=0
    else :
        i+=1
    
    
    


        


