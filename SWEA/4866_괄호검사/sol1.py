import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    text_stk = []
    ans = 1
    text_list = list(input().split(''))
    print(text_list)

    # for i in range(len(text_list)):
    #     if text_list[i] == '(' or text_list[i] == '{' :
    #         text_stk.append(text_list[i])
    #     elif text_list[i] == ')' or text_list[i] == '}':
    #         if not stk:
    #             ans = 0
    #             break
    #         P = text_stk.pop()
    #         if text_list[i] == ')' and P != '(':
    #             ans = 0
    #         elif text_list[i] == '}' and P != '{':
    #             ans = 0
    # if text_stk:
    #     ans = 0
    # print('#{} {}'.format(tc, ans))