with open("input/day1input.txt", "r") as f:
    numbers = set(int(x) for x in f.read().splitlines())

def findProduct(sumVal):
    for number in numbers:
        complement = sumVal - number
        if complement in numbers:
            return complement * number
    return -1

def find3Product(sumVal):
    for number in numbers:
        complement = sumVal - number
        prevProd = findProduct(complement)
        if prevProd != -1:
            return prevProd * number

print(findProduct(2020))
print(find3Product(2020))