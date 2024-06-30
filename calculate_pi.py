import time

def f(x: float) -> float:
    return (4 - x ** 2) ** (1 / 2)

def h(i: int, n: int) -> float:
    return f(i * (2 / n)) * (2 / n)

def g(i: int, n: int) -> float:
    return (f(i * (2 / n)) + f((i + 1) * (2 / n))) * (2 / n) * (1 / 2)

def pi_with_rectangle(e: float) -> float:
    v1: int | float = 0
    v2: float = f(0) * 2
    n: int = 1
    while abs(v1 - v2) > e:
        n = 2 * n
        v1 = v2
        v2 = 0
        for i in range(n):
            v2 = v2 + h(i, n)
    return v2

def pi_with_trapezoido(e: float) -> float:
    v1: int | float = 0
    v2: float = (f(0) + f(1)) * 2 * (1 / 2)
    n: int = 1
    while abs(v1 - v2) > e:
        n = 2 * n
        v1 = v2
        v2 = 0
        for i in range(n):
            v2 = v2 + g(i,n)
    return v2

start: float = time.time()
print(f'pi is {pi_with_rectangle(0.001)} where e is 0.001.')
end: float = time.time()
time_difference: float = end - start
print(f'Time: {time_difference}')

start = time.time()
print(f'pi is {pi_with_rectangle(0.000001)} where e is 0.000001.')
end = time.time()
time_difference = end - start
print(f'Time: {time_difference}')

start = time.time()
print(f'pi is {pi_with_rectangle(0.00000001)} where e is 0.00000001.')
end = time.time()
time_difference = end - start
print(f'Time: {time_difference}')

start = time.time()
print(f'pi is {pi_with_trapezoido(0.001)} where e is 0.001.')
end = time.time()
time_difference = end - start
print(f'Time: {time_difference}')

start = time.time()
print(f'pi is {pi_with_trapezoido(0.000001)} where e is 0.000001.')
end = time.time()
time_difference = end - start
print(f'Time: {time_difference}')

start = time.time()
print(f'pi is {pi_with_trapezoido(0.00000001)} where e is 0.00000001.')
end = time.time()
time_difference = end - start
print(f'Time: {time_difference}')
