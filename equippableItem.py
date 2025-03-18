from item import item

class equippableItem(item):

    def __init__(self, itemName, volume, weight):
        super().__init__(itemName, volume, weight)

    def name(self):
        return self.itemName + " (equippable)"