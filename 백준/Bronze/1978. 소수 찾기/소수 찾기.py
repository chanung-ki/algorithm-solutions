n = int(input())
nums = list(map(int, input().split()))

count = 0

for num in nums:
    for i in range(2, num+1):
        if num % i == 0:
            if i == num:
                count += 1
            else:
                break
print(count)