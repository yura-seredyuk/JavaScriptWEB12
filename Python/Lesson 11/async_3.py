import time
import tracemalloc

import asyncio


async def power(x):
    return x ** x

async def main():
    tasks = [asyncio.create_task(power(i)) for i in range(100000, 100016)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()

    asyncio.run(main())
    loop.close()

    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")