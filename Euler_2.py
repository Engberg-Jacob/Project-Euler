
def even_fib(n):
    summed = 0
    fib_list = [1,1]
    while fib_list[1] < n:
        if fib_list[1] % 2== 0:
            summed += fib_list[1]
        fib_list = [fib_list[1], sum(fib_list)]
    return summed

print(even_fib(4000000))
#Lærte om konstruktion a lister