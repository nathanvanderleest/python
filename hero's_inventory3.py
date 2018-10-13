
# Hero's Inventory 3.0
# Demonstrates tuples

# create a list with items and display it with a for loop
inventory = ["sword","armor","shield","healing potions"]
print("Your items:")
for item in inventory:
    print(item)

# get the length of the list
print("\nYou have", len(inventory), "items in your possession.")

# test for membership with in
if "healing potions" in inventory:
    print("\nYou have potions")

# display a slice
start = int(input("\nStart slice:"))
finish = int(input("Finish the slice:"))
print("Your item(s)", inventory[start:finish])

# concatenating two lists
chest = ["gold","gems"]
print("\nYou find a chest. It contains:")
print(chest)
print("Adding chest contents...")
inventory += chest
print("Your inventory is now:",end=" ")
print(inventory)

# assign by index
print("\nYou trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now:", inventory)

# assign by slice
print("\nYou trade your gold and gems for food.")
inventory[4:6] = ["food"]
print("Your inventory is now:", inventory)

# print the tuple
print("\nThe inventory is:")
print(inventory)

# deleting an element
print("\nYour shield brakes in battle.")
del inventory[2]
print("Your inventory is now:", inventory)

# delete a slice
print("\nYou crossbow and armor are stolen.")
del inventory[:2]
print("Your inventory is now:", inventory)

print("\ndone")




