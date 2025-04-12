import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# a가 속한 집합과 b가 속한 집합 합치기
def union(x, y):
    # 각 친구의 부모 노드를 찾는다.
    x = find(x)
    y = find(y)

    # 부모 노드가 같으면 리턴
    if x == y:
        return

    else:
        # 부모 노드가 다르면 y에 부모 노드를 x에 부모 노드로 바꿔준다.
        parent[y] = x
        # y를 탐색한 횟수도 x에 더해준다.
        visited[x] += visited[y]


# 부모 노드 찾기
def find(target):
    # 자신이 부모 노드이면 자기 자신을 리턴
    if target == parent[target]:
        return target

    # 재귀 함수를 통해 부모 노드 찾기
    else:
        parent[target] = find(parent[target])
        return parent[target]


t = int(sys.stdin.readline())
for _ in range(t):
    f = int(input())
    parent = dict() # 딕셔너리형
    visited = dict() # 딕셔너리형

    # 친구 관계의 수만큼 반복하여 친구의 관계를 확인
    for i in range(f):
        a, b = map(str, input().split())

        # 친구 관계의 없는 친구이면 추가해준다.
        # 탐색 횟수도 카운트한다.
        if a not in parent:
            parent[a] = a
            visited[a] = 1

        if b not in parent:
            parent[b] = b
            visited[b] = 1

        # 두 친구의 관계을 합친다.
        union(a, b)

        print(visited[find(a)])