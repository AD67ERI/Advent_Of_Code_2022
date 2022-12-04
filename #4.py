#Ouvrir et lire le fichier d'inputs
fichier=open("Input#4.txt", "r")
lignes=fichier.readlines()

nb_overlaps = 0

for ligne in lignes :
    
    #Création des listes de sections assignées à chacun des deux elfs
    l=ligne.split(',')
    l[1]=l[1][:(len(l[1])-1)]
    list=l[0].split('-') + l[1].split('-')
    elf_1=[i for i in range(int(list[0]),int(list[1])+1)]
    elf_2=[i for i in range(int(list[2]),int(list[3])+1)]
        
    #Test d'overlap
    if min(elf_1) in elf_2 and max(elf_1) in elf_2 or min(elf_2) in elf_1 and max(elf_2) in elf_1 :
        nb_overlaps += 1

print(nb_overlaps)