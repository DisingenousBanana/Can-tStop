class Player:
  
  def __init__(self, n):
    self.name = n
    self.totals = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    self.claimed = []

  def __repr__(self): 
    return ('Player {0} has totals {1} and has claimed columns {2}'.format(
      self.name, self.totals, self.claimed))
  
  def __eq__(self, other):
    return isinstance(other, Player) and\
		       self.name == other.name and\
		       self.claimed == other.claimed and\
		       self.totals == other.totals
  
  def update_totals(self, current, targets): 
    if current=={}:
      return []
    for item in current:
      self.totals[item]=current[item]
    L=[]
    for item in self.totals:
      if self.totals[item]==targets[item] and not(item in self.claimed):
        L+=[item]
        L.sort()
        self.claimed+=[item]
    (self.claimed).sort()
    return L