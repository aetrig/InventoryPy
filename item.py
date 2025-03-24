class item():

    __itemName: str = None
    __volume: float = None
    __weight: float = None

    def __init__(self, itemName, volume, weight):
        self.__itemName = itemName
        self.__volume = volume
        self.__weight = weight

    # Czy parent class powinien mieć jakieś użycie?
    def use(self):
        print("This item can't be used in any way")

    
    def name(self):
        return self.__itemName

    def setVolume(self, volume):
        self.__volume = volume
    def setWeight(self, weight):
        self.__weight = weight

    def getVolume(self):
        return self.__volume
    def getWeight(self):
        return self.__weight


    def displayStatus(self):
        print("Inspecting", self.name(), end=", ")
        print("weight: " + str(self.__weight), end=", ")
        print("volume: " + str(self.__volume))