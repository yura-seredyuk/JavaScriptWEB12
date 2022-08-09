from data import RESPONSES
import time
import logging
import tracemalloc

import threading


def func(name, dalay):
    logging.info(f"Thread {name}: starting")
    time.sleep(dalay)
    logging.info(f"Thread {name}: finished")


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    threads = []
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()

    for item in RESPONSES:
        thread = threading.Thread(target=func, args=(item[0], item[1],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")


