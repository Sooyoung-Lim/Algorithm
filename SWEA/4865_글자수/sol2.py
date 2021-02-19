import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    pattern = input()
    text = input()

    pattern_dict = {}
    for char in pattern:
        pattern_dict[char] = 0

    for char in text:
        if char in pattern_dict:
            pattern_dict[char] += 1

    print('#{} {}'.format(tc, max(pattern_dict.values())))

