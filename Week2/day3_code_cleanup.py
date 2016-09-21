# Inventory Tracker RPG

# Player
# Inventory
# Items

player = {"inventory": {"red potion": {"quantity": 20}}}

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
        item_name = input("What is this item called?\n>")
        item_quantity = int(input("How many?\n>"))
        player["inventory"][item_name] = {"quantity": item_quantity}
    elif choice == "i":
        print ("Looking at inventory")
        for item in player["inventory"].keys():
            quantity = player["inventory"][item]["quantity"]
            print ("{} - {}".format(item, quantity))
