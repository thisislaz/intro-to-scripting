words = list(input().split())
count={}

for n in words:
    print(f"{n} {words.count(n)}")