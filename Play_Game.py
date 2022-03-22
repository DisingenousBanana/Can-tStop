import Dice
import Player
import Game

def totalsupd8r(s):
  L=s.split()
  dic={}
  for strings in L:
    Q=strings.split(":")
    if Q[0]!="\n":
     dic[int(Q[0])]=0
     dic[int(Q[0])]=int(Q[1])
  return dic

def clamr(s):
  if s=="0":
    return []
  else:
    L=s.split()
    L1=[]
    for items in L:
      L1+=[int(items)]
    return L1

def mutator2(L1,s1,L2,s2):
  dic1={}
  for items in L1:
    dic1[items]=""
    dic1[items]=s1
  for items in L2:
    dic1[items]=""
    dic1[items]=s2
  return dic1

def mutator3(L1,s1,L2,s2,L3,s3):
  dic1={}
  for items in L1:
    dic1[items]=""
    dic1[items]=s1
  for items in L2:
    dic1[items]=""
    dic1[items]=s2
  for items in L3:
    dic1[items]=""
    dic1[items]=s3
  return dic1  

def mutator4(L1,s1,L2,s2,L3,s3,L4,s4):
  dic1={}
  for items in L1:
    dic1[items]=""
    dic1[items]=s1
  for items in L2:
    dic1[items]=""
    dic1[items]=s2
  for items in L3:
    dic1[items]=""
    dic1[items]=s3
  for items in L4:
    dic1[items]=""
    dic1[items]=s4
  return dic1  

def load_game(file_name):
  L2=[]
  for items in L1:
    if "\n" in items:
      i=items.index("\n")
      L2+=[items[0:i]]
    else:
      L2+=[items]
  leng=len(L1)
  if leng==6:
    dic1={}
    L=[L2[0],L2[3]]
    g=Game.Game(L)
    g.players[0].totals=totalsupd8r(L2[1])
    g.players[1].totals=totalsupd8r(L2[4])
    g.players[0].claimed=clamr(L2[2])
    g.players[1].claimed=clamr(L2[5])
    g.claimed=mutator2(g.players[0].claimed,g.players[0].name,g.players[1].claimed,g.players[1].name)
    return g
  elif leng==9:
    dic1={}
    L=[L2[0],L2[3],L2[6]]
    g=Game.Game(L)
    g.players[0].totals=totalsupd8r(L2[1])
    g.players[1].totals=totalsupd8r(L2[4])
    g.players[2].totals=totalsupd8r(L2[7])
    g.players[0].claimed=clamr(L2[2])
    g.players[1].claimed=clamr(L2[5])
    g.players[2].claimed=clamr(L2[8])
    g.claimed=mutator3(g.players[0].claimed,g.players[0].name,g.players[1].claimed,g.players[1].name,g.players[2].claimed,g.players[2].name)
    return g
  elif leng==12:
    dic1={}
    L=[L2[0],L2[3],L2[6],L2[9]]
    g=Game.Game(L)
    g.players[0].totals=totalsupd8r(L2[1])
    g.players[1].totals=totalsupd8r(L2[4])
    g.players[2].totals=totalsupd8r(L2[7])
    g.players[3].totals=totalsupd8r(L2[10])
    g.players[0].claimed=clamr(L2[2])
    g.players[1].claimed=clamr(L2[5])
    g.players[2].claimed=clamr(L2[8])
    g.players[3].claimed=clamr(L2[11])
    g.claimed=mutator4(g.players[0].claimed,g.players[0].name,g.players[1].claimed,g.players[1].name,g.players[2].claimed,g.players[2].name,g.players[3].claimed,g.players[3].name)
    return g
  g=Game.Game([L])
  g.players=[]

