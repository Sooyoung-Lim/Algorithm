import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = 'frehhgrf'
    for i in range(len(word)):
        if word[i] == word[len(word)-1-i]:
            result = 1
        else:
            result = 0
    print('#{} {}'.format(tc,result))