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
    return price


def get_price(code):
    data = get_html(code)
    return scrape_price(data)


print(get_price("6098"))
