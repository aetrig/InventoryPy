from inventory import inventory
from item import item
from consumableItem import consumableItem
from equippableItem import equippableItem
from usableItem import usableItem
from note import note

# test = backpack(20, 17)

# test.getContents()
# print()
# test.insert(item("kamien", 1, 5))
# test.insert(consumableItem("woda", 3, 2, 100))
# test.insert(usableItem("notatka", 1, 1))
# test.insert(equippableItem("miecz", 7, 3))
# test.insert(equippableItem("łopata", 7, 3))
# test.insert(note("notatka", 1, 1))

# test.equip(3)

# test.useUsable(4)

# test.scribbleNote(4, "Lorem ipsum dolor sit amet")

# test.useUsable(4)

# test.clearNote(4)

# test.useUsable(4)

# test.displayItemStatus(0)

# test.displayItemStatus(1)

# test.displayItemStatus(2)

# test.displayItemStatus(3)

# test.displayStatus()

print("Enter inventory max mass:")
mass = int(input())
print("Enter inventory max space:")
space = int(input())

inv = inventory(space, mass)

while(True):
	print()
	inv.displayStatus()
	print()
	print("Press 1 to insert an item, 2 to remove an item")
	action = int(input())
	match action:
		case 1:
			print("Enter item type (1. normal, 2. equippable, 3. consumable, 4. usable, 5. note):")
			type = int(input())
			match type:
				case 1:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = int(input())
					print("Enter item volume:")
					volume = int(input())
					inv.insert(item(name, volume, weight))
				case 2:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = int(input())
					print("Enter item volume:")
					volume = int(input())
					inv.insert(equippableItem(name, volume, weight))
				case 3:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = int(input())
					print("Enter item volume:")
					volume = int(input())
					print("Enter item durability")
					durability = int(input())
					inv.insert(consumableItem(name, volume, weight, durability))
				case 4:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = int(input())
					print("Enter item volume:")
					volume = int(input())
					inv.insert(usableItem(name, volume, weight))
				case 5:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = int(input())
					print("Enter item volume:")
					volume = int(input())
					inv.insert(note(name, volume, weight))
				case _:
					print("Incorrect option")
		case 2:
			print("Enter id of the item to remove:")
			id = int(input())
			inv.remove(id)
		case _:
			print("Incorrect option")