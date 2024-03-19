def minimumAddedCoins(coins, target):
    coins.sort()
    a=0
    min = 0
    for i in coins:
        if i > a + 1:
            return min + 1
        a += i
        min += 1
        if a >= target:
            return min
    while a < target:
        a += a + 1
        min += 1
    return min

print(minimumAddedCoins([1,1,1],20))
