import sys
import requests
from bs4 import BeautifulSoup
import httpx


def parse(ticker, field):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    try:
        hpx = httpx.get(url, headers=headers)
        if "lookup" in str(hpx.url):
            raise Exception("Error: Ticker name is invalid")
        if "financials" not in str(hpx.url):
            raise Exception(f"Error: Ticker '{ticker}' database can not be downloaded")
        soup = BeautifulSoup(hpx.text, 'html.parser')
        table = soup.find_all("div", attrs={"data-test": 'fin-row'})
        lst = []
        for i in table:
            if len(lst) > 0:
                break
            span = i.find_all("span")
            if span[0].text == field:
                for j in span:
                    lst.append(j.text)
        if len(lst) == 0:
            print("Error: field of the table is invalid")
            quit(3)
        return tuple(lst)
    except requests.RequestException as e:
        print(e)
        quit(1)
    except Exception as e:
        print(e)
        quit(2)


def run():
    if len(sys.argv) != 3:
        print("Error: input two arguments (ticker symbol, the field of the table).")
        quit(1)
    print(parse(sys.argv[1].lower(), sys.argv[2]))


if __name__ == "__main__":
    run()
