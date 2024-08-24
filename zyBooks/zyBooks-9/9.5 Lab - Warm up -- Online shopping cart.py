# Type code for classes here
class ItemToPurchase:

    def __init__(self,item_name:str="none", item_price:float=0.0, item_quantity:int=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity*self.item_price)}")

    def sum_total(self):
        return self.item_quantity * self.item_price

if __name__ == "__main__":
    # Type main section of code here
    count_of_items = 1
    item1 = ItemToPurchase()
    print(f"Item {count_of_items}")
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    item2 = ItemToPurchase()
    print(f"Item {count_of_items+1}")
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    total_cost = 0
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print(f"Total: ${int(item1.sum_total() + item2.sum_total())}")