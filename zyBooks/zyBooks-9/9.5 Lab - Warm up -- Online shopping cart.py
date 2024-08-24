# Type code for classes here
class ItemToPurchase:

    def __init__(self,item_name:str="None", item_price:float=0, item_quantity:int=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity*self.item_price)}")

    def sum_total(self):
        return self.item_quantity * self.item_price

if __name__ == "__main__":
    # Type main section of code here
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name: ')
    print(item1.item_name)
    item1.item_price = float(input("Enter the item price: "))
    print(item1.item_price)
    item1.item_quantity = int(input("Enter the item quantity: "))
    print(item1.item_quantity)

    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name: ')
    print(item2.item_name)
    item2.item_price = float(input("Enter the item price: "))
    print(item2.item_price)
    item2.item_quantity = int(input("Enter the item quantity: "))
    print(item2.item_quantity)

    total_cost = 0
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${item1.sum_total() + item2.sum_total()}")