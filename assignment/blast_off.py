number = int(input('Enter number: '))

while number <= -1:
	print('invalid')
	number = int(input('Enter number: '))

for number in range(number, -1, -1):
		print(number)
		if number == 1:
			print('Blast Off!')
			break
