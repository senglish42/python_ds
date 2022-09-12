import sys


def check_string(string):
    for i in string:
        if 0 > ord(i) or ord(i) > 127:
            raise Exception("The script does not support your language yet.")


def up_down(up, down, n, dec):
    if n > up:
        dif = n - up
        dec = dec + chr(down - 1 + dif)
    elif n < down:
        dif = down - n
        dec = dec + chr(up + 1 - dif)
    else:
        dec = dec + chr(n)
    return dec


def move_symbols(string, num):
    dec = ""
    for sym in string:
        i = ord(sym)
        if num < 0:
            n = i + num % -26
        else:
            n = i + num % 26
        if 65 <= i <= 90:
            dec = up_down(90, 65, n, dec)
        elif 97 <= i <= 122:
            dec = up_down(122, 97, n, dec)
        else:
            dec = dec + sym
    print(dec)


def run():
    if len(sys.argv) != 4:
        print("You should a command, text and shift")
        quit(1)
    num = 0
    try:
        num = int(sys.argv[3])
    except ValueError as e:
        print("Exception:", e)
        quit(2)
    check_string(sys.argv[2])
    if sys.argv[1].lower() == "decode":
        move_symbols(sys.argv[2], -num)
    elif sys.argv[1].lower() == "encode":
        move_symbols(sys.argv[2], +num)
    else:
        raise Exception("Error: invalid command. Please type 'decode' or 'encode' as the first argument.")


if __name__ == '__main__':
    run()
