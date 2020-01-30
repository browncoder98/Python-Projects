x= int(input("Enter the number of digits (minimum 2):"))
y=0
z=1

print("Fibonacci Sequence:\n")
print(y,",",z, end=", ")

for i in range (2,x):
    next=y+z
    print(next, end=", ")

    y=z
    z=next
