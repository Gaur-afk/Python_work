sandwich_orders = ["Grilled Cheese", "Pastrami", "Peanut Butter Jelly", "Pastrami", "Ham and Cheese", "Pastrami"]
finished_sandwiches = []
print ("The Deli is out of pastrami.")

sandwiches = True
while sandwiches:
    for sandwich in sandwich_orders:
        if sandwich == "Pastrami":
            sandwich_orders.remove(sandwich)
        else:
            print ("I made your " + sandwich + " sandwich.")
        sandwich_orders.remove(sandwich)
        finished_sandwiches.append(sandwich)
        sandwiches = False
print (sandwich_orders)
print (finished_sandwiches)