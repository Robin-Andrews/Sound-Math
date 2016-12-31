# 7-edo Keyboard
## Based on code from "Making Music with Computers"
from music import *
from gui import *

Play.setInstrument(74)   # set desired MIDI instrument (0-127)

# Create gui so we can use events
d = Display("ET-7 Keyboard", 300, 200)

# lists of virtual keys and pitches corresponding to above piano keys
virtualKeys = [VK_A, VK_S, VK_D, VK_F, VK_J, VK_K, VK_L, VK_SEMICOLON]
channels = range(8)

# Create pitches - this is the forumla for 7-tone equal temperment
a = 2 ** (1/7.0)
pitches = [261.6 * (a ** n) for n in range(8)]

#Here's an alternative set of pitches based on an Indian scale - use commenting to swap
# pitches     = [60, 61, 64, 65, 67, 68, 71, 72]

keysPressed = []   # holds which keys are currently pressed

# define callback functions
def beginNote( key ):
   """Called when a computer key is pressed.  Implements the corresponding 
      piano key press (i.e., adds key-down icon on display, and starts note).
      Also, counteracts the key-repeat function of computer keyboards.
   """
   for i in range( len(virtualKeys) ):   # loop through all known virtual keys
   
      # if this is a known key (and NOT already pressed)
      if key == virtualKeys[i] and key not in keysPressed:  
             
         Play.setInstrument(74, channels[i])
         Play.noteOn( pitches[i], 100, channels[i] )    # play corresponding note
         keysPressed.append( key )    # and remember key (to avoid key-repeat)

def endNote( key ):
   """Called when a computer key is released.  Implements the corresponding 
      piano key release (i.e., removes key-down icon, and stops note).
   """
   for i in range( len(virtualKeys) ):   # loop through known virtual keys
   
      # if this is a known key (we can assume it is already pressed)
      if key == virtualKeys[i]:  
             
         Play.noteOff( pitches[i], channels[i] )    # stop corresponding note
         keysPressed.remove( key )     # and forget key (for key-repeat)

# associate callback functions with GUI events
d.onKeyDown( beginNote )
d.onKeyUp( endNote )