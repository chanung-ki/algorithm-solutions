texts = list(input().split('.'))

def poliomino(texts):
    
    for index, text in enumerate(texts):
        if 'X' in text:
            length = len(text)
            count_a = length // 4
            count_b = (length % 4) // 2
            if ((length % 4) % 2) != 0:
                return -1
            else:
                updated_text = ('AAAA' * count_a) + ('BB' * count_b)
                texts[index] = updated_text
    return '.'.join(texts)

print(poliomino(texts))