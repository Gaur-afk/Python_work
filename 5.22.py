prompt = "Where do you want to go in the world? When everyone is done type quit."

yeet = True
while yeet:
    place = input(prompt)
    if input(prompt) == "quit":
        yeet = False
        print (place)
    else:
        print(place + "! That is cool")