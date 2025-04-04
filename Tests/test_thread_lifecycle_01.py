import threading
import time

class JLThread(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print("Start Working On Task")
        time.sleep(3)
        print("The End Of My Task")

if __name__ == '__main__':
    print("Start Working On Main Thread, And Creating Helper Thread")
    j_l_thread = JLThread()

    print("The Status Of j_l_thread is_alive: ", j_l_thread.is_alive()) # --> False

    print("Start The Helper Thread")
    j_l_thread.start()

    print("Do Some Work In Main Thread")
    time.sleep(0.5)

    print("The Status Of j_l_thread is_alive: ", j_l_thread.is_alive()) # --> True

    print("Make Main Thread Wait Until Helper Thread Finish")
    j_l_thread.join()

    print("The Status Of j_l_thread is_alive: ", j_l_thread.is_alive()) # --> False

    print("The End Of Main Script")