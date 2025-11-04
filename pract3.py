#create function that prints a person's full name
#parameters: string: first and last name

def full_name(name2):
  print(f"Hello {name2}")

def main():
    name = input("What is your name? ")
    name = name.title()
    full_name(name)

main()




