def isbnCheck():
    b = ''
    user = input("Enter your ISBN number: ")

    data = user.split("-")
    for i in data:
        b = b + str(i)
        