import Dice
import Player
I=[["|1    ","|1    ","|1    ","|1    ","|1    ","|1    ","|1    ","|1    ","|1    ","|1    ","|1    |"],
   ["|2    ","|2    ","|2    ","|2    ","|2    ","|2    ","|2    ","|2    ","|2    ","|2    ","|2    |"],
   ["|3    ","|3    ","|3    ","|3    ","|3    ","|3    ","|3    ","|3    ","|3    ","|3    ","|3    |"],
   ["|     ","|4    ","|4    ","|4    ","|4    ","|4    ","|4    ","|4    ","|4    ","|4    ","|     |"],
   ["|     ","|5    ","|5    ","|5    ","|5    ","|5    ","|5    ","|5    ","|5    ","|5    ","|     |"],
   ["|     ","|     ","|6    ","|6    ","|6    ","|6    ","|6    ","|6    ","|6    ","|     ","|     |"],
   ["|     ","|     ","|7    ","|7    ","|7    ","|7    ","|7    ","|7    ","|7    ","|     ","|     |"],
   ["|     ","|     ","|     ","|8    ","|8    ","|8    ","|8    ","|8    ","|     ","|     ","|     |"],
   ["|     ","|     ","|     ","|9    ","|9    ","|9    ","|9    ","|9    ","|     ","|     ","|     |"],
   ["|     ","|     ","|     ","|     ","|10   ","|10   ","|10   ","|     ","|     ","|     ","|     |"],
   ["|     ","|     ","|     ","|     ","|11   ","|11   ","|11   ","|     ","|     ","|     ","|     |"],
   ["|     ","|     ","|     ","|     ","|     ","|12   ","|     ","|     ","|     ","|     ","|     |"],
   ["|     ","|     ","|     ","|     ","|     ","|13   ","|     ","|     ","|     ","|     ","|     |"]]

def list_to_board(L):
   for pos1 in range(len(L)):
     s1=""
     for pos2 in range(len(L[pos1])):
      s1+=L[pos1][pos2]
     print(s1)

def claimed(L1,los):
  for numbers in los:
    if numbers!=12:
     for pos in range(len(L1)):
      L1[pos][numbers-2]="|     "
    else:
     for pos in range(len(L1)):
       L1[pos][numbers-2]="|     |"

def update_board(L1,Dic,name,claimed_cols):
  M=L1.copy()
  claimed(L1,claimed_cols)
  for item in Dic:
    if Dic[item]>=1 and L1[Dic[item]-1][item-2]!="|     ":
      if L1[Dic[item]-1][item-2][1:3].isnumeric():
       L1[Dic[item]-1][item-2]=M[Dic[item]-1][item-2][:1]+name+" "+M[Dic[item]-1][item-2][3:]
      elif L1[Dic[item]-1][item-2][1].isnumeric():
       L1[Dic[item]-1][item-2]=M[Dic[item]-1][item-2][:1]+name+M[Dic[item]-1][item-2][2:]
      else:
       i=L1[Dic[item]-1][item-2].index(" ")
       L1[Dic[item]-1][item-2]=M[Dic[item]-1][item-2][:i]+name+M[Dic[item]-1][item-2][i+1:]
  return L1

def testr(Los,L1,pos,new_L1,claimed_cols):
  if L1==[]:
    return []
  elif Los==[] or pos>=len(Los):
   return new_L1
  else:
   new_L1=update_board(L1,Los[pos][0],Los[pos][1],claimed_cols)
   return testr(Los,new_L1,pos+1,new_L1,claimed_cols)

def none_there(L1,L2):
    for items in L1:
      if items in L2:
        return False
    return True

def stringify(L):
  s=""
  L.sort()
  for items in L:
    s+=str(items) + " "
  return s

def stringifydic(dic):
  keyss=list(dic.keys())
  s=""
  keyss.sort()
  for items in keyss:
    m=keyss[0]
    s+=str(m)+":" + str(dic[m]) + " "
    keyss=keyss[1:]
  return s

print(stringifydic({2:3,1:2}))

print(stringify([1,3,2]))

