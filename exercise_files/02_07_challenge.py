import os
import time
import math
from termcolor import colored

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas    = canvas
        self.trail     = '.'
        self.mark      = '*'
        self.framerate = 0.2
        self.pos       = [ 0, 0 ]
        self.direction = [ 1, 0 ]          # Pointing right

    def up(self):
        self.direction = [ 0, -1 ]
        self.forward()
   
    def down(self):
        self.direction = [ 0, 1 ]
        self.forward()

    def right(self):
        self.direction = [ 1, 0 ]
        self.forward()

    def left(self):
        self.direction = [ -1, 0 ]
        self.forward()

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

    def drawSquare( self, size, x, y ):
        self.canvas.clear()
        self.pos = [ x, y ]
        print (f"Drawing a square of size {size} at {x},{y}")
        for i in range(0, size):
            self.right()
        for i in range(0, size):
            self.down()
        for i in range(0, size):
            self.left()
        for i in range(0, size):
            self.up()

    def forward( self ):
        newPos = [ self.pos[0] + self.direction[0], self.pos[1] + self.direction[1] ]
        if not self.canvas.hitsWall(newPos):
            self.pos = newPos
            self.draw(self.pos)
        
    def setDirection ( self, angle ):
        radians = angle / 180.0 * 3.14159265
        self.direction = [ math.sin(radians), -1 * math.cos(radians)]
        

# Create a new Canvas instance that is 30 units wide by 30 units tall 
canvas = Canvas(30, 30)

# Create a new scribe and give it the Canvas object
scribe = TerminalScribe(canvas)
scribe.pos = [10,10]
for i in range ( 0, 4 ):
    scribe.setDirection( i * 50 )
    for j in range (7):
        scribe.forward()


#scribe.drawSquare( 15, 3, 3 )
