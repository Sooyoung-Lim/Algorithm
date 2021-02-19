import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N= input()
    text_list = input().split()

    num_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}

    result = ''
    for word in text_list:
        num_dict[word] += 1
    # print(num_dict)

    for key, value in num_dict.items():
        tmp = ' '.join([key] * value)
        result += tmp + ' '
    print('#{}'.format(tc))
    print(result[:len(result)-1])