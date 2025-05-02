import math

print('Enter the principal amount, annual interest rate, and years needed.')

principal = int(input('Enter principal amount: '))

rate = int(input('Enter annual interest rate: '))

year = int(input('Enter the years needed: '))

percentageRate = (rate / 100) / 12;

duration = year * 12;

monthlyPayment = principal * (percentageRate * math.pow(1 + percentageRate, duration)) / (math.pow(1 + percentageRate, duration) - 1);

print('Monthly payment is:$',monthlyPayment)