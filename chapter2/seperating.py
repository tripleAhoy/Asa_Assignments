number = int(input('Enter a five-digit number: '))

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

	print(digit1    ,digit2    ,digit3    ,digit4    ,digit5)