class Game:
  
  targets = {2:3, 3:5, 4:7, 5:9, 6:11, 7:13, 8:11, 9:9, 10:7, 11:5, 12:3}
  
  def __init__(self, names): 
    self.players = []
    for i in range(len(names)):
        self.players.append(Player.Player(names[i]))
    self.claimed = {}
    self.curr_player = 0     
  
  def __repr__(self):
    s = ""
    for p in self.players:
      s += str(p) + "\n"
    s += "Claimed: " + str(self.claimed) + "\n"
    s += "Current Player: " + str(self.curr_player)
    return s
  
  def __eq__(self, other): 
    return isinstance(other, Game) and \
            (self.players == other.players) and \
            (self.claimed == other.claimed) and \
            (self.curr_player == other.curr_player)
        
  
   
  def print_board(self):
    max_target = 13
    row_length = 67
    num_spaces = 27
    spaces = num_spaces * " "
    title = "C A N ' T   S T O P"
    bar = "-" * row_length
    first_column = 2
    last_column = 12
    block = 5
    blank = "     |"
    
    print(spaces + title + spaces)
    print(bar)
    line = "|"
    for i in range(first_column, last_column+1):
      line += str(i).ljust(block) + "|"
    print(line)
    print(bar)
    Los=[]
    for pos in range(len(self.players)):
      Los+=[[(self.players[pos]).totals,self.players[pos].name[0]]]
    Los.sort(key = lambda M: M[1])
    M=testr(Los,I,0,I,self.claimed)
    list_to_board(M)
    print(row_length*"-")
    line = "|"
    for pos in range(first_column, last_column + 1):
      if pos in self.claimed: 
        line += self.claimed[pos][0] + blank[1:]
      else:
        line += blank
    line += " Claimed"
    print(line)
  
  def determine_options(self, possibles, current): 
    dic={}
    vals=current.keys()
    L1=[]
    for pos in range(len(possibles)):
      L1+=possibles[pos]
    if len(current)<=1:
      for pos in range(len(possibles)):
       a=possibles[pos][0]
       b=possibles[pos][1]
       if not(a in self.claimed) and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a,b]
       if not(a in self.claimed) and b in self.claimed:
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a]
       if not(b in self.claimed) and a in self.claimed:
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[b]
    if len(current)==2:
      for pos in range(len(possibles)):
       a=possibles[pos][0]
       b=possibles[pos][1]
       if a in current and b in current and not(a in self.claimed) and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a,b]
       elif (a in current and not (b in current) or not(a in current) and b in current) and not(a in self.claimed) and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a,b]
       elif not (a in current) and not(b in current) and not(a in self.claimed) and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a]
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[b]
       elif a in current and b in current and a in self.claimed and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[b]
       elif a in current and b in current and not(a in self.claimed) and b in self.claimed:
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a]
       elif a in current and not (b in current) and not(a in self.claimed) and b in self.claimed:
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a]
       elif not(a in current) and b in current and a in self.claimed and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[b]
       elif not (a in current) and not(b in current) and not(a in self.claimed) and b in self.claimed:
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a]
       elif not (a in current) and not(b in current) and a in self.claimed and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[b]
    if len(current)==3:
      for pos in range(len(possibles)):
       a=possibles[pos][0]
       b=possibles[pos][1]
       if a in current and b in current and not(a in self.claimed) and not (b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a,b]
       elif a in current and not(b in current) and not(a in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[a]
       elif b in current and not(a in current) and not(b in self.claimed):
         dic[len(dic)]=[]
         dic[len(dic)-1]+=[b]
    return dic

  def save_game(self, file_name):
    fout=open(file_name,'w')
    L=self.players[self.curr_player:]+self.players[:self.curr_player]
    for pos in range(len(L)):
      s=""
      if L[pos].claimed==[]:
       s=str(L[pos].name) + "\n" + stringifydic(L[pos].totals) + "\n" + "0"+"\n"
       fout.write(s)
      else:
        s=str(L[pos].name) + "\n" + stringifydic(L[pos].totals) + "\n" + stringify(self.players[pos].claimed)+"\n"
        fout.write(s)
  
  def take_turn(self, debug):  
    turn_message = "{0}, it is now your turn" 
    menu_prompt = "{0}: Enter (B or b) to see the board, (S or s) to suspend and save the game, anything else to roll dice: " 
    roll_message = "{0}: Your roll was {1},{2},{3},{4}" 
    pairs_message = "{0}: Combinations include: {1}" 
    no_options_message = '{0}: You cannot play. Your turn is over.' 
    option_message = "Enter {0} to play {1}"        
    choice_message = "{0}: Enter your choice now: "   
    current_begin = "Currently active for {0}: " 
    current_summary = "{0} (position {1} of {2}). " 
    again_prompt =  "{0}: Do you want to roll again? enter Y for Yes, Anything else for No. " 
    yes = ['y','yes']    
    game_won = '{0} has won the game.'
    column_claimed = '{0} has just claimed {1}'
    save_game_prompt = "{0} Enter name of file to save current game to:"
    save_game_confirmation = "Game saved to {0}"
    
    n = self.players[self.curr_player].name
    print(turn_message.format(n))
    ans = input(menu_prompt.format(n))
    while ans.lower()=="b": 
        self.print_board()
        print(turn_message.format(n))
        ans = input(menu_prompt.format(n))     
            
    if ans.lower()=="s":
        file_n = input(save_game_prompt.format(n))
        self.save_game(file_n)
        print(save_game_confirmation.format(file_n))
        return True
        
    again = True
    current = {} 
    while again:
        d1 = Dice.roll(debug)
        d2 = Dice.roll(debug)
        d3 = Dice.roll(debug)
        d4 = Dice.roll(debug)
        print(roll_message.format(n, d1,d2,d3,d4))
        possibles = Dice.pairs(d1,d2,d3,d4)
        print(pairs_message.format(n, possibles))
        
        choices_dir = self.determine_options(possibles,current)
            
        num_options = len(choices_dir)
        if num_options==0: 
            print(no_options_message.format(n))
            current = {}
            again = False
        else:
            for i in range(num_options):
                print(option_message.format(i, choices_dir[i]))
                        
            choice = input(choice_message.format(n))
            while not(choice.isdigit()) or (int(choice)<0 or int(choice)>=num_options):
                choice = input("Invalid choice. " + choice_message.format(n))
                    
            ch = int(choice)
            will_play = choices_dir[ch]
            for d in will_play: 
                if d in current: 
                    current[d] += 1
                else:
                    current[d] = self.players[self.curr_player].totals[d] + 1
                current[d] = min(current[d], self.targets[d])
                
            str_current = current_begin.format(n)
            curr_cols = list(current.keys())
            curr_cols.sort()
            for t in curr_cols:
                str_current += current_summary.format(t, current[t], self.targets[t])
            print(str_current)                
                
            answer = input(again_prompt.format(n))
            again = (answer.lower() in yes)
               
    just_claimed = self.players[self.curr_player].update_totals(current, self.targets)

    for loc in just_claimed: 
        print(column_claimed.format(n, loc))
        self.claimed[loc] = n
        for p in self.players:
            p.totals.pop(loc)
        
    current = {}
    if len(self.players[self.curr_player].claimed) >= 3: 
        print(game_won.format(n))
        return True
    else:
        self.curr_player = ( self.curr_player + 1) % len(self.players)
        return False