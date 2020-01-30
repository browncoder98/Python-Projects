from time import sleep

class A:
    def feature1(self):
        print("Eat")
    def feature2(self):
        print("Sleep")


class B:
    def feature3(self):
        print("Rave")

    def feature4(self):
        print("Repeat")


class C(A,B):
    def feature5(self):
        print("Fuck bitches get money")

    def feature6(self):
        print("Love is trash, bitches need cash")


a1 = A()
b1 = B()
c1 = C()

c1.feature1()
sleep(2)
c1.feature2()
sleep(2)
c1.feature3()
sleep(2)
c1.feature4()
sleep(2)
c1.feature5()
sleep(2)
c1.feature6()
