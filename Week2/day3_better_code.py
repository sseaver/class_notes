# Better file to edit!
# Inventory Tracker RPG

def add_to_inventory(player):
    item_name = input("What is this item called?\n>")
    item_quantity = int(input("How many?\n>"))
    if item_name in player["inventory"].keys():
        # updating quantity of existing item
        player["inventory"][item_name]["quantity"] += item_quantity
    else:
        # adding brand new item to inventory with quantity
        player["inventory"][item_name] = {"quantity": item_quantity}

def inspect_inventory(player):
    for item in player["inventory"].keys():
        quantity = player["inventory"][item]["quantity"]
        print ("{} - {}".format(item, quantity))

def player_input(player, choice):
    if choice == "a":
        add_to_inventory(player)
    elif choice == "i":
        inspect_inventory(player)

def make_character():
    player = {"inventory": {"red potion": {"quantity": 20}}}
    player_name = input("Welcome traveler! What do you call yourself?\n>")
    player["name"] = player_name
    return player

###########################################################

player = make_character()

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")
    player_input(player, choice)
