format_string = '{name:<16} {goals:<8}' #Left-aligned
# format_string = "{name:>16} {goals:>8}" #Right-aligned
# format_string = "{name:^16} {goals:^8}" #centered
format_string = '{name:<16} {goals:^8}'

print(format_string.format(name='Player Name', goals='Goals'))
print('-' * 24)

print(format_string.format(name='Sadio Mane', goals=22))
print(format_string.format(name='Gabriel Jesus', goals=7))
print(format_string.format(name="Lazaro Alvarez", goals=69))

name = 'Wayne Rooney'
goals = 36
# Use default empty space fill character
print('{name:<16}{goals:>6}'.format(name=name, goals=goals))
# Use '0' as a fill character for score
print('{name:<16}{goals:0>6}'.format(name=name, goals=goals))
# Use '_' as fill character for name
print('{name:_<16}{goals:0>6}'.format(name=name, goals=goals))

print()
import math
real_pi = math.pi  # math library provides close approximation of pi
approximate_pi = 22.0 / 7.0  # Approximately correct pi to within 2 decimal places

print('pi is {pi}'.format(pi=real_pi))
print('22/7 is {pi}'.format(pi=approximate_pi))
print('22/7 looks better like {pi:.2f}'.format(pi=approximate_pi))
print('{x:4.1f}'.format(x=5))

air_temp = float(input())
print("{x:.1f}C".format(x=air_temp))