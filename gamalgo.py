
import random


class gamalgo:
    def ratio(Weights):
        total = sum(Weights.values())
        roll = random.uniform(1, total)

        current = 0
        for enemy, weight in Weights.items():
            current += weight
            if roll <= current:
                return enemy



        
