#!/usr/bin/env python3

import sys
import timeit


def filter_test(lst):
    return list(filter(lambda i: i if i.partition('@')[2] == "gmail.com" else None, lst))


def map_test(lst):
    return list(map(lambda i: i if i.partition('@')[2] == "gmail.com" else None, lst))


def list_comprehension_test(lst):
    return [i for i in lst if i.partition('@')[2] == "gmail.com"]


def loop_test(lst):
    ll = []
    for i in lst:
        if i.partition('@')[2] == "gmail.com":
            ll.append(i)
    return ll


def run():
    try:
        if len(sys.argv) != 3:
            raise TypeError("input name of the function and number of calls")
        num = int(sys.argv[2])
        if num < 1:
            raise ValueError("number of calls should be positive")
        lst = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
        if sys.argv[1].lower() == "loop":
            print(timeit.timeit(f"loop_test({lst})", setup=f"from __main__ import {sys.argv[1]}_test", number=num))
        elif sys.argv[1].lower() == "list_comprehension":
            print(timeit.timeit(f"list_comprehension_test({lst})", setup=f"from __main__ import {sys.argv[1]}_test",
                                number=num))
        elif sys.argv[1].lower() == "map":
            print(timeit.timeit(f"map_test({lst})", setup=f"from __main__ import {sys.argv[1]}_test", number=num))
        elif sys.argv[1].lower() == "filter":
            print(timeit.timeit(f"filter_test({lst})", setup=f"from __main__ import {sys.argv[1]}_test",
                                number=num))
        else:
            raise TypeError("function name you entered is not valid")
    except ValueError as e:
        print(f"Exception: {e}")
        quit(2)
    except TypeError as e:
        print(f"Exception: {e}")
        quit(3)
    except KeyboardInterrupt:
        print("You quit the program")
        quit(4)


if __name__ == '__main__':
    run()
