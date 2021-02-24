import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    M = int(input())

    change = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
    for key, value in change.items():
        change[key] = M // key
        M %= key
        result = change.values()

    print('#{}'.format(tc))
    print(result)



