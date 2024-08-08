# Exercice 1 : Soit les trois listes suivantes :
L = ['C#', 'C++', 'Java', 'PHP', 'Python']
D = [2000, 1980, 1995, 1994, 1991]
C = ['Microsoft', 'Bjarne Stroustrup', 'Sun Microsystèms', 'Rasmus Lerdorf', 'Guido Van Rossum']

# Parcourer et afficher les elements des trois liste en meme temps avec for & Zip()
for language, date, createur in zip(L, D, C):
    print(f"=> {language} a étè crée en {date} par {createur} \n")

# --------------------------------------------------------------------------------------------
print("\n\n")
# Exercice 2 : ecrireun programme sui peut demander à l'utilisateur d'entrer les notes des
# étudiant, puis le programme affiche la liste des notes des etudiants

Notes = []
n = int(input("Quel est le nombre d'etudiant : "))

for i in range(n):
    note = float(input(f"Entrer la note de l'étudiant {i+1} : \n"))
    Notes.append(note)

for id, note in enumerate(Notes, start=1):
    print(f"La note de l'étudiant N°{id} est : {note}")

# --------------------------------------------------------------------------------------------
print("\n\n")
# Exercice 3 : Un programme qui demande à l'utilisateur de saisir une valeur x et de remplire
# une liste L avec 5 éléments. Ensuite le programme vérifie si la valeur x existe dans L ou non

# Demande de la valeur à l'utilisateur
x = int(input("Entrer une valeur : "))

# Initialisation de la liste
L = []

# Boucle pour remplir la liste avec 5 éléments
for i in range(5):
    valeur = int(input(f"Entrer l'élément {i + 1} de la liste : "))
    L.append(valeur)

# Vérification de l'existence de x dans L
if x in L:
    index = L.index(x)
    print(f"La valeur {x} existe dans la liste à l'index {index}.")
else:
    print(f"La valeur {x} n'existe pas dans la liste.")

# --------------------------------------------------------------------------------------------
print("\n\n")
# Exercice 4 : Écrire un programme qui demande à l'utilisateur
# de remplireune liste L avec 5 éléments. Ensuite, sans utiliser la fonction max, le programme
# determine et affiche le nombre maximum de la liste

# Initialisation de la liste N
N = []

# Remplir la liste avec 5 éléments saisis par l'utilisateur
for i in range(5):
    valeur = int(input(f"Entrer l'élément {i + 1} de la liste : "))
    N.append(valeur)

# Initialisation de la variable pour stocker le nombre maximum
max_valeur = N[0]

# Parcourir la liste pour trouver le nombre maximum
for valeur in N:
    if valeur > max_valeur:
        max_valeur = valeur

# Affichage du nombre maximum
print(f"Le nombre maximum de la liste est : {max_valeur}")

# --------------------------------------------------------------------------------------------
print("\n\n")
# Exercice 4 : Écrire un programme qui demande à un enseignant de 
# 1. rempir trois listes (Noms, Notes1 & Notes2)

# Initialisation des listes
Noms = []
Notes1 = []
Notes2 = []

# Demander le nombre d'élèves
nombre_eleves = int(input("Entrez le nombre d'élèves: "))

# Remplir les listes avec les informations des élèves
for i in range(nombre_eleves):
    nom = input(f"Entrer le nom de l'élève {i + 1}: \n")
    note1 = float(input(f"Entrer la première note pour {nom}: "))
    note2 = float(input(f"Entrer la deuxième note pour {nom}: "))

    Noms.append(nom)
    Notes1.append(note1)
    Notes2.append(note2)

# Afficher les listes pour vérifier les entrées
for N, n1, n2 in zip(Noms, Notes1, Notes2):
    print(f"\n=> {N} a comme note {n1} et {n2} \n")
