# Guess the Number Game

# Import the module
import simplegui
import random

# Define global variables (program state)
print "Instructions!"
print "_____________"
print ""
print "Pick a number range, i.e. from 1-100 or 1-1000."
print "The goal of the game is to guess correctly the number"
print "that the computer randomly picks. You get 7 chances"
print "to guess the number for the first game and 10 chances"
print "to guess the number for the second game. Good luck!"
secret_number = 0


# Define event handler functions

    
def new_game():
    print ""
    print "Step right up and guess the number!"
    input_guess
              
def secret_number():
    global secret_number
    secret_number = random.randrange(0, 101)
    global counter
    counter = 7
    global min
    min = 0
    global max
    max = 100
    new_game()
    
def secret_number2():
    global secret_number
    secret_number = random.randrange(0,1001)
    global counter
    counter = 10
    global min
    min = 0 
    global max
    max = 1000
    new_game()
    
def input_guess(guess):
    global counter
    counter = counter - 1
    counter2 = str(counter)
    guess2 = int(guess)
    print ""
    print "Your guess is: " + guess
    if counter == 0:
        print "Game over! You lose! Please start another game!"
    elif guess2 < min:
        print "Error, please choose a number within range."
        print "Number of tries: " + counter2
    elif guess2 > max:
        print "Error, please choose a number within range."
        print "Number of tries left: " + counter2
    elif guess2 < secret_number:
        print "Higher!"
        print "Number of tries left: " + counter2
    elif guess2 > secret_number:
        print "Lower!"
        print "Number of tries left: " + counter2
    elif guess2 == secret_number:
        print "Awesome! Good job guessing correctly. Play again!"
        print "Please choose, again, one of the game modes..."
        
# Create a frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# Register event handlers
frame.add_button("0-100", secret_number, 100)
frame.add_button("0-1000", secret_number2, 100)
frame.add_input("Number Game!", input_guess, 100)

# Start frame and timers
frame.start()
