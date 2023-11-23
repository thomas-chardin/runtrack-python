def tri_a_bulles(liste):
    n = 0
    for tpm in liste:
        n += 1
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
            j += 1
        i += 1
test = [64, 34, 25, 12, 22, 11, 90]
tri_a_bulles(test)
print(test)