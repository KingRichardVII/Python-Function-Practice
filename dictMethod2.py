words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 999}

def main():
    print("Welcome to the Spelling Bee!")
    #same as iterating over keys, values in words.items()
    #word, points == keys, values
    #just different variable names
    for word, points in words.items(): #.item returns a list of (key,
        # values) tuples
        #same as saying: key was worth value points
        print(f"{word} was worth {points} points.")

if __name__ == '__main__':
    main()