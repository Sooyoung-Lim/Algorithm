import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    text = list(input())
    stack = []

    for i in range(len(text)):
        # 스택이 비었거나, 스택의 마지막 값이 넣을값과 같지 않으면 넣어준다
        if not stack or stack[-1] != text[i]:
            stack.append(text[i])

        # 스택이 안 비어있고, 스택의 마지막 값이랑 넣을 값이 같으면 스택에서 제거
        elif stack[-1] == text[i]:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))





