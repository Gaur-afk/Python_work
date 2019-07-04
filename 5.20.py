sandwich_orders = ["Grilled Cheese", "Peanut Butter Jelly", "Ham and Cheese", "Pastrami"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print ("I made your " + sandwich + " sandwich.")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)
print (sandwich_orders)
print (finished_sandwiches)