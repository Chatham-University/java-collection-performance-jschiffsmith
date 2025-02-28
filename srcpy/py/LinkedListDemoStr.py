import random
import string
from collections import deque

dq = deque()
def linkedListDemoStr(howManyNums):
    for i in range(howManyNums):
        length = random.randint(1, 9)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        dq.append(random_string)
    for i in range(4):
        print(dq[i])


