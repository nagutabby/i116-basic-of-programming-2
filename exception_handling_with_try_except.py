from exception_handling import rev_fact_recur

print('n! is calculated.')
while True:
    try:
        s: str = input('Please input n: ')
        n: int = int(s)
        print(f'{n}! = {rev_fact_recur(n)}')
        break
    except Exception as em:
        print(em)
