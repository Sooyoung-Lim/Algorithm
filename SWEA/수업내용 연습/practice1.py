# arr = [[1,2,3,4],
#        [5,6,7,8],
#        [10,11,12,13]
#        ]
#
# N = 3 # 행의길이
# M = 4 # 열의길이
# len(arr) # 행의길이
# len(arr[0]) # 열의길이. 단 모든 요소의 열의 길이가 같다는 가정하에...

# 행 우선순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])

# 행 우선순회를 역으로
# for i in range(N):
#     for j in range(M-1, -1, -1):
#         print(arr[i][j])

# 열 우선순회
# for j in range(M):
#     for i in range(N):
#         print(arr[i][j])

# 열 우선순회를 역으로
# for j in range(M):
#     for i in range(N-1, -1, -1):
#         print(arr[i][j])

# 지그재그 순회
# for i in range(N):
#     if i % 2 == 0:
#         for j in range(M):
#             print(arr[i][j])
#     else:
#         for j in range(M-1, -1, -1):
#             print(arr[i][j])

# 지그재그 순회 방법2
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M-1-j-j)*(i % 2)])


#### 델타를 이용한 2차 배열 탐색
# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
#
# r = 0
# c = 1
# N = 3
# # 상하좌우
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# # 상하좌우 방법2
# drc = [[-1,0], [1,0], [0,-1], [0,1]]
#
# for i in range(4):
#     nr = r + dr[i]
#     nc = c + dc[i]
#
#     # 자 그런데, 파이썬은 음수인덱싱이 가능하기 떄문에 오히려 때때로 내 의도와 다르게 작동해버리는 경우가 있다.
#     # (차라리 에러가 나버렸으면 나을텐데 말이다.) 따라서...
#     # 방법1) 범위를 벗어나면 아무것도 하지마!
#     if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
#     print(arr[nr][nc])
#
#     # 방법2) 범위 안에서만 해!
#     if 0 <= nr < N and 0 <= nc < N:
#         print(arr[nr][nc])

# 대각선, 체스에서 나이트의 움직임 등도 위의 델타를 이용하여 방문하도록 짤수있다



# ##### 전치행렬 (대각선을 기준으로 뒤짚기)
# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
#
# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#
#         print(arr[i][j])



# 부분집합
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# arr = [3,6,7,1,5,4]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()


###### 순차검색
# 정렬되어있지 않은 경우
# arr = [4,9,11,23,19,7]
# key = 23
#
# for i in range(len(arr)):
#     if key == arr[i]:
#         print(i, "에 위치하고 있음")
#         break
#     else:
#         print('못찾음')

# 정렬되어 있는 경우
# arr = [4,7,9,19,23]
# key = 10
#
# for i in range(len(arr)):
#     if key == arr[i]:
#         print(i, "에 위치하고 있음")
#
#     elif key < arr[i]:
#         print(i, "번째까지만 탐색해봄")
#         break
# else:
#     print("못찾음")



####### 선택정렬
arr = [10,15,2,19,6,14]

for i in range(len(arr)-1):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)