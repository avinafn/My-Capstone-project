import turtle
import random
import time

# Sets up the screen
screen = turtle.Screen()

# Create two turtles: one for drawing the hangman, another for displaying messages
t = turtle.Turtle()
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, 200)

score = 0
words = ["responsibility","cycle","jazz","oxygen","rhythm","quiz","strength","equip","gossip","wizard","zombie", "wavy", "pizza","galaxy", "chair", "table", "computer", "airpods", "shoes", "book", "bottle", "nail", "marker", "cup", "tea", "coffee", "vase", "tie", "jacket"]
correct_guess = random.choice(words)

def show_message(message):
    message_turtle.write(message, align="center", font=("Arial", 14, "normal"))
    time.sleep(3)
    message_turtle.clear()
def show_less(message):
    message_turtle.write(message, align="center", font=("Arial", 14, "normal"))
    time.sleep(1)
    message_turtle.clear()

def draw_hangman(max_guesses):
    if max_guesses == 8:
        # Draw head
        t.speed("fastest")
        t.up()
        t.goto(10,50)
        t.down()
        t.circle(50)
        #current location(10,50)
    if max_guesses == 7:
        #draw eyes
        t.up()
        t.goto(40,52)
        t.color("blue")
        t.begin_fill()
        t.down()
        t.circle(5)
        t.end_fill()
        t.up()
    if max_guesses == 6:
        t.goto(70,52)
        t.begin_fill()
        t.down()
        t.circle(5)
        t.end_fill()
        #current location(70,52)
    if max_guesses == 5:
        #draw lips
        t.up()
        t.color("black")
        t.goto(50,20)
        t.down()
        t.left(90)
        t.forward(31)
       #current location(-40,20)
    if max_guesses == 4:
        #draw body line
         t.left(180)
         t.up()
         t.goto(64,20)
         t.left(90)
         t.goto(64,0)
         t.down()
         t.forward(170)
         #current location(64,-170)
    if max_guesses == 3:
        #draw right leg
         t.right(30)
         t.forward(70)
    if max_guesses == 2:
        #draw left leg
         t.up()
         t.goto(64,-170)
         t.left(60)
         t.down()
         t.forward(70)    
    if max_guesses == 1:
        #draw left arm
        t.up()
        t.goto(64,-170)
        t.right(210)
        t.forward(130)
        t.right(90)
        t.down()
        t.forward(80)
    if max_guesses == 0:
        #draw right arm
        t.left(180)
        t.forward(160)
        t.clear()

def create_base():
    show_message("Welcome to the Hangman game, guess letters to create the correct word")
    # Create the base of the hangman
    #creates the unchangable part of the visual
    t.color("black")
    t.up()
    t.goto(60,150)
    t.down()
    t.left(180)
    t.forward(150)
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(80)
    t.left(180)
    t.forward(160)
    t.up()
    t.goto(60,150)
    t.right(90)
    t.down()
    t.forward(50)
    #coordinates at this point: (60,100)
  


def play_game():
    global score
    t.reset()
    t.hideturtle()
    
    # Ask the user for their permission
    name = turtle.textinput("Welcome", "do you want to start the game?").lower()
    create_base()
    
    repetition = []
    max_guesses = 9
    correct_guess = random.choice(words)
    length = len(correct_guess)
    progress = length * "_"
    show_message("Your word has " + str(length) + " characters")

    while max_guesses > 0 and progress != correct_guess:
        guess = turtle.textinput(progress, "guess a letter?")
        if guess in correct_guess:
            for i in range(length):
                if correct_guess[i] == guess:
                    progress = progress[:i] + guess + progress[i + 1:]
                    print(progress)
                    show_less(progress)
            repetition.append(guess)
        elif guess in repetition:
            show_less("You have already tried this letter")
        else:
            show_less("Wrong letter")
            repetition.append(guess)
            max_guesses -= 1
            draw_hangman(max_guesses)
            if max_guesses >=1:
                show_less("You can try " + str(max_guesses) + " more times")
            
                
        
            
    if progress == correct_guess:
        show_message("Well done! You guessed -" + str(correct_guess) + "- correctly =)")
        score += 1
        show_message("Your score is: " +str(score))
        user = turtle.textinput("input", "do you want to play again?").lower()
        if user == "yes":
            play_again()
            
        
    else:
        show_message("Game Over :( The correct word was: " + str(correct_guess))
        show_message("your score is: " +str(score))
        user = turtle.textinput("input", "do you want to play again?").lower
        if user == "yes":
            play_again()

        
def play_again():
    t.clear()
    message_turtle.clear()
    play_game()
    

play_game()
play_again()
