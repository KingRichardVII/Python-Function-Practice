#create a function that delivers a user an invoice
#paramters: name, amount: .2f (rounded to 2 places), month due

def invoice(name, amount, month):
    print(f"Hello {name},")
    print(f"You have an invoice for ${amount:.2f} due {month}")

invoice("Richard", 50.674522, "Nov. 4th")