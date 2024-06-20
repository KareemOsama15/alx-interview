#!/usr/bin/python3
def makeChange(coins, total):
    """
    method determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1

# print(makeChange([1, 2, 25], 37))
# print(makeChange([1256, 54, 48, 16, 102], 1453))
