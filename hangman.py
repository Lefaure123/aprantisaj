import random
import time

print("\n* Byenvini nan jwet Hangman osinon le jeu du pendu *\n")
non = input("Se kiles kap jwe a svp: ")
print(f" OK  {non} ! Bon Chans!")
time.sleep(2)
print("Jwet la pral komanse!\n"
      "Eskew pare pou jwe Hangman!\n")
time.sleep(3)
g = ''
# def main():
#     global mots
#     global g
#     global b
#     global repons
mots = {'Jovenel': 'Pi resan prezidan ayisyen ki mouri sou pouvwa',
        'Disko': 'kote moun al danse bwe ak anpil  mizik',
        'Fim': 'On bagay moun al gade nan sinema',
        'Palmis': 'Pye bwa ki reprezante Ayisyen sou drapo yo a'}
g = random.choice(list(mots.keys()))
b = mots[g]
print(b)
for i in g:
    print('*', end='')
repons = input('Antre let ki manke a :')
if len(repons) >= 2 or len(repons) == 0:
    print("saw tape a envalid, tanpri tape yon sel let :")
else:
    print('ok')

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
