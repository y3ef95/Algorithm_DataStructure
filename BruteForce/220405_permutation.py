"""
순열 구하기
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두
출력합니다.
▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.
▣ 입력예제 1
3 2
▣ 출력예제 1
1 2
1 3
2 1
2 3
3 1
3 2
6
"""

import sys
input = sys.stdin.readline

def dfs(L):
    global cnt, res
    if L == m:
        print(*res)
        cnt += 1
    else:
        for i in range(1,n+1):
            if a[i] == 0:
                a[i] = 1
                res[L] = i
                dfs(L + 1)
                a[i] = 0

if __name__ == '__main__':
    n ,m = map(int,input().split())
    a = [0] * (n + 1)
    res = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)