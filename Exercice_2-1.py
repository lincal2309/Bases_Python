# Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est nul, négatif ou positif.

nb1 = float(input("Saisissez un premier nombre : "))
nb2 = float(input("Saisissez un second nombre : "))

if (nb1 * nb2) > 0:
    print("Le produit des 2 nombres est positif")
elif (nb1 * nb2) < 0:
    print("Le produit des 2 nombres est négatif")
else:
    print("Le produit des 2 nombres est nul")
