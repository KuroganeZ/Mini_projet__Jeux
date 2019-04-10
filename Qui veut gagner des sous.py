import time

print("Bienvenue dans le grand quizz de l'école LDLC !")

time.sleep(2)
total = 0
nbQuestions = 2
nom = input("Comment dois-je t'appeler ?")
print("Très bien",nom ,", c'est plutôt un joli nom dis moi !")
time.sleep(1)

begin = input("Est ce que tu es prêt à commencer ? \nOui ou Non")
while True:
    if begin == "Oui" or begin == "y" or begin == "o" or begin == "oui":

        # Question 1

        print("Alors on est parti !")
        print("")
        print("A) Paris")
        print("B) Lyon")
        print("C) Marseille")
        print("D) Perpignan")
        print("")
        question1 = input("Question pour 100€\nQuelle est la capitale de la France ?")
        if question1 == "a" or question1 == "A":
            print("Bien joué !")
            print("")
            total = total + 100
        elif question1 != "a" or question1 != "A":
            print("Oh c'est bien dommage ...")
            print("La réponse était : A ")
            print("Tu repars donc avec rien du tout ! Retente ta chance une prochaine fois !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir =="r" or partir =="R":
            print("On continue alors !")

            # Question 2

            print("")
            print("A) Nintendo")
            print("B) Playstation")
            print("C) Xbox")
            print("D) Dreamcast")
            print("")
        question2 = input("Question pour 200€\nDe quelle console, Mario est-il l'égérie ?")
        if question2 == "a" or question2 == "A":
            print("Bien joué !")
            print("")
            total = total + 100
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : A ")
            print("Tu repars donc avec rien du tout ! Retente ta chance une prochaine fois !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir =="r" or partir =="R":
            print("On continue alors !")

        # Question 3

        print("")
        print("A) Brad Pitt")
        print("B) Bradley Cooper")
        print("C) Tom Cruise")
        print("D) Will Smith")
        print("")
        question3 = input("Question pour 300€\nQuel est l'acteur ayant eu le rôle principal dans Men in Black")
        if question3 == "d" or question3 == "D":
            print("Bien joué !")
            print("")
            total = total + 100
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : D ")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir =="r" or partir =="R":
            print("On continue alors !")

        # Question 4

        print("")
        print("A) Iron man")
        print("B) Very Bad Trip")
        print("C) Bilbo le Hobbit")
        print("D) The Island")
        print("")
        question4 = input("Question pour 500€\nQuel série de film retrace l'histoire du voyage d'un hobbit ?")
        if question4 == "c" or question4 == "C":
            print("Bien joué !")
            print("")
            total = total + 200
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : C ")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir =="r" or partir =="R":
            print("On continue alors !")

        # Question 5

        print("")
        print("A) Salamèche")
        print("B) Pikachu")
        print("C) Tortank")
        print("D) Oulajesaipa")
        print("")
        question5 = input("Question pour 1 000€\nQuel est le nom du premier Pokémon de Sacha")
        if question5 == "b" or question5 == "B":
            print("Bien joué ! Tu as atteint le premier palier !")
            print("")
            total = total + 500
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : B ")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir =="r" or partir =="R":
            print("On continue alors !")

        # Question 6

        print("")
        print("A) Ron Weasley")
        print("B) Voldemort")
        print("C) Hagrid")
        print("D) Professeur Rogue")
        print("")
        question6 = input("Question pour 2 000€\nQui est l'ennemi juré d'Harry Potter dans la saga du même nom ?")
        if question6 == "b" or question6 == "B":
            print("Bien joué !")
            print("")
            total = total + 1000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : B ")
            print("Tu repars tout de même avec 1 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 7

        print("")
        print("A) Tails")
        print("B) Knuckles")
        print("C) Dr. Eggman")
        print("D) Rose")
        print("")
        question7 = input("Question pour 4 000€\nQuel est le nom du meilleur ami de Sonic, dans le jeu éponyme ?")
        if question7 == "a" or question7 == "A":
            print("Bien joué !")
            print("")
            total = total + 2000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : A")
            print("Tu repars tout de même avec 1 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 8

        print("")
        print("A) Parce qu'ils nous volent")
        print("B) Parce qu'ils nous endorment")
        print("C) Parce qu'ils nous font disparaître")
        print("D) Parce qu'ils nous tuent")
        print("")
        question8 = input("Question pour 8 000€\nPourquoi ne faut-il pas cligner des yeux devant un ange pleureur ?")
        if question8 == "d" or question8 == "D":
            print("Bien joué !")
            print("")
            total = total + 4000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était :  D")
            print("Tu repars tout de même avec 1 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 9

        print("")
        print("A) La Terre")
        print("B) Venus")
        print("C) Jupiter")
        print("D) Mars")
        print("")
        question9 = input("Question pour 16 000€\nSur quelle planète se déroule le jeu DOOM ?")
        if question9 == "d" or question9 == "D":
            print("Bien joué !")
            print("")
            total = total + 8000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : D ")
            print("Tu repars tout de même avec 1 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 10

        print("")
        print("A) Pantera")
        print("B) Ouganda")
        print("C) Wakanda")
        print("D) Amazonia")
        print("")
        question10 = input("Question pour 32 000€\nDe quel pays fictif, le héros Black Panther est-il le roi ?")
        if question10 == "C" or question10 == "c":
            print("Bien joué ! Tu as atteint le second palier !")
            print("")
            total = total + 16000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : C ")
            print("Tu repars tout de même avec 1 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 11

        print("")
        print("A) 7")
        print("B) 8")
        print("C) 9")
        print("D) 0")
        print("")
        question11 = input("Question pour 64 000€\nCombien d'ex-maléfique Scott Pilgrim doit-il affronter dans son jeu?")
        if question11 == "A" or question11 == "a":
            print("Bien joué !")
            print("")
            total = total + 32000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : A")
            print("Tu repars tout de même avec 32 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 12

        print("")
        print("A) Blinky")
        print("B) Pinky")
        print("C) Inky")
        print("D) Clyde")
        print("")
        question12 = input("Question pour 125 000€\nComment se prénome le fantôme rouge dans Pac-Man ?")
        if question12 == "A" or question12 == "a":
            print("Bien joué !")
            print("")
            total = total + 61000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : A ")
            print("Tu repars tout de même avec 32 000€, bien joué à toi !")
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 13

        print("")
        print("A) 1908")
        print("B) 1918")
        print("C) 1928")
        print("D) 1938")
        print("")
        question13 = input("Question pour 250 000€\nEn quelle année Mickey Mouse fit sa première apparition à l'écran ?")
        if question13 == "c" or question13 == "C":
            print("Bien joué !")
            print("")
            total = total + 125000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était :  C")
            print("Tu repars tout de même avec 32 000€, bien joué à toi !")
            time.sleep(3)
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter le million ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 14

        print("")
        print("A) Le mouiller")
        print("B) Lui donner à manger après minuit")
        print("C) L'exposer au soleil")
        print("D) Lui couper les poils")
        print("")
        question14 = input(
            "Question pour 500 000€\nQu'est ce qui est sans incidence sur un Mogwaï ?")
        if question14 == "d" or question14 == "D":
            print("Bien joué !")
            print("")
            total = total + 250000
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : D ")
            print("Tu repars tout de même avec 32 000€, bien joué à toi !")
            time.sleep(3)
            break
        time.sleep(1)
        partir = input("Veux-tu repartir avec %s €, ou rester et tenter l'ultime question ?\n Rester ou Partir" % total)
        if partir == "Partir" or partir == "partir" or partir == "PARTIR" or partir == "p" or partir == "P":
            print("Et bien tu repars donc avec", total, "€ ! Bien joué à toi !")
            time.sleep(3)
            break
        elif partir == "Rester" or partir == "rester" or partir == "RESTER" or partir == "r" or partir == "R":
            print("On continue alors !")

        # Question 15

        print("")
        print("A) Tychus")
        print("B) Jim Raynor")
        print("C) Sarah Kerrigan")
        print("D) Zeratul")
        print("")
        question15 = input("Question pour 1 000 000€\nDans Starcraft, quel est le nom du héros principal ? ")
        if question15 == "b" or question15 == "B":
            print("Tu as remporté le million ! Bien joué à toi, ta culture geek ne connaît aucune limite !")
            print("")
            total = total + 500000
            time.sleep(3)
            break
        else:
            print("Oh c'est bien dommage ...")
            print("La réponse était : B ")
            print("Perdre si près du but .... Tu repars tout de même avec 32 000€, bien joué à toi !")
            time.sleep(3)
            break
        time.sleep(1)
    else:
        print("Tant pis, on jouera une autre fois !")




