import time
import threading

def countdown(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print(f"{name} is counting down: {counter}...")
        counter -= 1
    print(f"{name} finished counting down")

if __name__ == "__main__":
    thread1 = threading.Thread(target=countdown, args=("Thread Alice", 1))
    thread2 = threading.Thread(target=countdown, args=("Thread Bob", 2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

