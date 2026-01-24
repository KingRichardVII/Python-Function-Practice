#Looping over keys of dictionary

#create a dict, where key/value is "region":"starter name"
fireType = {
    "Kanto": "Charmander",
    "Johto": "Cyndaquil",
    "Hoenn": "Torchic",
    "Sinnoh": "Chimchar"
}

def main():
    #print each region and starter name HINT: use a for loop
    for region in fireType.keys(): #.keys method returns all keys in dictionary
        print(f"{region}'s fire type starter is {fireType.get(region)}.")

main()