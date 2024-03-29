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
# Current: 2 156 420, Peak: 8 382 371.

# Current: 0, Peak: 0.
# 20:57:10: Fetch count 1, Time: 0.9773504734039307
# 20:57:12: Fetch count 10, Time: 1.5024409294128418
# 20:57:20: Fetch count 100, Time: 8.425093650817871
# 20:57:54: Fetch count 500, Time: 34.302616119384766
# 20:59:01: Fetch count 1000, Time: 66.27125334739685
# Current: 617 564, Peak: 17 942 206.

# 21:13:19: Fetch count 1, Time: 0.7997395992279053
# 21:13:20: Fetch count 10, Time: 0.7418296337127686
# 21:13:21: Fetch count 100, Time: 1.1118485927581787
# 21:13:24: Fetch count 500, Time: 2.8634135723114014
# 21:13:30: Fetch count 1000, Time: 5.5502753257751465
# Current: 8 679 052, Peak: 25 670 965.