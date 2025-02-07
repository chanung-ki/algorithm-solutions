price = int(input())
coins = [500, 100, 50, 10, 5, 1]

change = 1000 - price
result = 0

for coin in coins:
    if change == 0:
        break
    count, remain = divmod(change, coin)
    result += count
    change = remain
    
print(result)