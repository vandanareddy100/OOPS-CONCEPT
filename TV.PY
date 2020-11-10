


###IS-A-RELATIONSHIP###
class Tv:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        
    def features(self):
        print('features of tv- colour tv')
        
    """def Tvinfo(self):
        print("model name:",self.model)
        print("brand name:",self.brand)"""
class smartTv(Tv):
    
    def __init__(self,model,brand,screensize,price,resolution):
        super().__init__(model,brand)
        self.screensize=screensize
        self.price=price
        self.resolution=resolution
        
    def newfeature(self):
        print(" smarttv features-large screen soundsytem is high")
        print(" we can connect to internet")
        
    def smartTvInfo(self):
        print("model tv:",self.model)
        print("brand brand:",self.brand)
        print("screensize:",self.screensize)
        print("price:",self.price)
        print("resolution:",self.resolution)
        #print("Salary:",self.esal)
s=smartTv('UA32J4003AR','SUMSUNG','50inches', 15000,'1280*480')
s.features()
s.newfeature()
s.smartTvInfo()
