from random import *
from math import *

argent = 1000 
continuer_partie = True

print(" ")
print("Vous voilà installez à la roulette du LDLCasino avec", argent, "€.")
print(" ")

#Case du joueur

while continuer_partie: 
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 36:
        nombre_mise = input("Renseignez votre case de jeu (0 -> 36) : ")
        print(" ")
        try:
            nombre_mise = int(nombre_mise)
        except:
            print("Vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Ce nombre est négatif ...")
        if nombre_mise > 36:
            print("Ce nombre est supérieur à 36 ...")

#Mise du joueur

    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Renseignez le montant de votre mise : ")
        print(" ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "€")

#Gestion des gains

    numero_gagnant = randrange(37)
    print("La roulette tourne ...")
    print("Elle s'arrête sur le numéro", numero_gagnant)
    print(" ")

    if numero_gagnant == nombre_mise:
        print("GG ! Vous obtenez", mise * 3, "€")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2:
        mise = ceil(mise * 0.5)
        print("C'est la bonne couleur. Vous obtenez", mise, "€")
        argent += mise
    else:
        print("WP, mais ce ne sera pas pour cette fois. Vous perdez votre mise.")
        print(" ")
        argent -= mise

#Gestion du replay/leave

    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        print(" ")
        replay = str(input("Souhaitez-vous recommencer à jouer (o/n) ? "))
        print(" ")
        if replay == "O" or replay == "o":
            print("Une nouvelle partie ... commence !")
            print(" ")
            argent = 1000
        else:
            print("")
            print("À bientôt au LDLCasino !")
            continuer_partie = False
    else:
        print("Vous avez à présent", argent, "€")
        print(" ")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        print(" ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False
        else:
            print("Vous faites partie des courageux, vous continuez à miser !")
            print(" ")