#12

number = int(input('Enter five digit integer: '))

if number < 10000 or number > 99999:
	print('invalid number')

if number >= 10000 and number <= 99999:
	digit5 = number % 10
	remainder = number // 10
	digit4 = remainder % 10
	remainder = remainder // 10
	digit3 = remainder % 10
	remainder = remainder // 10
	digit2 = remainder % 10
	digit1 = remainder // 10	

	if digit1 == digit5 and digit2 == digit4:
		print(number, ' is a palindrome')
	else:
		print(number, ' is not a palindrome')
