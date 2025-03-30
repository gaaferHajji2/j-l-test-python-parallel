import os
import threading
import multiprocessing as mp

def cpu_waster():
    while True:
        pass

print("Hi, My Name Is: ", __name__)
print("My Process ID Is: ", os.getpid())
print("My Parent Process ID Is: ", os.getppid())

if __name__ == '__main__':
    print("\n Process ID: ", os.getpid())
    print("Thread Count: ", threading.active_count())

    for thread in threading.enumerate():
        print("Thread: ", thread)

    print("\nStarting 3 CPU Wasters...")
    for i in range(3):
        mp.Process(target=cpu_waster).start()

    print("\n Process ID: ", os.getpid())
    print("Thread Count: ", threading.active_count())

    for thread in threading.enumerate():
        print("Thread: ", thread)