# I/O bound task use Threading : Async Method
# CPU bound task use Multiprocessing

import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(sec):
    print(f"Sleeping {sec} Second....")
    time.sleep(sec)
    return f"Done Sleeping....{sec}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # print(f1.result())
    
    secs = [5, 4, 3, 2, 1]

    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = executor.map(do_something, secs)
    for result in results:
        print(result)


def _threading():
    threads = []

    for _ in range(10):
        t = threading.Thread(target=do_something,args=[1.5])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

