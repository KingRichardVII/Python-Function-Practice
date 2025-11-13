# Richard Phan
# 11/12/25

def main():
    pokemon = input("Enter a starter pokemon from gen 1: ")
    type(pokemon)

def type(name):
    match name:
        case "Charmander":
            print("Fire type pokemon")
        case "Squirtle":
            print("Water type pokemon")
        case "Bulbasaur":
            print("Grass type pokemon")
        case _:
            print("I don't recognize that type")

    main()