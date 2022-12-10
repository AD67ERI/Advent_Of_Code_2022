#Ouvrir et lire le fichier d'inputs
fichier=open("Input#10.txt", "r")
lignes=fichier.readlines()

#Création du dictionnaire des signal strengths
list=[20,60,100,140,180,220]
dict={}
for i in list :
    dict[i]=0
print(dict)


nb_cycles = 0
X = 1

for ligne in lignes :
    if nb_cycles in list and nb_cycles !=219:
        dict[nb_cycles]=nb_cycles*X
    if nb_cycles == 219 :
        dict[nb_cycles]=nb_cycles*X + X
    
    if ligne[:4]=='noop' :
        nb_cycles += 1
    else :
        nb_cycles += 1
        if nb_cycles in list and nb_cycles !=219:
            dict[nb_cycles]=nb_cycles*X
        if nb_cycles == 219 :
            dict[nb_cycles]=nb_cycles*X + X
        nb_cycles += 1
        X += int(ligne[5:len(ligne)-1])
print(dict)
sum_signal_strengths=0
for i in dict :
    sum_signal_strengths += dict[i]
print(sum_signal_strengths)
