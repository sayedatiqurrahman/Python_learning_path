import math


def circle_state(radius):
    area = round(math.pi * (radius ** 2),2)
    circumference = round(2 * math.pi * radius ,2)

    return area, circumference
a,b = circle_state(2)
print(f"Area: {a}, Circumference: {b}")  