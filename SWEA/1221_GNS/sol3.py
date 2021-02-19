import sys
sys.stdin = open('input.txt')

def solution(N, alien_list):
    def translator(number):
        # 외계어로 번역
        if type(number) == int:
            if number == 0:
                return 'ZRO'
            elif number == 1:
                return 'ONE'

        # 사람말로 번
        elif type(number) == str:
            if number == 'ZRO':
                return 0


        # translator 함수 하나를 두번 map하면 끝!
        return ' '.join(map(translator(sorted(list(map(translator, alien_list))))))

        # 근데 보기 너무 숭하니까 나눠서 적자
        human_list = list(map(translator, alien_list))
        human_list.sort()
        sorted_alien_list = map(translator, human_list)
        return ' '.join(sorted_alien_list)

    aliens = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


T = int(input())
for tc in range(1, T+1):
    N= int(input().split()[1])

    print('#{}\n{}'.format(tc, solution(N, input().split())))