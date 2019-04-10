from math import *

# Valeur de change des monnaies
EUR_TO_DOL_CHANGE_RATE = 1.13788
EUR_TO_YEN_CHANGE_RATE = 128.096

DOL_TO_EUR_CHANGE_RATE = 0.87865
DOL_TO_YEN_CHANGE_RATE = 112.501

YEN_TO_EUR_CHANGE_RATE = 0.00780
YEN_TO_DOL_CHANGE_RATE = 0.00887

KIL_TO_MIL = 0.621371
MIL_TO_KIL = 1.60934


# Euro à Dollar
def eur2dol(eur_value):
    return round(eur_value * EUR_TO_DOL_CHANGE_RATE, 2)


# Euro à Yen
def eur2yen(eur_value):
    return round(eur_value * EUR_TO_YEN_CHANGE_RATE, 2)


# Euro à tout
def eur2all(eur_value):
    print("Cela fait donc", eur2dol(eur_value), "en dollars !")
    print("Cela fait donc", eur2yen(eur_value), "en yens !")


# Dollar à Euro
def dol2eur(dol_value):
    return round(dol_value * DOL_TO_EUR_CHANGE_RATE, 2)


# Dollar à Yen
def dol2yen():
    return round(dol_value * DOL_TO_YEN_CHANGE_RATE, 2)


# Dollar à tout
def dol2all(dol_value):
    print("Cela fait donc", dol2eur(dol_value), "en euros !")
    print("Cela fait donc", dol2yen(dol_value), "en yens !")


# Yen à Euro
def yen2eur(yen_value):
    return round(yen_value * YEN_TO_EUR_CHANGE_RATE, 2)


# Yen à Dollar
def yen2dol(yen_value):
    return round(yen_value * YEN_TO_DOL_CHANGE_RATE, 2)


# Yen à tout
def yen2all(yen_value):
    print("Cela fait donc", yen2eur(yen_value), "en euros !")
    print("Cela fait donc", yen2dol(yen_value), "en dollars !")


# Kilomètre
def kilo2all(kilo_value):
    return round(kilo_value * KIL_TO_MIL, 2)


# Miles
def mile2all(mile_value):
    return round(mile_value * MIL_TO_KIL, 2)


# Celsius à Fahrenheit
def cel2far(cel_value):
    return round((cel_value * 9 / 5) + 32, 2)


# Fahrenheit à Celsius
def far2cel(far_value):
    return round((far_value - 32) * 5 / 9, 2)


# Décimal à Binaire
def dec2bin(value):
    digits = []
    while value > 0:
        digits.append(value % 2)
        value = value // 2
    digits.reverse()
    ret_value = "".join([str(d) for d in digits])
    return ret_value


# Binaire à Décimal
def bin2dec(value):
    result = 0
    for i in range(len(value)):
        char = int(value[i])
        if char == 1:
            result += 2 ** (len(value) - 1 - i)
    return result


# Boucle pour permettre utilisateur de convertir plusieurs nombres
while True:

    # INIT OUTPUT VALUE
    output_value = -1
    # Choix du convertisseur
    menu = int(input("Quel convertisseur veux-tu utiliser ?\n1: Devise\n2: Distance\n3: Température\n4: Décimal \n"))
    if menu == 1:
        # Demande à l'utilisateur le type de monnaie qu'il souhaite convertir
        choice = int(input("Que veux-tu rentrer comme première valeur ?\n1: Euro\n2: Dollar\n3: Yen \n"))
        input_value = float(input("Choisissez votre valeur d'entrée : \n"))

        # Choix Euro
        if choice == 1:
            current = int(input("Pour le convertir en quoi ?\n1: Dollar\n2: Yen\n3: Tout\n"))
            if current == 1:
                output_value = eur2dol(input_value)
            elif current == 2:
                output_value = eur2yen(input_value)
            elif current == 3:
                output_value = eur2all(input_value)

        # Choix Dollar
        elif choice == 2:
            current = int(input("Pour le convertir en quoi ?\n1: Euro\n2: Yen\n3: Tout\n"))
            if current == 1:
                output_value = dol2eur(input_value)
            elif current == 2:
                output_value = dol2yen(input_value)
            elif current == 3:
                output_value = dol2all(input_value)

        # Choix Yen
        elif choice == 3:
            current = int(input("Pour le convertir en quoi ?\n1: Euro\n2: Dollar\n3: Tout\n"))
            if current == 1:
                output_value = yen2eur(input_value)
            elif current == 2:
                output_value = yen2dol(input_value)
            elif current == 3:
                output_value = yen2all(input_value)

    if menu == 2:
        # Demande à l'utilisateur le type d'unité de mesure qu'il souhaite utiliser
        choice = int(input("Que veux-tu rentrer comme première mesure ?\n1: Kilomètre\n2: Mile\n"))
        input_value = float(input("Choisissez votre valeur d'entrée : \n"))
        if choice == 1:
            output_value = kilo2all(input_value)
        elif choice == 2:
            output_value = mile2all(input_value)

    if menu == 3:
        # Demande à l'utilisateur le type d'unité de température qu'il souhaite utiliser
        choice = int(input("Que veux-tu rentrer comme première mesure ?\n1: Celsius\n2: Fahrenheit \n"))
        input_value = float(input("Choisissez votre valeur d'entrée : \n"))
        if choice == 1:
            output_value = cel2far(input_value)
        elif choice == 2:
            output_value = far2cel(input_value)

    if menu == 4:
        choice = int(input("Que veux tu rentrer comme première unité ?\n1: Décimal\n2: Binaire\n"))
        input_value = float(input("Choisissez votre valeur d'entrée : \n"))
        if choice == 1:
            output_value = dec2bin(input_value)
        elif choice == 2:
            output_value = bin2dec(input_value)

    # SHOW OUTPUT
    if (output_value != -1):
        print("Cela fait donc : ", output_value)
    else:
        print("Mauvais Choix")
    # MAKE SOME SPACE
    print("\n\n")




