import random
option = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors. '))
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")

computer_select = random.randint(0,2)
list = [rock,paper,scissors]

print(f'You have selected {list[option]}')

print(f'Computer has selected {list[computer_select]}')

if option >= 3 or option <0:
    print('You typed an invalid number, you lose!')
elif option == 0 and computer_select == 2:
    print('You win')
elif computer_select ==0 and option == 2:
    print('You lose!')
elif computer_select > option:
    print('You lose.')
elif option > computer_select:
    print('You win.')
elif option == computer_select:
    print('It\' a draw.')