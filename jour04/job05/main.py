def remplace(liste, index):
    somme = liste[index - 1] + liste[index + 1]
    liste[index] = somme

L = [1, 2, 3, 4, 5]
print(L)
print(L[1])
remplace(L, 3)
print(L)
print(L[-1])

