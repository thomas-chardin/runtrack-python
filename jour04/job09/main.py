def recuperation():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    max = L[0]
    min = L[0]
    for n in L:
        if n > max:
            max = n
    print("La valeur max est :",max)
    for x in L:
        if x < min:
            min = x    
    print("La valeur min est :",min)
recuperation()