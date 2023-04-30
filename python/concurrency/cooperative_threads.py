import threading
import time
import requests
from enum import Enum
import datetime

from typing import NoReturn

class State(Enum):
    TRACK = 'track'
    EMPTY = 'empty'


class PublisherState:
    def __init__(self):
        initial_state = requests.get('http://localhost:8000/get_state').json()["state"]
        self._value = State(initial_state)
        self._lock = threading.Lock()
    
    def get(self):
        with self._lock:
            return self._value
    
    def set(self, value):
        with self._lock:
            self._value = State(value)


def publish_track(pub_state: PublisherState) -> NoReturn:
    while True:
        if pub_state.get() == State.TRACK:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} tracking task is ongoing")
            time.sleep(1)
        else:
            time.sleep(0.1)

def publish_empty(pub_state: PublisherState) -> NoReturn:
    while True:
        if pub_state.get() == State.EMPTY:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} no tracking - empty publish")
            time.sleep(1)
        else:
            time.sleep(0.1)

def get_state(pub_state: PublisherState):
    while True:
        response = requests.get('http://localhost:8000/get_state')
        if response.status_code == 200:
            state_str = response.json()['state']
            if pub_state.get().value != state_str:
                print("state changed")
            pub_state.set(state_str)
        time.sleep(1)


pub_state = PublisherState()
t1 = threading.Thread(target=publish_track, args=(pub_state,))
t2 = threading.Thread(target=publish_empty, args=(pub_state,))
t3 = threading.Thread(target=get_state, args=(pub_state,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()