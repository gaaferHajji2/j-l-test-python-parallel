import threading

import time

chopping = True

def vegetable_chopper():
    name = threading.current_thread().name

    print(f"The Name Of Current Thread Is: {name}")

    vegetable_count = 0

    while chopping:
        print(name, 'chopped vegetable') # This Will Make The Thread Slower
        vegetable_count += 1

    print(name, 'chopped', vegetable_count, 'vegetables.')

if __name__ == '__main__':
    threading.Thread(target=vegetable_chopper, name='J-L-01').start()
    threading.Thread(target=vegetable_chopper, name='J-L-02').start()

    time.sleep(1)

    chopping = False