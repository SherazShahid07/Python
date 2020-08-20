def factors(x):

    factor_list = []
    
    for i in range (1,x+1):
        if x % i == 0:
            factor_list.append(i)


    factor_list.pop(0)
    factor_list.pop(-1)

    
    print (factor_list)


factors(13)
