from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    score_list = []
    for i in range(1, N+1):
        a, b, c = map(int, input().split())
        score = a*0.35 + b*0.45 + c*0.2
        # key point1_학생의 점수와, 몇번째 학생인지를 튜플로 묶어서 함께 append 한다
        score_list.append((score, i))

    # 보기편하려고 내림차순 정렬
    score_list.sort(reverse=True)
    print(score_list)

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


    group_counts = N // 10  # 한 학점에 몇명까지 들어갈 수 있는가, 의 의미
    grade_idx = 0
    for i in range(N):
        if score_list[i][1] == K:
            # key point2_이렇게 몫으로 처리해버리는 게 핵심
            grade_idx = i // group_counts

    print('#{} {}'.format(tc, grade[grade_idx]))