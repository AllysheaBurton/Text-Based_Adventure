# Allyshea Burton

# Define introduction and rules
def intro():
    print("\t\tWelcome to The Babysitter Text Adventure Game\n\n"
          "Rules:\n\tYou must go through each room and collect all 6 play items, or face the boredom wrath of the Thompson triplets!\n\n"
          "Move commands:\n\t\"North.\" \"South.\" \"East.\" \"West.\"\n\n"
          "Searched items:\n\tBoard Games, Building Blocks, Coloring Books, Hula Hoops, Playing Cards, Video Games\n\n"
          "Type to add into inventory: Get \'item name\'\n\n"
          f"Type 'Exit' to leave game.\n{'-' * 50}\n\n")


# Display intro and rules
intro()

# Define main function of the game
def main():
    # Dictionary map of rooms and allocated items
    rooms = {
        "foyer": {"name": "foyer", "north": None, "south": None, "east": "living room", "west": None},
        "living room": {"name": "living room", "north": "kitchen", "south": "bathroom", "east": "closet",
                        "west": "foyer", "item": "video games"},
        "kitchen": {"name": "kitchen", "north": None, "south": "living room", "east": "laundry room", "west": None,
                    "item": "hula hoops"},
        "bathroom": {"name": "bathroom", "north": "living room", "south": None, "east": "kids' bedroom",
                     "west": "parent's room", "item": "coloring books"},
        "parent's room": {"name": "parent's room", "north": None, "south": None, "east": "bathroom", "west": None,
                          "item": "playing cards"},
        "closet": {"name": "closet", "north": "laundry room", "south": None, "east": None, "west": "living room",
                   "item": "board games"},
        "laundry room": {"name": "laundry room", "north": None, "south": "closet", "east": None, "west": "kitchen",
                         "item": "building blocks"},
        "kids' bedroom": {"name": "kids' bedroom", "north": None, "south": None, "east": None, "west": None}
    }

    # Location at the start of game
    current_room = "foyer"

    # Start of inventory list
    inventory = []

    # Movement or choice of the user
    action = ""

    # Defines function of user's current room location and inventory status
    def display_status():
        print(f"\nYou are in the {current_room}\nInventory {inventory}")
        if 'item' in rooms[current_room] != None:
            print('You see {}'.format(rooms[current_room]['item']))

    # Game loop
    while True:
        # Provide updated room location and inventory
        display_status()
        print(f"{'-' * 30}")
        # Request input move of the user
        action = input("Enter your move: \n").lower()
        # Verify if user wants to exit game
        if action == "Exit".lower():
            print("\nThe game wasn\'t finished!\n""\t\tGame over")
            # Exit game if user wants to quit
            break

        # Verify if requested action is a valid movement for current room
        if action in rooms[current_room]:
            # Check if action leads to another room
            if rooms[current_room][action] is not None:
                # Update current room
                current_room = rooms[current_room][action]
                # Continue loop
                continue
            else:
                # Output if user can not utilize direction in current room
                print("That\'s a wall!")

        # Verify if user action is to "get" an item present in the current room.
        elif (('item' in rooms[current_room]) and ('get ' + rooms[current_room]['item'] == action)):
            # Add roo item into inventory list.
            inventory.append(rooms[current_room]['item'])
            # Output that the item has been successfully retrieved.
            print(f"{rooms[current_room]['item']} retrieved!")
            # Delete item from current to prevent it from being picked up again.
            del rooms[current_room]['item']

        else:
            # Output if the input of the user is not understood
            print("What?")

        # Villain encounter
        if current_room == "kids' bedroom":
            # Check if the inventory has all 6 items
            if len(inventory) == 6:
                print("\nYOU CAN\'T GET OUT!!\n"
                      "\nYou see the triplets restless, bored, and ready to for trouble.\n"
                      "Luckily, you have come prepared...\n"
                      "Congratulations! You\'ve collected all of the items to occupy the triplets\' time.\n\n"
                      "\t\tGAME OVER")
                # Exit the loop as the game is won
                break
            # If the inventory does not have all 6 items
            else:
                print("\nYOU CAN\'T GET OUT!!\n"
                      "\nThe triplets are restless, bored, and ready for trouble.\n"
                      "You hear the triplets chant \"I\'m bored\" as they rip up the carpet and terrorize the cat.\n"
                      "You didn\'t collect all of the items to keep the triplet\'s boredom at bay.\n\n"
                      "\t\tYOU LOSE!\n\n"
                      "\t\tGAME OVER")
                # Exit the loop as the game is lost
                break

# Calls main function to start the game
main()