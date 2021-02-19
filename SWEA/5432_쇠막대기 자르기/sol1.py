import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = input().replace('()', '*')
    # print(data)

    # uncut은 내가 자를 수 있는 쇠막대기의 갯수. )로 끝나면 더이상 자를 수 없기 때문에 얘를 카운트 해줘야 함.
    # result는 쇠막대기 조각의 갯수. 잘리든 말든 일단 들어오면 하나가 추가되어야 하기 때문에, ( 와 함께 +1 해준다.
    uncut = 0
    result = 0
    for i in data:
        if i == '*':
            result += uncut
        elif i == '(':
            uncut += 1
            result += 1
        elif i == ')':
            uncut -= 1
    print('#{} {}'.format(tc, result))