import sys
sys.stdin = open('input.txt')

T = int(input())
total = 0
for i in range(T+1):
    total += i
print(total)