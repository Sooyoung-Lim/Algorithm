import sys
sys.stdin = open('input.txt')

number = int(input())
num_list = [i for i in range(1, number+1)]
num_str = ' '.join(map(str, num_list))
print(num_str)

# for num in num_str:
#     if num % 3 == 0:
#         num_str.replace
#     print(num_str)