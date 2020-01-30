class student:

    def _init_(self):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def _init_(self):
            self.brand = "HP"
            self.cpu = "5"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student('Rakin', 65)

s1.show()
