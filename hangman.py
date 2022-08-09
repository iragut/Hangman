import random

words = ["python", "java", "swift", "javascript"]

won = 0
lose = 0
print("H A N G M A N")
menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")  # menu
while True:
    if menu == "exit":
        break
    elif menu == "results":
        print(f"You won: {won} times.")   # game result
        print(f"You lost: {lose} times.")
        menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")

    elif menu == "play":
        counter = random.choice(words)  # create all list and choice the word
        answer = list("-" * len(counter))
        out = "-" * len(counter)
        word = list(counter)
        Flush_list = list()
        num = 0

        print("")
        print(out)

        while num < 8:
            while True:
                litre = input("Input a letter:")
                if len(litre) != 1:          # check if is lower,english letter
                    print("Please, input a single letter.\n")
                    print("".join(answer))
                    break
                elif litre.isnumeric() or not litre.islower():
                    print("Please, enter a lowercase letter from the English alphabet.\n")
                    print("".join(answer))
                    break
                elif litre not in word and litre not in Flush_list:
                    print("That letter doesn't appear in the word\n")
                    Flush_list.append(litre)
                    print("".join(answer))
                    num += 1
                    break
                elif litre in Flush_list:
                    print("You've already guessed this letter.\n")
                    print("".join(answer))
                    break
                for i in range(0, len(counter)):    # put the guessed letter
                    if word[i] == litre:
                        answer.pop(i)
                        answer.insert(i, litre)
                        Flush_list.append(litre)
                print("")
                print("".join(answer))
                break
            final = "".join(answer)
            if final in words:              # finish of the game
                print(f"You guessed the word {final}!")
                print("You survived!")
                won += 1
                menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
                break
        if num == 8:
            print("You lost!")
            lose += 1
            menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
