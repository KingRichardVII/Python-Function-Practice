#Create a function that capitalizes your first and last name
    #ensure it returns first and last

#set the return value to a variable named full_name and print it to the console


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name("richard","phan")
print(full_name)




