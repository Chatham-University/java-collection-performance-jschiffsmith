import time
import math

from py.LinkedListDemoStr import linkedListDemoStr
from py.VectorDemo import VectorDemo
from py.LinkedListDemo import linkedListDemo
from py.ArrayDemo import arrayDemo
from py.VectorDemoStr import VectorDemoStr

    # 10^3 = 1,000
    # 10^6 = 1 million
    # 10^9 = 1 billion
    # 10^10 = 10 billion, too big for Phil's computer

howManyNums = int(math.pow(10,7))

def main():
    print("The first few vector numbers are")
    start = time.time()
    VectorDemo(howManyNums)
    end = time.time()
    print(f"Vector Time:{(end - start) / 1000}")

    print("The first few vector strings are")
    start = time.time()
    VectorDemoStr(howManyNums)
    end = time.time()
    print(f"String Vector Time:{(end - start) / 1000}")

    print("The first few linked list numbers are")
    start = time.time()
    linkedListDemo(howManyNums)
    end = time.time()
    print(f"Linked List Time:{(end - start) / 1000}")

    print("The first few linked list strings are")
    start = time.time()
    linkedListDemoStr(howManyNums)
    end = time.time()
    print(f"Linked List Time:{(end - start) / 1000}")

    print("The first few array numbers are")
    start = time.time()
    arrayDemo(howManyNums)
    end = time.time()
    print(f"Array Time:{(end - start) / 1000}")


print(main())



