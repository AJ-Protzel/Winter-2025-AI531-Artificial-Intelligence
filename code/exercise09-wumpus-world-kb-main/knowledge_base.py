# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        self.facts = []

    def tell(self, fact):
        self.facts.append(fact)

    def ask(self, query):
        if query is None:
            return WumpusWorldAgent.climb # break sequence 
        else:
            for fact in self.facts:
                if f"{query} A" in fact:
                    return fact
            return self.find_action()
    
    def find_action(self):
        return WumpusWorldAgent.climb
        
