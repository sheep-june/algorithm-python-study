import sys
input = sys.stdin.readline

n= int(input())
ans = [0] * n
A=list(map(int,input().split()))
stack=[]
for i in range(n):
	#스택 안비어있고 top에 있는 값 확인
	while stack and A[stack[-1]] < A[i]:
		ans[stack.pop()] = A[i]
	stack.append(i)
while stack:
	ans[stack.pop()] = -1
print(' '.join(map(str, ans)))