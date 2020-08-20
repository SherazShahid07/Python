def vowel_swapper(string):

    for x in string:
        if x == "O":
            string = string.replace("O", '000')
            
    string = string.lower()
    
    for x in string:
        if x == "a" or "A":
            string = string.replace("a",'4')
        if x == "e" or "E":
            string = string.replace("e",'3')
        if x == "i" or "I":
            string = string.replace("i",'!')
        if x == "o":
            string = string.replace("o",'ooo')
        if x == "u" or "U":
            string = string.replace("u",'|_|')

    string = string.capitalize()
    
    print (string)

vowel_swapper("Everything's Available")
