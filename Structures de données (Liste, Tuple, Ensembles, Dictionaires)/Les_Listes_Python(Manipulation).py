# Les listes en python

# Methode de creation d'une liste
L0 = list("Hello, World!")
L1 = [0, 1, 2, "cheikh", 2.5, 22/7, "Z"]
L2 = list(("a", True, "c", "d", False))
L3 = list(range(0, 11))

# Maipulation des listes - Indexation
L = [10, 15, -6, 2]
print(f"{L} \n")
print(f"Acceder aux élément d'une liste : {L}")
print(f"Affichage du premier element d'une liste  : {L[0]}")
print(f"Affichage du dernier element d'une liste  : {L[-1]}")

L[1] = 3
print(f"Modification de la valeur du 2nd element(L[1] = 3) : {L}")

L.append(4)
print(f"Ajout d'un element à la fin de la liste (L.append(4)) : {L}")

L.insert(2, 100)
print(f"Ajout d'un element à une position précise (L.insert(2, 100)) : {L}\n")

# Maipulation des listes - Decoupage
L1 = [15, 6, 11, -9, 0, 14, 22, 34, -95, 2, 7, 24, 10]
print(f"{L1} \n")
print(f"Affichage des 4 premier élément de la liste : {L1[0:4]}")
print(f"Affichage des éléments de la position 6 jusqu'à la fin : {L1[6:]}")
print(f"Afficher les elements du tableu depuis le déut par inervalle de 3 : {L1[0::3]}")
print(f"Afficher les elements du tableu a l'envers: {L1[::-1]}")
print(f"Afficher les elements du tableu depuis la fin par inervalle de 3 : {L1[-3::-3]}")
print(f"Afficher les elements du tableu sauf le premier et les trois derier : {L1[1:-3:]}")