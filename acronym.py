def acro():

    inp  = input("Input your words: ")
    word = inp.split(" ")
    wordList = ""
    for w in word:
        first = w[0:1]
        wordList = wordList + first
        wordList = wordList
    print(f"({wordList})")
    

acro()