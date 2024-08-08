# Méthodes et fonctions de liste en python

# La methode list() : permet de créer une liste
nomListe1 = list(('annanase', 'coco', 'banane', 'goyave', 'fraise'))
nomListe2 = list(range(0, 11))

print(f"Liste N°1 = nomListe1 = list(('annanase', 'coco', 'banane', 'goyave', 'fraise')) \n "
      f"=> {nomListe1} \n"
      f"Liste N°2 = list(range(0, 11)) \n "
      f"=> {nomListe2} \n")

# La methode index() : permet de trouver l'index d'un élément dans la liste
print(f"Position de l'element 'goyave' dans Liste N°1 : nomListe1.index('goyave') \n "
      f"=> {nomListe1.index('goyave')} \n"
      f"Position de l'element 5 dans Liste N°2 : nomListe2.index(5) \n "
      f"=> {nomListe2.index(5)} \n")

# La methode append() : permet d'ajouter un élément à la fin de la liste
nomListe1.append("orange")
nomListe2.append(11)

print(f"Ajout d'un élément à la fin de Liste N°1 : nomListe1.append('orange') \n "
      f"=> {nomListe1} \n"
      f"Ajout d'un élément à la fin de Liste N°2: nomListe2.append(11) \n "
      f"=> {nomListe2} \n")

# La methode insert() : permet d'insérer un élément à une position donnée dans la liste
nomListe1.insert(2, 'mangue')
nomListe2.insert(5, 55)

print(f"Insertion d'un élément à une position donnée de Liste N°1 : nomListe1.insert(2, 'mangue') \n "
      f"=> {nomListe1} \n"
      f"Insertion d'un élément à une position donnée de Liste N°2 : nomListe2.insert(5, 55) \n "
      f"=> {nomListe2} \n")

# La methode extend() : permet d'ajouter les éléments d'une autre liste à la fin de la liste
nomListe1.extend(('abricot', 'pamplemousse'))
nomListe2.extend(range(12, 22))

print(f"Ajout d'une liste à une autre liste de Liste N°1 : nomListe1.extend(('abricot', 'pamplemousse')) \n "
      f"=> {nomListe1} \n"
      f"Ajout d'une liste à une autre liste de Liste N°2 : nomListe2.extend(range(12, 22)) \n "
      f"=> {nomListe2} \n")

# La methode remove() : permet de supprimer le premier élément correspondant à la valeur donnée
nomListe1.remove('banane')
nomListe2.remove(10)

print(f"Suppression d'un élément de Liste N°1 : nomListe1.remove('banane') \n "
      f"=> {nomListe1} \n"
      f"Suppression d'un élément de Liste N°2 : nomListe2.remove(10) \n "
      f"=> {nomListe2} \n")

# La methode pop() : permet de supprimer un élément à une position donnée et de le retourner
nomListe1.pop(3)
nomListe2.pop(4)

print(f"Suppression d'un élément à une position donnée de Liste N°1 : nomListe1.pop(3) \n "
      f"=> {nomListe1} \n"
      f"Suppression d'un élément à une position donnée de Liste N°2 : nomListe2.pop(4) \n "
      f"=> {nomListe2} \n")

# La methode count() : permet de compter le nombre d'occurrences d'un élément dans la liste
print(f"Comptage de l'element 'banane' dans Liste N°1 : nomListe1.count('banane') \n "
      f"=> {nomListe1.count('banane')} \n"
      f"Comptage de l'element 5 dans Liste N°2 : nomListe2.count(5) \n "
      f"=> {nomListe2.count(5)} \n")

# La methode copy() : permet de créer une copie superficielle de la liste
nomListe3 = nomListe1.copy()
nomListe4 = nomListe2.copy()

print(f"Copie de Liste N°1 vers Liste N°3 : nomListe3 = nomListe1.copy() \n "
      f"=> {nomListe3} \n"
      f"Copie de Liste N°2 vers Liste N°4 : nomListe4 = nomListe2.copy() \n "
      f"=> {nomListe4} \n")

# La methode reverse() : permet d'inverser l'ordre des éléments dans la liste
nomListe1.reverse()
nomListe2.reverse()

print(f"Inversion de Liste N°1 : nomListe1.reverse() \n "
      f"=> {nomListe1} \n"
      f"Inversion de Liste N°2 : nomListe2.reverse() \n "
      f"=> {nomListe2} \n")

# La methode sort() : permet de trier la liste en place par ordre croissant
nomListe1.sort(key=len, reverse=False)
nomListe2.sort()

print(f"Tri croissant (de mots) de Liste N°1 : nomListe1.sort(key=len, reverse=False) \n "
      f"=> {nomListe1} \n"
      f"Tri croissant de Liste N°2 : nomListe2.sort() \n "
      f"=> {nomListe2} \n")

# La fonction sorted() : permet de trier une liste dans une autre sans modifier l'originale
nomListe5 = sorted(nomListe1, key=len, reverse=False)
nomListe6 = sorted(nomListe2)

print(f"Tri croissant (de mots) de Liste N°5 : nomListe5 = sorted(nomListe1, key=len, reverse=False) \n "
      f"=> {nomListe5} \n"
      f"Tri croissant de Liste N°6 : nomListe6 = sorted(nomListe2) \n "
      f"=> {nomListe6} \n")


# La methode del() : permet de supprimer un élément à une position donnée
del nomListe1[0]
del nomListe2[-1]

print(f"Suppression de l'element à la première position de Liste N°1 : del nomListe1[0] \n "
      f"=> {nomListe1} \n"
      f"Suppression de l'element à la dernière position de Liste N°2 : del nomListe2[-1] \n "
      f"=> {nomListe2} \n")

# La methode len() : permet d'obtenir le nombre d'éléments dans la liste
print(f"Longueur de Liste N°1 : len(nomListe1) \n "
      f"=> {len(nomListe1)} \n"
      f"Longueur de Liste N°2 : len(nomListe2) \n "
      f"=> {len(nomListe2)} \n")

# La methode max() : permet d'obtenir l'élément le plus grand dans la liste
print(f"Element le plus grand de Liste N°1 : max(nomListe1) \n "
      f"=> {max(nomListe1)} \n"
      f"Element le plus grand de Liste N°2 : max(nomListe2) \n "
      f"=> {max(nomListe2)} \n")

# La methode min() : permet d'obtenir l'élément le plus petit dans la liste
print(f"Element le plus petit de Liste N°1 : min(nomListe1) \n "
      f"=> {min(nomListe1)} \n"
      f"Element le plus petit de Liste N°2 : min(nomListe2) \n "
      f"=> {min(nomListe2)} \n")

# La methode sum() : permet de calculer la somme des éléments de la liste (pour les listes numériques)
print(f"Somme des elements de Liste N°2 : sum(nomListe2) \n "
      f"=> {sum(nomListe2)} \n")

# La methode any() : permet de vérifier si au moins un élément de la liste satisfait une condition
print(f"A-t-on au moins un element 'orange' dans Liste N°1 : any(x == 'orange' for x in nomListe1) \n "
      f"=> {any(x == 'orange' for x in nomListe1)} \n"
      f"A-t-on au moins un element 5 dans Liste N°2 : any(x == 5 for x in nomListe2) \n "
      f"=> {any(x == 5 for x in nomListe2)} \n")

# La methode clear() : permet de supprimer tous les éléments d'une liste
nomListe1.clear()
nomListe2.clear()

print(f"Vidage de Liste N°1 : nomListe1.clear() \n "
      f"=> {nomListe1} \n"
      f"Vidage de Liste N°2 : nomListe2.clear() \n "
      f"=> {nomListe2} \n")
