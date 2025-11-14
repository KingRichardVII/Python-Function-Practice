
def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("CS GO")
    elif difficulty == "Difficult" and players == "Singleplayer":
        recommend("Elden Ring")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Minecraft")
    elif difficulty == "Casual" and players == "Singleplayer":
        recommend("Stardew-Valley")
    else:
        print("Enter a valid difficulty.")

def recommend(game):
    print("You might like", game)

main()