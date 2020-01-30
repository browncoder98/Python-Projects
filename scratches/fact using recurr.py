


def fact(n):
    if  n==0:
        return 1
    return n* fact(n-1)

x = int(input('Enter a number: '))

result = fact(x)


print ("The factorial is ", result)
