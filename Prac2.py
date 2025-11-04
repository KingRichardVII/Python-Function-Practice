#return = statement used to end a function
        #and send result back to the caller

#that return value can then be assigned to a variable

#create operator functions that will perform operations on 2 nums
#parameters: num1, num2
def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    quotient = num1 / num2
    return quotient


print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

"""
after the function resolves, this is what we actually have:
print(3)
print(-1)
print(2)
print(0.5)
"""