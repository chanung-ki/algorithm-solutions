import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())

a = set([input().strip() for _ in range(n)])
b = set([input().strip() for _ in range(m)])

c = a & b

c = list(c)
c.sort()
sys.stdout.write(str(len(c)) + '\n' + '\n'.join(c))