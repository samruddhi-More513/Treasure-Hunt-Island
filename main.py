import time
import os
def clear_screen():
    os.system('cls')  

clear_screen()
print("\nOpening the door...")
time.sleep(1.5)


while True:
  
   print(r'''
___________                                                     ___ ___               __   
\__    ___/______   ____ _____    ________ _________   ____    /   |   \ __ __  _____/  |_ 
  |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  /    ~    \  |  \/    \   __\
  |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  \    Y    /  |  /   |  \  |  
  |____|   |__|    \___  >____  /____  >____/ |__|    \___  >  \___|_  /|____/|___|  /__|  
                       \/     \/     \/                   \/         \/            \/  
''')
   
   
   print("Welcome to Treasure Island.")
   time.sleep(1)
   print("\n")
   print("Your mission is to find the treasure.")
   start = (input("okay lets start! you are standing at the cross road!\nWhich path would you like to choose? \nLeft or Right?\n")).lower()

   if start not in ["left","right"]:
    print("\nInvalid Direction! Please choose between the Given choices")
    continue 
   if start == "left": 
    river= input("\nTheres a river infront! So would you like to take the boat or swim across?\n").lower()

    if river not in ["boat", "swim"]:
            print("\nInvalid choice! Try again.")
            continue
    
    if river== "boat":
        door = input("\nHeres the boat!\nFinally you are at the island but there are three doors over here!\nWhich one will you choose? Red, Yellow Or Green?\n").lower().strip()
        if door == "yellow":
            print("Lets see whats behind the door", end="", flush=True)

            for i in range(3):
              time.sleep(1)
              print(".", end="", flush=True)
            
            time.sleep(1)
            print("\n")
            
            print("\nOhhh yeah!! 💰💰The Treasure Found💰💰\nYou Won!🎉\nCONGRATULATIONS!!!!🎉🎉")
            print(r''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
******************************************************************************* ''')
        elif door in ["red", "green"]:
        
          result = {"red": "Ohh No you fell into fire!🔥🔥🔥 \n Game Over!",
                    "green": "OMG Snakes!🐍🐍🐍\n Game Over! " }
          print("You chose the door", end="", flush=True)

          for i in range(3):
           time.sleep(0.5)
           print(".", end="", flush=True)
            
          time.sleep(1)
          print(f" {result[door]}")
          
              
        else:
         print("\nInvalid door choice!")
         continue
    elif river == "swim":
        print("Okay! You jumped in", end="",flush=True)
        for i in range(3):
         time.sleep(0.5)
         print(".", end="",flush=True) 
         
         time.sleep(0.3)
        print("Oh no you are drowned!🌊😵\n YOU LOST TRY AGAIN!")
        
   elif start == "right":
    print("You are walking on the road", end="",flush=True)
    for i in range(3):
         time.sleep(0.5)
         print(".", end="",flush=True) 
         
         time.sleep(0.3)
    print("Oops! 🌲🌫️you got lost in forest\n Game Over!!") 
   

   play_again = input("\nPlay again? (yes/no)\n").lower()
   time.sleep(1)
   clear_screen()

   if play_again != "yes":
    print("\nThanks for playing!")
    break
