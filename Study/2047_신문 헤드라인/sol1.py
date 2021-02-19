import sys
sys.stdin = open('input.txt')

T = input()
for char in T:
    if ord(char) >= 97:
        char = chr(ord(char)-32)
    print(char, end="")