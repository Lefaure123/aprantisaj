import random
import time

print("\n* Byenvini nan jwet Hangman osinon le jeu du pendu *\n")
non = input("Se kiles kap jwe a svp: ")
print(f" OK  {non} ! Bon Chans!")
time.sleep(2)
print("Jwet la pral komanse!\n"
      "Eskew pare pou jwe Hangman!\n")
time.sleep(3)


def main():
    global mots
    global longueur
    global jwet_la
    global konte
    global afichaj
    global rekipere
    global jwe
    mots = {'Jovenel': 'Pi resan prezidan ayisyen ki mouri sou pouvwa',
            'Disko': 'kote moun al danse bwe ak anpil  mizik',
            'Fim': 'On bagay moun al gade nan sinema',
            'Palmis': 'Pye bwa ki reprezante Ayisyen sou drapo yo a'}
    chwazi = random.choice(list(mots.keys()))
    longueur = len(chwazi)
    konte = 0
    afichaj = '*' * longueur
    rekipere = []
    jwe = ''


def jweAnBouk():
    global jwe
    jwe = input("Ou ta renmen rejwe anko ? W = wi, N = non \n")
    while jwe not in ['W', 'w', 'Y', 'y']:
        jwe = input("Ou ta renmen rejwe anko ? W = wi, N = non \n")
    if jwe == 'w':
        main()
    elif jwe == 'n':
        print('*Mesi bokou paskew te patisipe, nap tann ou anko*')
        exit()


def hangman():
    global i
    global repons
    global afichaj
    global chwa
    global mots
    global chwazi
    global konte
    global afichaj
    global mots
    global rekipere
    global jwet_la
    limit = 7
    chwazi = random.choice(list(mots.keys()))
    chwa = mots[chwazi]
    print(chwa)
    for i in chwazi:
        print('*', end='')
    print()
    repons = input("Antre mo a let pa let : ")
    repons = repons.strip()
    while len(repons.strip()) >= 2 or len(repons.strip()) == 0:
        print("saw tape a envalid, tanpri tape yon sel let :")
        repons = input("Antre yon mo a la fwa tanpri : ")

    if repons in chwazi:
        
        # rekipere.extend([repons])
        # index = chwazi.find(repons)
        # chwazi = chwazi[:index] + "*" + chwazi[index + 1:]
        # afichaj = afichaj[:index] + chwazi + afichaj[index + 1:]
        # print(afichaj + '\n')

    elif chwazi in rekipere:
        print("*Eseye tape yon lot let*")

    else:
        konte += 1

        if konte == 1:
            time.sleep(1)
            print('Move mo'+str(limit - konte)+'chans ki retew')

        elif konte == 2:
            time.sleep(1)
            print('Move mo' + str(limit - konte) + "chans ki retew")

        elif konte == 3:
            time.sleep(1)
            print('Move mo' + str(limit - konte) + "chans ki retew")

        elif konte == 4:
            time.sleep(1)
            print('Move mo' + str(limit - konte) + "chans ki retew")

        elif konte == 5:
            time.sleep(1)
            print('Move mo' + str(limit - konte) + "chans ki retew")

        elif konte == 6:
            time.sleep(1)
            print('Move mo' + str(limit - konte) + "chans ki retew")

        elif konte == 7:
            time.sleep(1)
            print('Move mo' + str(limit - konte) + "chans ki retew")

        if chwazi == '*' * longueur:
            print("Bravo, ou just byen reflchi, ou jwenn mo a ")
            jweAnBouk()

        elif konte != limit:
            hangman()

main()


hangman()


# import random
# import time
#
# # Initial Steps to invite in the game:
# print("\nWelcome to Hangman game by IT SOURCECODE\n")
# name = input("Enter your name: ")
# print("Hello " + name + "! Best of Luck!")
# time.sleep(2)
# print("The game is about to start!\n Let's play Hangman!")
# time.sleep(3)
#
#
# # The parameters we require to execute the game:
# def main():
#     global count
#     global display
#     global word
#     global already_guessed
#     global length
#     global play_game
#     words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
#                    ,"plants"]
#     word = random.choice(words_to_guess)
#     length = len(word)
#     count = 0
#     display = '_' * length
#     already_guessed = []
#     play_game = ""
#
# # A loop to re-execute the game when the first round ends:
#
# def play_loop():
#     global play_game
#     play_game = input("Do You want to play again? y = yes, n = no \n")
#     while play_game not in ["y", "n","Y","N"]:
#         play_game = input("Do You want to play again? y = yes, n = no \n")
#     if play_game == "y":
#         main()
#     elif play_game == "n":
#         print("Thanks For Playing! We expect you back again!")
#         exit()
#
# # Initializing all the conditions required for the game:
# def hangman():
#     global count
#     global display
#     global word
#     global already_guessed
#     global play_game
#     limit = 5
#     guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
#     guess = guess.strip()
#     if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
#         print("Invalid Input, Try a letter\n")
#         hangman()
#
#
#     elif guess in word:
#         already_guessed.extend([guess])
#         index = word.find(guess)
#         word = word[:index] + "_" + word[index + 1:]
#         display = display[:index] + guess + display[index + 1:]
#         print(display + "\n")
#
#     elif guess in already_guessed:
#         print("Try another letter.\n")
#
#     else:
#         count += 1
#
#         if count == 1:
#             time.sleep(1)
#             print("   _____ \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "__|__\n")
#             print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
#
#         elif count == 2:
#             time.sleep(1)
#             print("   _____ \n"
#                   "  |     | \n"
#                   "  |     |\n"
#                   "  |      \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "__|__\n")
#             print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
#
#         elif count == 3:
#            time.sleep(1)
#            print("   _____ \n"
#                  "  |     | \n"
#                  "  |     |\n"
#                  "  |     | \n"
#                  "  |      \n"
#                  "  |      \n"
#                  "  |      \n"
#                  "__|__\n")
#            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
#
#         elif count == 4:
#             time.sleep(1)
#             print("   _____ \n"
#                   "  |     | \n"
#                   "  |     |\n"
#                   "  |     | \n"
#                   "  |     O \n"
#                   "  |      \n"
#                   "  |      \n"
#                   "__|__\n")
#             print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
#
#         elif count == 5:
#             time.sleep(1)
#             print("   _____ \n"
#                   "  |     | \n"
#                   "  |     |\n"
#                   "  |     | \n"
#                   "  |     O \n"
#                   "  |    /|\ \n"
#                   "  |    / \ \n"
#                   "__|__\n")
#             print("Wrong guess. You are hanged!!!\n")
#             print("The word was:",already_guessed,word)
#             play_loop()
#
#     if word == '_' * length:
#         print("Congrats! You have guessed the word correctly!")
#         play_loop()
#
#     elif count != limit:
#         hangman()
#
#
# main()
#
#
# hangman()