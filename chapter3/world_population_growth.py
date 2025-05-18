#27

length = 100
world_population = 8200000000
growth_rate = 0.85 / 100

growth_per_year = 0
new_population = 0

print('\nYears', '\t', 'Growth per year', '\t', 'world population')
for length in range(1, length + 1):

	growth_per_year = world_population * growth_rate
	world_population += growth_per_year

	print(length, end=' \t')
	print(f"{growth_per_year:.2f}", end=' \t')
	print(f"{world_population:.2f}")
