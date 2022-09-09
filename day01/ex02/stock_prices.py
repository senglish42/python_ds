import sys


def check_dict(dic, name):
    if not dic.get(name, None):
        print("Unknown company")
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
    check_dict(COMPANIES, name.title())
    abv = COMPANIES.get(name.title(), None)
    check_dict(STOCKS, abv)
    print(STOCKS.get(abv, None))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        quit(1)
    find(sys.argv[1])
