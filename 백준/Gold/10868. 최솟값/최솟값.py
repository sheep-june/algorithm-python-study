# import math
# import copy
import sys
# from sys import *
# import heapq
# sys.setrecursionlimit(10 ** 5)
# from collections import *
# from queue import *

input = sys.stdin.readline

n,m=map(int,input().split())
treeHeight=0
length=n
while length!=0:
    length//=2
    treeHeight +=1
treeSize=pow(2,treeHeight+1)
leftNodeStartIndex=treeSize//2-1
tree=[sys.maxsize]*(treeSize+1)
for i in range(leftNodeStartIndex+1,leftNodeStartIndex+n+1):
    tree[i]=int(input())
def setTree(i):
    while i != 1:
        if tree[i//2]>tree[i]:
            tree[i//2]=tree[i]
        i -= 1
setTree(treeSize-1)
# def changeVal(index,value):
#     diff=value-tree[index]
#     while index>0:
#         tree[index]=tree[index]+diff
#         index=index//2
# def getSum(s,e):
#     partSum=0
#     while s<=e:
#         if s%2==1:
#             partSum+=tree[s]
#             s+=1
#         if e%2==0:
#             partSum+=tree[e]
#             e-=1
#         s=s//2
#         e=e//2
#     return partSum
def getMin(s,e):
    MIN=sys.maxsize
    while s<=e:
        if s%2==1:
            MIN=min(MIN,tree[s])
            s+=1
        if e%2==0:
            MIN=min(MIN,tree[e])
            e-=1
        s=s//2
        e=e//2
    return MIN
for _ in range(m):
    s,e=map(int,input().split())
    s=s+leftNodeStartIndex
    e=e+leftNodeStartIndex
    print(getMin(s,e))