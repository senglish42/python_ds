#!/usr/bin/env python3

import timeit
import random
from collections import Counter


def sort_dic_counter(lst):
    return Counter(lst).most_common(10)


def dic_counter(lst):
    return Counter(lst)


def sort_dic(lst):
    d = dic(lst)
    sort_val = sorted(d.values(), reverse=True)
    return {list(d.keys())[list(d.values()).index(sort_val[x])]: sort_val[x] for x in range(0, 10)}


def dic(lst):
    new_lst = [0] * 101
    for i in lst:
        new_lst[i] += 1
    return {x: new_lst[x] for x in range(0, 101)}


def loop_test(num):
    s = 0
    num += 1
    for i in range(1, num):
        s = i * i + s
    return s


def run():
    try:
        lst = [random.randint(0, 100) for i in range(0, 1000000)]
        print("my function:", timeit.timeit(f"dic({lst})", setup="from __main__ import dic", number=1))
        print("Counter:", timeit.timeit(f"dic_counter({lst})", setup="from __main__ import dic_counter", number=1))
        print("my top:", timeit.timeit(f"sort_dic({lst})", setup="from __main__ import sort_dic", number=1))
        print("Counter's top:", timeit.timeit(f"sort_dic_counter({lst})", setup="from __main__ import sort_dic_counter",
                                              number=1))
    except KeyboardInterrupt:
        print("You quit the program")
        quit(4)


if __name__ == '__main__':
    run()
