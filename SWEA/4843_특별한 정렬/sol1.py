import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 정수의 갯수
    numbers = list(map(int, input().split()))
    # print(numbers)

    result = []
    while len(numbers) > 0:
        max_value = max(numbers)
        result.append(max_value)
        numbers.remove(max_value)

        min_value = min(numbers)
        result.append(min_value)
        numbers.remove(min_value)

    result = ' '.join(map(str, result[0:10]))
    print('#{} {}'.format(tc, result))




    # idx_list = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    # new_list = []
    # for i in range(10):
    #     new_list.append(numbers[idx_list[i]])
    # print(new_list)
