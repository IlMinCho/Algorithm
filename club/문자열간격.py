# 하나의 스트링에서 양쪽에 programer라는 문자열을 만들수 있는 최소의 길이로 끊고 그사이의 인덱스 값을 찾는 방법 

# def programmerStrings(s):
#     require_letters = set('programmer')
#     len_require_letters = len(require_letters)

#     left_found = set()
#     for left_idx, c in enumerate(s):
#         if c in require_letters:
#             left_found.add(c)
#         if len(left_found) == len_require_letters:
#             break

#     right_found = set()
#     for right_idx in range(len(s)-1, -1, -1):
#         c = s[right_idx]
#         if c in require_letters:
#             right_found.add(c)
#         if len(right_found) == len_require_letters:
#             break

#     diff = right_idx - left_idx -2

#     return diff

from collections import Counter

def programmerStrings(s):

    require_letters = Counter('programmer')
    print(require_letters)

    def left_found(s, require_letters):
        counts = Counter()
        for i, char in enumerate(s):
            if char in require_letters:
                counts[char] += 1
            if all(counts[c] >= require_letters[c] for c in require_letters):
                return i  
        return -1 

    def right_found(s, require_letters):
        counts = Counter()
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char in require_letters:
                counts[char] += 1
            if all(counts[c] >= require_letters[c] for c in require_letters):
                return i 
        return -1 

    left_idx = left_found(s, require_letters)
    right_idx = right_found(s, require_letters)

    diff = right_idx - left_idx -1
    return diff

print(programmerStrings('programmerxxxprozmerqgram'))
print(programmerStrings('progxrammerrxproxgrammer'))
print(programmerStrings('programmerprogrammer'))


print(programmerStrings('programxxxxxxmexxxxrxxxprozmerqgram'))
print(programmerStrings('0'))











