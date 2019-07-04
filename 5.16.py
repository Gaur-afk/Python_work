prompt = "What toppings would you like on your pizza? Type quit when done."

fact = True
while fact:
    topping = input(prompt)
    print ("We will add " + topping + " to your pizza.")

    if input(prompt) == "quit":
        fact = False