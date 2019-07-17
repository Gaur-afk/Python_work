def make_sandwich(*items):
    print("\nI'll make you a sandwich:")
    for item in items:
        print("I'll add " + item + " to your sandwich.")
    print("Your sandwich is ready!")


make_sandwich("Cheese", "Tomatoes")
make_sandwich("Chicken", "Onions", "Lettuce")
make_sandwich("BBQ Sauce", "Ham", "Beef", "Turkey")