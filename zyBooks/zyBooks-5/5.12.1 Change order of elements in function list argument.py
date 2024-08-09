def swap(list):
    tmp = list[-1]
    list[-1] = list[0]
    list[0] = tmp
    return list

values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)