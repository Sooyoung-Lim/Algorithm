import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    numbers = list(map(int, input().split()))
    # print(numbers)

    # 최대 최소값 구하기
    max_value = max(numbers)
    min_value = min(numbers)
    # 최대 최소값 리스트에서 빼주고, 정렬
    numbers.remove(max_value)
    numbers.remove(min_value)
    numbers.sort()

    result = sum(numbers) / len(numbers)
    print('#{} {}'.format(tc, round(result)))





