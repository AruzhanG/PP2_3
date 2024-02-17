from math import tan, pi

n = float(input("number od sides: "))
s = float(input("The length of a side: "))
area = int(n * (s ** 2) / (4 * tan( pi/ n)))

print("Area of regular polygon: ", area)