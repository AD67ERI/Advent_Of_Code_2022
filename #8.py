#Ouvrir et lire le fichier d'inputs
fichier=open("Input#8.txt", "r")
lignes=fichier.readlines()

nb_lines=len(lignes)
nb_columns=len(lignes[0])-1
nb_visible_trees = 0


#Counting the edges
nb_trees_edges=2*nb_columns + 2*(nb_lines-2)

#Counting the interior
nb_visible_trees_interior = 0
for i in range(1,nb_lines-1) :
    for j in range(1,nb_columns-1) :
        #Left
        nb_higher_trees_left = 0 
        for k in range(0,j) :
            if lignes[i][j] <= lignes[i][k] :
                nb_higher_trees_left += 1
        if nb_higher_trees_left == 0 :
            nb_visible_trees_interior += 1
        else :
            #Right
            nb_higher_trees_right = 0
            for k in range(j+1,nb_columns) :
                if lignes[i][j] <= lignes[i][k] :
                    nb_higher_trees_right += 1
            if nb_higher_trees_right == 0 :
                nb_visible_trees_interior += 1
            else :
                #Up
                nb_higher_trees_up = 0
                for k in range(0,i) :
                    if lignes[i][j] <= lignes[k][j] :
                        nb_higher_trees_up +=1
                if nb_higher_trees_up == 0 :
                    nb_visible_trees_interior += 1
                else :
                    #Down
                    nb_higher_trees_down = 0
                    for k in range(i+1, nb_lines) :
                        if lignes[i][j] <= lignes[k][j] :
                            nb_higher_trees_down += 1
                    if nb_higher_trees_down == 0 :
                        nb_visible_trees_interior += 1

nb_visible_trees = nb_trees_edges + nb_visible_trees_interior

print(nb_visible_trees)
