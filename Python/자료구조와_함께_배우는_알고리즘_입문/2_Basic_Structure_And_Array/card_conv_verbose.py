# print out base notation among 2~36 converting with decimal number

def card_conv(x: int, r: int) -> str:
    """Return string representative number which convert integer 'x' to 'r' base notation"""

    d = ''    # The string after converting
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))    # The digit before conversion

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('    +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} ...{x % r}')
        else:
            print(f'    {x//r:{n}d} ... {x % r}')
        d += dchar [x % r]
        x //= r
    
    return d[::-1]

if __name__ == '__main__':
    print("Converts a decimal number to an 'n' base notation.") 

    while True:
        while True:    # Take the value which is a non-nagative integer
            no = int(input('Enter a non-negative integer for the conversion value: '))
            if no > 0:
                break

        while True:    # Take the integer of 2 ~ 36 base notation
            cd = int(input('what kind of base notation do you want to convert?: '))
            if 2 <= cd <= 36:
                break

        print(f'Here is the {card_conv(no, cd)} for {cd} base notation.')

        retry = input("Do you want to convert one more time? (Y/N): ")
        if retry in {'N', 'n'}:
            break
