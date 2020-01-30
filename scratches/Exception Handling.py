a = 5
b = 2

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter the number "))
    print(k)

except ZeroDivisionError as e:
    print("Hey you cannot decide a number by Zero", e)

except ValueError as e:
    print ("Invalid Input")

except Exception as e:
    print ("Nice try but no chicken fry")
finally:
    print ("Resource closed")