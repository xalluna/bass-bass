from threading import Thread
from pynput import keyboard

worker_queue = []
count = 0
isActive = True

def square(x: int):
    print(f"{x}^2 = {x ** 2}")

def on_press(key):
    global worker_queue
    global count
    global isActive

    try:
        k = key.char  # single-char keys
    except:
        k = key.name

    if k in ["a", "s", "d", "enter"]:
        print(k)
        worker_queue = [*worker_queue, (square, (count,))]
        count += 1
        return False
    elif k in ['q', 'esc']: 
        isActive = False
        return False

def worker():
    global worker_queue
    while(isActive):
        if(len(worker_queue) < 1):
            continue

        task, args, *_ = worker_queue[0]
        task(*args)

t1 = Thread(target=worker, args=(), daemon=True)
t1.start()


while(isActive):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()
    
listener.join()
t1.join()