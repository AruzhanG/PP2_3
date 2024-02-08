import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = float(self.x) - float(other_point.x)
        dy = float(self.y) - float(other_point.y)
        distance = math.sqrt(dx**2 + dy**2)
        return distance

x1 = float(input("Enter x-coordinate for the first point: "))
y1 = float(input("Enter y-coordinate for the first point: "))
point1 = Point(x1, y1)


x2 = float(input("Enter x-coordinate for the second point: "))
y2 = float(input("Enter y-coordinate for the second point: "))
point2 = Point(x2, y2)


point1.show()
point2.show()


distance = point1.dist(point2)
print(f"Distance between the points: {distance}")

new_x = float(input("Enter new x-coordinate for the first point: "))
new_y = float(input("Enter new y-coordinate for the first point: "))
point1.move(new_x, new_y)


point1.show()

