import time
import tracemalloc


def power(x):
    return x ** x 


if __name__ == "__main__":

    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    start = time.time()

    for i in range(100000, 100016):
        power(i)

    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())
    print(f"All done! {time.time()-start}")

# Current: 0, Peak: 0.
# Current: 28, Peak: 994972.
# All done! 1.4806311130523682

# D:\STEP\#WEB12\JavaScriptWEB12\Python\Lesson 11>python async_3.py
# Current: 0, Peak: 0.
# Current: 35790, Peak: 4364987.
# All done! 1.4218180179595947

# D:\STEP\#WEB12\JavaScriptWEB12\Python\Lesson 11>python thread_3.py 
# Current: 0, Peak: 0.
# Current: 46331, Peak: 1042059.
# All done! 1.473097801208496

# D:\STEP\#WEB12\JavaScriptWEB12\Python\Lesson 11>python process_3.py
# Current: 0, Peak: 0.
# Current: 1610166, Peak: 5370874.
# All done! 0.7221381664276123