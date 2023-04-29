
""" simple server to set a state variable through a form using fast api
    Usage: curl -X POST http://localhost:8000/set -d "state=value"
"""


from enum import Enum
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

class State(Enum):
    TRACK = 'track'
    EMPTY = 'empty'
    OTHER = 'other'

current_state = State.EMPTY
@app.get("/get_state")
async def get_state():
    global current_state
    return {"state": current_state.value}



@app.post("/set_state")
async def set_state(state: State = Form(...)):
    global current_state
    current_state = state
    return {"state": current_state.value}

