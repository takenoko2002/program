#改良版バブルソート

#A = [9,2,7,5,4]
A = [1,2,3,8,7,9]

for i in range(0,len(A)-1):
    print(A)
    count = 0
    for j in range(len(A)-1,i,-1):
        if A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
            count += 1
    if count == 0:
        break

print(A)
