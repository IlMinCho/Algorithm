# 최소 c이상의 문, N 열쇠, 열쇠갯수 K
# 문 열수있는 열쇠에 포함된 번호
# 가지고 있는 열쇠에 포함된 번호

# N, K, C = map(int, input().split())
# open_keys = set(map(int, input().split()))
# has_keys = set(map(int, input().split()))

# intersection_keys = open_keys.intersection(has_keys)

# if len(intersection_keys) >= C:
#     print('yes') 
# else:
#     print('no')

from collections import Counter

# 입력 처리
N, K, C = map(int, input().split())
open_keys = set(map(int, input().split()))  # 열 수 있는 열쇠 목록
has_keys = Counter(map(int, input().split()))  # 보유한 열쇠 목록 (중복 고려)

# 열 수 있는 열쇠 중 보유한 열쇠의 개수를 카운트
count = sum(has_keys[key] for key in open_keys if key in has_keys)

# 결과 출력
if count >= C:
    print("yes")
else:
    print("no")