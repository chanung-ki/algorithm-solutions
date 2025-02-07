t = int(input())

count_a = 0
count_b = 0
count_c = 0

if t % 10 != 0:
    print(-1)
else:
    count_a = t // 300
    count_b = (t%300)//60
    count_c = ((t%300)%60)//10
    print(f'{count_a} {count_b} {count_c}')