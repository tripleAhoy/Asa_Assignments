#19

#find all Pythagorean triples that sides are <= 20
print("Pythagorean triples (side1, side2, hypotenuse):")

for side1 in range(1, 21):
    for side2 in range(side1, 21):
        for hypotenuse in range(side2, 21):
            if side1 * 2 + side2 == hypotenuse * 2:
                print(f"{side1}, {side2}, {hypotenuse}")
