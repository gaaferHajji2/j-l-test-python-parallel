import os
import threading

def cpu_waster():
    while True:
        pass

print("\n Process ID: ", os.getpid())
print("Thread Count: ", threading.active_count())

for thread in threading.enumerate():
    print("Thread: ", thread)

print("\nStarting 12 CPU Wasters...")
for i in range(12):
    threading.Thread(target=cpu_waster).start()

print("\n Process ID: ", os.getpid())
print("Thread Count: ", threading.active_count())

for thread in threading.enumerate():
    print("Thread: ", thread)