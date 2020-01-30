from time import sleep
from threading import *

class Hi (Thread):
    def run(self):
        for i in range(5):
            print("Nice try but no chicken fry")
            sleep(2)


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Love is trash bitches need cash")
            sleep(2)


t1= Hi()
t2= Hello()

t1.start()
sleep(0.5)
t2.start()

t1.join()
t2.join()

print("Bye")