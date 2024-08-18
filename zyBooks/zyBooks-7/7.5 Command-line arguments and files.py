import sys
import os

if len(sys.argv) != 2:
    print('Usage: {} input_file'.format(sys.argv[0]))
    sys.exit(1) # 1 is indicating the error

print('Opening file {}.'.format(sys.argv[1]))

if not os.path.exists(sys.argv[1]):
    print('File does not exist.')
    sys.exit(1)

f = open(sys.argv[1], 'r')

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())

print('Closing file {}'.format(sys.argv[1]))
f.close()  # Done with the file, so close it

print('\nnum1: {}'.format(num1))
print('num2: {}'.format(num2))
print('num1 + num2: {}'.format(num1 + num2))