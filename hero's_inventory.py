
# Hero's Inventory
# Demonstrates tuple creation

# create an empty tuple
inventory = ()


# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("Press enter: ")


# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potions")

# print the tuple
print("\nThe tuple inventory is:")
print(inventory)

# print each element
print("\nYour items:")
for item in inventory:
    print(item)

print("done")



