class item():

    itemName = None
    __volume = None
    __weight = None

    def __init__(self, itemName, volume, weight):
        self.itemName = itemName
        self.__volume = volume
        self.__weight = weight

    # # Czy parent class powinien mieć jakieś użycie?
    # def use(self):
    #     print("Quack!")
    def name(self):
        return self.itemName

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