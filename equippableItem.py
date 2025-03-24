from item import item

class equippableItem(item):

    def __init__(self, itemName, volume, weight):
        super().__init__(itemName, volume, weight)

    def name(self):
        return self._item__itemName + " (equippable)"
    
    def use(self):
        pass
