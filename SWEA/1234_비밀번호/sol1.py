import sys
sys.stdin=open('input.txt')

T=10
for tc in range(1, T+1):
    N, code = input().split()
    N = int(N)
    stack = []

    for i in range(N):
        # 스택이 비었거나 스택의 마지막 값이 넣을 값과 같지 않으면 넣어준다
        if not stack or stack[-1] != code[i]:
            stack.append(code[i])

        # 스택이 안 비어있고, 스택의 마지막 값이랑 넣을 값이 같으면 스택에서 제거
        elif stack[-1] == code[i]:
            stack.pop()
    print('#{} {}'.format(tc, ''.join(stack)))