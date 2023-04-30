import threading
import time
import requests
from enum import Enum
import datetime

from typing import NoReturn

### needed tests
# Test that the track function runs only when shared_var is set to State.track, and does not run when shared_var is set to State.empty.
# Test that the empty function runs only when shared_var is set to State.empty, and does not run when shared_var is set to State.track.
# Test that the get_state function updates the value of shared_var correctly based on the HTTP response.
# Test that the threads cooperate and alternate correctly based on the value of pub_state.
# Test that the code runs without errors or exceptions, and all threads finish properly when the program terminates.


class State(Enum):
    """ Enum class for allowed states
    """
    TRACK = 'track'
    EMPTY = 'empty'


class PublisherState:
    """ Convenience class to interact with said state instance
        The lock is overly cautious, but adds call consistency/uniformity
    """
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


def get_state(pub_state: PublisherState) -> NoReturn:
    while True:
        response = requests.get('http://localhost:8000/get_state')
        if response.status_code == 200:
            state_str = response.json()['state']
            if pub_state.get().value != state_str:
                print("state changed")
            pub_state.set(state_str)
        time.sleep(1)


if __name__ == "__main__":
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