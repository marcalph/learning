import threading
import time
event = threading.Event()
lock = threading.Lock()

def worker1():
    while True:
        lock.acquire()
        if event.is_set():
            print("Worker 1 is working now!")
            time.sleep(1)
            # do some work here
            event.clear()
        lock.release()

def worker2():
    while True:
        lock.acquire()
        if not event.is_set():
            print("Worker 2 is working now!")
            # do some work here
            time.sleep(1)
            event.set()
        lock.release()

# start the workers
threading.Thread(target=worker1).start()
threading.Thread(target=worker2).start()

# allow worker 1 to start working
# event.set()
#todo figure out a way to wait on event