def revised_recursive_factorial_loop(n: int) -> int:
    if n < 0:
        raise Exception('The argument must be a natural number, such as 0, 1 and 2!')
    elif n == 0:
        return 1
    else:
        return n * revised_recursive_factorial_loop(n - 1)
