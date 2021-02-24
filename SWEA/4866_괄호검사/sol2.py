import sys
sys.stdin = open('sample_input.txt')

def solution(string):
    result = 1
    stack = []
    openers = ['(', '{', '[']
    closers = [')', '}', ']']

    for char in string:
        if char in openers:
            stack.append(char)

        if char in closers:
            # 닫는 괄호가 나왔는데 stack이 비어있다면 (opener < closer)
            if not len(stack): #stack에 아무것도 없다는 소리
                result = 0
                break
            # 닫는 괄호가 나왔는데 마지막 열린괄호랑 짝이 안맞는다면
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
        if len(stack):
            result = 0

    return result


T = int(input())
for tc in range(1, T+1):
    code = input()
    print('#{} {}'.format(tc, solution(code)))
