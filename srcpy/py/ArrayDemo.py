import random
import array as arr

a = arr.array('i')
def arrayDemo(howManyNums):
    for i in range(howManyNums - 1):
        a.append(random.randint(0,howManyNums))
    for i in range(4):
        print(a[i])









