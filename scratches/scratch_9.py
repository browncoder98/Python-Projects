from time import sleep

print ("This is my file to demonstrate best practices ")

def process_data(data):
    print("Data processing....")
    modified_data = data + "that has been modified"
    sleep(3)
    print("Data processing has been finished.")

    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()

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
