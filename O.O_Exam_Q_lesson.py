class building:
    
    def __init__(self, numberFloors, width, height):

        self.numberFloors = numberFloors
        self.width = width
        self.height = height

        super(building,self).__init__()

        
    def getNumberFloors(self):
        print("getNumberFloors works")
        
    def getWidth(self):
        print("getWidth works")

    def getheight(self):
        print("getHeight works")

    def setNumberFloors(self):
        print("setNumberFloors works")

    def setWidth(self):
        print("setWidth works")
    
    def setHeight(self):
        print("setHeight works")

class office: 

    def __init__self(self,numDesks, numCompanies):

        self.numDesks = int(numDesks)
        self.numCompanies = int(numCompanies)


        super(office,self). __init__()

    def getDesks(self):
        print("getDesks works")

    def getCompanies(self):
        print("getCompanies works")

    

myBuilding = building(pfloors = 2,)
floors = myBuilding.getNumberFLoors()
print(f"floors = {floors}")
