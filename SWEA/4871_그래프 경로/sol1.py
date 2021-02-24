import sys
sys.stdin=open('sample_input.txt')

def dfs(S):
    visit[S] = True
    for i in graph[S]:
        if visit[i] == False:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    # 방문 여부 확인
    # visit에 False를 일단 다 넣어놓고, 방문한적 있으면 True 넣어줄거임
    visit = [False for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        # 각 노드별로 간선 추가
        graph[a].append(b)

    S, G = map(int, input().split())
    dfs(S)
    result = 1
    if visit[G] == False: # 방문한 적이 없다
        result = 0
    print('#{} {}'.format(tc, result))

