#スタックによる深さ優先探索とキューによる幅優先探索

from collections import deque

#スタック
def depth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T)
    while len(D) > 0:
        L,a,R = D.pop()
        print(a,end=',')
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
    print()

#キュー
def breadth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T)
    while len(D) > 0:
        L,a,R = D.popleft()
        print(a,end=',')
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
    print()
