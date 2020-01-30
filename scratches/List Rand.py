#Let’s say I give you a list saved in a variable:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a
# Make a new list that has only the even elements of this list in it.

import random

numlist = []
list_length = random.randint(5, 15)

while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))

evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)

#write a program that returns a list that contains only the elements that are common between the lists

import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
result = [i for i in a if i in b]

print(result)