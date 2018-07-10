# Exercice 12

prix_ht = float(input("Indiquez le prix HT de l\'article :\n"))
nb_art = float(input("Indiquez le nombre d\'articles : \n"))

tva = 0.20

print("Le prix TTC total est de :", prix_ht * (1 + tva) * nb_art, "€")
