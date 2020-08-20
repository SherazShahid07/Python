def vowel_swapper(string):

    for x in string:
        if x == "O":
            string = string.replace("O", '000')
            
    string = string.lower()

##    pos = string.index('a', string.index('a') + 1) 
##    string = string[:pos] + '4' + string[pos + 1:] 
    
    
    string = string.capitalize()
    
    print (string)
    
    for x in string:
        if x == "a":
            string = string.replace("a",'4', 2)
        if x == "e":
            string = string.replace("e",'3')
        if x == "i":
            string = string.replace("i",'!')
        if x == "o":
            string = string.replace("o",'ooo')
        if x == "u":
            string = string.replace("u",'|_|')




vowel_swapper("abababab")



