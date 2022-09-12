def print_dict(d):
    e = dict(sorted(d.items()))
    e = {k: e[k] for k in sorted(e, key=e.get, reverse=True)}
    for keys, l_values in e.items():
        for values in l_values:
            print(keys)


def tuples_to_dict():
    list_of_tuples = [
        ("Russia", "25"),
        ("France", "132"),
        ("Germany", "132"),
        ("Spain", "178"),
        ("Italy", "162"),
        ("Portugal", "17"),
        ("Finland", "3"),
        ("Hungary", "2"),
        ("The Netherlands", "28"),
        ("The USA", "610"),
        ("The United Kingdom", "95"),
        ("China", "83"),
        ("Iran", "76"),
        ("Turkey", "65"),
        ("Belgium", "34"),
        ("Canada", "28"),
        ("Switzerland", "26"),
        ("Brazil", "25"),
        ("Austria", "14"),
        ("Israel", "12"),
    ]
    d = {}
    for x, y in list_of_tuples:
        d.setdefault(x, []).append(int(y))
    return d


if __name__ == '__main__':
    print_dict(tuples_to_dict())
