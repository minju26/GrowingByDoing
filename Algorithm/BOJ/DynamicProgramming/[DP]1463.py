#boj 1463 :: 1로 만들기 :: silv.3

import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1):
    if i%6 == 0:
        dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) +1
    elif i%3 == 0: 
        dp[i] = min(dp[i//3], dp[i-1]) +1
    elif i%2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) +1
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])



# 1. 런타임 에러: index out of range, line7에서 dp 배열은 index 0 부터 시작하므로 n 이 아니라 n+1
# 2. 틀렸습니다: 6의 배수인 경우, 3으로 나눈 경우와 2로 나눈 경우 중 최소인 값을 선택


'''
<다른풀이>

for i in range(2, n + 1):

    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

-> i가 6의 배수인 경우: 먼저 i//3 경우와 i-1 중 최소값을 저장하고, 그 값을 다시 아래 if문 안에서 i//2 경우와 비교

'''