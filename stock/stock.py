# get stock price from Yahoo Finance by scraping
# required BeautifulSoup
# # yum install -y gcc libxml2 libxml2-devel libxslt libxslt-devel python-devel
# # pip install BeautifulSoup4
# # pip install lxml

#-*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup 

YAHOO_URL="http://stocks.finance.yahoo.co.jp/stocks/detail/?code="

# "code" is stock code
def get_html(code):
    url = YAHOO_URL + code
    html = urllib.request.urlopen(url).read()
    return html


# get price from html source text
def scrape_price(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("td", class_ = "stoksPrice")
    price = data[1].string.replace(",", "")
    return int(float(price))


def get_price(code):
    data = get_html(code)
    return scrape_price(data)


# arg: filename includes stock_code list(newline separated)
def get_price_list(filename):
    f = open(filename, 'r')
    l = f.readlines()
    code_list=[]
    for i in l:
        i=i.strip()
        if i:
            code_list.append(i)
    f.close()

    ret = {}
    for i in code_list:
        ret.update({i: get_price(i)})
    return ret

print(get_price_list("./list.txt"))
