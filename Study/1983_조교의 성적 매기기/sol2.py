import sys
sys.stdin = open('input.txt')

def my_calc(total_list, K):
    # K번의 등수 계산
    for i in range(1, len(total_list)+1): # 순위
        my_max = 0 # 최고점수
        max_index = 0 # 최고점인 애 번호
        for j in range(len(total_list)):
            if my_max < total_list[j]:
                my_max = total_list[j]
                max_index = j
        if total_list[max_index] == total_list[K-1]:
            return i
        else:
            total_list[max_index] = i

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    my_list = [list(map(int, input().split())) for _ in range(N)]
    # 점수 계산
    total_list = [0] * N
    for idx in range(N):
        total_list[idx] += my_list[idx][0] * 0.35
        total_list[idx] += my_list[idx][1] * 0.45
        total_list[idx] += my_list[idx][2] * 0.2
    # k가 몇등인지 계산
    k_index = my_calc(total_list, K)
    result = 0
    for i in range(10):
        if k_index <= N/10*(i+1):
            result = scores[i]
            break
    print('#{} {}'.format(tc, result))