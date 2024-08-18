import os

fname = input('Enter file name: ')
path = os.path.join(fname)
print()

for d,sd,f in os.walk(path):
    print(d, 'contains subdirectories:', sd, end=" ")
    print('and files:',f)