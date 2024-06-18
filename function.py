def fact_loop(n: int) -> int:
    red_box: int = 1
    blue_box: int = 1
    while blue_box < n or blue_box == n:
        red_box = red_box * blue_box
        blue_box = blue_box + 1
    return red_box

print(f'5! = {fact_loop(5)}')
print(f'0! = {fact_loop(0)}')
print(f'10! = {fact_loop(10)}')
print(f'100! = {fact_loop(100)}')
