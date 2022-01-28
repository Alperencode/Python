# I asked to github copilot to make a game and thats what it did.
# First of all it completed the game name as Hangman
# and it made all the variables and conditions by itself.
 
# make a game of hangman

def main():
    print("Welcome to Hangman!")
    print("You will be given a word, and you must guess the letters in the word.")
    print("You will have 6 incorrect guesses before you lose.")
    print("Good luck!")
    print("")

    word = input("Enter a word: ")
    word = word.lower()
    word_list = list(word)
    print("")

    guesses = []
    incorrect_guesses = 0
    correct_guesses = 0

    while incorrect_guesses < 6:
        print("")
        print("Word: " + "".join(word_list))
        print("Guesses: " + " ".join(guesses))
        print("Incorrect Guesses: " + str(incorrect_guesses))
        print("")

        guess = input("Guess a letter: ")
        guess = guess.lower()

        if guess in guesses:
            print("You already guessed that letter.")
            print("")
        elif guess in word_list:
            print("That letter is in the word!")
            print("")
            correct_guesses += 1
            word_list[word_list.index(guess)] = guess
        else:
            print("That letter is not in the word.")
            print("")
            incorrect_guesses += 1
            guesses.append(guess)
        
        if correct_guesses == len(word_list):
            print("You win!")
            break
        elif incorrect_guesses == 6:
            print("You lose!")
            print("The word was: " + word)
            break

    print("")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
    