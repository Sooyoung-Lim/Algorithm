import sys
sys.stdin = open('input.txt')

def BruteForce(pattern, text):
    i = 0  # pattern index
    j = 0  # text index
    while i < M and j < N:
        if pattern[i] != text[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == M :
        return 1
    else:
        return 0



T = int(input())
for tc in range(1,T+1):
    pattern = input()
    M = len(pattern)
    text = input()
    N = len(text)

    print('#{} {}'.format(tc, BruteForce(pattern, text)))

