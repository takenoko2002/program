#フィボナッチ数列の6個目を求める(分割統治法)

def fib(n):
    if ( n < 2):
        return n
    else:
        a = fib(n-1)
        b = fib(n-2)
        c = a + b
        return c

print(fib(6))
