import sys
sys.stdin=open('input.txt')

T = 10
for tc in range(1, T+1):
    tc, N = map(int, input().split())
    adj_list = list(map(int, input().split()))
    # print(adj_list)

    adj = {x:[] for x in range(100)}
    for i in range(0, N*2, 2):
        s = adj_list[i]
        e = adj_list[i+1]
        adj[s].append(e)
    # print(adj)

    stack = [0]
    visit = [False] * 100
    visit[0] = True

    answer = 0
    while stack:
        a = stack.pop()
        for neighbor in adj[a]:
            if neighbor == 99: # 바로 99 나오면 더 볼것도 없이 끝내면 됨
                answer = 1
                break
            if visit[neighbor] == False:
                stack.append(neighbor)
                visit[neighbor] = True
    print('#{} {}'.format(tc, answer))

    # 아 너무 어렵다






