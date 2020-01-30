#Exercise 06 (Practice):

word = str(input("Enter a word: "))

rvs=word[::-1]
print(rvs)
if word == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")