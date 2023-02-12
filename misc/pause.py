import time
from multiprocessing import Process,Event

def ad(e):
    adloop = lambda : input("input\n>>") != "1"
    while adloop():
        print("Checking for popups...")
        e.set()
    

    print("Popup!")
    e.clear()


def count(e):
    amount = 0
    while True:
        e.wait()  # sleep process when event is clear.
        amount += 1
        print(amount)
        time.sleep(1)


def main():
    print("here")
    # Create an event to share between the processes.
    # When set, the counting process will count.
    e = Event()
    e.set()
    print("here")

    # Make processes daemons, so exiting main process will kill them.
    p1 = Process(target = ad, args=(e,), daemon=True)
    p1.start()
    print("here")
    p2 = Process(target = count, args=(e,), daemon=True)
    p2.start()
    input('hit ENTER to exit...')


if __name__ == "__main__":
    main()