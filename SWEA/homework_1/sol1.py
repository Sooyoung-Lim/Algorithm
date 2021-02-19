import sys
sys.stdin = open('input.txt')

# tc 갯수 10개
for tc in range(1, 11):
    T = int(input())

    # 빌딩 높이
    heights = list(map(int, input().split()))
    # 조망권을 확보한 건물의 수
    count = 0
    # 인덱스. 앞에 두칸은 건물을 안지으니까 2부터 시작한다.
    idx = 2

    # 맨 마지막 두칸도 건물을 안지으니까 그전까지만 돌면 되고
    while idx < T-2:
        # 왼쪽으로 두개, 하나 /  오른쪽으로 하나 비교해서 건물이 가장 놓은지를 확인한다.
        # 가장 높지 않은 경우, 오른쪽으로 한칸 이동해서 쭉~~~ 비교
        if heights[idx] <= heights[idx-2] or heights[idx] <= heights[idx-1] or heights[idx] <= heights[idx+1]:
            idx += 1
            pass
        # 근데 만약 오른쪽 두칸보다 작으면, 오른쪽 한칸은 더 볼것도 없이 바로 두칸 이동이 가능하다.
        elif heights[idx] <= heights[idx+2]:
            idx += 2
            pass
        # 만약 왼쪽2 오른쪽2 총 4구역 중 지금이 가장 높은 건물이면, 카운트에 추가해준다.
        # 그리고 오른쪽으로 세칸 점프
        else:
            count += heights[idx] - max(heights[idx-2], heights[idx-1], heights[idx+1], heights[idx+2])
            idx += 3

    print('#{} {}'.format(tc, count))

