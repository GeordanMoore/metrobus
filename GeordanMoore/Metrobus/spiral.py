import sys

size = 5
empty = []
maxnum = size * size
p = 0
number = 1

def print_square(square):
    print("-"*(2*size))
    for y in range(len(square)):
        for x in range(len(square[y])):
            print("{:6}".format(square[x][y]), end="")
        print()
    print("-"*(2*size))
    
    
while (number < maxnum):
    for n in range(maxnum):
        empty.append(number)
        number += 1

while (p < size):
    p += 1
    for w in range(size):
        square[w] = empty[w]
    print(square)
    
square = [[f"{square}" for x in range(size)] for y in range(size)]

print_square(square)
