# -*- coding: utf-8 -*-
from datetime import datetime

from bs4 import BeautifulSoup
import requests


# Scrape newspaper editorial section of the day and guess the main subject
def tema_del_dia():
    today = datetime.today().strftime("%d-%m-%Y")
    url = "http://www.larepublica.pe/politica/editorial-" + today
    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    entry = soup.find("div", "glr-post-entry")

    editorial = ""
    for i in entry.find_all("p"):
        for item in i.contents:
            editorial += str(item.encode("utf-8"))

    editorial = strip_tags(editorial)
    print editorial


def strip_tags(string):
    string = string.replace("<br/>", "")
    string = string.replace("<p>", "")
    string = string.replace("</p>", "")
    return string


def main():
    tema_del_dia()


if __name__ == "__main__":
    main()
