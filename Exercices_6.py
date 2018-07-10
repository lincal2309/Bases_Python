#1 Vérifier que le nombre saisi est un entier

user_nb_int = False

while user_nb_int == False:
    user_nb = input("Entrez un nombre entier : ")
    try:
        user_nb = int(user_nb)
        print("Correct !")
        user_nb_int = True
    except ValueError:
        print("Ce nombre n\'est pas un entier, merci d\'essayer à nouveau")


input("\nAppuyer sur une touche passer à l'exercice 2")
