# KnowledgeBase
# A knowledge base for a knowledge-based agent.
# Adrien Protzel

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def tell(self, var):
        pass

    def ask(self, var=None):
        if var is None:
            return WumpusWorldAgent.climb
        else:
            pass
            
