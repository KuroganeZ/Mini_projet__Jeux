
WORD_TO_GUESS = "banane"
word_display = "______"

missed_count = 0
MAX_COUNT = 4

print("Bienvenue dans la première version du pendu, devine le mot !")
print(word_display)

while True:
    a = input("Entre une lettre (autre chose pour quitter) :")

    if len(a) != 1 or not a.isalpha():
        print("Mauvais input, on quitte !")
        break

    if a in WORD_TO_GUESS:
        print("Bien joué ! ", a,"est dans le mot !")
        # On doit convertir la "string" en "list"
        wd = list(word_display)
        for i in range(len(WORD_TO_GUESS)):
            # Si la lettre est la même, on update le wd
            if WORD_TO_GUESS[i] == a:
                wd[i] = a

        # On reconverti la "list" en "string"
        word_display = "".join(wd)

        if word_display == WORD_TO_GUESS:
            print("TU AS GAGNE !! Le mot était", WORD_TO_GUESS)
            break

    else:
        print("Raté, réessaie !")
        missed_count += 1

        if missed_count >= MAX_COUNT:
            print("Tu as perdu !!")
            break

    print("Il te reste",MAX_COUNT-missed_count,"essais restants.")
    print(word_display)

