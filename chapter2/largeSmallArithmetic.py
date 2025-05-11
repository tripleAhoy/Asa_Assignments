number1 = int(input('Enter a number: '))
number2 = int(input('Enter a number: '))
number3 = int(input('Enter a number: '))

sum = number1 + number2 + number3
average = sum // 3
product = number1 * number2 * number3
smallest = number1
largest = number1

if number2 < smallest:
	smallest = number2
if number3 < smallest:
	smallest = number3
if number2 > largest:
	largest = number2
if number3 > largest:
	largest = number3

print(sum)
print(average)
print(product)
print(smallest)
print(largest)