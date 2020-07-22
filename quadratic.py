import math
a = int(input("Input the first coefficient: "))
b = int(input("Input the second coefficient: "))
c = int(input("Input the constant: "))

ans1 = ((-b) + (math.sqrt((b**b)-(4*a*c)))) / (2*a)
ans2 = ((-b) - (math.sqrt((b**b)-(4*a*c)))) / (2*a)

print(f"The answers to the quadratic equation are {ans1} and {ans2}")