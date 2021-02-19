
# 1. 내장함수 안쓰
word = 'abcde'
reversed_word = ''
for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

# 2. 내장함수 쓰기
word = 'abcde'
reversed_word = reversed(word)
print(''.join(reversed_word))

# 3. 다른 방법
word = 'abcde'
print(word[::-1])
기

# 4. 재귀로 짜기_나
def reverse(text, idx):
    if idx >= len(text):
        return
    reverse(text, idx+1)
    print(text[idx], end= '')
text = 'abcde'
reverse(text, 0)

# 4-1. 재귀로 짜기_1
def sol1(word):
    idx = len(word) - 1
    r_word = ''
    while idx >= 0:
        r_word += word[idx]
        idx -= 1
    return r_word

# 4-2. 재귀로 짜기_2
def sol2(word):
    idx = len(word) - 1
    last_char = word[idx]
    if idx == 0:
        return last_char
    return last_char + sol2(word[:idx])