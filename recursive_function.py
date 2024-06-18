def fact_recur(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact_recur(n - 1)

print(f'5! = {fact_recur(5)}')
print(f'0! = {fact_recur(0)}')
print(f'10! = {fact_recur(10)}')
print(f'100! = {fact_recur(100)}')
