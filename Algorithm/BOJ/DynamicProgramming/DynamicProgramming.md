# Dynamic Programming (동적 계획법)

### 메모리 공간을 약간 더 사용하면서 연산 속도를 비약적으로 증가시키는 방법.

    "한 번 계산한 문제는 다시 계산하지 않는다 !"

* 아래의 조건을 만족시키는 문제
    * 큰 문제를 작은 문제로 나눌 수 있다.
    * 동일한 작은 문제를 반복적으로 해결한다.
    * 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.


* 메모이제이션(memoization) 기법 사용
    * Topdown 방식
    * 연산 한 것을 메모리에 저장해 놓고,   
     다음에 똑같은 결과가 필요한 경우 다시 연산하지 않고 메모리에 저장된 값을 가져와 사용

* 
```python
# 대표적인 예시인 피보나치 수열

''' 
1. 재귀함수로 구현
 - O(2^N)의 시간복잡도
 - 동일한 함수가 반복적으로 호출되어 이미 계산 한 적 있는 경우에도 호출될 때 마다 계산
'''
def fibo(x):
    if x==1 or x==2: return 1
    return fibo(x-1) + fibo(x-2)


'''
2. Topdown(memoization)
'''
memo = [0]*100

def fibo(x):
    if x==1 or x==2: return 1
    if memo[x] != 0: return memo[x]
    memo[x] = fibo(x-1) + fibo(x-2)
    return memo[x]

```