def solution(n):
    fib = [0, 1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[-1] % 1234567