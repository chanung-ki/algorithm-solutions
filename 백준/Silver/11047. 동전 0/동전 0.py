n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
    
coins.sort(reverse=True)

result = 0

for coin in coins:
    if n == 0:
        break
    if k >= coin:
        count, remain = divmod(k, coin)
        result += count
        k = remain

print(result)