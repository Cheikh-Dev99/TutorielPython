# Exercices sur les

'''-----------------------------------------------------------------------------------------'''
# Exercice 1: Ecrire un programme qui a partir d'une liste nommée 'L'
            # constituer des lettres de la langue française qui affiche le prenom et nom (cheikh gueye)
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(f"{L[2]}{L[7]}{L[4]}{L[8]}{L[10]}{L[7]} {L[6]}{L[20]}{L[4]}{L[24]}{L[4]}")
'''-----------------------------------------------------------------------------------------'''
# Exercice 2 : Ecrire u programme qui vous permet de :
    # 1. Cree un liste "semaine"
    # 2. Proposer deux methodes pour afficher le premier jour de la semaine
    # 3. Proposer deux methodes pour afficher les jour de week-end

semaine = ['lundi', 'mardi','mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

'''Affichage 1er jour de la semaine'''
print(f"1er methode : {semaine[0]}")
print(f"2nd methode : {semaine[-7]}")

'''Affichage 1er jour du week-end'''
print(f"1er methode : {semaine[5], semaine[6]}")
print(f"2nd methode : {semaine[-2], semaine[-1]}")

'''-----------------------------------------------------------------------------------------'''
# Exercice 3 : Ecrire u programme qui vous permet de :
    # 1. Demader à l'utilisateur d'etrer un nombre positif N
N = int(input("Entrez un nombre positif : "))
while N < 1:
    N = int(input("Veuillez entrer un nombre positif : "))
    # 2. Affiche la serie de nombre de 1 à N
L1 = list(range(1, N + 1))
print(f"La serie de nomre entre 1 & {N} est : {L1}")
    # 3. Affiche la serie de nombre pairs entre 1 et N
L2 = list(range(2, N+1, 2))
print(f"La serie de nombres pairs entre 1 et {N} est : {L2}")
    # 4. Affiche la serie de nombre impairs entre 1 et N
L3 = list(range(1, N+1, 2))
print(f"La serie de nombres impairs entre 1 et {N} est : {L3}")
