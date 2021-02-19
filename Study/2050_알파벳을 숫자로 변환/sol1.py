import sys
sys.stdin = open('input.txt')

T = input()
for char in T:
    print(ord(char)-64, end=" ")

