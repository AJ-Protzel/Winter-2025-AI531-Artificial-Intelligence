# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        self.facts = []
        # self.rules = [
        #     # Example rules
        #     ("Breeze", "AdjacentPit"),
        #     ("Stench", "AdjacentWumpus"),
        #     ("Glitter", "GoldHere"),
        #     # Add more rules as needed
        # ]

    # def __init__(self):
    #     self.knowledge = []

    def tell(self, fact):
        # pass
        self.facts.append(fact)
        # # Apply rules to infer new facts
        # self.apply_rules()


    # def tell(self, sentence):
    #     # Add the sentence to the knowledge base
    #     self.knowledge.append(sentence)

    def ask(self, query=None):
        if query is None:
            return WumpusWorldAgent.sit
        else:
            pass

    # def ask(self, query):
    #     # For simplicity, return a fake action based on the query
    #     return "FAKE_ACTION"
    


    
    # def apply_rules(self):
    #     # Example logic to apply rules and infer new facts
    #     for fact in self.facts:
    #         for rule in self.rules:
    #             if fact == rule[0]:
    #                 inferred_fact = rule[1]
    #                 if inferred_fact not in self.facts:
    #                     self.facts.append(inferred_fact)

    # def determine_best_action(self):
    #     # Example logic to determine the best action
    #     # This could be based on the current state of the knowledge base
    #     # For now, let's return a placeholder action
    #     return "MoveForward"
            
