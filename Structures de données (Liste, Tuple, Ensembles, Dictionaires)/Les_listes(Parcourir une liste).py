# Parcourir une liste en python (B N b n {} [] = \)
# Soit les deux tableaux suivants :
A = ['Cheikh', 'Oumar', 'Fatima', 'Astou', 'Babacar', 'Saliou', 'Maoudo']
B = [12, 16, 10, 18, 20, 11, 15]

# Parcourir une liste avec: (for)
for a in A:
    print(a, "\n")

# Parcourir une liste avec: (for, range() & len())
for b in range(len(B)):
    print(f"La Note de l'étudiant N°{b + 1} est : {B[b]} \n")

# Parcourir une liste avec: (for & enumerate())
for id, nom in enumerate(A, start=1):
    print(f"Le nom de l'étudiant N°{id} est : {nom} \n")

# Parcourir plusieur listes avec: (for & zip())
for a, b in zip(A, B):
    print(f"L'étudiant {a} a eu la note de : {b} \n")
