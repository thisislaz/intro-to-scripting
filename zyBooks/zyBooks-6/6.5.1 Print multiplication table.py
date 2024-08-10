user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

''' Your solution goes here '''
for row in mult_table:
    for i, num in enumerate(row):
        if i < len(row) - 1:
            print(num, end=' | ')
        else:
            print(num)

nums = [10, 20, 30, 40, 50]

for pos, value in enumerate(nums):
    tmp = value / 2
    if (tmp % 2) == 0:
        nums[pos] = tmp
