from fastapi import FastAPI
from .participants import participants
from .random import pick_winner
from .history import history

app = FastAPI()

@app.get("/participants")
def get_participants():
    return participants

@app.post("/participants")
def add_participant():
    participants.append("Участник")
    return {"ok": True}

@app.post("/random")
def random_pick():
    winner = pick_winner()
    if winner:
        history.append(winner)
        return {"winner": winner}
    return {"winner": None}

@app.get("/history")
def get_history():
    return history
