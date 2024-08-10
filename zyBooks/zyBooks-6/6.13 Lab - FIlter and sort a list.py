numbers = list(map(int, input().split()))
n=sorted(x for x in numbers if x >= 0)
for i in n: print(i, end=" ")