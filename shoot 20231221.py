import pgzrun

from pgzrun import *
from random import randint

#Create an actor
apple = Actor("apple")

# Set the update interval in frames (60 frames per second)
update_interval = 60
timer = update_interval

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)

place_apple()

def update():
    global timer

    # Decrement the timer on each frame
    timer -= 1

    # When the timer reaches zero, update the apple's position and reset the timer
    if timer <= 0:
        place_apple()
        timer = update_interval


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()


pgzrun.go()
    
