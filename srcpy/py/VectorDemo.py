import random


nums = []
def VectorDemo(howManyNums):
    for i in range(howManyNums - 1):
        nums.append(random.randint(0,howManyNums - 1))
    for x in range(4):
        print(nums[x])
    return nums




