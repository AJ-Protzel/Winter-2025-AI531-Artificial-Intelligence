# Wumpus World Scratchpad
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase


x = 20


print("\nGAME 1 - Surrounded by Pits\n")
"""
Scenario 1: An agent in the initial location, surrounded by pits, should
climb out of the cave.
. . . .
W G . .
P . . .
A P . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1,3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 1) ]
    )
kb = KnowledgeBase(wumpus_world.agent_location, wumpus_world.agent_direction)
agent = WumpusWorldAgent(kb)
for _ in range(x):
    if not wumpus_world.agent_alive:
        break
    action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
    action(agent, wumpus_world)



print("\nGAME 2 - Hallway of Pits\n")
"""
Scenario 2: An agent in the initial location, with pits to every immediate
location to the north, would *at least* move once to the east.
. . . .
W G . .
P P P P
A . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase(wumpus_world.agent_location, wumpus_world.agent_direction)
agent = WumpusWorldAgent(kb)
for _ in range(x):
    if not wumpus_world.agent_alive:
        break
    action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
    action(agent, wumpus_world)



print("\nGAME 3 - Gold at end of hallway\n")
"""
Scenario 3: An agent in the initial location, with pits to every immediate
location to the north, would move to the east and collect the gold and make it safely back.
. . . .
W . . .
P P P P
A . . G
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (4, 1),
    pit_locations = [ (1, 2), (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase(wumpus_world.agent_location, wumpus_world.agent_direction)
agent = WumpusWorldAgent(kb)
for _ in range(x):
    if not wumpus_world.agent_alive:
        break
    action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
    action(agent, wumpus_world)



print("\nGAME 4 - Make a turn though pits\n")
"""
Scenario 4: An agent in the initial location, with pits to every immediate
location to the north, would move to the east and make a turn to the north 
and collect the gold and make it safely back.
. . . .
W . G .
P P . P
A . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (3, 3),
    pit_locations = [ (1, 2), (2, 2), (4, 2) ]
    )

kb = KnowledgeBase(wumpus_world.agent_location, wumpus_world.agent_direction)
agent = WumpusWorldAgent(kb)
for _ in range(x):
    if not wumpus_world.agent_alive:
        break
    action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
    action(agent, wumpus_world)




print("\nGAME 5 - Kill the Wumpus\n")
"""
Scenario 5: An agent in the initial location, wumpus to the north
in which it will do battle and win.
. . . .
W . G .
. P . P
A . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'North',
    wumpus_location = (1, 3),
    gold_location = (3, 3),
    pit_locations = [ (2, 2), (4, 2) ]
    )

kb = KnowledgeBase(wumpus_world.agent_location, wumpus_world.agent_direction)
agent = WumpusWorldAgent(kb)
for _ in range(x):
    if not wumpus_world.agent_alive:
        break
    action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
    action(agent, wumpus_world)
