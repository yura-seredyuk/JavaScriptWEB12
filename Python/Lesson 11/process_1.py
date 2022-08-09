from data import RESPONSES
import time
import logging
import tracemalloc

from multiprocessing import Pool


def func(response):
    print(f"{time.strftime('%H:%M:%S', time.localtime())}: Process {response[0]}: starting")
    time.sleep(response[1])
    print(f"{time.strftime('%H:%M:%S', time.localtime())}: Process {response[0]}: finished")

def main():
    p = Pool()
    p.map(func, RESPONSES)

if __name__ == "__main__":

    
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()

    main()

    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")