curr_value = int(input())

min_value = curr_value

while curr_value > 0:
    if curr_value < min_value:
        min_value = curr_value
    curr_value = int(input())

print('Min value:', min_value, end='')