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
mass = float(input())
print("Enter inventory max space:")
space = float(input())

inv = inventory(space+100, mass+100) #+100 do testow

inv.insert(item("rock", 10, 10))
inv.insert(usableItem("note", 1, 1))
inv.insert(consumableItem("bottle", 5, 10, 100))
inv.insert(equippableItem("shovel", 40, 20))
inv.insert(equippableItem("sword", 10, 15))

work = True

while(work):
	print()
	inv.displayStatus()
	print()
	print("Press 0 to exit the program, 1 to insert an item, 2 to remove an item, 3 to use an item, 4 to get details about an item")
	action = int(input())
	match action:
		case 0:
			work = False
		case 1:
			print("Enter item type (1. normal, 2. equippable, 3. consumable, 4. usable, 5. note):")
			type = int(input())
			match type:
				case 1:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = float(input())
					print("Enter item volume:")
					volume = float(input())
					inv.insert(item(name, volume, weight))
				case 2:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = float(input())
					print("Enter item volume:")
					volume = float(input())
					inv.insert(equippableItem(name, volume, weight))
				case 3:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = float(input())
					print("Enter item volume:")
					volume = float(input())
					print("Enter item durability")
					durability = float(input())
					inv.insert(consumableItem(name, volume, weight, durability))
				case 4:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = float(input())
					print("Enter item volume:")
					volume = float(input())
					inv.insert(usableItem(name, volume, weight))
				case 5:
					print("Enter item name:")
					name = input()
					print("Enter item weight:")
					weight = float(input())
					print("Enter item volume:")
					volume = float(input())
					inv.insert(note(name, volume, weight))
				case _:
					print("Incorrect option")
		case 2:
			print("Enter id of the item to remove:")
			id = int(input())
			inv.remove(id)
		case 3:
			print("Enter id of an item to use")
			id = int(input())
			inv.useItem(id)
		case 4:
			print("Enter id of an item to inspect")
			id = int(input())
			inv.displayItemStatus(id)
		case _:
			print("Incorrect option")