def polls():
    votes = 0
    aList = []
    bList = []
    cList = []
    dList = []
    invalid = []
    count = 1
    while votes < 8:
        vote = input("Who is the top artist in nigeria at the moment 'a : Wizkid', 'b: Davido', 'c: Olamide', 'd: Burnaboy' please select the character that matches your vote. Thank you:").lower()
        if vote == "a":
            print("Hello")
            aList.append(vote)
        elif vote == "b":
            bList.append(vote)
        elif vote == "c":
            cList.append(vote)
        elif vote == "d":
            dList.append(vote)
        else:
            invalid.append(count)

        votes = votes + 1

    summationA = len(aList)    
    summationB = len(bList)    
    summationC = len(cList)    
    summationD = len(dList)
    sumInvalid = len(invalid)    


    print(f"The values of all our votes are a: {summationA}, b: {summationB}, c: {summationC}, d: {summationD}, Invalid votes: {sumInvalid}")
    return summationA,summationB, summationC, summationD

polls()