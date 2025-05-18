#8

first_number = int(input('Enter number: '))
	
largest = first_number
smallest = first_number
sum = first_number
product = first_number
count = 1
	
for numbers in range(1, 4):
	number = int(input('Enter number: '))
		
	if number > largest:
		largest = number
	if number < smallest:
		smallest = number

	sum += number
	count = count + 1
	product *= number
	average = sum // count



print('the sum is ', sum)
print('the average is ', average)
print('the product is ', product)
print('the smallest is ', smallest)
print('the largest is ', largest)
