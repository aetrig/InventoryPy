from importlib.resources import contents

from equippableItem import equippableItem
from usableItem import usableItem
from note import note

class backpack():

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
        print("Equipped slot: ", self.__equippedItem.itemName if self.__equippedItem != None else "None", sep="")

    # pozwala na wyekwipowanie przedmiotu (przedmiot uprzednio wyekwipowany wraca do plecaka)
    def equip(self, index):
        if(len(self.__contents) >= index and isinstance(self.__contents[index], equippableItem)):
            if(self.__equippedItem is not None):
                result = self.__contents.insert(self.__equippedItem)
                if(result == -1):
                    print("Cannot equip item, item currently equipped doesn't fit into the backpack.")
                    return -1
            self.__equippedItem = self.remove(index)


    def useConsumable(self, index):
        if(len(self.__contents) <= index or index < 0):
            return -1

        if (not isinstance(self.__contents[index], consumableItem)):
            return -1
        else:
            self.__contents[index].use()

    def useConsumable(self, index, amount):
        if (len(self.__contents) <= index or index < 0):
            return -1

        if (not isinstance(self.__contents[index], consumableItem)):
            return -1
        else:
            self.__contents[index].use(amount)

    def useUsable(self, index):
        if (len(self.__contents) <= index or index < 0):
            return -1

        if(not isinstance(self.__contents[index], usableItem)):
            return -1
        else:
            self.__contents[index].use()


    def displayStatus(self):
        print("The current weight is:", self.__currentWeight, "out of", self.__weightLimit)
        print("The current volume is:", self.__currentVolume, "out of", self.__volumeLimit)
        print("The contents are:")
        self.getContents()

    def displayItemStatus(self, index):
        self.__contents[index].displayStatus()

    def scribbleNote(self, index, text):
        if (len(self.__contents) <= index or index < 0):
            return -1
        if (not isinstance(self.__contents[index], note)):
            return -1
        else:
            self.__contents[index].scribble(text)

    def clearNote(self, index):
        if (len(self.__contents) <= index or index < 0):
            return -1
        if (not isinstance(self.__contents[index], note)):
            return -1
        else:
            self.__contents[index].clear()

