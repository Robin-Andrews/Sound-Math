# Sonify a square 1
from gturtle import *
from music import *

# Create a turtle and name it "bob" 
# If your teacher complains about the lowercase "b" then tell them you have good reason
bob = Turtle()

# Set speed
#bob.speed(-1)

# Set background color
bob.clean("black")

# Choose instrument
Play.setInstrument(XYLOPHONE)

# Initial position
bob.penUp()
bob.moveTo(-100, 100)
bob.right(135)
bob.penDown()

# Top of square
for x in range(200/5):
   bob.forward(5)
   Play.midi(Note(bob.getY()+ 200, 0.5))
   
# Right-hand edge
bob.right(90)
for x in range(200/5):
   bob.forward(5)
   print bob.getY()
   Play.midi(Note(bob.getY() + 200, 0.5))
   
# Bottom of square
bob.right(90)
for x in range(200/5):
   bob.forward(5)
   Play.midi(Note(bob.getY()+ 200, 0.5))
   
# Left-hand edge
bob.right(90)
for x in range(200/5):
   bob.forward(5)
   print bob.getY()
   Play.midi(Note(bob.getY() + 200, 0.5))
   
# Can you use your knowledge of loops and/or function to make this program quite a bit shorter?


