points = []
one = {1:["a","e","i","o","u","l","n","r","s","t"]}
two = {2:["d","g"]}
three = {3:["b","c","m","p"]}
four = {4: ["f","h","v","w","y"]}
five = {5:"k"}
eight = {8:["j","x"]}
ten = {10:["q","z"]}
word = input("Type in your word: ")
# letters = word.split()
for l in word:
    if (l in one[1]):
        points.append(1)
    elif (l in two[2]):
        points.append(2)
    elif (l in three[3]):
        points.append(3)
    elif (l in four[4]):
        points.append(4)
    elif (l in five[5]):
        points.append(5)
    elif (l in eight[8]):
        points.append(8)
    elif (l in ten[10]):
        points.append(10)
total_points = sum(points)
print(total_points)
        
