prompt = "Please input a number."
number = input(prompt)
if int(number) % 10 == 0:
    print ("This is a multiple of 10.")
else:
    print ("This is not a multiple of ten.")