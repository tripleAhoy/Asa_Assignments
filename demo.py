Calculate ROI for an investment for a given number of years.
write a program that prompt for the investment amount , the number of years and 
interest rate and present the return investment from one to the given number of years.

"""

amount = int(input('Enter the amount invested: '))
years = int(input('Enter the number of years: '))
rate = int(input('Enter the interest rate: ')) / 100


for years in range(1, years + 1):
	roi = amount * (1 + rate) ** years
	print(f"{roi:,.2f}")
