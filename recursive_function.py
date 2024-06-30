def recursive_factorial_loop(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * recursive_factorial_loop(n - 1)

print(f'5! = {recursive_factorial_loop(5)}')
print(f'0! = {recursive_factorial_loop(0)}')
print(f'10! = {recursive_factorial_loop(10)}')
print(f'100! = {recursive_factorial_loop(100)}')
