#20

number = int(input('Enter a binary number: '))
decimal = 0
power = 0

while number > 0:
	digit = number % 10
	decimal += digit * (2 ** power)
	number //= 10
	power += 1

print('Decimal is: decimal')
