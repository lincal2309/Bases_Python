# ======= Les Boucles FOR ========

#1 Afficher les chiffres de 0 à 5
my_list = [0, 1, 2, 3, 4, 5]
for item in my_list:
    print(item)

input("\nAppuyer sur une touche passer à l'exercice 2...\n")

#2 Liste de mots, nombre de caractères e chaque mot
my_list = ["Chien", "Eléphant", "Crocodile"]
for item in my_list:
    print("Le mot", item, "est composé de", len(item), "caractères.")

input("\nAppuyer sur une touche passer à l'exercice 3...\n")

#3 Afficher toutes les lettres d'un mot
x = "anticonstitutionnellement"
for char in x:
    print(char)

input("\nAppuyer sur une touche passer à l'exercice 4...\n")

#4 Afficher tous les nombres d'une liste
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for elt in x:
    for item in elt:
        print(item)

input("\nAppuyer sur une touche passer à l'exercice 5...\n")

#5 Calculer la somme d'éléments d'une liste
x = [1,10,20,30,40,50]
a = 0
for value in x:
    a += value
print("Méthode 1 - boucle For - LA sommes des éléments est :", a)

x_len = len(x)
b = 0


input("\nAppuyer sur une touche passer à l'exercice 6...\n")

