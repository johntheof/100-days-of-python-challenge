import random
option = input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors.')
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
---.__(___)
""")

computer_select = random.randint(2)
print(computer_select)

