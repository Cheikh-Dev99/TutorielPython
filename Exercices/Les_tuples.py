# Exercice 1 :
#   1. Demander à l'utiilisateur d'entrer un nombre positif.
N = int(input(" \nEntrer un nombre (N) positifs : "))

#   2. Afficher la serie de nombre de 1 à N
print(f"\n La serie de nombre de 1 jusqu'a {
      N} est la suivante: {tuple(range(1, N + 1))} ")

#  3. Afficher la serie de nombres pairs entre 1 et N
print(f"\n La serie de nombres pairs entre 1 et {
      N} est la suivante : {tuple(range(2, N + 1, 2))}")

#  3. Afficher la serie de nombres impairs entre 1 et N
print(f"\n La serie de nombres impairs entre 1 et {
      N} est la suivante : {tuple(range(1, N + 1, 2))}")
