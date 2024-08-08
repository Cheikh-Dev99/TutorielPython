# Opérateur sur les liste e python
L1 = [2, 7, 24, 10]
L2 = [15, 2, -6, 45]
L3 = L1 + L2
print(f"L1 = {L1}")
print(f"L2 = {L2}")
print(f"La concatenation de L1 et L2 donne L = {L3}\n")

# Affectation des éléments au variales
moi = ["John Doe", 2004, 1.75]
# 1er methode
nom = moi[0]
date = moi[1]
taille = moi[2]

print(f"moi = {moi}")
print(f"Mon nom est {nom}, je suis né en {date} et mon poids est de {taille} m \n")

#2 eme methode
elle = ["Janne Doe", 2000, 1.65]
nom2, date2, taille2 = elle

print(f"elle = {elle}")
print(f"Son nom est {nom2}, elle est né en {date2} et elle pèse {taille2} m \n")




# Affectation des éléments au variales - Decoupage
moi[:1] = ["Cheikh Gueye"]
moi[-2:] = [1999, 1.85]
print(f"Apres affectation le tableau (moi) est : {moi}")

moi[:] = []
print(f"{moi}")
