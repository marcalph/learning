import threading
import time
import requests
from enum import Enum
import datetime

from typing import NoReturn

class State(Enum):
    TRACK = 'track'
    EMPTY = 'empty'

initial_state = requests.get('http://localhost:8000/get_state')
initial_state = initial_state.json()["state"]
current_state = State(initial_state)


def publish_track() -> NoReturn:
    while True:
        if current_state == State.TRACK:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} tracking task is ongoing")
            time.sleep(1)
        else:
            time.sleep(0.1)

def publish_empty() -> NoReturn:
    while True:
        if current_state == State.EMPTY:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} no tracking - empty publish")
            time.sleep(1)
        else:
            time.sleep(0.1)
''
def get_state():
    global current_state
    while True:
        response = requests.get('http://localhost:8000/get_state')
        if response.status_code == 200:
            state_str = response.json()['state']
            if current_state.value != state_str:
                print("state changed")
            if state_str == State.TRACK.value:
                current_state = State.TRACK
            else:
                current_state = State.EMPTY
        time.sleep(1)

t1 = threading.Thread(target=publish_track)
t2 = threading.Thread(target=publish_empty)
t3 = threading.Thread(target=get_state)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()