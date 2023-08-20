# multi-processing = running tasks in parallel on different cpu cores, bypass GIL used for threading
                   # multiprocessing = better for cpu bound tasks (Heavy cpu usage)
                   # multithreading = better for io bound tasks (waiting around)

from multiprocessing import cpu_count, Process
import time

def counter(num):
    count = 0
    while count < num:
        count+=1

def main():

    print(cpu_count())
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print(time.perf_counter())
# if __name__ == '__main__': is to ensure that the script's main logic is only executed by the main process and not by processes spawned by the multiprocessing module.
# if __name__ == '__main__': block is not present, each process you create would again start executing from the top of the script, leading to multiple processes creating more processes, and so on

if __name__ == '__main__':
    main()


"""
= The code demonstrates how to use the multiprocessing module to create parallel processes that  perform a computation.

= Parallelism can take advantage of multiple CPU cores to speed up computation, especially for   CPU-bound tasks.

= Each process runs independently, allowing for true parallel execution.

= The actual speedup you achieve depends on the number of CPU cores available and the nature of  the task. In your case, with 4 cores and a runtime of around 40 seconds, the parallel
  execution seems to have provided a speedup to some extent.
  
"""