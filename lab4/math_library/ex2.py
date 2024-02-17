import math

h = float(input("Height: "))
base_a = float(input("Base, first value: "))
base_b = float(input("Base, second value: "))


def are_trapezoid(base_a,base_b,h):
    area = ((base_a + base_b) / 2) * h
    return area

result = are_trapezoid(base_a,base_b,h)
print("Area of trapezoid: ",result)