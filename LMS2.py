class Library:

    def __init__(self, name, url, address):
        self.name = name.title()
        self.url = url
        self.address = address
        self.lists = []

    def lib_info(self):
        print('Library: ' + self.name)
        print('Url: ' + self.url)
        print('Address: ' + self.address)

    def add_lists(self, checkout):
        self.lists.append(checkout)

    def print_lists(self):
        for checkout in self.lists:
            student = checkout.student
            print('\nStudent Name: ' + student.name)
            book = checkout.book
            print('Book Checked Out: ' + book.name)
            date = checkout.checkout_date
            print('Date Checked Out: ' + date + " (All books must be returned in a weeks time!)")

    def checkout_book(self):
        borrow = []
        prompt1 = "\nWhat book would you like? "
        prompt2 = "What is your name? "
        prompt3 = "What is the date?(mm-dd-yy) "

        for checkout in self.lists:
            book = checkout.book
            while True:
                if input(prompt1) == book.name:
                    print('That is checked out. You will be able to get it when it is returned.')
                else:
                    print('Ok.')
                    borrow.append(input(prompt1))
                    if input(prompt2) != "":
                        borrow.append(input(prompt2))
                        if input(prompt3) != "":
                            borrow.append(input(prompt3))
                            print(borrow)
                            break
                    else:
                        print('Try again!')

class Checkout:

    def __init__(self, student, book, checkout_date):
        self.student = student
        self.book = book
        self.checkout_date = checkout_date


class Student:

    def __init__(self, name, major):
        self.name = name.title()
        self.major = major.title()


class Book:

    def __init__(self, name, author, isbn):
        self.name = name.title()
        self.author = author.title()
        self.isbn = isbn


GMU = Library('George Mason University Library', 'www.library.gmu.edu', '4400 University Dr, Fairfax, VA 22030')

Bob = Student('Bob', 'chemistry')
Vedant = Student('Vedant', 'physics')
Anika = Student('Anika', 'mathematics')

HP4 = Book('Harry Potter and the Goblet of Fire', 'J. K. rowling',
           '1028364839463')
PJ1 = Book('Percy Jackson and the Lightning Thief', 'Rick riordan', '3639273849283')
IC1 = Book('Eragon', 'Christopher Paolini', '2633847264938')

List1 = Checkout(Bob, HP4, '7-29-19')
List2 = Checkout(Vedant, PJ1, '8-12-19')
List3 = Checkout(Anika, IC1, '8-15-19')

GMU.lib_info()
GMU.add_lists(List1)
GMU.add_lists(List2)
GMU.add_lists(List3)
GMU.print_lists()
GMU.checkout_book()