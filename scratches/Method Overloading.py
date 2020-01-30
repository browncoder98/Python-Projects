class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b, c):

        s = 0

        if a!= None and  b!= None and c!= None:
             s = a + b + c
        elif a!= None and b!= None:
                s = a + b
        else:
            s=a
            return s




s1 = Student(54,67)

print(s1.sum(50,60,90))

