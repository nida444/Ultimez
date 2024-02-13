slicesOfLarge = 8
slicesOfMedium = 6
slicesOfRegular = 4
slicesOfSmall = 1

totalSlices = 0

peopleCount = int(input("Enter the number of people: "))

large = 0
medium = 0
regular = 0
small = 0

while True:
    if totalSlices == peopleCount:
        break
    num = peopleCount - totalSlices
    if num >= 8:
        for i in range(8):
            totalSlices += 1
        large += 1
    if totalSlices == peopleCount:
        break
    num = peopleCount - totalSlices
    if num >= 6:
        for i in range(6):
            totalSlices += 1
        medium += 1
    if totalSlices == peopleCount:
        break
    num = peopleCount - totalSlices
    if num >= 4:
        for i in range(4):
            totalSlices += 1
        regular += 1
    if totalSlices == peopleCount:
        break
    num = peopleCount - totalSlices
    if num > 2:
        for i in range(1):
            totalSlices += 1
        small += 1

print("Number of Large Pizzas: ", large)
print("Number of Medium Pizzas: ", medium)
print("Number of Regular Pizzas: ", regular)
print("Number of Small Pizzas: ", small)
print("Number of total slices: ", totalSlices)
