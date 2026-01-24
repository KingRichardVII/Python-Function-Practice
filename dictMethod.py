#key/value = correct word/points worth
words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 999}

def main():
    print("Welcome to the Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(words) > 0:
        #len tells us how many keys in dict
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ")

        #Check if guess in dictionary
        #if our input is one of the keys in this dict
        if guess == "GRAPHIC":
            #clears entire dict
            words.clear()
            print("You've guessed the SUPER word! Congratulations! You've won!")
        if guess in words.keys():
            #.pop gives you the value of the key and removes the key from dict
            # supply the key 'guess' as the argument
            points = words.pop(guess)
            #guess = key, so we use words[key]
            print(f"Correct! You got {points} points!")


    print("GG, thanks for playing!")

if __name__ == '__main__':
    main()