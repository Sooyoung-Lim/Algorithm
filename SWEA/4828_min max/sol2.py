import sys
sys.stdin = open('input.txt')

def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    number = list(map(int, input().split()))

    Bubble_sort(number)

    print('#{} {}'.format(tc, number[-1] - number[0]))