def max_num(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

max_num(10,12,9)


def max_num1(*args):
    big = args[0]
    for i in args:
        if i > big:
            args = i
    return args

max_num1(10,12,9,15)