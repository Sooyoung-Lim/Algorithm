import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    # A가 이기는 경우
    if (A==1 and B==3) or (A==2 and B==1) or (A==3 and B==2):
        print('A')
    # 비기는 경우
    elif A==B:
        print('tie')
    # B가 이기는 경우
    else:
        print('B')