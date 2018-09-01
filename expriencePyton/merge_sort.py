#マージソート

def sort(A):
    if len(A) < 2:
        return A
    c = len(A)//2
    return merge(sort(A[:c]),sort(A[c:]))

def merge(X,Y):
    if len(X) < 1:
        return Y
    if len(Y) < 1:
        return X    
    if (X[0] > Y[0]):
        return [Y[0]] + merge(X,Y[1:])
    else:
        return [X[0]] + merge(X[1:],Y)
