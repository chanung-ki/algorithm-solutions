import sys
t = int(sys.stdin.readline())
test_cases = [sys.stdin.readline().strip() for _ in range(t)]

for test_case in test_cases:
    
    while True:
        replace_test_case = test_case.replace('()', '')
        
        if test_case == replace_test_case:
            print('NO')
            break
        
        test_case = replace_test_case
        
        if test_case == '':
            print('YES')
            break