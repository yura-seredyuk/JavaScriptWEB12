import time
import logging
import tracemalloc
import requests

import threading


def fetch_url(url):
    try:
        resp = requests.get(url)
    except:
        logging.info(f"Error with requested url: {url}")
    else:
        return resp.content

def fetch_all(url_list):
    threads = []
    for link in url_list:
        thread = threading.Thread(target=fetch_url, args=(link,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

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
