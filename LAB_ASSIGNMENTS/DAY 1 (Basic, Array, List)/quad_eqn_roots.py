import math

a = int(input("Enter the Coeff. X^2 "))
b = int(input("Enter the Coeff. X^1 "))
c = int(input("Enter the Coeff. X^0 "))

print("Quadratic Equation: (", a, ") X^2 + (", b, ") X^1 + (", c, ")")

d = (b * b) - 4 * a * c

if d > 0:
    x = ((-b) + math.sqrt(d)) / (2 * a)
    y = ((-b) - math.sqrt(d)) / (2 * a)
    print("Roots are real and different:\n", x, ",", y)
elif d == 0:
    x = (-b) / (2 * a)
    print("Roots are real and same:\n", x, ",", x)
else:
    x = (-b) / (2 * a)
    y1 = -(d / (2 * a))
    y2 = (d / (2 * a))
    print("Roots are complex:\n(", x, ") + i(", y1, ") and (", x, ") - i(", y2, ")")