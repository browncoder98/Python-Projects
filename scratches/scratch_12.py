num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)

#Exercise 5 (Practice)

a = [1,2,4,6,78,90]
b = [1,2,5,78,91]

print(set(a) & set(b))

#Exercise 6 (Practice)

