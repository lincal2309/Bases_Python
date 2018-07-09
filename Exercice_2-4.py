# Demander un nombre et indiquer s'il est compris entre 5 et 10 (strictement)

nb = int(input("Saississez un nombre entier strictement compris entre 5 et 10 : "))

if nb > 5 and nb < 10:
    print("Correct !")
else:
    print("Erreur, ce nombre n'est pas strictement compris entre 5 et 10")
