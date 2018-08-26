#バブルソート

#A=[9,2,7,4,5]
A = [1,2,3,8,7,9]

for i in range(0,len(A)-1):
    print(A)
    for j in range(len(A)-1 ,i,-1):
        if A[j] < A[j-1]:
            A[j-1],A[j] = A[j],A[j-1] 

print(A)