prompt1 = "How old are you?"

while True:
    if input(prompt1) <= str(3):
        print ("Your ticket is free!")
    elif input(prompt1) <= str(12):
        print ("Your ticket is 10 dollars.")
    else:
        print ("Your ticket is 15 dollars.")
