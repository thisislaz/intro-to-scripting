''' Your solution goes here '''
def print_total_inches(num_feet,num_inches):
    print(f"Total inches: {num_feet*12 + num_inches}")


feet = int(input())
inches = int(input())
print_total_inches(feet, inches)