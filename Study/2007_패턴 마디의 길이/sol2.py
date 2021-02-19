import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()

    pattern = []
    for i in range(1, 11):
        pattern.append(text[:i])
    # print(pattern)

    for i in range(10):
