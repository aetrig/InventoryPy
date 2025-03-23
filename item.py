class item():

    itemName = None
    volume = None
    weight = None

    def __init__(self, itemName, volume, weight):
        self.itemName = itemName
        self.volume = volume
        self.weight = weight

    # # Czy parent class powinien mieć jakieś użycie?
    # def use(self):
    #     print("Quack!")
    def name(self):
        return self.itemName

    def displayStatus(self):
        print("Inspecting", self.name(), end=", ")
        print("weight: " + str(self.weight), end=", ")
        print("volume: " + str(self.volume))