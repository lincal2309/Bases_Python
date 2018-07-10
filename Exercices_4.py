# Exercices sur les fonctions

#1 fonction qui prends un nombre en paramètre et le multiplie par 5. Afficher le résultat
def multiplication_5(nb):
    return nb * 5

#2 fonction qui prend une liste de nombres en paramètre et qui retourne tous les nombres pairs
def extract_even_nb(list_nb):
    list_even = []
    for nb in list_nb:
        if nb % 2 == 0:
            list_even.append(nb)
    return list_even

#3 suite de fibonacci, et prend en paramètre un nombre. La fonction n'ira pas plus loin que ce nombre
def fibonacci_suite(max_nb):
    a = 0
    b = 1
    print(a)
    print(b)
    while a + b < max_nb:
        print(a+b)
        a , b = b, a + b

#4-1 Fonction qui compte les voyelles avec boucle For
def nb_voyelles_for(chaine):
    liste_voyelles = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    nb_voyelles = 0
    for char in chaine:
        if char in liste_voyelles:
            nb_voyelles += 1
    return nb_voyelles
        
#4-2 Fonction qui compte les voyelles avec boucle While
def nb_voyelles_while(chaine):
    liste_voyelles = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    cpt_char = 0
    nb_voyelles = 0
    while cpt_char < len(chaine):
        if chaine[cpt_char] in liste_voyelles:
            nb_voyelles += 1
        cpt_char += 1
    return nb_voyelles

#4-3 Fonction qui compte les voyelles avec string
def nb_voyelles_str(chaine):
    liste_voyelles = "aeiouyAEIOUY"
    cpt_char = 0
    nb_voyelles = 0
    for char in chaine:
            if char in liste_voyelles:
                nb_voyelles += 1
    return nb_voyelles

#5 fonction qui retourne la factorielle d'un nombre passé en argument
def fact(nb):
    fact_nb = cpt_nb = nb
    while cpt_nb > 1:
        cpt_nb -= 1
        fact_nb *= cpt_nb
    return fact_nb

#6 Factorielle avec fonction récurrente


#7 Fonction à nombre variable d'arguments
def somme_arg(*args):
    nb_arg = len(args)
    somme_args = cpt_args = 0
    while cpt_args < nb_arg:
        somme_args += args[cpt_args]
        cpt_args += 1
    print("Il y a", nb_arg, "arguments dont la somme fait", somme_args)

#8 Compter le nombre d'apparition d'un chiffre en 1er caractère d'une liste de nombres
def extract_first_digit(nb):
    str_nb = str(nb)
    first_digit = int(str_nb[0])
    return first_digit

def count_first_digits(my_list):
    stats_digits = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for item in my_list:
        f_dgt = extract_first_digit(item)
        if f_dgt in stats_digits:
            stats_digits[f_dgt] += 1
    return stats_digits
        

# ============ Fin déclaration des fonctions  ================

print("\nExercice 1 : ")
user_nb = float(input("Entrer un nombre : "))
print(multiplication_5(user_nb))

input("\nAppuyer sur une touche passer à l'exercice 2")

print("\nExercice 2 : ")
ma_liste = [1, 2, 5, 6, 12, 37, 50, 72, 43]
print("Liste complète :", ma_liste)
print("Nombres pairs de la liste :", extract_even_nb(ma_liste))

input("\nAppuyer sur une touche passer à l'exercice 3")

print("\nExercice 3 : ")
nb_max = int(input("Entrée un entier strictement positif : "))
fibonacci_suite(nb_max)

input("\nAppuyer sur une touche passer à l'exercice 4")

print("\nExercice 4 : ")
chaine_test = "Bienvenue en Occitanie"
print("Chaîne de caractères :", chaine_test)
print("Méthode FOR :", nb_voyelles_for(chaine_test), "voyelles")
print("Méthode WHILE :", nb_voyelles_while(chaine_test), "voyelles")
print("Méthode avec STRING :", nb_voyelles_str(chaine_test), "voyelles")

input("\nAppuyer sur une touche passer à l'exercice 5")

print("\nExercice 5 : ")
user_nb = int(input("Entrée un entier strictement positif : "))
print("Factorielle", user_nb, "=", fact(user_nb))

input("\nAppuyer sur une touche passer à l'exercice 7")

print("\nExercice 7 : ")
print("liste des valeurs : 1, 5, 12, 22")
somme_arg(1, 5, 12, 22)

input("\nAppuyer sur une touche passer à l'exercice 8")

print("\nExercice 8 : ")
liste_demo = [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]
print(count_first_digits(liste_demo))