def play_game():
  welcome = "WELCOME TO CAN'T STOP"
  debug_prompt = "Enter D for debug mode, anything else for random play. "
  debug_yes = ['d', 'D']
  debug_message = "Playing debug mode - be prepared to enter all die values."
  game_prompt = "Enter R to re-load a game, Anything else for a new game. "
  reload_yes = ['r', 'R']
  name_message1 = "You will be asked for the number of players and each player's name."
  name_message2 = "Each player's name must start with a different letter."
  name_message3 = "Player names will be entered individually, and each must start with a different letter."
  name_message4 = "The order of play will correspond to the order in which they are entered."
  name_message5_prompt = "Enter player name (first letter must be unique): "
  name_message6_prompt = 'Each player name must start with a different letter. Enter a different name. '
  num_player_prompt = "Enter the number of players [2-4]: "   
  invalid_num_player = "You entered '{0}' which is not acceptable." 
  load_file_prompt = "Enter filename to load game from: "
  
  print(welcome)
  s=input(debug_prompt)
  if s=="D" or s=="d":
    debug=True
    print("Playing debug mode - be prepared to enter all die values.")
    s1=input(game_prompt)
    if s1=="R" or s1=="r":
     s4=input(load_file_prompt)
     g=load_game(s4)
    else:
     print(name_message1)
     print(name_message2)
     s2=input(num_player_prompt)
     while int(s2)>4 or int(s2)<2 or 2<int(s2)<3 or 3<int(s2)<4:
       print(invalid_num_player.format(s2))
       s2=input(num_player_prompt)
     if int(s2)==2:
       print(name_message3)
       print(name_message4)
       L=[]
       L1=[]
       p=0
       while p<=1:
         s3=input(name_message5_prompt)
         while s3[0] in L:
           s3=input(name_message6_prompt)
         L+=[s3[0]]
         L1+=[s3]
         p+=1
       g=Game.Game(L1)
       if int(s2)==3:
        print(name_message3)
        print(name_message4)
        L=[]
        L1=[]
        p=0
        while p<=2:
          s3=input(name_message5_prompt)
          while s3[0] in L:
            s3=input(name_message6_prompt)
          L+=s3[0]
          L1+=s3
          p+=1
       g=Game.Game(L1)
       if int(s2)==4:
        print(name_message3)
        print(name_message4)
        L=[]
        L1=[]
        p=0
        while p<=3:
          s3=input(name_message5_prompt)
          while s3[0] in L:
            s3=input(name_message6_prompt)
          L+=s3[0]
          L1+=s3
          p+=1
       g=Game.Game(L1)
  else:
   debug=False
   s1=input(game_prompt)
   if s1=="R" or s1=="r":
     s4=input(load_file_prompt)
     g=load_game(s4)
   else:
     print(name_message1)
     print(name_message2)
     s2=input(num_player_prompt)
     while int(s2)>4 or int(s2)<2 or 2<int(s2)<3 or 3<int(s2)<4:
       print(invalid_num_player.format(s2))
       s2=input(num_player_prompt)
     if int(s2)==2:
       print(name_message3)
       print(name_message4)
       L=[]
       L1=[]
       p=0
       while p<=1:
         s3=input(name_message5_prompt)
         while s3[0] in L:
           s3=input(name_message6_prompt)
         L+=[s3[0]]
         L1+=[s3]
         p+=1
       g=Game.Game(L1)
       if int(s2)==3:
        print(name_message3)
        print(name_message4)
        L=[]
        L1=[]
        p=0
        while p<=2:
          s3=input(name_message5_prompt)
          while s3[0] in L:
            s3=input(name_message6_prompt)
          L+=s3[0]
          L1+=s3
          p+=1
       g=Game.Game(L1)
       if int(s2)==4:
        print(name_message3)
        print(name_message4)
        L=[]
        L1=[]
        p=0
        while p<=3:
          s3=input(name_message5_prompt)
          while s3[0] in L:
            s3=input(name_message6_prompt)
          L+=s3[0]
          L1+=s3
          p+=1
       g=Game.Game(L1)
  over = False
  while not over: 
      over = g.take_turn(debug)
