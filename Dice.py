import random

def roll(debug_mode): 
  if debug_mode:
    debugging_prompt = "Enter a die value between 1 and 6: "
    die = input( debugging_prompt)
    while not(die.isdigit()) or ( int(die)<1 or int(die)>6 ): 
      die = input( "Invalid entry. " + debugging_prompt )   
    return( int(die) )        
  else:
    return random.randint(1,6)    
        
def pairs(d1,d2,d3,d4):
  L=[[d1+d2,d3+d4],[d1+d3,d2+d4],[d1+d4,d2+d3]]
  for stuff in L:
    stuff.sort()
  L1=[]
  for stuff in L:
    if L1.count(stuff)==0:
      L1+=[stuff]
  N1 = sorted(L1, key = lambda M: M[0])
  return N1