from pynput import keyboard
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
from playsound import playsound

count = 0
pooler = ProcessPoolExecutor()
sound = Process(target=playsound, args=('a.mp3',))
newSound = lambda : Process(target=playsound, args=('a.mp3',))

def main():
    print(sound)
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
#end main

def on_press(key):
    global count
    global pooler
    global sound

    if key == keyboard.Key.esc:
        sound.terminate()
        pooler.shutdown()
        return False
    try:
        k = key.char
    except:
        k = key.name

    if k in ['a', 'enter']:
        pooler.submit(square, count)
        sound.start()
        count += 1
    
    elif k not in ['q']:
        print_key(k)
    else:
        print_baka()
        sound.terminate()
        sound = newSound()
#end on_press

def print_key(k):
    print('Key pressed: ' + k)

def print_baka():
    print('baka')

def square(x: int):
    print(f"{x}^2 = {x ** 2}")

if __name__ == '__main__':
    main()