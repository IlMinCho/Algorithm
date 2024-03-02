# https://www.acmicpc.net/problem/21920

# 서로소 평균
# 문제
# 효성이는 길이가 
# $N$인 수열 
# $A$에서 
# $X$와 서로소인 수들을 골라 평균을 구해보려고 한다.

# 효성이를 도와 이를 계산해주자.

# 입력
# 첫 번째 줄에 입력될 수들의 개수 
# $N$이 주어진다. 
# $(2 \le N \le 500,000)$ 

# 두 번째 줄에는 수열 
# $A$를 이루는 자연수 
# $A_{i}$ 가 공백으로 구분되어 주어진다. 
# $(2 \le A_{i} \le 1,000,000)$ 

# 수열 
# $A$에 
# $X$와 서로소인 수가 최소 1개 이상 존재한다.

# 마지막 줄에는 
# $X$가 주어진다. 
# $(2\le X \le 1,000,000)$ 

# 출력
# 첫째 줄에 수열 A에서 X와 서로소인 수들의 평균을 출력한다.

# 절대/상대 오차는 10-6까지 허용한다.
from math import gcd

def calc_coprime_avg_from_input():
    # 입력값 받기
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    
    coprime_sum = 0
    coprime_count = 0
    
    for num in A:
        if gcd(num, X) == 1:  # 서로소인 경우
            coprime_sum += num
            coprime_count += 1
    
    # 서로소인 수들의 평균 계산
    coprime_avg = coprime_sum / coprime_count
    return coprime_avg

# 실행 예제는 주석 처리
print(calc_coprime_avg_from_input())