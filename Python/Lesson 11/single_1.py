from data import RESPONSES
import time
import logging
import tracemalloc


def func(name, dalay):
    logging.info(f"Response {name}: starting")
    time.sleep(dalay)
    logging.info(f"Response {name}: finished")


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()

    for item in RESPONSES:
        func(item[0], item[1])

    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")

# Current: 16 160, Peak: 18 252.
# All done! 155.26223397254944

# Current: 152 939, Peak: 158 549.
# All done! 10.021612167358398

# Current: 1 447 713, Peak: 1 470 930.
# All done! 24.335220336914062

# Current: 68 367, Peak: 96 822.
# All done! 10.010364770889282 