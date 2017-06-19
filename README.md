# Agent-for-wumpus-world

The agent uses the explore_world function to obtain knowledge of the environment around, If there is no threat for the agent in the current tile, the tile is marked as “OK”
in the internal board, correspondingly the 4 adjacent tiles are checked and each threat perceived at each of these tiles is
then used to update the agents internal board.

![Alt text](https://github.com/khamkarajinkya/Agent-for-wumpus-world/wumpus1.png?raw=true "Console image")

Two separate knowledge bases are used, one keeps a track of the stench that is observed all over the environment, second keeps a track 
of all the breeze that the agent may encounter.

Once the explore_world step is performed, my agent randomly selects one of the safe tiles adjacent to the current tile using the make_move 
function and performs the same task again.

Two separate functions are written, killed_wumpus function uses the agents internal board to track the wumpus, as the tile containing the wumpus is accompanied by stench, the agent uses this knowledge, He
requires accurately 2 adjacently placed tiles and 1 safe tile to accurately locate the wumpus on the board and uses the arrow to kill the wumpus.

![Alt text](https://github.com/khamkarajinkya/Agent-for-wumpus-world/wumpusw.png?raw=true "Console image")

The agent uses the check_pit and locate_pits to accurately decipher where the pits in the environment may be lying, since the environment is partially visible, 
not all the pits are accurately located
