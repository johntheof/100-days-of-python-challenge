print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

#first method that does not check other options, my initial try
# print('Welcome to the treasure island!')
# print('Your mission is to find the treasure.')
# direction = (input("You're at a cross road. Where do you want to go? Type 'left' or 'right '"))
# direction_lower = str(direction.lower())
# if direction_lower == 'right':
#     print('Sorry, game over.')
# else:
#     swim_or_wait = (input("You come to a lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. "))
#     swim_or_wait_lower = str(swim_or_wait.lower())
#     if swim_or_wait_lower == 'swim':
#         print('Sorry, game over.')
#     else:
#         door_selection = (input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? "))
#         door_selection_lower = str(door_selection.lower())
#         if door_selection_lower == 'red' or door_selection_lower == 'blue':
#             print('Sorry, game over.')
#         else:
            # print('You win!')

#in all above code, we're not checking for other inputs. We are assuming the user will type

#second method that checks all other options

print('Welcome to the treasure hunt.')
print('Your mission is to find the treasure.')
direction = (input("You're at a cross road. Where do you want to go? Type 'left' or 'right '")).lower()
if direction == 'left':
    swim_or_wait = (input("You come to a lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")).lower()
    if swim_or_wait == 'wait':
        door_selection = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if door_selection == 'red':
            print('You have entered a game full of fire. Game over')
        elif door_selection == 'yellow':
            print('You found the treasure your win!')
        elif door_selection == 'blue':
            print('You have jumped in an ocean full of sharks. Game over.')
        else:
            print('Door does not exist. Game over.')
    elif swim_or_wait == 'swim':
        print('You got attacked by an angry trout. Game over')
    else:
        print('You have selected an option that deos not exist. Game over.')
elif direction == 'right':
    print('You fell into a hole. Game over.')
else:
    print('you have selected a direction that does not exist. Game over.')