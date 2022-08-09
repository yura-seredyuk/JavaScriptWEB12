import time
import logging
import tracemalloc
import requests


def fetch_url(url):
    try:
        resp = requests.get(url)
    except:
        logging.info(f"Error with requested url: {url}")
    else:
        return resp.content

def fetch_all(url_list):
    for link in url_list:
        response = fetch_url(link)

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
