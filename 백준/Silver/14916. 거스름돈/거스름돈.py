n = int(input())

def get_coin_count(n):
    
    count_2 = 0
    
    while True:
        
        if n == 1:
            return -1
        elif n % 5 == 0:
            count_5 = n // 5
            return count_5 + count_2
        elif n == 0:
            return count_5 + count_2
        else:
            n -= 2
            count_2 += 1

print(get_coin_count(n))