montant_initial = 11000
taux_rendement_annuel = 0.02
gain_annuel = taux_rendement_annuel*montant_initial
# mise en place des variables de base
montant_total = montant_initial+gain_annuel
print(montant_total)
# valeur initial apres 1 ans
montant_initial += 5000
taux_rendement_annuel += 0.02
nouveau_gain_annuel = taux_rendement_annuel*montant_initial
# mise a jour du capital du taux de rendement et du gain annuel
print(nouveau_gain_annuel)
# on calcule la nouvelle valeur des gains a l'année
montant_total = montant_initial+nouveau_gain_annuel
# montant total contient la valeur de tout le compte
retrait = 0.10 * montant_total
# on stock la valeur des 10% dans la var retrait
montant_initial -= retrait
print(montant_initial)
# mise a jour du compte apres le retrait de 10%
taux_rendement_annuel -= 0.01
# on diminue le rendement de 1%
montant_final = montant_initial + nouveau_gain_annuel
nouveau_gain = taux_rendement_annuel*montant_final
print(nouveau_gain)