# blockus-ai
Creating an AI to play and win Blockus, A Board game

Article goes here
==============
Introduction

What is blockus?

Rules?

In three-player games, either one of the players takes two colours or else "the pieces of the fourth colour are placed on the board in a non-strategic way."

where idea come from?

================================================================

Procedure:
Develop game
- rules on legal moves
- represent game states, how to represent board, pieces, and moves

Function to find legal moves:
- available corners
- place piece with any orientation and translation given corner 

Repeat:
Create AI, which takes state of board, remaining pieces, and whose turn it is
After each AI, it will play against itself (play against 3 other random movements), play 400 games? (100 as each colour) see how many they win and by how much
REsults
Improve AI by adding new heuristics e.g. another evalution point for AI to consider

====================================================

Different AI's
Human Player:

DEvelooping AI:
Heuristics, based from experience and sources
Tips and Strategies summed up:
- Use larger pieces at the beginning
    - when given an option pick the largest piece and this reduces your score the most and smaller peices are easier to place down later on than larger ones
- Control the centre ground
    - first few rounds, reward AI for moving towards center, after that do not care
- Leave your pieces’ corners open for options
    - when placing a piece down, see if it provides more or less corners than before
- Shut down the corners on your opponents’ pieces
    - when placing a piece down, see if we a blocking any of their legal corners
- Think about when best to use the single square
    - typically only as a last resort? or when the likely hood of an opponent blocking you so place a 1 would prevent that
- Leave free placements for later
    - what is a free placement? based on if other players can get to it/get to it in the next move?
- Watch your opponents’ moves and their remaining pieces
    - predict which move the opponents could play next, if its a good move for htem, try to prevent it...


Random Movements:
- Picks a random legal move
Noticable remarks:
- Because there are more way to orientate complex pieces, the random decider is more likely to pick the more valuable complex pieces to put down first
- this meant that piece X which is of value 5, is rarely being placed 

Greedy AI:
- Ranks the legal moves based on the value of the piece being placed down, higher value placed before smaller
Dominates random everytime

AI that wants to head to the center in the beginning


AI that looks for placements that allow for more legal moves


AI that looks to block other (place pieces that cover other player's legal corners)
- aim is to minimise the score of the opponent, not just maximise your points

==========================
MILESTONE REACHED

After this point, we need to consider how the AI performs against the best version we have
As we want to look into the best move that the opponent could make and try to prevent that 

AI that leave free placements for later
- A free placement = a move which can't be done by anyone else
- To do this we must know the possible moves, and remaining pieces of our opponents

AI that watches your opponents’ moves and their remaining pieces

THEN WORRY ABOUT: optimisations and thinking time
move should be made within a reasonable amount of time

Discuss final results
- also record the percentage increase in wins when who goes first

COnclusion

Evaluation
Technical Challenges
- Was python the best choice?

Limitations
COmpared to Chess or Connect 4, 
BLockus is a game designed for 2 or 4 players. 
when experiencing 4 players computations very heavy, cannot go indepth

Further Work
Develop general command line engine, which is general enough for potentially other bots to play??
Solve games which are about to end? Ensure victory when there are X amount of pieces left...
Reinforment/Deep learning strategies?
Search algorithms? look further ahead to moves opponent could make (2/3 rounds)
