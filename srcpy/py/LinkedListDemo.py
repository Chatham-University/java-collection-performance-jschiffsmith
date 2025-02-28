import random
from collections import deque

dq = deque()
def linkedListDemo(howManyNums):
    for i in range(howManyNums):
        dq.append((random.randint(0,howManyNums)))
    for i in range(4):
        print(dq[i])


