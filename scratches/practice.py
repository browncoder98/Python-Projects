from  numpy import *

arr1 = array([2,4,6,8,7])
arr2 = array ([3,7,8,9,7])
arr3 = array([])

for i in range (5):
    x = arr1 + arr2
    arr3.append(x)


print(arr3)

from array import *

arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the next value"))

    arr.append(x)

print(arr)

val = int(input("Enter the next value for search"))
k = 0
for e in arr:
    if e == val:
        print(k)
        break

k += 1
