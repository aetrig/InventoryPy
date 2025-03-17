import item

# Poszczególne typy użycia w klasach dziedziczących

class usableItem(item):
    def __init__(self, name, volume, weight):
        super().__init__(itemName, volume, weight)

    def use(self):
        print("Item ", self.itemName, "has been used.", sep = "")
