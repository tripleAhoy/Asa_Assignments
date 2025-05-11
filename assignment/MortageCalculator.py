

print('Enter the principal amount, annual interest rate, and years needed.')

principal = int(input('Enter principal amount: '))

rate = int(input('Enter annual interest rate: '))

year = int(input('Enter the years needed: '))

percentageRate = (rate / 100) / 12

duration = year * 12

a = percentageRate * (1 + percentageRate)**duration
b = ((1 + percentageRate)**duration) -1

monthlyPayment = principal * (a / b)

print('Monthly payment is:$', round(monthlyPayment, 2))