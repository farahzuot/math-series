def fibonacci(n):
    if n == 0 or n == 1 :
        return n
    if type(n) != int:
        return 'invalid input'
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if type(n) != int:
       return 'invalid input'
    first = 2
    sec = 1
    if (n == 0) : 
        return 2 
    for i in range(2, n + 1) : 
        result = first + sec 
        first = sec 
        sec = result 
      
    return sec        


def sum_series(n, first=0, second=1):
    if type(n) != int:
       return 'invalid input'
    if type(first) != int:
       return 'invalid input'
    if type(second) != int:
       return 'invalid input'
    if n == 0:
        return first
    if n == 1:
        return second
    if type(n) != int:
        return 'invalid input'
    return sum_series(n-1,first,second) + sum_series(n-2,first,second)
