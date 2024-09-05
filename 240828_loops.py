for i in range(0,8):
    for j in range(0,8):
        print(i,j)

for i in range(0,8):
    for j in range(0,8):
        for k in range(0,8):
            print(i,j,k)

for i in range(2):
    for j in range(0,2):
        for k in range(0,2):
            for l in range(0,2):
                print(i,j,k,l)

class Car:
    def __init__(self, model, color):
        self.color = color
        self.model = model
        self.gas = 20

class Car:
    def __init__(self, model, color):
        wheels =4
        self.color = color
        self.model = model
        self.gas = 20
    def drive(self, used_gas):
        self.gas-=used_gas
        if self.gas<0:
            return "no gas is there"
        print("Gas remaining: ", self.gas)
    def fill_gas(self):
        self.gas = 20
        print("full gas")

tes = Car("tesla", "black")

tes.color
tes.model

tes.drive(10)