# Richard Phan
# 11/12/25

def main():
    pokemon = str(input("Choose a starter pokemon from gens 1-4: "))
    type(pokemon)

def type(name):
    match name:
        case "Charmander" | "Cyndaquil" | "Torchic" | "Chimchar" :
            print("Congratulations! You have chosen " + name + ", the FIRE type pokemon")
        case "Squirtle" | "Totodile" | "Mudkip" | "Piplup" :
            print("Congratulations! You have chosen " + name + ", the WATER type pokemon")
        case "Bulbasaur"| "Chikorita" | "Treecko" | "Turtwig" :
            print("Congratulations! You have chosen " + name + ", the GRASS type pokemon")
        case _:
            print("Hmm, the pokedex doesn't register that pokemon... a new species perhaps?")

main()