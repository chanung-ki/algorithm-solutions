n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

count = 1

weight_list = []

for rope in ropes:
    weight_list.append(rope * count)
    count += 1
    
print((max(weight_list)))