import sys
sys.stdin = open('input.txt')

T= int(input())
for i in range(T+1):
    print(2**i, end=" ")