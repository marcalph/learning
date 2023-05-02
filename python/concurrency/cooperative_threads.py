
import threading
import time

event = threading.Event()
lock = threading.Lock()

def worker1():
    while True:
        with lock:
            event.wait()  # wait for the event to be set by worker2
            while event.is_set():
                print("Worker 1 is working now!")
                time.sleep(1)
                # do some work here
                event.clear()  # clear the event to signal that we're done
                event.set()  # set the event to signal that it's worker2's turn

def worker2():
    while True:
        with lock:
            event.wait()  # wait for the event to be cleared by worker1
            while not event.is_set():
                print("Worker 2 is working now!")
                # do some work here
                time.sleep(1)
                event.set()  # set the event to signal that it's worker1's turn
                event.clear()  # clear the event to signal that we're done

# start the workers
threading.Thread(target=worker1).start()
threading.Thread(target=worker2).start()

# allow worker 1 to start working
event.set()
