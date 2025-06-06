# import math
import sys
import heapq
# sys.setrecursionlimit(10 ** 5)
# from collections import deque

input = sys.stdin.readline
n=int(input())
m=int(input())
distance=[[sys.maxsize for j in range(n+1)]for i in range(n+1)]
for i in range(1,n+1):
    distance[i][i]=0
for i in range(m):
    s,e,v=map(int,input().split())
    if distance[s][e]>v:
        distance[s][e]=v
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==sys.maxsize:
            print(0,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()