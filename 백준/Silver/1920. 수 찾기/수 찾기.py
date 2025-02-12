import sys
n = int(sys.stdin.readline())
a = set(sys.stdin.readline().split())
m = int(sys.stdin.readline())
m_num = sys.stdin.readline().split()

for num in m_num:
    if num in a:
        sys.stdout.write('1'+'\n')
    else:
        sys.stdout.write('0'+'\n')