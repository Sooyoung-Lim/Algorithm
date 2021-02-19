# 정렬(버블정렬) 이용! 제일 높은 박스는 오른쪽 끝으로, 제일 낮은 박스는 왼쪽 끝으화로.
# 그리고, 제일 높은 박스를 왼쪽으로 이동하는 것까지 생각해보
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101

    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자
    for i in range(len(box)):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value - 1:
        # 상자 옮기기
        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value - 1] += 1

        # 포인터를 변경하자
        if h_cnt[min_value] == 0:
            min_value += 1

        if h_cnt[max_value] == 0:
            max_value -= 1

        # 덤프 줄이기
        N -= 1

    print('#{} {}'.format(tc, max_value - min_value))