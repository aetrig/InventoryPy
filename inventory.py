from importlib.resources import contents

from equippableItem import equippableItem
from usableItem import usableItem
from consumableItem import consumableItem
from note import note

class inventory():

    __currentWeight = 0
    __currentVolume = 0
    __contents = []
    __equippedItem = None # slot na wyekwipowany przedmiot

    def __init__(self, volumeLimit, weightLimit):
        self.__volumeLimit = volumeLimit
        self.__weightLimit = weightLimit

    # wkładamy do środka obiekt (na koniec listy)
    # Zwraca -1 jeżeli przedmiot nie zmiesci sie
    def insert(self, item):
        if (item.getWeight() <= self.__weightLimit - self.__currentWeight and item.getVolume() <= self.__volumeLimit - self.__currentVolume):
            self.__contents.append(item)
            self.__currentVolume += item.getVolume()
            self.__currentWeight += item.getWeight()
        else:
            print("Can't insert item")
            return -1

    # wyciągnięcie przedmiotu z plecaka odbywa się poprzez podanie indeksu na którym przedmiot się znajduje
    def remove(self, index):
        if(len(self.__contents) >= index):
            self.__currentVolume -= self.__contents[index].getVolume()
            self.__currentWeight -= self.__contents[index].getWeight()
            return self.__contents.pop(index)
        else:
            return -1;

    # pozwala na wypisanie zawartości plecaka wraz z indeksem
    def getContents(self):
        for index, item in enumerate(self.__contents):
            print(index, ". ", item.name(), sep="")
        print("Equipped slot: ", self.__equippedItem._item__itemName if self.__equippedItem != None else "None", sep="")

    # pozwala na wyekwipowanie przedmiotu (przedmiot uprzednio wyekwipowany wraca do ekwipunku)
    def equip(self, index):
        if (self.__equippedItem is not None):
            result = self.insert(self.__equippedItem)
            if(result == -1):
                print("Cannot equip item, item currently equipped doesn't fit into the inventory.")
                return -1
        self.__equippedItem = self.remove(index)

    def unequip(self):
        result = self.insert(self.__equippedItem)
        if(result == -1):
            print("Cannot unequip item, item currently equipped doesn't fit into the inventory.")
            return -1
        self.__equippedItem = None

    def displayStatus(self):
        print("The current weight is:", self.__currentWeight, "out of", self.__weightLimit)
        print("The current volume is:", self.__currentVolume, "out of", self.__volumeLimit)
        print("The contents are:")
        self.getContents()

    def displayItemStatus(self, index):
        self.__contents[index].displayStatus()

    def useItem(self, index):
        if index >= len(self.__contents) or index < 0:
            return -1
        else:
            self.__contents[index].use()
            if (isinstance(self.__contents[index], equippableItem)):
                self.equip(index)
            newWeight = 0
            newVolume = 0
            for item in self.__contents:
                newWeight += item.getWeight()
                newVolume += item.getVolume()
            self.__currentWeight = newWeight
            self.__currentVolume = newVolume

