# Main
# A demonstration of the WumpusWorld and WumpusWorldAgent.
# Adrien Protzel

from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    agent_alive = True,
    wumpus_alive = True,
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (3, 1), (3, 3), (4, 3) ]
    )

kb = KnowledgeBase()

agent = WumpusWorldAgent(kb)

action = agent.action(wumpus_world.percept((1, 1)))
action(agent, wumpus_world)