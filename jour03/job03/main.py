def Add(num1 , num2):
    if type(num1) == int and type(num2) == int :
        resultat = num1 + num2
        print(resultat)
    else :
        print("les parametres doivent etre des nombres entier")

Add(1 , 3)