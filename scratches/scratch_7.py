from numpy import *

def multiplication_or_sum (num1, num2):
    product = num1*num2
    if (product < 1000):
        return product
    else:
        return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))

result = multiplication_or_sum (num1, num2)

print("The result is ", result)




def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )
inputStr = input("Enter String ")


print("Original String is ", inputStr)
print("Printing only even index chars")

printEveIndexChar(inputStr)
