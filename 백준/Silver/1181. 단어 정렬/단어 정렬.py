import sys
n = int(sys.stdin.readline())
words = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    if not word in words:
        words.append(word)

words.sort(key=lambda x: (len(x), x))

sys.stdout.write('\n'.join(words))