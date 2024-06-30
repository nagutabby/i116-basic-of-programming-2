from exception_handling import revised_recursive_factorial_loop

print('n! is calculated.')
while True:
    try:
        s: str = input('Please input n: ')
        n: int = int(s)
        print(f'{n}! = {revised_recursive_factorial_loop(n)}')
        break
    except Exception as e:
        print(e)
