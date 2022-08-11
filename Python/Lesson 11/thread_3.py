import time
import tracemalloc

import threading


def power(x):
    return x ** x 

if __name__ == "__main__":
    threads = list()
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()
    for i in range(100000, 100016):
        thread = threading.Thread(target=power, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")