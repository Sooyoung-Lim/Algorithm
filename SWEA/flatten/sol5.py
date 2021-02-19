# 함수로 해보기
# 정렬 일단 안할거다. 데이터 갯수가 많아지면 정렬은 조금 부담스러울 수도 있어서...
# 재귀함수 푸는거 대비
import sys
sys.stdin = open('input.txt')

T = 10

def solution(dump_limit, boxes):

    for _ in range(dump_limit):
        max_idx = min_idx = 0
        # 가장 큰 / 작은 박스 찾기
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # dump 한 회차가 끝나고 확인
        max_idx = min_idx = 0
        # 가장 큰 / 작은 박스 찾기
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        diff = boxes[max_idx] - boxes[min_idx]
        if diff == 0:
            return 0
        elif diff == 1:
            return 1

    # for 문 끝났으면 (dump_limit 만큼 종료)
    max_idx = min_idx = 0
    for idx in range(len(boxes)):
        if boxes[idx] > boxes[max_idx]:
            max_idx = idx
        elif boxes[idx] < boxes[min_idx]:
            min_idx = idx
    return boxes[max_idx] - boxes[min_idx]


for tc in range(1, T+1):
    dump_limit = int(input())
    boxes = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(dump_limit, boxes)))