from item import item

# Stan zużycia na poziomie poniżej zera oznacza, że przedmiot jest zużyty

class consumableItem(item):
    __singleUse = True
    def __init__(self, itemName, volume, weight, durability):
        super().__init__(itemName, volume, weight)
        if(durability < 0):
            return -1
        elif(durability == 0):
            self.__durability = 0
        else:
            self.__durability = durability
            self.__singleUse = False

    def use(self):
        if(self.__durability >= 0):
            self.__durability -= (self.__durability+1)
        else:
            return -1;


    # co jeśli chcemy użyć więcej niż mamy?
    def use(self, amount):
        if(amount <= 0):
            return -1;

        if(self.__singleUse == False and self.__durability - amount >= 0):
            self.__durability -= amount
            if(self.__durability == 0):
                self.__durability -= 1
        else:
            return -1;

    def name(self):
        return self.itemName + " (consumable)"

    def displayStatus(self):
        print("Inspecting", self.name(), end=", ")
        print("weight: " + str(self.getWeight()), end=", ")
        print("volume: " + str(self.getVolume()),end=", ")
        if (self.__singleUse == True):
            print("Single use")
        else:
            print("durability: " + str(self.__durability))