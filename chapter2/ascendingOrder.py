num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))

largest = num1
smallest = num1
middle = num1

if num2 >= largest:
	largest = num2
if num3 >= largest:
	largest = num3
if num2 <= smallest:
	smallest = num2
if num3 <= smallest:
	smallest = num3
if num2 <= largest and num2 >= smallest:
	middle = num2 
if num3 != largest and num3 != smallest:
	middle = num3

print(smallest)
print(middle)
print(largest)