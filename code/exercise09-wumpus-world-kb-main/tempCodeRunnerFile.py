
from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

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
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 1) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # climb?