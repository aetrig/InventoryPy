from backpack import backpack
from item import item
from consumableItem import consumableItem
from equippableItem import equippableItem
from usableItem import usableItem

test = backpack(20, 17)

test.getContents()
print()
test.insert(item("kamien", 1, 5))
#test.insert(consumableItem("woda", 3, 2))
test.insert(usableItem("notatka", 1, 1))
test.insert(equippableItem("miecz", 7, 3))
test.insert(equippableItem("łopata", 7, 3))
test.getContents()

