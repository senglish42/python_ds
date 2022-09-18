#!/usr/bin/env python3

import timeit

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
        if lcn <= ln:
            print("it is better to use a list comprehension")
            print(f"{lcn} vs {ln}")
        elif ln < lcn:
            print("it is better to use a loop")
            print(f"{ln} vs {lcn}")
    except KeyboardInterrupt:
        print("You quit the program")
        quit(4)


if __name__ == '__main__':
    run()
