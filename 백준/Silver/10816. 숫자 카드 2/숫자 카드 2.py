import sys
from collections import Counter

n = int(sys.stdin.readline())
holded_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
problem_cards = list(map(int, sys.stdin.readline().split()))

card_count = Counter(holded_cards)

for card in problem_cards:
    sys.stdout.write(str(card_count[card]) + ' ')