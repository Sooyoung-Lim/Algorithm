# 정렬(버블정렬) 이용! 제일 높은 박스는 오른쪽 끝으로, 제일 낮은 박스는 왼쪽 끝으
import sys
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        bubble_sort(box)
        box[0] += 1
        box[-1] -= 1
    # 마지막에도 정렬한번!
    bubble_sort(box)

    print('#{} {}'.format(tc, box[-1]-box[0]))