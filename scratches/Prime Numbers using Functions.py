#Prime number using functions:
while 1==1:
    def prime(n):
        if n==1:
            return False
        elif n==2:
            return True
        else:
            for i in range(2,n):
                if n%i == 0:
                    return False
            return True


    y = int(input("Enter a number from 1-100: "))

    if prime(y) == True:
        print("The number is prime. ")
    else:
        print("The number is not prime.")


