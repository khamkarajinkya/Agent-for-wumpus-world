import wumpus
width = 5

blocks = set()

for x in range(width+1):
    blocks.add((0, x))
    blocks.add((x, 0))
    blocks.add((width,x))
    blocks.add((x, width))

gold = {(4,4)}
pits = {(3,3)}
wumpus_location = {(2,2)}
initial_location = (1,1)

world1 = wumpus.WumpusWorld(blocks = blocks, gold = gold, wumpus = wumpus_location, pits = pits, initial_location = initial_location)

