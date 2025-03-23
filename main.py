from backpack import backpack
from item import item
from consumableItem import consumableItem
from equippableItem import equippableItem
from usableItem import usableItem
from note import note

test = backpack(20, 17)

test.getContents()
print()
test.insert(item("kamien", 1, 5))
test.insert(consumableItem("woda", 3, 2, 100))
test.insert(usableItem("notatka", 1, 1))
test.insert(equippableItem("miecz", 7, 3))
test.insert(equippableItem("łopata", 7, 3))
test.insert(note("notatka", 1, 1))

test.equip(3)

test.useUsable(4)

test.scribbleNote(4, "Lorem ipsum dolor sit amet")

test.useUsable(4)

test.clearNote(4)

test.useUsable(4)

test.displayItemStatus(0)

test.displayItemStatus(1)

test.displayItemStatus(2)

test.displayItemStatus(3)

test.displayStatus()

