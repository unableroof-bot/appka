import random
from .participants import participants

def pick_winner():
    if not participants:
        return None
    winner = random.choice(participants)
    participants.clear()
    return winner
