import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    text = ''
    for _ in range(N):
        Ci, Ki = input().split()
        # 일단 인풋대로 한줄로 쭉 풀어서 적기
        text += Ci * int(Ki)

    print('#{}'.format(tc))
    # 인덱스 10씩 올라가면서 슬라이싱으로 10개씩 뽑아내
    for i in range(0, len(text), 10):
        print(text[i:i+10])

