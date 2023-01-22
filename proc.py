from concurrent.futures import ThreadPoolExecutor, Future
from playsound import playsound
from pynput import keyboard

task: Future
pool: ThreadPoolExecutor
args = (playsound, 'a.mp3', False)

def main():
    global task
    global args
    global pool

    pool = ThreadPoolExecutor(max_workers=2)
    task = pool.submit(*args)

    # sleep(1000)

    # task.cancel()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
#end main

def on_press(key):
    global task
    global args
    global pool

    if key == keyboard.Key.esc:
        task.cancel()
        pool.shutdown()
        return False
    try:
        k = key.char
    except:
        k = key.name

    if k in ['a', 'enter']:
        pool.submit(*args)
    else:
        task.cancel()
#end on_press

if __name__ == '__main__':
    main()