import sys
sys.stdin = open('input.txt')

N = int(input())
result = 0
while N > 0:
    result += N % 10
    N = N // 10

print(result)