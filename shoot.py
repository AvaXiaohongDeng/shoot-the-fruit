import pgzrun
from random import randint

# Create actors for apple, strawberry, and kiwi
apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")

# Set the initial actor to apple
current_actor = apple

# Set the update interval in frames (60 frames per second)
update_interval = 60
timer = update_interval

def draw():
    screen.clear()
    current_actor.draw()

def place_actor():
    current_actor.x = randint(10, 800)
    current_actor.y = randint(10, 600)

place_actor()

def update():
    global timer

    # Decrement the timer on each frame
    timer -= 1

    # When the timer reaches zero, update the actor's position
    if timer <= 0:
        place_actor()
        timer = update_interval

def on_mouse_down(pos):
    global current_actor
    if current_actor.collidepoint(pos):
        print("Good shot!")
        place_actor()
        # Switch to the next actor immediately after a successful shot
        if current_actor == apple:
            current_actor = pineapple
        elif current_actor == pineapple:
            current_actor = orange
        else:
            current_actor = apple
    else:
        print("You missed!")
        #quit()
        exit()  # Close the game window when a shot is missed

pgzrun.go()
