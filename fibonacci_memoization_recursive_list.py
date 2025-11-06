#fibonacci = [0,1]
def fibo_memo(n,fibonacci = [0,1]):
    if n < len(fibonacci):
        return fibonacci[n]
    x = fibo_memo(n-1)+ fibonacci[n-2]
    fibonacci.append(x)
    return x

print(fibo_memo(10))

print(fibo_memo.__defaults__[0])  # shows the saved list


"""for negative numbers

def fibo_memo(arg,fibonacci = [0,1]):
    if arg < len(fibonacci):
        return fibonacci[arg]
    x = fibo_memo(arg-1)+ fibonacci[arg-2]
    fibonacci.append(x)
    return x

def neg(n):
    if n < 0 and n % 2 == 0:
        return fibo_memo(abs(n))*-1
    else:
        return fibo_memo(abs(n))

    """