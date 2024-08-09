# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

''' Your solution goes here '''
def split_check(bill, people, tax_percentage=0.09, tip_percentage=0.15):
    tip_amount = bill * tip_percentage
    bill_with_tip = bill + tip_amount
    tax_amount = bill * tax_percentage
    total = bill_with_tip + tax_amount
    return round(total / people, 2)

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))