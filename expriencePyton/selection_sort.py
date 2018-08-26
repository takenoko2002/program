#選択ソート

def sort(A):
    for i in range(0,len(A)-1):
        select_min(A,i)

def select_min(A,i):
    min = i
    for j in range(i+1,len(A)):
        if A[min] > A[j]:
            min = j
    A[i],A[min] = A[min],A[i]

A = [8,4,3,9,6]
print(A)
sort(A)
print(A)