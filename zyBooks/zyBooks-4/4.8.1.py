# c1 = 'a'
# while c1 < 'b':
#     c2 = 'a'
#     while c2 <= 'c':
#         print('{}{}'.format(c1, c2), end=' ')
#         c2 = chr(ord(c2) + 1)
#     c1 = chr(ord(c1) + 1)

i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print('{}{}'.format(i1,i2), end=' ')
        i2 = i2 + 3
    i1 = i1 + 10