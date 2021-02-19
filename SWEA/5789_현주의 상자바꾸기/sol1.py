import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        boxes[L-1 : R] = [i] * (R-L+1)

    print('#'+str(i), ' '.join([str(i) for i in boxes]))
