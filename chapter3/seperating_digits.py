#9
number = int(input('Enter five digit integer: '))
denominator = 10000
if number < 10000 or number > 99999:
	print('invalid number')

if number >= 10000 and number <= 99999:

	for numbers in range(5):
		digit = number // denominator 
		number = number % denominator 
		print(digit, end=' ')
		denominator = denominator // 10
