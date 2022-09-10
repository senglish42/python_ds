import sys


def get_key(dic, name):
    for k, v in dic.items():
        if v == name:
            return k
    print(name + " is a ticker, but the company is an unknown")
    return


def check_dict(c_dic, s_dic, name):
    if not c_dic.get(name.title(), None):
        if not s_dic.get(name.upper(), None):
            print(name + " is an unknown company or an unknown ticker symbol")
            return
        k = get_key(c_dic, name.upper())
        print(name.upper() + ' is a ticker for ' + k + ' company')
        return
    abv = c_dic.get(name.title(), None)
    if not s_dic.get(abv, None):
        print(name.title() + " is a company, but its ticket is not found in STOCKS dictionary")
        return
    price = s_dic.get(abv, None)
    print(name.title() + ' stock price is ' + str(price))


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
    check_dict(COMPANIES, STOCKS, name)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        quit(1)
    s = ','.join(sys.argv[1:])
    lst = s.split(',')
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
        if lst[i].find(' ') != -1:
            quit(2)
        if lst[i] == "":
            quit(2)
    for i in range(len(lst)):
        find(lst[i])
