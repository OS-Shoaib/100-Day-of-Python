# day 003
# 4-02-2021

def t_island():
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
     _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
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
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    f_choice = input("You are at a cross road. where do you want to go? type 'left' or 'right'. \n").lower()

    if f_choice == "left":
        s_choice = input("You came to a lake. There is an island in the meddle of the lake.\n"
                         "Type 'wait' to wait for a boat.\n"
                         "Type 'swim' to swim across.\n").lower()

        if s_choice == 'wait':
            rd_choice = input("You arrived at the island unharmed.\n"
                              "There is a house with three doors.\n"
                              "red, yellow and blue.\n"
                              "Which color do you want to choose?\n").lower()

            if rd_choice == 'yellow':
                print("You Win")
            elif rd_choice == 'blue':
                print("Eaten by beasts.")
                print("Game Over")
            elif rd_choice == 'red':
                print("Burned by fire.")
                print("Game Over")
            else:
                print("Game Over")

        else:
            print("You attacked by a trout.")
            print("Game Over")
    else:
        print("Fall into a hole.")
        print("Game Over")


if __name__ == '__main__':
    x = "y"
    while x == "y":
        t_island()
        x = input("Do you want to play again? ")
