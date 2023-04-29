from multiprocessing import current_process, Process
from threading import main_thread

process = current_process()
mainthread = main_thread()
print(f'Process: {process.name}, main thread: {mainthread}')

# SuperFastPython.com
# example of a thread executing a custom function
from time import sleep
from threading import Thread
 
# custom task function
def task():
    # execute a task in a loop
    for i in range(5):
        # block for a moment
        sleep(1)
        # report a message
        print('Worker thread running...')
    print('Worker closing down')
 
# create and configure a new thread
thread = Thread(target=task)
# start the new thread
thread.start()
# wait for the new thread to finish
thread.join()