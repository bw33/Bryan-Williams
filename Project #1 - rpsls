# Program for rock, paper, lizard, scissors, spock
##########################################################


import random

# Assigning numerical values to each choice
def name_to_number(name):
    if name == "rock":
        name = 0
    elif name == "spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        print "Error!"
    return name


# Assigning a choice to each numerical value
def number_to_name(number):
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "scissors"
    else:
        print "Error!"
    return number


# Functions that determine if the player or computer wins based on modular arithmetic
def rpsls(player_choice):
    if player_choice == "rock":
        player_number = name_to_number("rock")
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        final_number = (((player_number - comp_number) - 5) % 5)        
        print "Player chooses " + player_choice
        print "Computer chooses " + comp_choice
        if final_number == 0:
            print "It's a draw!"
        elif final_number == 1:
            print "Player wins!"
        elif final_number == 2:
            print "Player wins!"
        elif final_number == 3:
            print "Computer wins!"
        elif final_number == 4:
            print "Computer wins!"
                  
    elif player_choice == "spock":
        player_number = name_to_number("spock")
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        final_number = (((player_number - comp_number) - 5) % 5)
        print "Player selects " + player_choice
        print "Computer chooses " + comp_choice
        if final_number == 0:
            print "It's a draw!"
        elif final_number == 1:
            print "Player wins!"
        elif final_number == 2:
            print "Player wins!"
        elif final_number == 3:
            print "Computer wins!"
        elif final_number == 4:
            print "Computer wins!"
            
    elif player_choice == "paper":
        player_number = name_to_number("paper")
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        final_number = (((player_number - comp_number) - 5) % 5)
        print "Player selects " + player_choice
        print "Computer chooses " + comp_choice
        if final_number == 0:
            print "It's a draw!"
        elif final_number == 1:
            print "Player wins!"
        elif final_number == 2:
            print "Player wins!"
        elif final_number == 3:
            print "Computer wins!"
        elif final_number == 4:
            print "Computer wins!"
            
    elif player_choice == "lizard":
        player_number = name_to_number("lizard")
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        final_number = (((player_number - comp_number) - 5) % 5)
        print "Player selects " + player_choice
        print "Computer chooses " + comp_choice
        if final_number == 0:
            print "It's a draw!"
        elif final_number == 1:
            print "Player wins!"
        elif final_number == 2:
            print "Player wins!"
        elif final_number == 3:
            print "Computer wins!"
        elif final_number == 4:
            print "Computer wins!"
            
    elif player_choice == "scissors":
        player_number = name_to_number("scissors")
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        final_number = (((player_number - comp_number) - 5) % 5)
        print "Player selects " + player_choice
        print "Computer chooses " + comp_choice
        if final_number == 0:
            print "It's a draw!"
        elif final_number == 1:
            print "Player wins!"
        elif final_number == 2:
            print "Player wins!"
        elif final_number == 3:
            print "Computer wins!"
        elif final_number == 4:
            print "Computer wins!"
    return ""

# Prints the results of each of player's choice based on a computer ramdomly generated choice
print rpsls("rock")
print rpsls("spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")
