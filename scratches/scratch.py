x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))
z = int(input("Enter 3rd number:"))
print("The greatest number is ")

if x>y:
    if x>z:
        print (x)
    else:
        print (z)

elif y>x:
    if y>z:
        print(y)
    else:
        print(z)


elif z>y:
    if z>x:
        print(z)
    else:
        print(x)



