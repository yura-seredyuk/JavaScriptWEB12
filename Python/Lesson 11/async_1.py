from data import RESPONSES
import time
import logging
import tracemalloc

import itertools
import asyncio


loop = asyncio.get_event_loop()

async def func(name, dalay):
    logging.info(f"Response {name}: starting")
    await asyncio.sleep(dalay)
    logging.info(f"Response {name}: finished")


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()
    tasks = itertools.starmap(func, RESPONSES)
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")

# Current: 16 160, Peak: 18 252.
# All done! 155.26223397254944

# Current: 152 939, Peak: 158 549.
# All done! 10.021612167358398

# Current: 1 447 713, Peak: 1 470 930.
# All done! 24.335220336914062