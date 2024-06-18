
def sr_by_linear_search(v0: int) -> int | None:
    for i in range(v0):
        if i * i > v0:
            return i - 1
    return None

print(f'The square root of 200000000 is {sr_by_linear_search(200000000)}.')
print(f'The square root of 20000000000000000 is {sr_by_linear_search(20000000000000000)}.')
