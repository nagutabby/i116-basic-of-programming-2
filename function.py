def factorial_loop(n: int) -> int:
    red_box: int = 1
    blue_box: int = 1
    while blue_box < n or blue_box == n:
        red_box = red_box * blue_box
        blue_box = blue_box + 1
    return red_box

print(f'5! = {factorial_loop(5)}')
print(f'0! = {factorial_loop(0)}')
print(f'10! = {factorial_loop(10)}')
print(f'100! = {factorial_loop(100)}')
