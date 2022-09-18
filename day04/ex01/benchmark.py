#!/usr/bin/env python3

import timeit


def map_test(lst):
    return list(map(lambda i: i if i.partition('@')[2] == "gmail.com" else None, lst))


def comprehension_list_test(lst):
    return [i for i in lst if i.partition('@')[2] == "gmail.com"]


def loop_test(lst):
    ll = []
    for i in lst:
        if i.partition('@')[2] == "gmail.com":
            ll.append(i)
    return ll


def run():
    try:
        lst = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
        ln = timeit.timeit(f"loop_test({lst})", setup="from __main__ import loop_test", number=90000000)
        lcn = timeit.timeit(f"comprehension_list_test({lst})", setup="from __main__ import comprehension_list_test",
                            number=90000000)
        lm = timeit.timeit(f"map_test({lst})", setup="from __main__ import map_test", number=90000000)
        limit = sorted([lm, lcn, ln])
        if lm <= ln and lm <= lcn:
            print("it is better to use a map")
        elif lcn <= ln:
            print("it is better to use a list comprehension")
        else:
            print("it is better to use a loop")
        print(f"{limit[0]} vs {limit[1]} vs {limit[2]}")
    except KeyboardInterrupt:
        print("You quit the program")
        quit(1)


if __name__ == '__main__':
    run()
