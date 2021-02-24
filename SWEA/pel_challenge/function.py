
import sys
from datetime import datetime
sys.stdin = open('test.txt')
# s가 들어왔을 떄 가장 긴 회문의 길이 뽑는 함수
def solution(s):
    n = len(s)

    # 회문 판별
    # 회문이면 result에 append
    result = []
    for i in range(n):
        for j in range(n, i, -1):
            if s[i:i+j] == s[i:i+j][::-1]:
                result.append(s[i:i+j])

    # result 결과들 중에 제일 긴 길이 뽑기
    max_length = 0
    for word in result:
        if len(word) > max_length:
            max_length = len(word)

    return(max_length)

T = int(input())
for tc in range(1, T+1):
    start = datetime.now()
    solution(input())
    end = datetime.now()
    print('#{} {}'.format(10 * 10**tc, end-start))