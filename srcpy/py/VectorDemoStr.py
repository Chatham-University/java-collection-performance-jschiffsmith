import random
import string

stringslist = []
def VectorDemoStr(howManyNums):
    for i in range(howManyNums - 1):
        length = random.randint(1, 9)
        randomString = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        stringslist.append(randomString)
    for x in range(4):
        print(stringslist[x])
    return stringslist



