#11/7/25

#create a function that sings happy birthday when called.
#should have the parameters name, age, animal

def happy_birthday(name, age, animal):
    print(f"Happy birthday to {name}!")
    print(f"You're turning {age} ")
    print(f"You smell like a {animal} ")
    print(f"And you look like one too ")
    print(f"Happy birthday to {name}! ")



def main():
    name = str(input("What is your name? ")).strip().title()
    age = int(input("How old are you? "))
    animal = str(input("What is your favorite animal? "))
    print()
    happy_birthday(name, age, animal)

main()