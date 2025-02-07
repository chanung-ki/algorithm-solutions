import sys
t = int(sys.stdin.readline())
for _ in range(t):
    
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    apart = []
    apart.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    
    for i_k in range(1, k+1):
        temp_list = []
        for i_n in range(0, n):
            if i_n == 0:
                temp_list.append(1)
            else:
                # 자기 앞 호수 + 자기 아래층 호수
                people_num = temp_list[i_n-1] + apart[i_k-1][i_n]
                temp_list.append(people_num)
            
        apart.append(temp_list)
        
    sys.stdout.write(str(apart[k][n-1]) + '\n')