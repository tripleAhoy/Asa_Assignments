#13

number = int(input('Enter a non-negative number: '))
factorial = 1
factor = 1

if number <= 0:
	print('invalid')
else:
	for factor in range(1, number + 1):

		factorial = factorial * factor
		factor+= 1

	print('factorial of ', number,' is ', factorial)
