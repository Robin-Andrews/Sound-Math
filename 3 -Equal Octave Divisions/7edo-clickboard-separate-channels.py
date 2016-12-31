from gui import *
from music import *

class Key(object):
  ''' Define Key object '''
  def __init__(self, pitch, channel):
    self.is_playing = False
    self.pitch = pitch
    # channel needed as float pitches don't play nicely together (pitch bends added to existing notes)
    self.channel = channel
    Play.setInstrument(74, self.channel)
    self.button = Button(str(round(pitch, 2)), self.callback)
      
  def callback(self):
    if not self.is_playing:
      Play.noteOn(self.pitch, 100, self.channel)
      self.is_playing = True
    elif self.is_playing:
      Play.noteOff(self.pitch, self.channel)  
      self.is_playing = False
    print self.is_playing
     
# Create display
d = Display("7-edo Clickboard", 600, 400, 100, 100)

# Create pitches
a = 2 ** (1/7.0)
pitches = [261.6 * (a ** n) for n in range(8)]
# pitches = [60, 61, 63, 65, 67, 68, 71, 72]
channels = range(8)

# Create keys
keys = [Key(pitch, channel) for pitch, channel in zip(pitches, channels)]

# Add keys
for i in range (len(keys)):
  x_coords = [40, 180, 320, 460, 40, 180, 320, 460]
  y_coords = [40, 40, 40, 40, 240, 240, 240, 240]
  d.add(keys[i].button, x_coords[i], y_coords[i])

# Stop button
def kill():
  Play.allNotesOff()
  for key in keys:
    key.is_playing = False
  
stop = Button("Kill sound", kill)
d.add(stop, 450, 350)
  
