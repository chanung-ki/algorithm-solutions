import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

memos = {}
for _ in range(n):
    url, password = input().rstrip().split()
    memos[url] = password

for _ in range(m):
    url = input().rstrip()
    print(memos[url])