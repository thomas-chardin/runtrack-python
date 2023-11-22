def pair_ou_impair(nombre):
    if type(nombre) == int and nombre > 0:
        if nombre % 2 == 0:
            print("pair")
        else:
            print("impair")
    else:
        print("veuillez mettre un chifrre positif et entier")
        
pair_ou_impair(10)
pair_ou_impair(-10)