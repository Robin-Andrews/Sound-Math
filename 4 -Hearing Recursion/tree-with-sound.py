from gturtle import *
from music import *

def tree(branchLen,t):
    '''
    Main recursive function.
    Note the base case which allows the program to 
    eventually stop.
    '''
    if branchLen > 5:
        t.forward(branchLen)
        Play.midi(Note(60, branchLen/100.0))
        t.right(25)
        tree(branchLen-20,t)
        t.left(50)
        tree(branchLen-20,t)
        t.right(25)
        t.back(branchLen)
        Play.midi(Note(58, branchLen/100.0))

def main():
    # Get things ready
    Play.setInstrument(35)
    frame = TurtleFrame()
    t = Turtle(frame)
    t.clean("black")
    # play with this speed to see how it helps your understanding
    # of what's going on. Try -1 for "as fast as possible," other numbers 
    # are pixels per second
    t.speed(-1)
    t.pu()
    t.bk(100)
    t.pd()
    t.setPenColor("green")
    tree(100,t)
    
main()
