# Type code for classes here
class ItemToPurchase:

    def __init__(self, item_name: str = "none", item_price: float = 0.0, item_quantity: int = 0,
                 item_description: str = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(
            f"{self.item_name} "
            f"{self.item_quantity} @ $"
            f"{int(self.item_price)} = $"
            f"{int(self.item_quantity * self.item_price)}"
        )

    def sum_total(self):
        return self.item_quantity * self.item_price

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:

    def __init__(self, customer_name: str, current_date: str, cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        if item_name not in self.cart_items:
            print("Item not found in cart. Nothing removed.")
        else:
            self.cart_items.remove(item_name)

    def modify_item(self, item_to_modify: ItemToPurchase, new_quantity: int):
        if item_to_modify not in self.cart_items:
            print("Item not found in cart. Nothing modified.")
        else:
            item_to_modify.item_quantity = new_quantity

    def get_num_items_in_cart(self):
        total_of_items = 0
        for item in self.cart_items:
            total_of_items += item.item_quantity
        return total_of_items

    def get_cost_of_cart(self):
        sum = 0
        if self.cart_items is None:
            return sum
        for i in range(len(self.cart_items)):
            sum += self.cart_items[i].sum_total()
        return sum

    def print_total(self):
        if len(self.cart_items) <= 0:
            print(f'OUTPUT SHOPPING CART')
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            total_items = 0
            print(f"Number of Items: {total_items}")
            print("SHOPPING CART IS EMPTY")
            print(f'Total: ${0}')
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            total_items = 0
            print(f"Number of Items: {total_items}")
            print()
            for item in self.cart_items:
                total_items += item.item_quantity
                item.print_item_cost()
            print(f'Total: ${self.get_cost_of_cart()}')

    def print_description(self):
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.print_item_description())


def print_menu():
    print("MENU\n"
          "a - Add item to cart\n"
          "r - Remove item from cart\n"
          "c - Change item quantity\n"
          "i - Output items' descriptions\n"
          "o - Output shopping cart\n"
          "q - Quit\n")


def execute_menu(char, shopping_cart):
    shopping_cart.print_total()


if __name__ == "__main__":
    # Type main section of code here
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    shopping_cart1 = ShoppingCart(customer_name, current_date, [])

    print(f"Customer name: {shopping_cart1.customer_name}")
    print(f"Today's date: {shopping_cart1.current_date}")
    print()

    print_menu()

    user_input = ""
    while user_input != 'q':
        user_input = input("Choose an option:\n")
