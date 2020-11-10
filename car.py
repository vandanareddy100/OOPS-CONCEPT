class car:
    def __init__(self,model,brand,colour):
        self.model=model
        self.brand=brand
        self.colour=colour
    def start(self):
        print(' car is going to start')
    def move(self):
        print('car is moving')
    def stop(self):
        print('car is stopping')
class BMW(car):
    def __init__(self,model,brand,colour):
        super().__init__(model,brand,colour)
        #self.screensize=model
        #self.brand=brand
        #self.colour=colour
    def autopilot(self):
        print('driverless car ')
    def autogear(self):
        print('automatics gare change')
    def BMWInfo(self):
        print("model:",self.model)
        print("brand:",self.brand)
        print("colour:",self.colour)
        #print("Salary:",self.esal)
b=BMW('bmw x6','mini','black')

b.autopilot()
b.start()
b.autogear()
b.move()
b.stop()
b.BMWInfo()
