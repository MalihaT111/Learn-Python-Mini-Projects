print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
def wrongdirection():
    print("You chose your own path. Commendable! But goes againt the game :C\nThus:")

def restart():
    restart = input("\nGame over. Would you like to start again? Type \"R\" to restart.\n")
    if restart == "R" or restart == 'r' or restart == 'restart' or restart == "RESTART":
        start()

def start ():
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 

  crossroad= input("You're at a crossroad. Where do you want to go? You hear nothing on the left and roars on the right. Type \"left\" or \"right\"\n")

  if crossroad == 'left' or crossroad == 'Left' or crossroad == 'L' or crossroad == 'l' or crossroad == 'LEFT':
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")

    if lake == "wait" or lake == 'w' or lake == 'Wait' or lake == "W" or lake == "WAIT":
      color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one green. Which color do you choose?\n")

      if color == "red" or color == 'r' or color == 'Red' or color == "R" or color == 'RED':
        print("Behind this door is a raging hot fire. Surprise! You have been scorched to death.")
        restart()

      elif color == 'yellow' or color == 'y' or color == "Y" or color == "YELLOW" or color == "Yellow":
        print("Did the color clue you in? After all, gold can be described as yellow. Congratulations!\nYou found the treasure!")
        restart()

      elif color == 'green' or color == "GREEN" or color == "G" or color == "Green" or color == "g":
        print("Sorry dude. That's where we keep our pet bear...anyway, you've been mauled to death. Sorry!")
        restart()
      
      else:
        wrongdirection()
        restart()

    elif lake == "swim" or lake == 'Swim' or lake == 'S' or lake == 's' or lake == "SWIM":
        print("This lake is home to a sea dragon. Bet ya didn't know that did you? Anyway you're dead.")
        restart()

    else:
        wrongdirection()
        restart()

  elif crossroad == 'right' or crossroad == 'RIGHT' or crossroad == 'r' or crossroad == 'R' or crossroad == "Right":
      print("You approach a minotaur. It takes one look at you and decides that you're too dumb to be left alive. Like couldn't you hear his bellows? Thus, in one swift move, it impales you with its horns. You are dead.")
      restart()

  else :
        wrongdirection()
        restart()

start()
                
  