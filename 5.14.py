prompt = "How many people are in your group?"

while True:
    if input(prompt) >= str(8):
        print ("Please wait for your table to be ready.")
    else:
        print ("Your table is ready.")