class Backpack():

    __currentWeight = 0
    __currentVolume = 0
    __contents = []
    equippedItem # slot na wyekwipowany przedmiot

    def __init__(self, volumeLimit, weightLimit):
        self.__volumeLimit = volumeLimit
        self.__weightLimit = weightLimit

    # wkładamy do środka obiekt (na koniec listy)
    def insert(self, item):
        if (item.weight < self.weightLimit - self.weight and item.volume < self.volumeLimit - self.weightLimit):
            self.__contents.append(item)
            self.__currentVolume += item.Volume
            self.__currentWeight += item.Weight
        else:
            return -1

    # wyciągnięcie przedmiotu z plecaka odbywa się poprzez podanie indeksu na którym przedmiot się znajduje
    def remove(self, index):
        if(len(self.____contents) >= index):
            self.__currentVolume -= item.Volume
            self.__currentWeight -= item.Weight
            return self.__contents.pop(index)
        else:
            return -1;

    # pozwala na wypisanie zawartości plecaka wraz z indeksem
    def getContents(self):
        for index in range(len(self.__contents)):
            print(index, ". ", self.__contents[index].itemName, sep="")

    # pozwala na wyekwipowanie przedmiotu (przedmiot uprzednio wyekwipowany wraca do plecaka)
    def equip(self, index):
        if(len(self.__contents) >= index and isinstance(self.__contents[index], equippedItem)):
            if(equippedItem is not None):
                self.__contents.append(equippedItem)
            equippedItem = self.__contents.pop(index)