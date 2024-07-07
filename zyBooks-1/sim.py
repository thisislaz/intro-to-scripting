triangle_base = 0    # Triangle base (cm)
triangle_height = 0  # Triangle height (cm)
triangle_area = 0

print('Enter triangle base:')
triangle_base = int(input())

print('Enter triangle height:')
triangle_height = int(input())

triangle_area = (triangle_base * triangle_height) / 2
print('Triangle area = (', end="")
print(triangle_base)
print("*",end='')

print(triangle_height, end="")
print(') / 2 =', end="")

print(triangle_area, end="")
print('cm**2')