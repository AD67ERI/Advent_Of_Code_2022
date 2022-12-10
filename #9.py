def head_move(head_pos,instruction) :
    
    if instruction[0]=='U' :
        head_pos[1] += int(instruction[2:len(instruction)-1])
    elif instruction[0]=='D' :
        head_pos[1] -= int(instruction[2:len(instruction)-1])
    elif instruction[0]=='L' :
        head_pos[0] -= int(instruction[2:len(instruction)-1])
    elif instruction[0]=='R' :
        head_pos[0] += int(instruction[2:len(instruction)-1])
    return head_pos



def tail_move(tail_pos,head_pos) :
    #Sur la même colonne
    if tail_pos[0] == head_pos[0] :
        if tail_pos[1] > head_pos[1] :
            tail_pos[1] -= 1
        elif tail_pos[1] < head_pos[1] :
            tail_pos[1] += 1
    #Sur la meme ligne
    if tail_pos[1] == head_pos[1] :
        if tail_pos[0] > head_pos[0] :
            tail_pos[0] -= 1
        elif tail_pos[0] < head_pos[0] :
            tail_pos[0] += 1
    #Sur une ligne et une colonne différentes
    if tail_pos[0] != head_pos[0] and tail_pos[1] != head_pos[1] :
        if tail_pos[0]<head_pos[0] and tail_pos[1]<head_pos[1] :
            tail_pos[0] += 1
            tail_pos[1] += 1
        elif tail_pos[0]>head_pos[0] and tail_pos[1]>head_pos[1] :
            tail_pos[0] -= 1
            tail_pos[1] -= 1
        elif tail_pos[0]>head_pos[0] and tail_pos[1]<head_pos[1] :
            tail_pos[0] -= 1
            tail_pos[1] += 1
        elif tail_pos[0]<head_pos[0] and tail_pos[1]>head_pos[1] :
            tail_pos[0] += 1
            tail_pos[1] -= 1
    return tail_pos


#Ouvrir et lire le fichier d'inputs
fichier=open("Input#9.txt", "r")
lignes=fichier.readlines()

head_pos=[0,0]
tail_pos=[0,0]
list_of_positions_visited=[(0,0)]

for ligne in lignes : 
    head_move(head_pos,ligne)
    while abs(head_pos[0]-tail_pos[0]) > 1 or abs(head_pos[1]-tail_pos[1]) > 1 :
        tail_move(tail_pos,head_pos)
        list_of_positions_visited.append((tail_pos[0],tail_pos[1]))

liste_sans_doublons=[]
for i in list_of_positions_visited :
    if i not in liste_sans_doublons :
        liste_sans_doublons.append(i)
print(list_of_positions_visited)
print(liste_sans_doublons)
print(len(liste_sans_doublons))


