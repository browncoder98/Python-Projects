#Exercise 1 (Practice)

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2018 - age)+100)
print(name + " will be 100 years old in the year " + year)


#Exercise 2(Practice)

num = int(input("Enter a number: "))
check = int(input("Enter the denominator: "))

rem = num % check

if rem == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Exercise 4 (Practice)

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)