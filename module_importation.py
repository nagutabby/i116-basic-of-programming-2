from recursive_function import recursive_factorial_loop

print('n! is calculated.')
s: str = input('Please input n: ')
n: int = int(s)
print(f'{n}! = {recursive_factorial_loop(n)}')
