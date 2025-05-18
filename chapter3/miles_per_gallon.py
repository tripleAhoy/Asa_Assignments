#11

gallons = 0
miles = 0
total_miles = 0
total_gallons = 0
overallaverage = 0

while gallons != -1:
	gallons = float(input('Enter gallons used (-1 to end): '))
	if gallons == -1:
		break
	miles = float(input('Enter miles driven: '))

	milesgallons = miles / gallons
	print(milesgallons)
	total_miles += miles
	total_gallons += gallons

overallaverage = total_miles / total_gallons
print(f"the overall average miles/ gallon is {overallaverage:.6f}")
