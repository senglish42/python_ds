import sys


def check_dict(dic, name):
    if not dic.get(name, None):
        print("Unknown ticket")
        quit(2)


def get_key(dic, name):
    for k, v in dic.items():
        if v == name:
            return k
    print("Unknown ticket")
    quit(2)


def find(name):
    COMPANIES = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Tesla": "TSLA",
        "Nokia": "NOK",
    }
    STOCKS = {
        "AAPL": 287.73,
        "MSFT": 173.79,
        "NFLX": 416.90,
        "TSLA": 724.88,
        "NOK": 3.37,
    }
    key = get_key(COMPANIES, name.upper())
    check_dict(STOCKS, name.upper())
    print(key, STOCKS.get(name.upper(), None))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        quit(1)
    find(sys.argv[1])
