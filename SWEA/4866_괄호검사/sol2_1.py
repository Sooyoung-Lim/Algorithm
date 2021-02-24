import sys
sys.stdin=open('sample_input.txt')

def solution(text):
    result = 1
    stack = []
    opener = ['(', '{', '[']
    closer = [')', '}', ']']

    for char in text:
        if char in opener:
            stack.append(char)

        if char in closer:
            if len(stack) == 0:
                result = 0
                break
            elif char == ')' and stack.pop() != '(':
                result = 0
                break
            elif char == '}' and stack.pop() != '{':
                result = 0
                break
            elif char == ']' and stack.pop() != '[':
                result = 0
                break
    # 스트링이 끝났는데, stack이 남아있다면. (opener > closer)
    else:
        if len(stack) :
            result = 0
    return result


T = int(input())
for tc in range(1, T+1):
    text = input()

    print('#{} {}'.format(tc, solution(text)))
