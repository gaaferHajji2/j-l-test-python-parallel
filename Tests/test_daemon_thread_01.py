import threading

import time

def thread_worker():
    while True:
        print("Do The Current Task...")
        time.sleep(1)

if __name__ == '__main__':
    j_l_worker = threading.Thread(target=thread_worker, daemon=True)
    # j_l_worker.daemon = True --> Same Above
    j_l_worker.start()

    print("Do Task 01")
    time.sleep(0.5)

    print("Do Task 02")
    time.sleep(0.6)

    print("Do Task 03")
    time.sleep(0.7)

    print("Finish From Tasks")