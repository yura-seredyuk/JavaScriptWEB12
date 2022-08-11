import time
import tracemalloc

from multiprocessing import Pool


def power(x):
    return  x ** x

def main():
    p = Pool()
    p.map(power, [i for i in range(100000, 100016)])

if __name__ == "__main__":

    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()

    main()

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