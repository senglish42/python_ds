#!/usr/bin/env python3

import sys
import timeit
from functools import reduce


def reduce_test(num):
    num += 1
    return reduce(lambda x, y: x + y * y, range(1, num))


def loop_test(num):
    s = 0
    num += 1
    for i in range(1, num):
        s = i * i + s
    return s


def run():
    try:
        if len(sys.argv) != 4:
            raise TypeError("input name of the function, the number of calls, the number for "
                  "the sum of the calculation of squares")
        call = int(sys.argv[2])
        calc = int(sys.argv[3])
        if calc < 1 or call < 1:
            raise ValueError("numbers you entered should be positive")
        if sys.argv[1].lower() == "loop":
            print(timeit.timeit(f"loop_test({calc})", setup="from __main__ import loop_test", number=call))
        elif sys.argv[1].lower() == "reduce":
            print(timeit.timeit(f"reduce_test({calc})", setup="from __main__ import reduce_test", number=call))
        else:
            raise TypeError(f"{sys.argv[1]} is not the function name")
    except ValueError as e:
        print(f"Error: {e}")
        quit(1)
    except TypeError as e:
        print(f"Error: {e}")
        quit(2)
    except KeyboardInterrupt:
        print("You quit the program")
        quit(4)


if __name__ == '__main__':
    run()
