money = int(input())
n = 0
coins = [500, 100, 50, 10]
for coin in coins:
    n += money // coin
    money = money % coin
print("%d" % n)