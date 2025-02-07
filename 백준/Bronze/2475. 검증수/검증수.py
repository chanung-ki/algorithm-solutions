num_list = list(map(int, input().split()))

sum = 0

for num in num_list:
    sum += num * num

print(sum%10)