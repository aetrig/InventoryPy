from item import item

# Stan zużycia na poziomie równy lub poniżej zera oznacza, że przedmiot jest zużyty

class consumableItem(item):
    __durability: float = None
    def __init__(self, itemName, volume, weight, durability):
        super().__init__(itemName, volume, weight)
        if(durability <= 0):
            return -1
        else:
            self.__durability = durability

    # def use(self):
    #     self.__durability = 0
    #     self.__weight = 0


    # co jeśli chcemy użyć więcej niż mamy?
    def use(self):
        print("Enter amount to use up:")
        amount = float(input())
        if(amount <= 0):
            return -1;

        ratio = 1.0 - amount/self.__durability
        self._item__weight = self._item__weight * ratio if amount < self.__durability else 0
        self.__durability = self.__durability - amount if amount < self.__durability else 0

    def name(self):
        return self._item__itemName + " (consumable) " + "uses left: " + str(self.__durability)
