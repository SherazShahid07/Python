def factors(number):

    factor_list = []
    
    for i in range (1,number+1):
        if number % i == 0:
            factor_list.append(i)


    factor_list.pop(0)
    factor_list.pop(-1)


    if not factor_list:
        print (number, 'is a prime number')
    else:
        print (factor_list)


factors(100)
