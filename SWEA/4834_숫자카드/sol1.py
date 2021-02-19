import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 카드 갯수
    N = int(input())
    numbers = list(map(int, input()))

    # 0~9 자리 만들고(counter) 숫자카드 있는 것들은 각각의 갯수로 표시
    counter = [0] * 10
    for number in numbers:
        counter[number] += 1

    # for 문 돌면서 갯수 제일 큰거랑 인덱스 가져오기
    max_index = 0
    max_num = 0
    # 만약 같은 갯수이면 큰 숫자를 뽑아야 하니까, range 범위를 큰수에서 -> 작은수로 줄여간다.
    for i in range(9, -1, -1):
        if counter[i] > max_num:
            max_num = counter[i]
            max_index = i

    print("#{} {} {}".format(tc, max_index, max_num))
