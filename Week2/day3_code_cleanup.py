# Inventory Tracker RPG

# Player
# Inventory
# Items

player = {"inventory": {}}

{
    "red potion": {
        "quantity": 1
    }

}
player_name = input("Welcome traveler! What do you call yourself?\n>")
player["name"] = player_name
print (player)

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")
    if choice == "a":
        print ("Adding item to inventory")
    elif choice == "i":
        print ("Looking at inventory")
        print (player["inventory"])
