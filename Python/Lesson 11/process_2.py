import time
import logging
import tracemalloc
import requests

from multiprocessing import Pool


def fetch_url(url):
    try:
        resp = requests.get(url)
    except:
        logging.info(f"Error with requested url: {url}")
    else:
        return resp.content

def fetch_all(url_list): 
    pool = Pool()
    pool.map(fetch_url, url_list)

if __name__ == "__main__":

    URL = "https://www.google.com/"
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    
    for ntimes in [1, 10, 100, 500, 1000]:
        start = time.time()
        responses = fetch_all([URL]*ntimes)
        logging.info(f"Fetch count {ntimes}, Time: {time.time()-start}")
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())


# Current: 0, Peak: 0.
# 20:44:52: Fetch count 1, Time: 0.238814115524292
# 20:44:54: Fetch count 10, Time: 2.1485793590545654
# 20:45:22: Fetch count 100, Time: 28.657430171966553
# 20:47:31: Fetch count 500, Time: 128.68104481697083
# 20:51:52: Fetch count 1000, Time: 261.29435300827026
# Current: 1 657 166, Peak: 1 796 249.

# Current: 0, Peak: 0.
# 20:54:12: Fetch count 1, Time: 0.5086781978607178
# 20:54:12: Fetch count 10, Time: 0.28859853744506836
# 20:54:14: Fetch count 100, Time: 1.1940011978149414
# 20:54:18: Fetch count 500, Time: 4.733238697052002
# 20:54:27: Fetch count 1000, Time: 8.771993398666382
# Current: 2156420, Peak: 8382371.