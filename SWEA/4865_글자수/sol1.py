import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    pattern = input()
    text = input()

    pattern_dict = {}
    for i in range(0, len(pattern)):
        for j in range(1, len(pattern)+1):
            pattern_dict.update({pattern[i:i+j] : 0})

    for key, value in pattern_dict.items():
        if key in text:
            value += 1

    print(pattern_dict)

