#16

number = 0
largest = 0
secondlargest = 0

for number in range(10):
	number = int(input('enter number: '))
	for numbers in range(10):
		if number > largest:
			secondlargest = largest
			largest = number
		if number > secondlargest and number != largest:
			secondlargest = number

 
print(largest, ' is the largest number')
print(secondlargest, 'is the second largest number')	
