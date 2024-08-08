# Exercices : Les Operateurs sur les listes
L1 = list(range(1,10,4))
print(f"L1 = list(range(1,10,4)) donne {L1} \n")

L2 = list(range(2, 16, 5))
print(f"L2 = list(range(2, 16, 5)) donne {L2} \n")

L3 = L1 + L2
print(f"L1 + L2 donne L3 = {L3} \n")

L4 = L1 * 2
print(f"L1 * 2 donne L4 = {L4} \n")

print(L4 == L3, "\n")

L3[-3:-1] = [1, 5, 9]
print(f"L3[-3:-1] = [1, 5, 9] donne L3 = {L3} \n")

L4[1:5] = [4, 5] * 2 + L1[::-1]
print(f"L4[1:5] = [4, 5] * 2 + L1[::-1] donne L4 = {L4} \n")

L5 = list(range(0, 5, 3)) + L2 * 3
print(f"L5 = list(range(0, 5, 3)) + L2 * 3 donne L5 = {L5} \n")

print(L5 <= L3)