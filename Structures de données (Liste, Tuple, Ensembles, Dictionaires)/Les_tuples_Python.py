# Créer & Comprendre des Tuples en Python

# Creation d'un tuple : Tuple vide
T = ()

# Creation d'un tuple : 1ere methode
T1 = ('A', 'b', 'c', 'D', 'e')

# Creation d'un tuple : 2eme methode
T2 = 1, 2, -3, 4, 5

# Creation d'un tuple : avec un seul element
T3 = ("Pomme")

# Creation d'un tuple : avec une fonction tuple()
T4 = tuple(('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

# Creation d'un tuple : avec une fonction tuple()
T5 = tuple(('Cheikh', True, 3.25, 22/7))

# Creation d'un tuple : avec une fonction tuple() & range()
T6 = tuple(range(2, 17, 2))

# Afficher les tuples
# print(f"\n => Mon_Tuple = {T} \n")

# Afficher les tuples - Decoupage
print(f"\n => Mon_Tuple = {T4[0:10]}")
print(f"\n => Mon_Tuple = {T4[10:]}")
print(f"\n => Mon_Tuple = {T4[0::3]}")
print(f"\n => Mon_Tuple = {T4[-3::-3]}")
print(f"\n => Mon_Tuple = {T4[::-1]}")
print(f"\n => Mon_Tuple = {T4[1:-3]}")
