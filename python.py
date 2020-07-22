count = 0
degrees = []
while count < 3:
    correct = True
    while correct:
        try:
            userInput = int(input("Please input the angles of a triangle: "))
            correct = False
            count++
        except:
            True
            print("Not a valid angle")

summation = sum(degrees)
if degrees == 180:
    print("Valid Triangle")
    if (degrees[0] == 90) or (degrees[1] == 90) or (degrees[2] == 90):
        print("A right angle triangle")
    else:
        print("Not a right angle triangle")
else:
    print("Not a type of triangle")           