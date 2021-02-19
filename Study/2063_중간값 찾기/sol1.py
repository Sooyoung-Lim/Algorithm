import sys
sys.stdin = open('input.txt')

T = 199
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    for i in range(len(numbers)-1):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    print(numbers[len(numbers)//2])