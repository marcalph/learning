#daemon thread runs in bg and not awaited by main thread
#thread pool executor, map threads to multiple threads
#dead lock // e.g. two acquire on a lock
# reentry lock  allows multiple locking of the mutex


import random
import time
import concurrent.futures
FINISH = "THE END"

class Pipeline:
    def __init__(self, capacity):
        self. capacity = capacity
        self.message = None
    
    def set_message(self, message):
        print(f"producing message {message}")
        producer_pipe.append(message)
        self.message = message
    
    def get_message(self):
        print(f"consuming message of {self.message}")
        message = self.message
        consumer_pipe.append(message)
        return message

def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1,100)
        pipeline.set_message(message)
    
    pipeline.set_message(FINISH)


def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())

consumer_pipe=[]
producer_pipe=[]

if __name__ == "__main__":
    pipe = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipe)
        ex.submit(consumer, pipe)
    print(f"consumer: {consumer_pipe}")
    print(f"producer: {producer_pipe}")
