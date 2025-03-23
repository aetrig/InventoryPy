from importlib.resources import contents

from equippableItem import equippableItem
from usableItem import usableItem

class backpack():

    currentWeight = 0
    currentVolume = 0
    contents = []
    equippedItem = None # slot na wyekwipowany przedmiot

    def __init__(self, volumeLimit, weightLimit):
        self.volumeLimit = volumeLimit
        self.weightLimit = weightLimit

    # wkładamy do środka obiekt (na koniec listy)
    # Zwraca -1 jeżeli przedmiot nie zmiesci sie
    def insert(self, item):
        if (item.weight <= self.weightLimit - self.currentWeight and item.volume <= self.volumeLimit - self.currentVolume):
            self.contents.append(item)
            self.currentVolume += item.volume
            self.currentWeight += item.weight
        else:
            return -1

    # wyciągnięcie przedmiotu z plecaka odbywa się poprzez podanie indeksu na którym przedmiot się znajduje
    def remove(self, index):
        if(len(self.contents) >= index):
            self.currentVolume -= self.contents[index].volume
            self.currentWeight -= self.contents[index].weight
            return self.contents.pop(index)
        else:
            return -1;

    # pozwala na wypisanie zawartości plecaka wraz z indeksem
    def getContents(self):
        for index, item in enumerate(self.contents):
            print(index, ". ", item.name(), sep="")
        print("Equipped slot: ", self.equippedItem.itemName if self.equippedItem != None else "None", sep="")

    # pozwala na wyekwipowanie przedmiotu (przedmiot uprzednio wyekwipowany wraca do plecaka)
    def equip(self, index):
        if(len(self.contents) >= index and isinstance(self.contents[index], equippableItem)):
            if(self.equippedItem is not None):
                result = self.contents.insert(self.equippedItem)
                if(result == -1):
                    print("Cannot equip item, item currently equipped doesn't fit into the backpack.")
                    return -1
            self.equippedItem = self.remove(index)


    def useConsumable(self, index):
        if(len(self.contents) <= index or index < 0):
            return -1

        if (not isinstance(self.contents[index], consumableItem)):
            return -1
        else:
            self.contents[index].use()

    def useConsumable(self, index, amount):
        if (len(self.contents) <= index or index < 0):
            return -1

        if (not isinstance(self.contents[index], consumableItem)):
            return -1
        else:
            self.contents[index].use(amount)

    def useUsable(self, index):
        if (len(self.contents) <= index or index < 0):
            return -1

        if(not isinstance(self.contents[index], usableItem)):
            return -1
        else:
            self.contents[index].use()


    def displayStatus(self):
        print("The current weight is:", self.currentWeight, "out of", self.weightLimit)
        print("The current volume is:", self.currentVolume, "out of", self.volumeLimit)
        print("The contents are:")
        self.getContents()

    def displayItemStatus(self, index):
        self.contents[index].displayStatus()
