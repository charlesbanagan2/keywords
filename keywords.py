import time
from datetime import datetime

class Bookstore:
    def __init__(self):
        self.inventory = {}
    
    def add_book(self, book_name, quantity=1):
        if book_name in self.inventory:
            self.inventory[book_name] += quantity
        else:
            self.inventory[book_name] = quantity
        return f"Book '{book_name}' successfully added with a quantity of {quantity}."
    
    def borrow_book(self, book_name):
        if book_name in self.inventory and self.inventory[book_name] > 0:
            self.inventory[book_name] -= 1
            return f"Book '{book_name}' has been borrowed. Remaining copies: {self.inventory[book_name]}"
        elif book_name not in self.inventory:
            return f"Book '{book_name}' is not available in the bookstore."
        else:
            return f"Book '{book_name}' is currently unavailable."
    
    def return_book(self, book_name):
        if book_name in self.inventory:
            self.inventory[book_name] += 1
            return f"Book '{book_name}' returned. Total copies: {self.inventory[book_name]}"
        else:
            self.inventory[book_name] = 1
            return f"Book '{book_name}' added back to the inventory."
    
    def check_availability(self, book_name):
        return self.inventory.get(book_name, 0)

def borrow_or_return_action(bookstore, book_name, action):
    if action == "borrow":
        return bookstore.borrow_book(book_name)
    elif action == "return":
        return bookstore.return_book(book_name)
    else:
        return "Invalid action. Please choose 'borrow' or 'return'."

def show_books(bookstore):
    for book, quantity in bookstore.inventory.items():
        if quantity == 0:
            continue
        print(f"Book: {book}, Available Quantity: {quantity}")
        if quantity > 10:
            break

def safely_add_book(bookstore, book_name, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        return bookstore.add_book(book_name, quantity)
    except ValueError as e:
        return f"Error: {e}"
    finally:
        print("Attempt to add a book has finished.")

def verify_book(bookstore, book_name):
    assert book_name in bookstore.inventory, f"Book '{book_name}' is not available in the bookstore."
    print(f"Book '{book_name}' is available for borrowing.")

get_total_inventory = lambda bookstore: sum(bookstore.inventory.values())

total_books_added = 0

def update_total_books(quantity):
    global total_books_added
    total_books_added += quantity
    print(f"Total books added: {total_books_added}")

def outer_scope_example():
    count = 0
    
    def inner_scope_example():
        nonlocal count
        count += 1
        print(f"Count in inner scope: {count}")
    
    inner_scope_example()

def remove_book(bookstore, book_name):
    if book_name in bookstore.inventory:
        del bookstore.inventory[book_name]
        return f"Book '{book_name}' successfully removed from the inventory."
    return f"Book '{book_name}' not found in the inventory."

def save_inventory_to_file(bookstore):
    with open("bookstore_inventory.txt", "w") as file:
        for book, quantity in bookstore.inventory.items():
            file.write(f"{book}: {quantity}\n")
    print("Bookstore inventory has been saved to a file.")

def book_details_generator(bookstore):
    for book, quantity in bookstore.inventory.items():
        yield f"Book: {book}, Available Quantity: {quantity}"

def placeholder_action():
    pass

def check_for_none(bookstore, book_name):
    if bookstore.check_availability(book_name) is None:
        return f"Book '{book_name}' is not available."
    return f"Book '{book_name}' is in stock."

def bookstore_simulation():
    while True:
        action = input("\nChoose an action (add/borrow/return/quit): ").lower()
        if action == "quit":
            print("Exiting the bookstore simulation.")
            break
        elif action in ['add', 'borrow', 'return']:
            book_name = input("Enter the name of the book: ")
            print(borrow_or_return_action(bookstore, book_name, action))
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    bookstore = Bookstore()

    print(safely_add_book(bookstore, "Python Programming", 5))
    print(safely_add_book(bookstore, "Data Science Guide", 3))
    update_total_books(8)

    print(bookstore.check_availability("Python Programming"))

    show_books(bookstore)

    print(remove_book(bookstore, "Data Science Guide"))

    save_inventory_to_file(bookstore)

    for book in book_details_generator(bookstore):
        print(book)

    outer_scope_example()

    bookstore_simulation()

    verify_book(bookstore, "Python Programming")

    print(check_for_none(bookstore, "Python Programming"))
