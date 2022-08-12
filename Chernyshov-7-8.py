from queue import Queue
from random import random
from threading import Thread,  Event as Event_th
from time import sleep
from multiprocessing import Process, Event as Event_proc, Queue as Queue_proc


def queue_print(my_queue, i, event):
    # print(my_queue, i, event)
    while not my_queue.empty():
        event.wait(1)
        print(my_queue.get(), ' thread (process) ', i)
        event.set()
        sleep(0.1)


def queue_put(my_queue: Queue):
    for i in range(20):
        my_queue.put(random())


def test_queue():
    def queue_threads():
        threads = []
        for i in range(4):
            threads.append(Thread(target=queue_print, args=(my_queue, i, event)))
            threads[i].start()
        for i in range(4):
            threads[i].join()

    def queue_process():
        proces = []
        for i in range(4):
            proces.append(Process(target=queue_print, args=(my_queue, i, event)))
            proces[i].start()
        for i in range(4):
            proces[i].join()

    event = Event_th()
    my_queue = Queue()
    queue_put(my_queue)
    print('threads')
    queue_threads()

    event = Event_proc()
    my_queue = Queue_proc()
    queue_put(my_queue)
    print('process')
    queue_process()



if __name__ == '__main__':
    test_queue()