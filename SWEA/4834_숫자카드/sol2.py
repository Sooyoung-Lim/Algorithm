# 문자열로 다루는 방법
# 앞에서부터 세기, 뒤에서부터 세기, 카드 최대장수 알 때 등의 다양한 조합
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 카드 갯수
    N = int(input())
    # 문자열로 그냥 써보자
    card = input()

    counter = [0] * 10

    max_count = -1
    max_num = -1

    #### 1) 앞에서 부터 셀때
    for i in card:
        counter[int(i)] += 1

    for i in range(len(counter)):
        # 여기서 등호가 들어가는 이유는, 카드 장수가 같을 때 큰 수를 출력해야하기 때문
        if max_count <= counter[i] :
            max_count = counter[i]
            max_num = i
    ###########################


    #### 2) 뒤에서부터 셀 때. (등호가 없어도 됨!)
    for i in card:
        counter[int(i)] += 1
        # 카드의 최대 장수를 먼저 찾고 풀이하는 방법!
        if max_count < counter[int(i)]:
            max_count = counter[int(i)]


    for i in range(len(counter)-1, -1, -1):
        if max_count == counter[i] :
            max_num = i
            break
    #############################

    print('#{} {} {}'.format(tc, max_num, max_count))