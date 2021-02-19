from pandas import DataFrame
import sys
sys.stdin = open('sample_input.txt')

def palindrome(lst):
    for i in range(len(lst)//2):
        if lst[i] == lst[len(lst)-1-i]:
            return True
        else:
            return False

T = 1
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(5)]
    # print(DataFrame(matrix))
    matrix_T = list(zip(*matrix))
    # print(DataFrame(matrix_T))

    # l : 회문의 길이
    sample = []
    for i in range(5):
        for l in range(5-i):
            for r_list in matrix:
                if palindrome(r_list[i:i+l]) :
                    sample.append(r_list[i:i+l])
    print(sample)

