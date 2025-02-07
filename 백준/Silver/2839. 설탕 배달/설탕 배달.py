n = int(input())

def get_suger_count(n):
    
    bag_3 = 0
    
    while True:
        
        if n == 1 or n == 2:
            return -1
        elif n == 0:
            return bag_3
        else:
            if n % 5 == 0:
                bag_5 = n // 5
                return bag_3 + bag_5
            n -= 3
            bag_3 += 1
            

print(get_suger_count(n))