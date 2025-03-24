from item import item

# Poszczególne typy użycia w klasach dziedziczących

class usableItem(item):
    def __init__(self, itemName, volume, weight):
        super().__init__(itemName, volume, weight)

    def use(self):
        print("Item ", self._item__itemName, " has been used.", sep = "")

    def name(self):
        return self._item__itemName + " (usable)"
