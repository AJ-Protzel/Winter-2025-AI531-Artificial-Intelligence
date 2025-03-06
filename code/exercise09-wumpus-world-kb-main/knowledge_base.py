# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        self.facts = []
        # self.rules = []

    def tell(self, fact):
        self.facts.append(fact)

    def ask(self, var=None):
        if var is None:
            return WumpusWorldAgent.climb
        else:
            pass
            
