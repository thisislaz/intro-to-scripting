num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces
letters = "abcdefghijklmnopqrstuvwxyz".upper()

for i in range(num_rows):
    for k in range(num_cols):
        print("{}{}".format(i+1,letters[k]),end=" ")
print()