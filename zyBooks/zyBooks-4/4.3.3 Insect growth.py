# num_insects = int(input()) # Must be >= 1

# while num_insects <= 100:
#     print(num_insects, end=" ")
#     num_insects *= 2


'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.08
annual_contribution = 12000

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings at beginning of year {}: ${:.2f}. Total from yearly contributions: ${:.2f}.'.format(i, savings, (annual_contribution * i)))

    savings = savings + (savings*interest_rate) + annual_contribution
    i = i + 1  # Increment loop variable

print('\n')
