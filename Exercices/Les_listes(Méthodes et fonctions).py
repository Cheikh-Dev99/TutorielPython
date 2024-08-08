# Exercices sur les Méthodes et fonctions de liste

# Exercice 1 : Ecrire un programme qui permet de :
# 1. Créer une liste (P) qui contient les 5 pays suivants : Mali, Guinée, Maroc, Sénégal, France
# 2. Demander à l'utilisateur de choisir deux de ces 5 pays.
# 3. Ajouter les instructions nécessaires pour effectuer l'échange des positions de ces deux pays dans la liste P.

# Création de la liste
P = ['Mali', 'Guinée', 'Maroc', 'Senegal', 'France']

print("Soit la liste suivante : \n"
      "P = ['Mali', 'Guinée', 'Maroc', 'Senegal', 'France'] \n")

# Demande à l'utilisateur de choisir deux pays de la liste
pays1 = input("Choisissez un 1er pays de la liste : ").strip().lower()
pays2 = input("Choisissez un 2ème pays de la liste : ").strip().lower()

# Création d'une version de la liste en minuscules pour la comparaison
P_lower = [p.lower() for p in P]

# Vérification de la présence des pays dans la liste
if pays1 in P_lower and pays2 in P_lower:
    # Obtention des index des pays choisis
    index1 = P_lower.index(pays1)
    index2 = P_lower.index(pays2)

    # Échange des positions des pays dans la liste originale
    P[index1], P[index2] = P[index2], P[index1]

    # Affichage du résultat après échange
    print(f"Les pays ont été échangés avec succès : \n"
          f"P = {P} \n")
else:
    print("Un ou les deux pays choisis ne sont pas dans la liste.\n")

'''--------------------------------------------------------------------------------'''
'''
Le professeur de mathématique enseigne à 5 élèves les matières d'analyse, 
d'algèbre, de probabilité et de statistique. 
Le tableau suivant représente les notes de chacun des élèves dans chaque matière.
'''

# Exercice 2 : Ecrire un programme qui permet de :
# 1. Cree 4 listes pour 4 matières
# 2. Calcule la somme et la moyenne de toutes les notes dans 4 matières
# 3. Détrminer la note maximal et minimale parmi toutes les notes dans les 4 matières

analyse = [10, 12, 9, 10, 15]
algebre = [0, 13, 10, 10, 19]
probabilite = [10, 15, 16, 10, 20]
statistique = [11, 17, 14, 10, 18]

S = sum(analyse + algebre + probabilite + statistique)
M = S / len(analyse + algebre + probabilite + statistique)
Max = max(analyse + algebre + probabilite + statistique)
Min = min(analyse + algebre + probabilite + statistique)

print(f"La somme des notes est de {S} \n"
      f"La moyenne des notes est de : {M} \n"
      f"La note maximale est de : {Max} \n"
      f"La note minimale est de : {Min} \n")

'''--------------------------------------------------------------------------------'''

# Exercice 3 : Écrire un programme qui vérifie si un mot est palindrome ou non.

# 1er methode :
while True:
    mot = input("Veuillez saisir un mot (ou tapez 'exit' pour quitter) : ").strip()

    if mot.lower() == 'exit':
        print("Programme terminé.")
        break
    # Vérifier si l'entrée contient uniquement des lettres
    if not mot.isalpha():
        print("Veuillez entrer un mot valide contenant uniquement des lettres.")
        continue
    if len(mot) <= 2:
        print("Veuiller saisir un mot de plus de 3 lettres")
        continue

    # Créer une liste pour le mot
    L = list(mot)
    # Créer une copie de la liste pour ne pas modifier la liste originale
    P = L.copy()
    # Inverser la liste pour vérifier si le mot est un palindrome
    L.reverse()

    if P == L:
        print(f"'{mot}' est un palindrome.")
    else:
        print(f"'{mot}' n'est pas un palindrome.")

# 2eme methode :
while True:
    mot = input("Veuillez saisir un mot (ou tapez 'exit' pour quitter) : ").strip()

    if mot.lower() == 'exit':
        print("Programme terminé.")
        break
    # Vérifier si l'entrée contient uniquement des lettres
    if not mot.isalpha():
        print("Veuillez entrer un mot valide contenant uniquement des lettres.")
        continue
    if len(mot) <= 2:
        print("Veuiller saisir un mot de plus de 3 lettres")
        continue

    if mot == mot[::-1]:
        print(f"{mot} est un palindrome.")
    else:
        print(f"{mot} n'est pas un palindrome.")

'''--------------------------------------------------------------------------------'''

# Exercice 4 : Ecrire un programme sans utiliser la fonction max qui détermine le mot le plus long dans une liste de mots

language = ['C++', 'PHP', 'Java', 'Python', 'C#']
print(f"language = {language} \n ")

language.sort(key=len, reverse=True)
print(f"Le mot le plus long de la liste est : {language[0]}")
