class Item():

    def __init__(self, itemName, volume, weight):
        self.itemName = itemName
        self.__volume = volume
        self.__weight = weight

    # Czy parent class powinien mieć jakieś użycie?
    def use(self):
        print("Quack!")