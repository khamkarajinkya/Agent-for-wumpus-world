# this class simulates a wumpus world

class WumpusWorld:
  def __init__(self, blocks, pits, gold, wumpus, initial_location):
    self.initial_location = initial_location    # copy the input
    self.wumpus = wumpus
    self.pits = pits
    self.gold = gold
    self.blocks = blocks
    self.player = self.initial_location
    self.has_arrow = True

    self.breeze = {}    # stores locations of breezy squares
    self.stench = {}    # stores location of smelly squares
    
    for p in self.pits: # initalise breezy squares
      for l in self.neighbours(p):
        self.breeze[l] = True
    for w in self.wumpus: # intialise smelly squares
      for l in self.neighbours(w):
        self.stench[l] = True
      
      
  def neighbours(self, loc):    # returns neighbours of tuple loc = (x,y) 
    return [(loc[0]+1,loc[1]), (loc[0]-1,loc[1]), (loc[0],loc[1]+1), (loc[0],loc[1]-1)]

  def arrow_hits(self, location, dx, dy): # scans to see if the arrow hits
    while location not in self.blocks:
      location = (location[0]+dx, location[1]+dy)
      if location in self.wumpus:
        return True
    return False
  
  def print(self):            # print the board state (useful for debugging)
    print(self.player)
    xmin = min([x for x,y in self.blocks])
    xmax = max([x for x,y in self.blocks])
    ymin = min([y for x,y in self.blocks])
    ymax = max([y for x,y in self.blocks])
    for y in range(ymin, ymax+1):
      for x in range(xmin, xmax+1): 
        
        if (x,ymax-y) in self.blocks:
          print('B',end='')
        elif (x,ymax-y) in self.wumpus:
          print('W',end='')
        elif (x,ymax-y) in self.pits:
          print('P',end='')
        elif (x,ymax-y) in self.gold:
          print('G',end='')
        elif self.player == (x, ymax - y):
          print('Y',end='')
        else:
          print(' ',end='')
      print("")
    b = self.player in self.breeze       # is their square breezy?
    s = self.player in self.stench       # is it smelly?
    print("arrow: " + str(self.has_arrow))
    print("breezy: " + str(b))
    print("stenchy: " + str(s))

    

  def sim(self, agent):
    t = 0
    self.has_arrow = True
    self.player = self.initial_location
    while t < 1000: 
      t+=1

      self.print()

      b = self.player in self.breeze       # is their square breezy?
      s = self.player in self.stench       # is it smelly?
      agent.give_senses(self.player, b, s)  # give the agent its senses
      action = agent.get_action()       # get the agents action
      print(action, end='\n\n')

      new_location = self.player
      if action == 'MOVE_UP':             # update the location for moving up/down/left/right
        new_location = (self.player[0], self.player[1]+1)
      elif action == 'MOVE_DOWN':
        new_location = (self.player[0], self.player[1]-1)
      elif action == 'MOVE_LEFT':
        new_location = (self.player[0]-1,self.player[1])
      elif action == 'MOVE_RIGHT':
        new_location = (self.player[0]+1,self.player[1])
      elif not self.has_arrow and action[0:5] == 'SHOOT':  # check the agent has the arrow if they shot
        return 'NO ARROW'
      elif action == 'SHOOT_UP':                      # check to see if the agent killed the wumpus
        if self.arrow_hits(self.player, 0, 1):
          self.wumpus = {}
          agent.killed_wumpus()
      elif action == 'SHOOT_DOWN':
        if self.arrow_hits(self.player, 0, -1):
          self.wumpus = {}
          agent.killed_wumpus()
      elif action == 'SHOOT_LEFT':
        if self.arrow_hits(self.player, -1, 0):
          self.wumpus = {}
          agent.killed_wumpus()
      elif action == 'SHOOT_RIGHT':
        if self.arrow_hits(self.player, 1, 0):
          self.wumpus = {}
          agent.killed_wumpus()
      elif action == 'QUIT':
        return 'QUIT'


      if action[0:5] == 'SHOOT':      # remove the arrow if it was shot
        self.has_arrow = False

      if new_location in self.pits:   # check if fell into a pit
        return 'FELL'
      if new_location in self.wumpus: # check if eaten by wumpus
        return 'EATEN'
      if new_location in self.gold:   # check if found gold
        return 'GOLD'

      if new_location not in self.blocks: # if agent ran into a wall, then reset position
        self.player = new_location
      
           
      
  

    



