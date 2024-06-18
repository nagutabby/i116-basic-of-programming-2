def rev_fact_recur(n: int) -> int:
    if n < 0:
        raise Exception('The argument must be a natural number, such as 0, 1 and 2!')
    elif n == 0:
        return 1
    else:
        return n * rev_fact_recur(n - 1)

print(f'5! = {rev_fact_recur(5)}')
print(f'0! = {rev_fact_recur(0)}')
print(f'10! = {rev_fact_recur(10)}')
print(f'100! = {rev_fact_recur(100)}')
