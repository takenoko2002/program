#クイックソート(ピポットは先頭)

def sort(A):
    if len(A) < 2:
        return A
    p = A[0]
    X,Y = divide(p,A[1:])
    return sort(X) + [p] + sort(Y)

def divide(p,A):
    if len(A) < 1:
        return ([],[])
    X,Y = divide(p,A[1:])
    a = A[0]
    if a < p:
        return ([a] + X,Y)
    else:
        return (X,[a] + Y)