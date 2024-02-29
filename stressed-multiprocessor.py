#!/usr/bin/env python3

from multiprocessing import Process

print("Stress testing CPU")

def burn(myprocess):
    print(f"Starting process {myprocess}") 
    while True:
        pass

if __name__ == "__main__":
    for i in range(8):
        p = Process(target=burn, args=(i,))
        p.start()

# If we weren't being silly and cooking the cpu we'd use p.join() here to tie things together.
