def calculator(a, b, c):

    a = int(a)
    b = int(b)

    if c == '+':
        answer = a + b
    elif c == '-':
        answer = a - b
    elif c == '*':
        answer = a * b
    elif c == '/':
        answer = a / b


    print (answer)

calculator(8, 7, '*')
