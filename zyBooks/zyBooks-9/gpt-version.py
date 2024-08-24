class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:
"""
    option = ""
    while option != 'q':
        print(menu)
        option = input().strip()
        execute_menu(option, cart)


def execute_menu(option, cart):
    if option == 'a':
        print("ADD ITEM TO CART")
        item_name = input("Enter the item name:\n")
        item_description = input("Enter the item description:\n")
        item_price = int(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        cart.add_item(new_item)
    elif option == 'r':
        print("REMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove:\n")
        cart.remove_item(item_name)
    elif option == 'c':
        print("CHANGE ITEM QUANTITY")
        item_name = input("Enter the item name:\n")
        new_quantity = int(input("Enter the new quantity:\n"))
        modified_item = ItemToPurchase(item_name=item_name, item_quantity=new_quantity)
        cart.modify_item(modified_item)
    elif option == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
    elif option == 'o':
        print("OUTPUT SHOPPING CART")
        cart.print_total()
    elif option == 'q':
        return
    else:
        print("Invalid option, please try again.")


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)
