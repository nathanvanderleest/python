
# Hero's Inventory 2.0
# Demonstrates tuples

# create an empty tuple
inventory = ()

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potions")

# print each element
print("\nYour items:")
for item in inventory:
    print(item)


# get the length of the tuple
print("\nYou have", len(inventory), "items in your inventory")

# test for membership with in
if "healing potions" in inventory:
    print("\nYou have potions")

# display one item through an index
index = int(input("\nEnter the index for an item:"))
print("Index", index, "has", inventory[index])

# create new tuple
chest = ("gold","gems")
print("\nYou find a chest. It contains:")
print(chest)
print("Adding chest contents your inventory...")
inventory += chest
print("Your inventory is now:",end=" ")
print(inventory)

# print the tuple
print("\nThe tuple inventory is:")
print(inventory)


print("\ndone")



