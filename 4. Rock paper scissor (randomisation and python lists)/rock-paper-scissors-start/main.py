rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user_choice = int(input("What do you choose ? Type 0 for rock ,1 for paper, 2 for scissors."))

comp_choice = random.randint(0,2)
if user_choice >=3 or user_choice < 0:
  print("you entered a number out of range")
else:
  li = [rock,paper,scissors]

  print(li[user_choice])
  print("Comp Chose:")
  print(li[comp_choice])


  if user_choice == 0 and comp_choice == 2:
    print("You win!")
  elif comp_choice == 0 and user_choice == 2:
    print("You lose")
  elif comp_choice == 0 and user_choice == 1:
    print("You win")
  elif comp_choice > user_choice:
    print("You lose")
  elif comp_choice == user_choice:
    print("it's a draw")

