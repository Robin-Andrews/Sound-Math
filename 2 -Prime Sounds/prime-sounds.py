from music import *

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# create lists of pitches and durations
pitches1   = []
durations1 = []
for n in range(500):
  if isprime(n):
    pitches1.append(67)
    durations1.append(0.1)
  else:
    pitches1.append(60)
    durations1.append(0.1)
    
# create an empty phrase, and construct piece using pitch/rhythm data
piece = Phrase()   
piece.addNoteList(pitches1, durations1)
 
# set the instrument and tempo for the piece
piece.setInstrument(35)
piece.setTempo(60)
 
# play it
Play.midi(piece)