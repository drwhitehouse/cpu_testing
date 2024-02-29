#!/usr/bin/env python3

import threading

print("Stress testing CPU")

def burn(mythread):
    print(f"Starting thread {mythread}") 
    while True:
        pass

if __name__ == "__main__":
    for i in range(8):
        x = threading.Thread(target=burn, args=(i,))
        x.start()

# If we weren't being silly and cooking the cpu we'd use x.join() here to tie things together.
