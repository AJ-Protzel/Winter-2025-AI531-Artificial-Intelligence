# Main
# A demonstration of the WumpusWorldAgent and KnowledgeBase.
# Adrien Protzel

















# from wumpus_world import WumpusWorld
# from wumpus_world_agent import WumpusWorldAgent
# from knowledge_base import KnowledgeBase
# import random

# # randomize the map
# coordinates = [
#     (1, 1),  # Agent
#     (1, 3),  # Wumpus
#     (2, 3),  # Gold
#     (3, 1),  # Pit 1
#     (3, 3),  # Pit 2
#     (4, 3)   # Pit 3
# ]

# random_coordinates = set()
# while len(random_coordinates) < 6:
#     x = random.randint(1, 4)
#     y = random.randint(1, 4)
#     random_coordinates.add((x, y))
# random_coordinates = list(random_coordinates)

# coordinates = random_coordinates

# wumpus_world = WumpusWorld(
#     agent_location = coordinates[0],
#     agent_direction = random.choice(["North", "South", "East", "West"]),
#     agent_alive = True,
#     wumpus_alive = True,
#     wumpus_location = coordinates[1],
#     gold_location = coordinates[2],
#     pit_locations = coordinates[3:6]
#     )

# kb = KnowledgeBase()
# agent = WumpusWorldAgent(kb)


# print("NOTE: Percept 'Bump' will either all be True or False because the agent doesn't move")
# print('-------')

# # print the current map cells
# map = [["." for _ in range(4)] for _ in range(4)]
# map[4 - wumpus_world.wumpus_location[1]][wumpus_world.wumpus_location[0] - 1] = "W"
# map[4 - wumpus_world.gold_location[1]][wumpus_world.gold_location[0] - 1] = "G"
# for pit in wumpus_world.pit_locations:
#     map[4 - pit[1]][pit[0] - 1] = "P"
# map[4 - wumpus_world.agent_location[1]][wumpus_world.agent_location[0] - 1] = "A"
# for row in map:
#     print(" ".join(row))

# print('-------')

# # print the percepts at each cell
# for x in range(1, 5):
#     for y in range(1, 5):
#         percept = wumpus_world.percept((x, y))
#         print(f'({x},{y}) {percept}')
