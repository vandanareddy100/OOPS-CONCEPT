
###HAS-A-RELATIONSHIP####
class memory:
    def __init__(self,internal,secondary,ram):
        self.internal=internal
        self.secondary=secondary
        self.ram=ram
    def getinfo(self):
        print("internal:{} , secondary:{} and ram:{}".format(self.internal,self.secondary,self.ram))
class mobile:
    def __init__(self,model,brand,price,memory):
        self.model=model
        self.brand=brand
        self.price=price
        self.memory=memory
    """def add(self,price,memory):
        self.price=price
        self.memory=memory"""
    def mbinfo(self):
        print("Model Name:",self.model)
        print("Mobile brand:",self.brand)
        print("Mobile price:", self.price)
        print("Mobile memory Info:",end=" ")
        self.memory.getinfo()
m=memory("128gb","256gb","6gb")

e=mobile('realme2pro','oppo',16000,m)
e.mbinfo()
