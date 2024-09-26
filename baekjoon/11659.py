# https://www.acmicpc.net/problem/11659

# 구간 합 구하기 4 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	131500	53896	39460	38.496%
# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N, M = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # 구간 합 배열을 생성
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    results = []
    for k in range(2, 2 + M):
        i, j = map(int, data[k].split())
        # 구간 합 계산
        results.append(str(prefix_sum[j] - prefix_sum[i - 1]))
    
    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()