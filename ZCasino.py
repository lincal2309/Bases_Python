from math import ceil
from random import randrange

def numero_pair(numero):
    """Indique si le nombre en entrée est pair ou pas
    Retourne un booléen qui est True si le nombre est pair """
    pair = False
    if numero % 2 == 0:
        pair = True
    return pair

def roulette(numero):
    """Fonction définissant le résultat du trage de la roulette
    Retourne le gain obtenu"""
    gain = 0
    tirage = randrange(50)
    if  tirage == numero:
        gain = 4
    elif numero_pair(numero) == numero_pair(tirage):
        gain = 1.5
    return gain
    
numero_valide = False

while numero_valide == False:
    try:
        numero_mise = input("Misez sur un numro entre 0 et 49 : ")
        montant_mise = input("Quel montant souhaitez-vous miser ? ")
        numero_mise = int(numero_mise)
        montant_mise = float(montant_mise)
        numero_valide = True
    except ValueError:
        print("Choisissez un numéro entier et une mise numérique")

resultat = roulette(numero_mise)
if resultat == 0:
    print("Vous avez perdu !")
else:
    print("Bravo ! Vous avez gagné", ceil(montant_mise * resultat), "$ !")


