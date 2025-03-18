from equippableItem import equippableItem

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
            if(equippedItem is not None):
                self.contents.append(equippedItem)
            equippedItem = self.contents.pop(index)