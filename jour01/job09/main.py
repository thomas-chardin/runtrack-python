produit = "baguette"
prix = 1
stock = 10
print("produit:", produit)
print("prix:", prix)
print("stock:", stock)
quantite_achat = int(input("Veuillez mettre la quantité a acheter : "))
stock += quantite_achat
prix *= 1.1
print("\nAprès l'achat et l'ajustement du prix :")
print("produit:", produit)
print("prix (après inflation):", prix)
print("stock:", stock)
