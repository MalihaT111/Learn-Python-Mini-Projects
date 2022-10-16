import random
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
def game ():
    print("Welcome to rock, paper, scissors!")
    user = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
    computer = random.randint(0,2)
    if user == '0':
        print("You chose:" + rock)
        if computer == 0:
            print("Computer chose:" + rock)
            again = input("Draw. Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
        elif computer==1:
            print("Computer chose: " + paper)
            again = input("You lose. Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
        elif computer==2:
            print("Computer chose: " + scissors)
            again = input("You win! Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()

    elif user == '1':
        print("You chose:" + paper)
        if computer == 0:
            print("Computer chose:" + rock)
            again = input("You win! Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
        elif computer==1:
            print("Computer chose: " + paper)
            again = input("Draw. Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
        elif computer==2:
            print("Computer chose: " + scissors)
            again = input("You lose. Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()

    elif user == '2':
        print("You chose:" + scissors)
        if computer == 0:
            print("Computer chose:" + rock)
            again = input("You lose. Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
        elif computer==1:
            print("Computer chose: " + paper)
            again = input("You win! Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
        elif computer==2:
            print("Computer chose: " + scissors)
            again = input("Draw. Try again? Press 'Y' to continue.\n")
            if again == 'Y':
                game()
    else: 
        input("Invalid input. Try again? Press 'Y' to continue.\n ")
        if again == 'Y':
            game()
game()