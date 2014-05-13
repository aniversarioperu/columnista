# -*- coding: utf-8 -*-
from datetime import datetime

from BeautifulSoup import BeautifulSoup
import requests


# Scrape newspaper editorial section of the day and guess the main subject
def tema_del_dia():
	today = datetime.today().strftime("%d-%m-%Y")
	url = "http://www.larepublica.pe/politica/editorial-" + today
	r = requests.get(url)

	soup = BeautifulSoup(r.text)
	print soup
	for i in soup.find_all("div", "glr-post-social glr-mb-10"):
		print i


def main():
	tema_del_dia()


if __name__ == "__main__":
	main()
