# Simple Threads Pool

from multiprocessing.dummy import Pool as ThreadPool
from datetime import date
from datetime import datetime
import time

multiply_results = []
def squareNumber(n):
    multiply_results.append(n ** 2)
    dt_string = datetime.now().strftime("%H:%M:%S")
    millis = int(round(time.time() * 1000))
    print("Each Thread Time - %d" % millis)
    time.sleep(2)
    return n ** 2

# function to be mapped over
def calculateParallel(numbers, threads=10):
    pool = ThreadPool(threads)
    results = pool.map(squareNumber, numbers)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    squaredNumbers = calculateParallel(numbers, 15)
    for n in multiply_results:
        print(n)
    print("Results Length - %d" % len(multiply_results))