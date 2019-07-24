class Amazon:

    def __init__(self, name, url):
        self.name = name.title()
        self.url = url
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_items(self):
        print('\n_______ITEMS_______')
        for items in self.inventory:
            name = items.name
            print('\nItem: ' + name)
            cost = items.price
            print('Price: ' + cost)

    def admin_view_inventory(self):
        print('\n_________INVENTORY_________')
        for items in self.inventory:
            name = items.name
            print('\nItem: ' + name)
            cost = items.price
            print('Price: ' + cost)
            qty = items.qty
            print('Quantity: ' + str(qty))


class Person:

    def __init__(self, name):
        self.name = name.title()


class ShoppingCart(Person):

    def __init__(self, name):
        super().__init__(name)
        self.cart = []

    def add_goods(self, item):
        self.cart.append(item)

    def print_receipt(self):
        print('\n________Receipt________')
        print('Customer Name: ' + self.name)
        for goods in self.cart:
            good = goods.name
            print('\nItem: ' + good)
            cost = goods.price
            print('Cost: ' + cost)
            qty = goods.qty
            goods.qty = int(qty) - 1


class Item:

    def __init__(self, name, price, qty):
        self.name = name.title()
        self.price = price
        self.qty = qty


amazon = Amazon('Amazon', 'www.amazon.com')
Cheese = Item('Cheese', '1.50', '50')
Chicken = Item('Chicken', '5.00', '15')
Grapes = Item('Grapes', '3.00', '150')

amazon.add_item(Cheese)
amazon.add_item(Chicken)
amazon.add_item(Grapes)
amazon.admin_view_inventory()
amazon.show_items()
Cart1 = ShoppingCart('Avyakt')
Cart1.add_goods(Cheese)
Cart1.add_goods(Grapes)
Cart1.print_receipt()
amazon.admin_view_inventory()
