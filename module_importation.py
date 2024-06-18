from recursive_function import fact_recur

print('n! is calculated.')
s: str = input('Please input n: ')
n: int = int(s)
print(f'{n}! = {fact_recur(n)}')
