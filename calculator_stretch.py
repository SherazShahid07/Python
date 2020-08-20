def calculator(a, b, operator):

    a = int(a)
    b = int(b)

    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    elif operator == '/':
        answer = a / b

    answer = int(answer)

    print ("{0:b}".format(answer))

calculator(15, 2, '/')
