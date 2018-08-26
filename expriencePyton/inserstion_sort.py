#挿入ソート

A = [6,3,8,5,7]

for i in range(1,len(A)):
    temp = A[i]
    for j in range(i-1,-1,-1):
        if temp < A[j] :
            A[j+1] = A[j]
        else:
            A[j+1] = temp
            break
    else:
        A[0] = temp

print(A)
    