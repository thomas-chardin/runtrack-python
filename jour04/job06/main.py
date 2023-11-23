test = [1, 2, 3, 4, 5]

def echange():
    print(test)
    test[0],test[4] = test[4], test[0]
    print(test)

echange()
